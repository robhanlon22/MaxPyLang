"""Helpers for patch-level validation reporting."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

PatchObject = object
PatchObjectMap = dict[str, PatchObject]

_UNKNOWN_HEADER = "PatchCheck: unknown objects :"
_UNLINKED_JS_HEADER = "PatchCheck: unlinked js objects :"
_LINKED_JS_HEADER = (
    "PatchCheck: linked js objects (files must be in same folder as patch file):"
)
_ABSTRACTION_HEADER = (
    "PatchCheck: linked abstractions (files must be in same folder as patch file):"
)


def _write_stdout(*parts: object, end: str = "\n") -> None:
    """Write a space-joined line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + end)


def _object_name(obj: PatchObject) -> str:
    """Return the object's display name."""
    return str(getattr(obj, "name", getattr(obj, "_name", "")))


def _object_ref_file(obj: PatchObject) -> str | None:
    """Return the object's reference marker."""
    return cast("str | None", getattr(obj, "ref_file", getattr(obj, "_ref_file", None)))


def _object_ext_file(obj: PatchObject) -> str | None:
    """Return the object's linked external file."""
    return cast("str | None", getattr(obj, "ext_file", getattr(obj, "_ext_file", None)))


def _emit_object_lines(objects: PatchObjectMap) -> None:
    """Emit one line per labeled object."""
    for label, obj in objects.items():
        _write_stdout("              ", label, ":", obj)


def _emit_linked_lines(objects: PatchObjectMap) -> None:
    """Emit one line per labeled object with a linked filename."""
    for label, obj in objects.items():
        ext_file = _object_ext_file(obj)
        linked_name = "" if ext_file is None else Path(ext_file).name
        _write_stdout("              ", label, ":", obj, "-->", linked_name)


def check(self: MaxPatch, *flags: str) -> None:
    """Report unknown objects, js links, and abstractions."""
    flag_list = list(flags)
    if not flag_list or "all" in flag_list:
        flag_list.extend(["unknown", "js", "abstractions"])

    if "unknown" in flag_list or "unknowns" in flag_list:
        unknown_objs = self.get_unknowns()
        if unknown_objs:
            _write_stdout(_UNKNOWN_HEADER)
            _emit_object_lines(unknown_objs)
        else:
            _write_stdout(f"{_UNKNOWN_HEADER} no unknown objects")
        _write_stdout()

    if "js" in flag_list:
        linked_js, unlinked_js = self.get_js_objs()
        if unlinked_js:
            _write_stdout(_UNLINKED_JS_HEADER)
            _emit_object_lines(unlinked_js)
        else:
            _write_stdout(f"{_UNLINKED_JS_HEADER} no unlinked js objects")
        _write_stdout()

        if linked_js:
            _write_stdout(_LINKED_JS_HEADER)
            _emit_linked_lines(linked_js)
        else:
            _write_stdout(f"{_LINKED_JS_HEADER} no linked js objects")
        _write_stdout()

    if "abstractions" in flag_list or "abstraction" in flag_list:
        abstractions = self.get_abstractions()
        if abstractions:
            _write_stdout(_ABSTRACTION_HEADER)
            _emit_linked_lines(abstractions)
        else:
            _write_stdout(f"{_ABSTRACTION_HEADER} no linked abstractions")
        _write_stdout()


def get_unknowns(self: MaxPatch) -> PatchObjectMap:
    """Return unresolved objects in the patch."""
    return {
        label: obj for label, obj in self._objs.items() if _object_ref_file(obj) is None
    }


def get_abstractions(self: MaxPatch) -> PatchObjectMap:
    """Return abstraction objects in the patch."""
    return {
        label: obj
        for label, obj in self._objs.items()
        if _object_ref_file(obj) == "abstraction"
    }


def get_js_objs(self: MaxPatch) -> tuple[PatchObjectMap, PatchObjectMap]:
    """Return linked and unlinked js objects in the patch."""
    linked: PatchObjectMap = {}
    unlinked: PatchObjectMap = {}
    for label, obj in self._objs.items():
        if _object_name(obj) != "js":
            continue
        if _object_ext_file(obj) is None:
            unlinked[label] = obj
        else:
            linked[label] = obj
    return linked, unlinked
