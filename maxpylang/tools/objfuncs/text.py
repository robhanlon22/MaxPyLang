"""Helpers for parsing and rebuilding `MaxObject` text."""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

Atom = Union[str, int, float]


def parse_text(
    self: MaxObject,
    text: str,
) -> tuple[str, list[Atom], dict[str, list[str]]]:
    """Parse in-box text into name, positional args, and attributes."""
    parts = text.strip(" ").split(" ")

    name = parts[0]
    args: list[str] = []
    text_attribs: dict[str, list[str]] = {}

    i = 1
    while (i < len(parts)) and (parts[i][0] != "@"):
        args.append(parts[i])
        i += 1

    while (i < len(parts)) and (parts[i][0] == "@"):
        attrib_name = parts[i][1:]
        i += 1

        attrib_val: list[str] = []
        while i < len(parts) and parts[i][0] != "@":
            attrib_val.append(parts[i])
            i += 1

        text_attribs[attrib_name] = attrib_val

    typed_args: list[Atom] = self.get_typed_args(args)
    return name, typed_args, text_attribs


def update_text(self: MaxObject) -> None:
    """Update the stored Max box text from object state."""
    self._dict["box"]["text"] = self.get_text()


def get_text(self: MaxObject) -> str:
    """Build the Max box text from object name, args, and attributes."""
    text = self._name if self._name != "message" else ""

    if len(self._args) != 0:
        str_args = [str(x) for x in self._args]
        text += " " + " ".join(str_args)

    for attrib, val in self._text_attribs.items():
        text += " @" + str(attrib)
        if val:
            text += " " + " ".join(str(part) for part in val)

    return text
