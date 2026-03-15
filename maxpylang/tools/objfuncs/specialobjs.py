"""Helpers for Max special objects such as `js` and abstractions."""

from __future__ import annotations

import copy
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

from maxpylang.tools import constants as _constants
from maxpylang.tools import typechecks as tc

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

_LOGGER = logging.getLogger(__name__)


def _strip_assignment_value(line: str) -> str:
    """Extract the right-hand side of a Max js assignment line."""
    before_semicolon = line.split(";", maxsplit=1)[0]
    before_comment = before_semicolon.split("//", maxsplit=1)[0]
    return before_comment.split("=", maxsplit=1)[1].strip()


def create_js(self: MaxObject, *, from_dict: bool | None = None) -> None:
    """Create or refresh a `js` object from args or saved metadata."""
    if not from_dict:
        filename = self.get_js_filename()
        if filename is None:
            _LOGGER.error("no filename specified")
            return
        self._dict["box"]["saved_object_attributes"]["filename"] = filename
    else:
        filename = str(self._dict["box"]["saved_object_attributes"]["filename"])

    js_path = Path(filename)
    if js_path.exists():
        self._ext_file = str(js_path.resolve())
    elif not from_dict:
        _LOGGER.error("%s not found", filename)
        return

    if from_dict:
        if js_path.exists():
            _LOGGER.info("%s found, parsing for inlet/outlet numbers", filename)
        numinlets = self._dict["box"]["numinlets"]
        numoutlets = self._dict["box"]["numoutlets"]
        self._args = [numinlets, numoutlets, filename]
        self.update_text()
        return

    self.update_js_from_file(filename, log_var="creation")


def update_js_from_file(
    self: MaxObject,
    filename: str,
    log_var: str | None = None,
) -> None:
    """Update a `js` object from a linked source file."""
    numinlets, numoutlets = self.get_js_io(filename, log_var=log_var)
    self._args = [numoutlets, numinlets, filename]

    new_args_string = [str(numoutlets), str(numinlets), filename]
    self.edit(text=" ".join(new_args_string), text_add="replace")

    if log_var is not None:
        _LOGGER.info(
            "%s : %s updated to %s inlets and %s outlets",
            log_var,
            filename,
            numinlets,
            numoutlets,
        )


def get_js_io(
    _self: MaxObject,
    filename: str,
    log_var: str | None = None,
) -> tuple[str | int, str | int]:
    """Read inlet and outlet counts from a js file."""
    with Path(filename).open(encoding="utf-8") as handle:
        lines = handle.readlines()

    numinlets: str | int | None = None
    numoutlets: str | int | None = None
    line_index = 0
    while line_index < len(lines) and (numinlets is None or numoutlets is None):
        line = lines[line_index]
        if "inlets" in line:
            numinlets = _strip_assignment_value(line)
        elif "outlets" in line:
            numoutlets = _strip_assignment_value(line)
        line_index += 1

    if numinlets is None or numoutlets is None:
        numinlets = 1
        numoutlets = 1
        if log_var is not None:
            _LOGGER.warning(
                "%s : %s defaults assumed (1 inlet, 1 outlet)",
                log_var,
                filename,
            )

    return numinlets, numoutlets


def get_js_filename(self: MaxObject) -> str | None:
    """Return the first non-numeric js filename argument, if present."""
    try:
        filename = str(next(arg for arg in self._args if not tc.check_number(arg)))
    except StopIteration:
        return None

    if ".js" not in Path(filename).suffixes:
        filename += ".js"
    return filename


def link_js(self: MaxObject, link_file: str | None = None) -> None:
    """Link a `js` object to an external source file."""
    if link_file is None:
        link_file = str(self._dict["box"]["saved_object_attributes"]["filename"])
        if link_file == "":
            _LOGGER.error("no filename specified")
            return

    js_path = Path(link_file)
    if not js_path.exists():
        _LOGGER.error("%s not found", link_file)
        return

    self._ext_file = str(js_path.resolve())
    self.update_js_from_file(link_file, log_var="link")


def create_abstraction(
    self: MaxObject,
    text: str | None = None,
    extra_attribs: dict[str, Any] | None = None,
    *,
    from_dict: bool = True,
) -> None:
    """Create or refresh abstraction metadata."""
    self._ext_file = self.name
    if ".maxpat" not in self.name:
        self._ext_file += ".maxpat"

    if from_dict:
        self.make_xlets_from_self_dict()
        _LOGGER.info("abstraction created")
        return

    if text is None:
        message = "text is required when building an abstraction from specs"
        raise AssertionError(message)

    self.update_abstraction_from_file(
        text,
        extra_attribs or {},
        log_var="creation",
    )


def update_abstraction_from_file(
    self: MaxObject,
    text: str | None,
    extra_attribs: dict[str, Any] | None,
    log_var: str | None = None,
) -> None:
    """Refresh abstraction I/O and attributes from the linked file."""
    numinlets, numoutlets = self.get_abstraction_io()
    extra_attribs = extra_attribs or {}

    unknown_obj_dict = getattr(self, "unknown_obj_dict", _constants.unknown_obj_dict)
    self._dict = copy.deepcopy(unknown_obj_dict)
    self._dict["box"]["numinlets"] = numinlets
    self._dict["box"]["numoutlets"] = numoutlets
    self._dict["box"]["outlettype"] = [""] * numoutlets
    self._dict["box"]["patching_rect"] = [0.0, 0.0]
    self._dict["box"]["text"] = text

    attrib_info = [{"name": "COMMON"}]
    _, valid_extra_attribs = self.get_all_valid_attribs({}, extra_attribs, attrib_info)
    self.add_extra_attribs(valid_extra_attribs)
    self.make_xlets_from_self_dict()

    if log_var is not None:
        _LOGGER.info("%s : file found, abstraction created", log_var)


def create_declared_abstraction(
    self: MaxObject,
    text: str,
    numinlets: int,
    numoutlets: int,
    extra_attribs: dict[str, Any],
) -> None:
    """Create an abstraction with user-declared inlet and outlet counts."""
    self._ext_file = self.name
    if ".maxpat" not in self.name:
        self._ext_file += ".maxpat"

    self._dict = copy.deepcopy(self.unknown_obj_dict)
    self._dict["box"]["numinlets"] = numinlets
    self._dict["box"]["numoutlets"] = numoutlets
    self._dict["box"]["outlettype"] = [""] * numoutlets
    self._dict["box"]["patching_rect"] = [0.0, 0.0]
    self._dict["box"]["text"] = text

    self._text_attribs, extra_attribs = self.get_all_valid_attribs(
        self._text_attribs,
        extra_attribs,
        [{"name": "COMMON"}],
    )
    self.add_extra_attribs(extra_attribs)
    self.update_text()
    self.make_xlets_from_self_dict()


def get_abstraction_io(self: MaxObject) -> tuple[int, int]:
    """Return the inlet and outlet counts in the linked abstraction file."""
    if self._ext_file is None:
        message = "abstraction file must be linked before I/O can be read"
        raise AssertionError(message)

    with Path(self._ext_file).open(encoding="utf-8") as handle:
        boxes = json.loads(handle.read())["patcher"]["boxes"]

    numinlets = 0
    numoutlets = 0
    for box in boxes:
        if box["box"]["maxclass"] == "inlet":
            numinlets += 1
        elif box["box"]["maxclass"] == "outlet":
            numoutlets += 1

    return numinlets, numoutlets


def link_abstraction(self: MaxObject, link_file: str | None = None) -> None:
    """Link an object to an external abstraction file."""
    if link_file is None:
        link_file = self.name

    if ".maxpat" not in link_file:
        link_file += ".maxpat"

    abstraction_path = Path(link_file)
    if not abstraction_path.exists():
        _LOGGER.error("%s not found", link_file)
        return

    self._ref_file = "abstraction"
    self._ext_file = link_file
    self._name = abstraction_path.stem
    self.update_abstraction_from_file(
        self.get_text(),
        self.get_extra_attribs(),
        log_var="link",
    )


def get_trigger_out_types(self: MaxObject) -> list[str]:
    """Return trigger outlet types inferred from the current args."""
    types: list[str] = []
    for arg in self._args:
        if arg == "b":
            types.append("bang")
        elif tc.check_int(arg) or arg == "i":
            types.append("int")
        elif tc.check_number(arg) or arg == "f":
            types.append("float")
        elif arg == "s":
            types.append("")
        else:
            types.append(str(arg))
    return types


def get_unpack_out_types(self: MaxObject) -> list[str]:
    """Return unpack outlet types inferred from the current args."""
    types: list[str] = []
    for arg in self._args:
        if tc.check_int(arg) or arg == "i":
            types.append("int")
        elif tc.check_number(arg) or arg == "f":
            types.append("float")
        else:
            types.append("")
    return types


def update_vst(self: MaxObject) -> None:
    """Refresh the saved `vst~` payload from the current args."""
    self._dict["box"]["save"].remove(";")
    self._dict["box"]["save"] += self._args
    self._dict["box"]["save"].append(";")
