"""Generate API reference pages at MkDocs build time.

Pages are written through mkdocs-gen-files (virtual overlay) so they never
land in git. Data comes from pytdbot.ai.lookup — the same source as
``python -m pytdbot.docs``.
"""

from __future__ import annotations

import html
import re
from collections import defaultdict

import mkdocs_gen_files

from pytdbot.ai.lookup import get_lookup

_SPHINX_ROLE = re.compile(
    r":(?:py:)?(?:class|meth|func|obj|attr|exc|data|mod|ref):`(?:~)?([^`]+)`"
)
_CLIENT_METH = re.compile(r"(?:^|\.)Client\.(\w+)$")
_UTILS_FN = re.compile(r"(?:^|\.)utils\.(\w+)$")
_VECTOR = re.compile(r"^vector<(.+)>$", re.I)
_LIST_ANN = re.compile(r"^(?:list|sequence|tuple)\[(.+)\]$", re.I)
_QUAL = re.compile(
    r"^(?:pytdbot\.)?(types|functions|classes|updates)\.(\w+)$"
)
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

_PRIMITIVES = {
    "int",
    "int32",
    "int53",
    "int64",
    "double",
    "string",
    "bytes",
    "bool",
    "Bool",
    "str",
    "float",
    "list",
    "dict",
    "None",
    "true",
    "false",
}


def _safe(name: str) -> str:
    cleaned = _SAFE.sub("_", name).strip("._")
    return cleaned or "unnamed"


def _pascal(name: str) -> str:
    """TL ``message`` → Python ``Message``; leave empty / already-capped names alone."""
    if not name:
        return name
    return name[0].upper() + name[1:]


def _letter(name: str) -> str:
    ch = (name or "?")[0].upper()
    return ch if ch.isalpha() else "#"


def _safe_desc(text: str, linker: Linker | None = None) -> str:
    """Turn Sphinx roles into autorefs; escape leftover [markdown](links)."""
    kept: list[str] = []

    def stash(match: re.Match[str]) -> str:
        target = match.group(1)
        if linker:
            kept.append(linker.ref_md(target))
        else:
            title = target.rsplit(".", 1)[-1]
            kept.append(f"[{title}][{target}]")
        return f"@@SPHINX{len(kept) - 1}@@"

    text = _SPHINX_ROLE.sub(stash, text or "")
    text = text.replace("[", "\\[").replace("]", "\\]")
    for i, chunk in enumerate(kept):
        text = text.replace(f"@@SPHINX{i}@@", chunk)
    return text.replace("\n", " ")


def _ident(kind: str, name: str, on: str | None = None) -> str:
    if kind == "helper":
        return f"pytdbot.{on}.{name}" if on else f"pytdbot.{name}"
    if kind == "function":
        return f"pytdbot.functions.{name}"
    if kind == "update":
        return f"pytdbot.types.{_pascal(name)}"
    if kind == "class":
        return f"pytdbot.classes.{_pascal(name)}"
    return f"pytdbot.types.{_pascal(name)}"


def _path(kind: str, name: str, on: str | None = None) -> str:
    folder = {
        "helper": "helpers",
        "function": "functions",
        "type": "types",
        "update": "updates",
        "class": "classes",
    }[kind]
    if kind == "helper":
        return f"reference/{folder}/{_safe(on or 'Client')}.{_safe(name)}.md"
    return f"reference/{folder}/{_safe(name)}.md"


class Linker:
    def __init__(self, lookup) -> None:
        self.lookup = lookup
        self.known: dict[str, str] = {}
        for section, kind in (
            ("types", "type"),
            ("functions", "function"),
            ("updates", "update"),
            ("classes", "class"),
        ):
            for name in lookup.td_api.get(section) or {}:
                self.known[name] = kind
                self.known[_pascal(name)] = kind
        self.helpers_by_name: dict[str, list[dict]] = defaultdict(list)
        for helper in lookup.helpers:
            on = helper.get("on") or "Client"
            self.known[f"{on}.{helper['name']}"] = "helper"
            self.helpers_by_name[helper["name"]].append(helper)

    def ref_md(self, raw: str) -> str:
        """Map a Sphinx target (`pytdbot.Client.deleteFile`) to an autoref."""
        raw = (raw or "").strip()
        title = raw.rsplit(".", 1)[-1]
        if not raw:
            return "`?`"
        if raw in _PRIMITIVES or title in _PRIMITIVES:
            return f"`{title}`"
        client = _CLIENT_METH.search(raw)
        if client:
            name = client.group(1)
            client_helpers = [
                h
                for h in self.helpers_by_name.get(name) or []
                if (h.get("on") or "Client") == "Client"
            ]
            if client_helpers:
                return f"[{name}][{_ident('helper', name, 'Client')}]"
            if name in self.known and self.known[name] == "function":
                return f"[{name}][{_ident('function', name)}]"
            return f"[{name}][pytdbot.Client.{name}]"
        utils = _UTILS_FN.search(raw)
        if utils:
            name = utils.group(1)
            return f"[{name}][pytdbot.utils.{name}]"
        kind = self.known.get(title) or self.known.get(_pascal(title))
        if kind and kind != "helper":
            display = title if kind == "function" else _pascal(title)
            return f"[{display}][{_ident(kind, title)}]"
        helpers = self.helpers_by_name.get(title)
        if helpers:
            h = helpers[0]
            return f"[{title}][{_ident('helper', h['name'], h.get('on'))}]"
        return f"`{title}`"

    def type_md(self, raw: str) -> str:
        raw = (raw or "").strip()
        if not raw:
            return "`?`"
        if "|" in raw:
            return " | ".join(self.type_md(part.strip()) for part in raw.split("|"))
        listed = _VECTOR.match(raw) or _LIST_ANN.match(raw)
        if listed:
            return f"list of {self.type_md(listed.group(1))}"
        qual = _QUAL.match(raw)
        if qual:
            return self.type_md(qual.group(2))
        if raw in _PRIMITIVES:
            return f"`{raw}`"
        kind = self.known.get(raw) or self.known.get(_pascal(raw))
        if not kind:
            return f"`{raw}`"
        display = _pascal(raw) if kind != "function" else raw
        return f"[{display}][{_ident(kind, raw)}]"


def _sig_block(call: str, params: list[tuple[str, str]], returns: str | None) -> str:
    lines = ['<div class="api-sig" markdown>', "", html.escape(call) + "("]
    if params:
        lines.append("<br>")
        last = len(params) - 1
        for i, (name, typ) in enumerate(params):
            comma = "," if i < last else ""
            lines.append(
                f"&nbsp;&nbsp;{html.escape(name)}: {typ}{comma}<br>"
            )
    closing = ")"
    if returns:
        closing += f" → {returns}"
    lines += [closing, "", "</div>", ""]
    return "\n".join(lines)


def _fields_block(
    items: list[tuple[str, str, str]], linker: Linker | None = None
) -> str:
    """Each field is an h3 so the page TOC is a jump list of names."""
    parts = ['<div class="api-fields" markdown>', ""]
    for name, typ, desc in items:
        desc_md = _safe_desc(desc, linker)
        hid = _safe(name)
        parts += [
            f"### {name} {{ #{hid} }}",
            "",
            f'<p class="api-type" markdown>{typ}</p>',
            "",
        ]
        if desc_md:
            parts += [f'<p class="api-desc" markdown>{desc_md}</p>', ""]
    parts += ["</div>", ""]
    return "\n".join(parts)


def _tdlib_line(lookup) -> str:
    ver = lookup.version
    commit = lookup.commit_hash
    if commit:
        url = f"https://github.com/tdlib/td/commit/{commit}"
        return f"TDLib {ver} · [{commit[:8]}]({url})"
    return f"TDLib {ver}"


def _meta_p(text: str) -> str:
    return f'<p class="api-meta" markdown>{text}</p>'


def _tdlib_params(linker: Linker, args: dict) -> tuple[list[tuple[str, str]], list[tuple[str, str, str]]]:
    sig: list[tuple[str, str]] = []
    fields: list[tuple[str, str, str]] = []
    for arg_name, info in args.items():
        if isinstance(info, dict):
            typ = linker.type_md(str(info.get("type", "")))
            desc = str(info.get("description") or "")
        else:
            typ = ""
            desc = str(info)
        sig.append((arg_name, typ))
        fields.append((arg_name, typ, desc))
    return sig, fields


def _az_index(
    items: list[tuple[str, str, str]], linker: Linker | None = None
) -> str:
    """items: (name, ident, description)"""
    groups: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for item in items:
        groups[_letter(item[0])].append(item)
    lines: list[str] = []
    letters = sorted(groups, key=lambda k: (k == "#", k))
    lines.append(" ".join(f"[{L}](#{L.lower() if L != '#' else 'other'})" for L in letters))
    lines.append("")
    for letter in letters:
        hid = "other" if letter == "#" else letter.lower()
        lines.append(f"## {letter} {{ #{hid} }}")
        lines.append("")
        for name, ident, desc in sorted(groups[letter], key=lambda x: x[0].lower()):
            short = _safe_desc(desc or "", linker)
            if len(short) > 120:
                short = short[:117] + "..."
            suffix = f" — {short}" if short else ""
            lines.append(f"- [`{name}`][{ident}]{suffix}")
        lines.append("")
    return "\n".join(lines)


def _write(path: str, body: str) -> None:
    with mkdocs_gen_files.open(path, "w") as fh:
        fh.write(body)
    mkdocs_gen_files.set_edit_path(path, "generate_docs.py")


def _entity_page(lookup, linker: Linker, kind: str, name: str, meta: dict) -> str:
    ident = _ident(kind, name)
    title = _pascal(name) if kind != "function" else name
    desc = _safe_desc(meta.get("description") or "", linker)
    lines = [
        f"[](){{ #{ident} }}",
    ]
    if kind == "function":
        lines.append(f"[](){{ #pytdbot.Client.{name} }}")
    kind_label = {"function": "Function", "type": "Type", "update": "Update", "class": "Class"}[kind]
    lines += [
        f"# `{title}`",
        "",
        _meta_p(f"{kind_label} · {_tdlib_line(lookup)}"),
        "",
    ]
    if desc:
        lines += [desc, ""]
    parent = meta.get("type")
    returns = linker.type_md(str(parent)) if parent and kind != "class" else None
    args = meta.get("args")
    if isinstance(args, dict) and args:
        sig, fields = _tdlib_params(linker, args)
        lines.append(_sig_block(title, sig, returns))
        lines.append(_fields_block(fields, linker))
    elif returns:
        lines.append(_sig_block(title, [], returns))
    if kind == "class":
        types_list = meta.get("types") or []
        funcs = meta.get("functions") or []
        if types_list:
            lines += ["## Subclasses", ""]
            for t in types_list:
                lines.append(f"- {linker.type_md(t)}")
            lines.append("")
        if funcs:
            lines += ["## Functions", ""]
            for fn in funcs:
                lines.append(f"- {linker.type_md(fn)}")
            lines.append("")
    return "\n".join(lines)


def _helper_page(lookup, linker: Linker, helper: dict, *, unique_name: bool) -> str:
    name = helper["name"]
    on = helper.get("on") or "Client"
    ident = _ident("helper", name, on)
    desc = _safe_desc(helper.get("description") or helper.get("doc") or "", linker)
    lines = [
        f"[](){{ #{ident} }}",
        f"[](){{ #{on}.{name} }}",
    ]
    if unique_name:
        lines.append(f"[](){{ #{name} }}")
    kind_bits = helper.get("kind", "helper").replace("_", " ")
    if helper.get("async"):
        kind_bits += " · async"
    lines += [
        f"# `{on}.{name}`",
        "",
        _meta_p(kind_bits),
        "",
    ]
    if desc:
        lines += [desc, ""]
    returns = linker.type_md(str(helper["returns"])) if helper.get("returns") else None
    args = helper.get("args") or []
    sig: list[tuple[str, str]] = []
    fields: list[tuple[str, str, str]] = []
    for arg in args:
        if not isinstance(arg, dict):
            continue
        arg_name = str(arg.get("name") or "")
        typ = linker.type_md(str(arg.get("type") or ""))
        if "default" in arg:
            typ += f" = `{arg['default']}`"
        sig.append((arg_name, typ))
        fields.append((arg_name, typ, ""))
    lines.append(_sig_block(f"{on}.{name}", sig, returns))
    if any(desc for _, _, desc in fields):
        lines += ["## Parameters", "", _fields_block(fields, linker)]
    if helper.get("source"):
        url = (
            "https://github.com/pytdbot/client/blob/main/"
            + str(helper["source"])
        )
        lines += [f"_Source: [{helper['source']}]({url})_", ""]
    return "\n".join(lines)


def main() -> None:
    lookup = get_lookup()
    linker = Linker(lookup)
    stats = lookup.stats()

    _write(
        "reference/index.md",
        "\n".join(
            [
                "# API reference",
                "",
                _meta_p(_tdlib_line(lookup)),
                "",
                "| | Count |",
                "| --- | ---: |",
                f"| [Helpers](helpers/index.md) | {stats['helpers']:,} |",
                f"| [Functions](functions/index.md) | {stats['functions']:,} |",
                f"| [Types](types/index.md) | {stats['types']:,} |",
                f"| [Updates](updates/index.md) | {stats['updates']:,} |",
                f"| [Classes](classes/index.md) | {stats['classes']:,} |",
                "",
            ]
        ),
    )

    helper_items: list[tuple[str, str, str]] = []
    name_counts: dict[str, int] = {}
    for helper in lookup.helpers:
        name_counts[helper["name"]] = name_counts.get(helper["name"], 0) + 1
    for helper in lookup.helpers:
        name = helper["name"]
        on = helper.get("on") or "Client"
        label = f"{on}.{name}"
        ident = _ident("helper", name, on)
        helper_items.append(
            (label, ident, helper.get("description") or "")
        )
        _write(
            _path("helper", name, on),
            _helper_page(
                lookup, linker, helper, unique_name=name_counts[name] == 1
            ),
        )
    _write(
        "reference/helpers/index.md",
        "# Helpers\n\n"
        + _az_index(helper_items, linker),
    )

    for section, kind, title in (
        ("functions", "function", "Functions"),
        ("types", "type", "Types"),
        ("updates", "update", "Updates"),
        ("classes", "class", "Classes"),
    ):
        items: list[tuple[str, str, str]] = []
        for name, meta in (lookup.td_api.get(section) or {}).items():
            ident = _ident(kind, name)
            display = _pascal(name) if kind != "function" else name
            items.append((display, ident, meta.get("description") or ""))
            _write(_path(kind, name), _entity_page(lookup, linker, kind, name, meta))
        _write(
            f"reference/{section}/index.md",
            f"# {title}\n\n" + _az_index(items, linker),
        )

    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav:
        nav.write(
            "\n".join(
                [
                    "* [Overview](index.md)",
                    "* [Helpers](helpers/index.md)",
                    "* [Functions](functions/index.md)",
                    "* [Types](types/index.md)",
                    "* [Updates](updates/index.md)",
                    "* [Classes](classes/index.md)",
                    "",
                ]
            )
        )


# mkdocs-gen-files uses runpy.run_path, which sets __name__ to "<run_path>"
# (Python 3.11+), not "__main__".
if __name__ in ("__main__", "<run_path>"):
    main()
