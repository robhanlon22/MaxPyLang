"""Helpers for patch-level validation reporting."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

PatchObject = Any
PatchObjectMap = dict[str, PatchObject]
_LOGGER = logging.getLogger(__name__)

_UNKNOWN_HEADER = "PatchCheck: unknown objects :"
_UNLINKED_JS_HEADER = "PatchCheck: unlinked js objects :"
_LINKED_JS_HEADER = (
    "PatchCheck: linked js objects (files must be in same folder as patch file):"
)
_ABSTRACTION_HEADER = (
    "PatchCheck: linked abstractions (files must be in same folder as patch file):"
)


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
        _LOGGER.info("              %s : %s", label, obj)


def _emit_linked_lines(objects: PatchObjectMap) -> None:
    """Emit one line per labeled object with a linked filename."""
    for label, obj in objects.items():
        ext_file = _object_ext_file(obj)
        linked_name = "" if ext_file is None else Path(ext_file).name
        _LOGGER.info("              %s : %s --> %s", label, obj, linked_name)


def check(self: MaxPatch, *flags: str) -> None:
    """Report unknown objects, js links, and abstractions."""
    flag_list = list(flags)
    if not flag_list or "all" in flag_list:
        flag_list.extend(["unknown", "js", "abstractions"])

    if "unknown" in flag_list or "unknowns" in flag_list:
        unknown_objs = self.get_unknowns()
        if unknown_objs:
            _LOGGER.info(_UNKNOWN_HEADER)
            _emit_object_lines(unknown_objs)
        else:
            _LOGGER.info("%s no unknown objects", _UNKNOWN_HEADER)

    if "js" in flag_list:
        linked_js, unlinked_js = self.get_js_objs()
        if unlinked_js:
            _LOGGER.info(_UNLINKED_JS_HEADER)
            _emit_object_lines(unlinked_js)
        else:
            _LOGGER.info("%s no unlinked js objects", _UNLINKED_JS_HEADER)

        if linked_js:
            _LOGGER.info(_LINKED_JS_HEADER)
            _emit_linked_lines(linked_js)
        else:
            _LOGGER.info("%s no linked js objects", _LINKED_JS_HEADER)

    if "abstractions" in flag_list or "abstraction" in flag_list:
        abstractions = self.get_abstractions()
        if abstractions:
            _LOGGER.info(_ABSTRACTION_HEADER)
            _emit_linked_lines(abstractions)
        else:
            _LOGGER.info("%s no linked abstractions", _ABSTRACTION_HEADER)


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
