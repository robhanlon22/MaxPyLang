"""Attribute validation and application helpers for ``MaxObject``."""

from __future__ import annotations

import logging
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from maxpylang.tools import typechecks as tc

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectDict = dict[str, Any]
AttribSpec = Mapping[str, Any]
AttribSpecList = Sequence[AttribSpec]
_LOGGER = logging.getLogger(__name__)


def add_extra_attribs(self: MaxObject, extra_attribs: ObjectDict) -> None:
    """Apply extra attributes to the object's backing dictionary.

    Args:
        self: Object being mutated.
        extra_attribs: Validated attributes to apply directly to the box dict.
    """
    for key, val in extra_attribs.items():
        self._dict["box"][key] = val


def get_all_valid_attribs(
    self: MaxObject,
    text_attribs: ObjectDict,
    extra_attribs: ObjectDict,
    attrib_info: AttribSpecList,
) -> tuple[ObjectDict, ObjectDict]:
    """Filter text and extra attributes against reference metadata.

    Args:
        self: Object whose metadata should be consulted.
        text_attribs: Attributes expressed inside the object text.
        extra_attribs: Additional box attributes supplied separately.
        attrib_info: Imported attribute metadata.

    Returns:
        A tuple of ``(valid_text_attribs, valid_extra_attribs)``.
    """
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
    """Remove unsupported attributes or invalid attribute values.

    Args:
        self: Object whose metadata should be consulted.
        attribs: Candidate attributes to validate.
        attrib_speclist: Imported attribute specifications.

    Returns:
        The filtered attribute dictionary after invalid entries are removed.
    """
    notvalid: set[str] = set()
    for attrib, raw_vals in attribs.items():
        vals = raw_vals if isinstance(raw_vals, list) else [raw_vals]

        if len(vals) == 0:
            _LOGGER.warning(
                "warning: %s : no argument given for attribute %s",
                self._name,
                attrib,
            )
            continue

        matching_specs = [spec for spec in attrib_speclist if spec["name"] == attrib]
        if len(matching_specs) == 0:
            _LOGGER.error(
                "Error: %s : %s is not a valid attribute argument",
                self._name,
                attrib,
            )
            notvalid.add(attrib)
            continue

        attrib_spec = matching_specs[0]
        if len(vals) < int(attrib_spec["size"]):
            _LOGGER.error(
                "Error: %s : %s requires %s arguments",
                self._name,
                attrib,
                attrib_spec["size"],
            )
            notvalid.add(attrib)

        if not all(
            tc.check_type([str(attrib_spec["type"])], single_val) for single_val in vals
        ):
            _LOGGER.error(
                "Error: %s : %s requires arguments of type %s",
                self._name,
                attrib,
                attrib_spec["type"],
            )
            notvalid.add(attrib)

    for badattrib in notvalid:
        del attribs[badattrib]

    return attribs


def retain_attribs(self: MaxObject, other: MaxObject) -> None:
    """Retain overlapping extra attributes from another object.

    Args:
        self: Object receiving attributes.
        other: Object supplying attributes.
    """
    extra_attribs = other.get_extra_attribs()
    self.edit(**extra_attribs)


def get_extra_attribs(self: MaxObject) -> ObjectDict:
    """Return non-default attributes stored on the object.

    Args:
        self: Object to inspect.

    Returns:
        A dictionary of box attributes not part of Max's standard box fields.
    """
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
