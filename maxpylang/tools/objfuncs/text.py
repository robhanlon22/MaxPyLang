"""
tools.obj.text

Methods that deal with MaxObject text.

    parse_text() --> parse given text into name, args, attribs
    update_text() --> update MaxObject dict with name, args, attribs
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject


def parse_text(
    self: MaxObject, text: str
) -> tuple[str, list[Union[str, int, float]], dict[str, list[str]]]:
    """
    Helper function for building objects.

    Parses in-box text into name, arguments, and in-text attributes.

    name --> str
    args --> list of str
    text_attribs --> dict, {attribute_name: [vals]}
    """
    # remove leading/trailing whitespace and split into pieces
    parts = text.strip(" ").split(" ")

    # name is first word
    name = parts[0]
    args: list[str] = []
    text_attribs: dict[str, list[str]] = {}

    # first, get args:
    # args must come before attributes
    # so take all elements until you hit one that starts with @
    i = 1
    while (i < len(parts)) and (parts[i][0] != "@"):
        args.append(parts[i])
        i += 1

    # get attributes; delineated by @
    while (i < len(parts)) and (parts[i][0] == "@"):
        attrib_name = parts[i][1:]

        i += 1
        attrib_val: list[str] = []
        while i < len(parts) and (
            parts[i][0] != "@"
        ):  # get values that come after attribute name
            attrib_val.append(parts[i])
            i += 1

        # add attribute, val to dictionary
        text_attribs[attrib_name] = attrib_val

    typed_args: list[Union[str, int, float]] = self.get_typed_args(args)

    return name, typed_args, text_attribs


def update_text(self: MaxObject) -> None:
    """
    Update text in MaxObject dict with name/args/attributes.
    """
    self._dict["box"]["text"] = self.get_text()


def get_text(self: MaxObject) -> str:
    """
    Get text field for MaxObject dict from self.name/args/text_attribs.
    """
    if self._name != "message":
        text = self._name
    else:
        text = ""

    if len(self._args) != 0:
        str_args = [str(x) for x in self._args]
        text += " " + " ".join(str_args)

    for attrib, val in self._text_attribs.items():
        text += " @" + str(attrib)
        if val is not None:
            text += " " + " ".join(str(part) for part in val)

    return text
