"""Local TDLib / Pytdbot API lookup for coding agents and the docs CLI."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any


def _package_path(*parts: str) -> Path | None:
    """Resolve a file shipped inside the ``pytdbot`` package."""
    try:
        base = resources.files("pytdbot")
        target = base.joinpath(*parts)
        # importlib.resources may return a Traversable
        if hasattr(target, "is_file") and target.is_file():
            return Path(str(target))
    except (TypeError, FileNotFoundError, ModuleNotFoundError, AttributeError):
        pass

    # Fallback: filesystem next to installed / source package
    pkg_root = Path(__file__).resolve().parents[1]
    candidate = pkg_root.joinpath(*parts)
    if candidate.is_file():
        return candidate

    return None


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _score_match(query: str, name: str, description: str = "") -> int:
    """Higher is better. 0 means no match."""
    q = query.strip()
    if not q:
        return 0
    qn = _norm(q)
    nn = _norm(name)
    desc = (description or "").lower()
    ql = q.lower()

    if qn == nn:
        return 1000
    if nn.startswith(qn) or qn.startswith(nn):
        return 800
    if qn in nn:
        return 600
    if ql in name.lower():
        return 500
    if ql in desc or qn in _norm(desc):
        return 200
    # token overlap
    tokens = [t for t in re.split(r"\W+", ql) if t]
    if tokens and all(t in name.lower() or t in desc for t in tokens):
        return 100 + 10 * len(tokens)
    return 0


class ApiLookup:
    """Search and fetch TDLib entities and Pytdbot helpers from local files."""

    def __init__(
        self,
        td_api: dict[str, Any] | None = None,
        helpers: list[dict[str, Any]] | None = None,
    ) -> None:
        if td_api is None:
            path = _package_path("td_api.json")
            if path is None:
                raise FileNotFoundError(
                    "pytdbot/td_api.json not found. Reinstall pytdbot or run "
                    "generate_json.py from the repo root."
                )
            td_api = _load_json(path)
        self.td_api = td_api

        if helpers is None:
            path = _package_path("ai", "helpers.json")
            helpers = _load_json(path) if path else []
        self.helpers = helpers

        self.version = str(td_api.get("version", "unknown"))
        self.commit_hash = str(td_api.get("commit_hash", ""))

    # --- TDLib sections -------------------------------------------------

    def _section(self, kind: str) -> dict[str, Any]:
        key = {
            "function": "functions",
            "functions": "functions",
            "type": "types",
            "types": "types",
            "class": "classes",
            "classes": "classes",
            "update": "updates",
            "updates": "updates",
        }.get(kind, kind)
        data = self.td_api.get(key)
        if not isinstance(data, dict):
            raise KeyError(f"Unknown API section: {kind}")
        return data

    def get_function(self, name: str) -> dict[str, Any] | None:
        return self._get_entity("functions", name)

    def get_type(self, name: str) -> dict[str, Any] | None:
        return self._get_entity("types", name)

    def get_class(self, name: str) -> dict[str, Any] | None:
        return self._get_entity("classes", name)

    def get_update(self, name: str) -> dict[str, Any] | None:
        return self._get_entity("updates", name)

    _KIND_BY_SECTION = {
        "functions": "function",
        "types": "type",
        "classes": "class",
        "updates": "update",
    }

    def _get_entity(self, section: str, name: str) -> dict[str, Any] | None:
        data = self.td_api.get(section) or {}
        kind = self._KIND_BY_SECTION.get(section, section)
        if name in data:
            return {"name": name, "kind": kind, **data[name]}
        # case-insensitive / camel-insensitive
        target = _norm(name)
        for key, value in data.items():
            if _norm(key) == target:
                return {"name": key, "kind": kind, **value}
        return None

    def search(
        self,
        query: str,
        *,
        kinds: list[str] | None = None,
        limit: int = 20,
    ) -> list[dict[str, Any]]:
        """Search functions, types, classes, updates, and helpers."""
        kinds = kinds or ["function", "type", "class", "update", "helper"]
        results: list[tuple[int, dict[str, Any]]] = []

        section_map = {
            "function": "functions",
            "type": "types",
            "class": "classes",
            "update": "updates",
        }

        for kind, section in section_map.items():
            if kind not in kinds and f"{kind}s" not in kinds:
                continue
            for name, meta in (self.td_api.get(section) or {}).items():
                desc = meta.get("description") or ""
                score = _score_match(query, name, desc)
                if score:
                    results.append(
                        (
                            score,
                            {
                                "kind": kind,
                                "name": name,
                                "description": desc,
                                "return_type": meta.get("type"),
                                "score": score,
                            },
                        )
                    )

        if "helper" in kinds or "helpers" in kinds:
            for h in self.helpers:
                desc = h.get("description") or h.get("doc") or ""
                label = f"{h.get('on', '')}.{h['name']}"
                score = max(
                    _score_match(query, h["name"], desc),
                    _score_match(query, label, desc),
                )
                if score:
                    results.append(
                        (
                            score,
                            {
                                "kind": "helper",
                                "name": h["name"],
                                "on": h.get("on"),
                                "helper_kind": h.get("kind"),
                                "description": h.get("description") or "",
                                "score": score,
                            },
                        )
                    )

        results.sort(key=lambda x: (-x[0], x[1].get("name", "")))
        return [item for _, item in results[:limit]]

    def get_helper(self, name: str) -> list[dict[str, Any]]:
        """Return all helpers matching name (may be multiple hosts)."""
        target = _norm(name)
        # allow Message.reply_text
        if "." in name:
            on, _, method = name.partition(".")
            on_n, method_n = _norm(on), _norm(method)
            return [
                h
                for h in self.helpers
                if _norm(h["name"]) == method_n and _norm(h.get("on", "")) == on_n
            ]
        return [h for h in self.helpers if _norm(h["name"]) == target]

    def search_helpers(self, query: str, *, limit: int = 30) -> list[dict[str, Any]]:
        return self.search(query, kinds=["helper"], limit=limit)

    def format_entity(self, entity: dict[str, Any]) -> str:
        """Pretty markdown for a function/type/class/update."""
        lines: list[str] = []
        kind = entity.get("kind", "entity")
        name = entity.get("name", "?")
        lines.append(f"# {kind}: `{name}`")
        if entity.get("description"):
            lines.append("")
            lines.append(entity["description"])
        if entity.get("type") and kind != "class":
            lines.append("")
            lines.append(f"**Returns / parent type:** `{entity['type']}`")

        args = entity.get("args")
        if isinstance(args, dict) and args:
            lines.append("")
            lines.append("## Arguments")
            for arg_name, info in args.items():
                if isinstance(info, dict):
                    opt = "optional" if info.get("is_optional") else "required"
                    lines.append(
                        f"- `{arg_name}` (`{info.get('type', '?')}`, {opt}): "
                        f"{info.get('description', '')}"
                    )
                else:
                    lines.append(f"- `{arg_name}`: {info}")

        if kind == "class":
            types_list = entity.get("types") or []
            funcs = entity.get("functions") or []
            if types_list:
                lines.append("")
                lines.append("## Subclasses")
                for t in types_list:
                    lines.append(f"- `{t}`")
            if funcs:
                lines.append("")
                lines.append("## Functions")
                for f in funcs:
                    lines.append(f"- `{f}`")

        lines.append("")
        lines.append(
            f"_TDLib {self.version}"
            + (f" ({self.commit_hash[:8]})" if self.commit_hash else "")
            + "_"
        )
        return "\n".join(lines)

    def format_helper(self, helper: dict[str, Any]) -> str:
        lines = [
            f"# helper: `{helper.get('on', '?')}.{helper['name']}`",
            "",
            f"**Kind:** {helper.get('kind', '?')}",
            f"**Async:** {helper.get('async', False)}",
        ]
        if helper.get("returns"):
            lines.append(f"**Returns:** `{helper['returns']}`")
        if helper.get("description"):
            lines.append("")
            lines.append(helper["description"])
        args = helper.get("args") or []
        if args:
            lines.append("")
            lines.append("## Arguments")
            for a in args:
                if isinstance(a, dict):
                    bits = [f"`{a['name']}`"]
                    if a.get("type"):
                        bits.append(f"(`{a['type']}`)")
                    if a.get("optional"):
                        bits.append("optional")
                        if "default" in a:
                            bits.append(f"default={a['default']}")
                    lines.append("- " + " ".join(bits))
                else:
                    lines.append(f"- `{a}`")
        doc = helper.get("doc") or ""
        if doc and doc != helper.get("description"):
            lines.append("")
            lines.append("## Documentation")
            lines.append(doc)
        if helper.get("source"):
            lines.append("")
            lines.append(f"_Source: {helper['source']}_")
        return "\n".join(lines)

    def stats(self) -> dict[str, Any]:
        return {
            "tdlib_version": self.version,
            "commit_hash": self.commit_hash,
            "functions": len(self.td_api.get("functions") or {}),
            "types": len(self.td_api.get("types") or {}),
            "classes": len(self.td_api.get("classes") or {}),
            "updates": len(self.td_api.get("updates") or {}),
            "helpers": len(self.helpers),
        }


@lru_cache(maxsize=1)
def get_lookup() -> ApiLookup:
    return ApiLookup()
