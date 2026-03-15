"""Miscellaneous helpers for `MaxObject`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject


def notknown(self: MaxObject) -> bool:
    """Return whether the object has no resolved reference file."""
    return self._ref_file is None


def repr_object(self: MaxObject) -> str:
    """Return a compact developer-facing object representation."""
    rep = self.name + " ["
    if "text" in self._dict["box"]:
        rep += str(self._dict["box"]["text"])
    else:
        rep += str(self._dict["box"]["maxclass"])
    rep += "]"
    return rep


__repr__ = repr_object
