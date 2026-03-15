"""Miscellaneous helpers for `MaxObject`."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject


def notknown(self: MaxObject) -> bool:
    """Return whether the object has no resolved reference file."""
    return self._ref_file is None


def repr_object(self: MaxObject) -> str:
    """Return a compact developer-facing object representation."""
    rep = self.name + " ["
    box = cast("dict[str, Any]", self._dict["box"])
    if "text" in box:
        rep += str(box["text"])
    else:
        rep += str(box["maxclass"])
    rep += "]"
    return rep


__repr__ = repr_object
