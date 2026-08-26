from __future__ import annotations

from collections import Counter
from typing import Any

from .obj_encoder import obj_to_dict


def _diff_path(path: str, key: Any) -> str:
    return f"{path}.{key}" if path else str(key)


def _all_hashable(seq: list) -> bool:
    try:
        for item in seq:
            hash(item)
        return True
    except TypeError:
        return False


def deepdiff(d1: Any, d2: Any) -> list[str]:
    d1 = obj_to_dict(d1)
    d2 = obj_to_dict(d2)
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return [] if d1 == d2 else [f"changed to {d2}"]

    logs: list[str] = []

    def walk(a: Any, b: Any, path: str) -> None:
        if a is b or a == b:
            return
        if isinstance(a, dict) and isinstance(b, dict):
            for k, bv in b.items():
                if k not in a:
                    logs.append(f"{_diff_path(path, k)} changed to {bv}")
            for k, av in a.items():
                if k not in b:
                    logs.append(f"{_diff_path(path, k)} removed")
                else:
                    walk(av, b[k], _diff_path(path, k))
            return
        if isinstance(a, list) and isinstance(b, list):
            if _all_hashable(a) and _all_hashable(b):
                if Counter(a) == Counter(b):
                    return
                n = min(len(a), len(b))
                for i in range(n):
                    if a[i] != b[i]:
                        walk(a[i], b[i], _diff_path(path, i))
                return
            b_used = [False] * len(b)
            a_unmatched = []
            for i, item in enumerate(a):
                found = False
                for j, other in enumerate(b):
                    if not b_used[j] and item == other:
                        b_used[j] = True
                        found = True
                        break
                if not found:
                    a_unmatched.append((i, item))
            b_unmatched = [(j, b[j]) for j, used in enumerate(b_used) if not used]
            n = min(len(a_unmatched), len(b_unmatched))
            for i in range(n):
                idx, av = a_unmatched[i]
                walk(av, b_unmatched[i][1], _diff_path(path, idx))
            return
        logs.append(f"{path} changed to {b}")

    walk(d1, d2, "")
    return logs
