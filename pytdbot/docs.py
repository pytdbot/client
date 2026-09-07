"""CLI: ``python -m pytdbot.docs`` / ``pytdbot-docs``."""

from __future__ import annotations

import argparse
import json
import sys

from pytdbot.ai.lookup import get_lookup

_BATCH_KINDS = {
    "function": "function",
    "fn": "function",
    "type": "type",
    "class": "class",
    "update": "update",
    "helper": "helper",
}


def _print_json(data: object) -> None:
    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


def _print_separated(texts: list[str]) -> None:
    for i, text in enumerate(texts):
        if i:
            print("\n---\n")
        print(text)


def _helpers_for_name(lookup, name: str) -> list:
    matches = lookup.get_helper(name)
    if not matches:
        q = name.lower()
        matches = [
            h
            for h in lookup.helpers
            if q in h["name"].lower() or q in (h.get("on") or "").lower()
        ]
    return matches


def cmd_stats(_: argparse.Namespace) -> int:
    _print_json(get_lookup().stats())
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    lookup = get_lookup()
    kinds = args.kind
    results = lookup.search(args.query, kinds=kinds, limit=args.limit)
    if args.json:
        _print_json(results)
    else:
        if not results:
            print(f"No results for {args.query!r}")
            return 1
        for r in results:
            kind = r.get("kind")
            name = r.get("name")
            on = r.get("on")
            label = f"{on}.{name}" if on else name
            desc = (r.get("description") or "").replace("\n", " ")
            if len(desc) > 100:
                desc = desc[:97] + "..."
            print(f"[{kind:8}] {label:40} {desc}")
    return 0


def _cmd_entities(args: argparse.Namespace, kind: str) -> int:
    lookup = get_lookup()
    getter = {
        "function": lookup.get_function,
        "type": lookup.get_type,
        "class": lookup.get_class,
        "update": lookup.get_update,
    }[kind]
    label = kind.capitalize()
    found = []
    missing = False
    for name in args.name:
        entity = getter(name)
        if entity:
            found.append(entity)
        else:
            missing = True
            print(f"{label} not found: {name}", file=sys.stderr)
    if not found:
        return 1
    if args.json:
        _print_json(found if len(args.name) > 1 else found[0])
    else:
        _print_separated([lookup.format_entity(e) for e in found])
    return 1 if missing else 0


def cmd_function(args: argparse.Namespace) -> int:
    return _cmd_entities(args, "function")


def cmd_type(args: argparse.Namespace) -> int:
    return _cmd_entities(args, "type")


def cmd_class(args: argparse.Namespace) -> int:
    return _cmd_entities(args, "class")


def cmd_update(args: argparse.Namespace) -> int:
    return _cmd_entities(args, "update")


def cmd_helper(args: argparse.Namespace) -> int:
    lookup = get_lookup()
    if args.name:
        found = []
        missing = False
        for name in args.name:
            matches = _helpers_for_name(lookup, name)
            if not matches:
                missing = True
                print(f"Helper not found: {name}", file=sys.stderr)
            else:
                found.extend(matches)
        if not found:
            return 1
        if args.json:
            if len(args.name) == 1:
                _print_json(found if len(found) > 1 else found[0])
            else:
                _print_json(found)
        else:
            _print_separated([lookup.format_helper(h) for h in found])
        return 1 if missing else 0

    # list / search helpers
    if args.query:
        results = lookup.search_helpers(args.query, limit=args.limit)
        if args.json:
            _print_json(results)
        else:
            for r in results:
                print(
                    f"{r.get('on', '?')}.{r['name']:30} {r.get('description', '')[:80]}"
                )
        return 0 if results else 1

    # list all
    if args.json:
        _print_json(lookup.helpers)
    else:
        for h in lookup.helpers:
            print(f"[{h.get('kind', '?'):14}] {h.get('on', '?'):28} {h['name']}")
    return 0


def cmd_batch(args: argparse.Namespace) -> int:
    lookup = get_lookup()
    getters = {
        "function": lookup.get_function,
        "type": lookup.get_type,
        "class": lookup.get_class,
        "update": lookup.get_update,
    }
    found: list[tuple[str, dict]] = []
    missing = False
    for spec in args.item:
        if ":" not in spec:
            print(
                f"Invalid batch item {spec!r}; expected kind:name",
                file=sys.stderr,
            )
            missing = True
            continue
        kind_raw, _, name = spec.partition(":")
        kind = _BATCH_KINDS.get(kind_raw.lower())
        if not kind or not name:
            print(
                f"Invalid batch item {spec!r}; expected kind:name "
                f"(function|fn|type|class|update|helper)",
                file=sys.stderr,
            )
            missing = True
            continue
        if kind == "helper":
            matches = _helpers_for_name(lookup, name)
            if not matches:
                print(f"Helper not found: {name}", file=sys.stderr)
                missing = True
            else:
                found.extend(("helper", h) for h in matches)
        else:
            entity = getters[kind](name)
            if not entity:
                print(f"{kind.capitalize()} not found: {name}", file=sys.stderr)
                missing = True
            else:
                found.append((kind, entity))

    if not found:
        return 1
    if args.json:
        _print_json([entity for _, entity in found])
    else:
        texts = []
        for kind, entity in found:
            if kind == "helper":
                texts.append(lookup.format_helper(entity))
            else:
                texts.append(lookup.format_entity(entity))
        _print_separated(texts)
    return 1 if missing else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pytdbot-docs",
        description=(
            "Look up TDLib methods/types and Pytdbot helpers. "
            "Pytdbot is a TDLib wrapper with high-level helpers, "
            "not the Telegram Bot API."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Machine-readable JSON output",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_stats = sub.add_parser("stats", help="Show API surface counts")
    p_stats.set_defaults(func=cmd_stats)

    p_search = sub.add_parser(
        "search", help="Search functions, types, classes, updates, helpers"
    )
    p_search.add_argument("query", help="Search query")
    p_search.add_argument(
        "--kind",
        action="append",
        choices=["function", "type", "class", "update", "helper"],
        help="Limit to kind (repeatable)",
    )
    p_search.add_argument("--limit", type=int, default=20)
    p_search.set_defaults(func=cmd_search)

    p_fn = sub.add_parser("function", aliases=["fn"], help="Show a TDLib function")
    p_fn.add_argument("name", nargs="+", help="Function name(s), e.g. sendMessage")
    p_fn.set_defaults(func=cmd_function)

    p_ty = sub.add_parser("type", help="Show a TDLib type")
    p_ty.add_argument("name", nargs="+", help="Type name(s), e.g. inputMessagePhoto")
    p_ty.set_defaults(func=cmd_type)

    p_cl = sub.add_parser("class", help="Show a TDLib abstract class")
    p_cl.add_argument("name", nargs="+", help="Class name(s), e.g. InputFile")
    p_cl.set_defaults(func=cmd_class)

    p_up = sub.add_parser("update", help="Show a TDLib update")
    p_up.add_argument("name", nargs="+", help="Update name(s), e.g. updateNewMessage")
    p_up.set_defaults(func=cmd_update)

    p_help = sub.add_parser(
        "helper", help="Show or list Pytdbot helpers / bound methods"
    )
    p_help.add_argument(
        "name",
        nargs="*",
        help="Helper name(s) (e.g. reply_text or Message.reply_text)",
    )
    p_help.add_argument("-q", "--query", help="Search helpers")
    p_help.add_argument("--limit", type=int, default=30)
    p_help.set_defaults(func=cmd_helper)

    p_batch = sub.add_parser(
        "batch",
        help="Look up several functions/types/helpers in one call",
    )
    p_batch.add_argument(
        "item",
        nargs="+",
        help="kind:name items, e.g. function:sendMessage type:message helper:reply_text",
    )
    p_batch.set_defaults(func=cmd_batch)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
