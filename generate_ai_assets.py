#!/usr/bin/env python3
"""Generate AI-agent assets (helpers catalog).

Expects ``pytdbot/td_api.json`` (from ``generate_json.py`` + root ``td_api.tl``).

    python generate_ai_assets.py
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT / "pytdbot"
BOUND_METHODS_DIR = PACKAGE / "types" / "bound_methods"
METHODS_FILE = PACKAGE / "methods" / "methods.py"
UTILS_DIR = PACKAGE / "utils"
OUT_HELPERS = PACKAGE / "ai" / "helpers.json"
PKG_TD_API = PACKAGE / "td_api.json"

# Internal helpers not useful for agent lookup
UTILS_SKIP = {
    "JSON_ENCODER",
    "RETRY_AFTER_PREFEX",
    "empty_callback_data",
    "dict_to_obj",
    "obj_to_dict",
    "obj_to_json",
    "deepdiff",
    "json_dumps",
    "json_loads",
    "create_extra_id",
    "to_camel_case",
    "MediaAlbumFuture",
}

# Bound-method host types (class name → TDLib / Pytdbot type name)
BOUND_ON = {
    "MessageBoundMethods": "Message",
    "FileBoundMethods": "File",
    "CallbackQueryBoundMethods": "UpdateNewCallbackQuery",
    "MessageSenderBoundMethods": "MessageSender",
    "ChatActions": "ChatActions",
    "InlineQueryBoundMethods": "UpdateNewInlineQuery",
    "ChosenInlineResultBoundMethods": "UpdateNewChosenInlineResult",
}

SKIP_NAMES = {
    "__init__",
    "__await__",
    "__aenter__",
    "__aexit__",
    "__loop_action",
}


def _annotation_to_str(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return None


def _first_doc_line(doc: str | None) -> str:
    if not doc:
        return ""
    for line in doc.strip().splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def _full_doc(doc: str | None) -> str:
    if not doc:
        return ""
    return doc.strip()


def _extract_args(func: ast.AsyncFunctionDef | ast.FunctionDef) -> list[dict]:
    args_out: list[dict] = []
    positional = list(func.args.args) + list(func.args.kwonlyargs)
    plain_args = func.args.args
    plain_defaults = [None] * (len(plain_args) - len(func.args.defaults)) + list(
        func.args.defaults
    )
    default_map: dict[str, ast.AST | None] = {}
    for a, d in zip(plain_args, plain_defaults):
        default_map[a.arg] = d
    for a, d in zip(func.args.kwonlyargs, func.args.kw_defaults):
        default_map[a.arg] = d

    for a in positional:
        if a.arg in ("self", "cls"):
            continue
        entry: dict = {"name": a.arg}
        ann = _annotation_to_str(a.annotation)
        if ann:
            entry["type"] = ann
        if a.arg in default_map and default_map[a.arg] is not None:
            entry["optional"] = True
            try:
                entry["default"] = ast.unparse(default_map[a.arg])
            except Exception:
                entry["optional"] = True
        args_out.append(entry)

    if func.args.vararg:
        args_out.append({"name": f"*{func.args.vararg.arg}", "optional": True})
    if func.args.kwarg:
        args_out.append({"name": f"**{func.args.kwarg.arg}", "optional": True})

    return args_out


def _methods_from_class(
    class_node: ast.ClassDef,
    *,
    kind: str,
    on: str,
    source_file: str,
) -> list[dict]:
    helpers: list[dict] = []
    for item in class_node.body:
        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if item.name in SKIP_NAMES or item.name.startswith("_"):
            continue
        # Skip property setters only; include properties as helpers
        is_property = any(
            isinstance(d, ast.Name)
            and d.id == "property"
            or (isinstance(d, ast.Attribute) and d.attr == "property")
            for d in item.decorator_list
        )
        doc = ast.get_docstring(item)
        helpers.append(
            {
                "name": item.name,
                "kind": "property" if is_property else kind,
                "on": on,
                "async": isinstance(item, ast.AsyncFunctionDef) and not is_property,
                "args": [] if is_property else _extract_args(item),
                "description": _first_doc_line(doc),
                "doc": _full_doc(doc),
                "source": source_file,
                "returns": _annotation_to_str(item.returns),
            }
        )
    return helpers


def extract_client_helpers() -> list[dict]:
    tree = ast.parse(METHODS_FILE.read_text(encoding="utf-8"))
    rel = str(METHODS_FILE.relative_to(ROOT))
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Methods":
            return _methods_from_class(
                node, kind="client_method", on="Client", source_file=rel
            )
    return []


def extract_bound_helpers() -> list[dict]:
    helpers: list[dict] = []
    for path in sorted(BOUND_METHODS_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        rel = str(path.relative_to(ROOT))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            on = BOUND_ON.get(node.name, node.name)
            kind = "bound_method"
            if node.name == "ChatActions":
                kind = "chat_action"
            helpers.extend(_methods_from_class(node, kind=kind, on=on, source_file=rel))
    return helpers


def extract_utils() -> list[dict]:
    """Public functions re-exported / defined under pytdbot.utils."""
    from pytdbot import utils as utils_mod

    public = set(getattr(utils_mod, "__all__", []))
    helpers: list[dict] = []

    for path in sorted(UTILS_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        rel = str(path.relative_to(ROOT))
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_") or node.name in UTILS_SKIP:
                continue
            if public and node.name not in public:
                continue
            doc = ast.get_docstring(node)
            helpers.append(
                {
                    "name": node.name,
                    "kind": "util",
                    "on": "utils",
                    "async": isinstance(node, ast.AsyncFunctionDef),
                    "args": _extract_args(node),
                    "description": _first_doc_line(doc),
                    "doc": _full_doc(doc),
                    "source": rel,
                    "returns": _annotation_to_str(node.returns),
                }
            )
    return helpers


def main() -> None:
    if not PKG_TD_API.is_file():
        raise SystemExit(
            f"Missing {PKG_TD_API}. Run generate_json.py first "
            "(reads td_api.tl from repo root)."
        )

    helpers = extract_client_helpers() + extract_bound_helpers() + extract_utils()
    helpers.sort(key=lambda h: (h["kind"], h["on"], h["name"]))

    OUT_HELPERS.parent.mkdir(parents=True, exist_ok=True)
    OUT_HELPERS.write_text(
        json.dumps(helpers, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    by_kind: dict[str, int] = {}
    for h in helpers:
        by_kind[h["kind"]] = by_kind.get(h["kind"], 0) + 1

    print(f"Wrote {OUT_HELPERS} ({len(helpers)} helpers)")
    for k, v in sorted(by_kind.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
