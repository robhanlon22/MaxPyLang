"""
.tools.obj.misc

Miscellaneous functions for the MaxObject class.

    notknown() --> check to see if the object has a reference file
    __str__(), __repr__() --> printing and rep of object, for info/debugging purposes

"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject


def notknown(self: "MaxObject") -> bool:
    """
    Return true if the object has no ref_file.
    """

    return self._ref_file is None


# def isempty(self):
# """
# Returns true if the object is empty; wrapper for notknown(), for clarity.
# """
# return self.notknown()


def __repr__(self: "MaxObject") -> str:

    rep = self.name + " ["
    if "text" in self._dict["box"].keys():
        rep += str(self._dict["box"]["text"])
    else:
        rep += str(self._dict["box"]["maxclass"])

    rep += "]"

    return rep
