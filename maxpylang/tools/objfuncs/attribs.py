"""Helpers for validating and applying `MaxObject` attributes."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from maxpylang.tools import typechecks as tc
from maxpylang.tools.misc import write_stdout

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectDict = dict[str, Any]
AttribSpec = Mapping[str, Any]
AttribSpecList = Sequence[AttribSpec]


def add_extra_attribs(self: MaxObject, extra_attribs: ObjectDict) -> None:
    """Apply extra attributes to the object's backing dictionary."""
    for key, val in extra_attribs.items():
        self._dict["box"][key] = val


def get_all_valid_attribs(
    self: MaxObject,
    text_attribs: ObjectDict,
    extra_attribs: ObjectDict,
    attrib_info: AttribSpecList,
) -> tuple[ObjectDict, ObjectDict]:
    """Filter text and extra attributes against reference metadata."""
    text_attrib_info = list(attrib_info)
    if "COMMON" in [attrib["name"] for attrib in attrib_info]:
        text_attrib_info += self.common_box_attribs

    text_attribs = self.remove_bad_attribs(text_attribs, text_attrib_info)

    total_attrib_info = list(attrib_info)
    total_attrib_info.append({"name": "patching_rect", "type": "float", "size": "4"})
    if "COMMON" in [attrib["name"] for attrib in attrib_info]:
        total_attrib_info += self.common_box_attribs

    extra_attribs = self.remove_bad_attribs(extra_attribs, total_attrib_info)
    return text_attribs, extra_attribs


def remove_bad_attribs(
    self: MaxObject,
    attribs: ObjectDict,
    attrib_speclist: AttribSpecList,
) -> ObjectDict:
    """Remove unsupported attributes or invalid attribute values."""
    notvalid: set[str] = set()
    for attrib, raw_vals in attribs.items():
        vals = raw_vals if isinstance(raw_vals, list) else [raw_vals]

        if len(vals) == 0:
            write_stdout(
                "warning:",
                self._name,
                ": no argument given for attribute",
                attrib,
            )
            continue

        matching_specs = [spec for spec in attrib_speclist if spec["name"] == attrib]
        if len(matching_specs) == 0:
            write_stdout(
                "Error:",
                self._name,
                ":",
                attrib,
                "is not a valid attribute argument",
            )
            notvalid.add(attrib)
            continue

        attrib_spec = matching_specs[0]
        if len(vals) < int(attrib_spec["size"]):
            write_stdout(
                "Error:",
                self._name,
                ":",
                attrib,
                "requires",
                attrib_spec["size"],
                "arguments",
            )
            notvalid.add(attrib)

        if not all(
            tc.check_type([str(attrib_spec["type"])], single_val) for single_val in vals
        ):
            write_stdout(
                "Error:",
                self._name,
                ":",
                attrib,
                "requires arguments of type",
                attrib_spec["type"],
            )
            notvalid.add(attrib)

    for badattrib in notvalid:
        del attribs[badattrib]

    return attribs


def retain_attribs(self: MaxObject, other: MaxObject) -> None:
    """Retain overlapping extra attributes from another object."""
    extra_attribs = other.get_extra_attribs()
    self.edit(**extra_attribs)


def get_extra_attribs(self: MaxObject) -> ObjectDict:
    """Return non-default attributes stored on the object."""
    normal = [
        "id",
        "maxclass",
        "numinlets",
        "numoutlets",
        "outlettype",
        "patching_rect",
        "text",
    ]
    return {
        attrib: val for attrib, val in self._dict["box"].items() if attrib not in normal
    }
