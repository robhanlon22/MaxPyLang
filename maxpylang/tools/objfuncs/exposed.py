"""User-facing helpers exposed through `MaxObject`."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from maxpylang.tools.misc import write_stdout

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectDict = dict[str, Any]


def move(self: MaxObject, x: float, y: float) -> None:
    """Move an object to the requested patcher position."""
    self._dict["box"]["patching_rect"][0] = x
    self._dict["box"]["patching_rect"][1] = y


def edit(
    self: MaxObject,
    text_add: str = "append",
    text: str | None = None,
    **extra_attribs: object,
) -> None:
    """Edit object text and attributes without changing the object class."""
    if self.notknown():
        write_stdout("Error: attempting edit on empty object")
        write_stdout("       nothing edited")
        return

    new_args: list[Any] = []
    new_text_attribs: ObjectDict = {}

    if text is not None:
        if not text.startswith(self.name):
            text = self.name + " " + text
        _, new_args, new_text_attribs = self.parse_text(text)

    if text_add == "append":
        new_args = self._args + new_args
        new_text_attribs = self._text_attribs | new_text_attribs

    if self._ref_file == "abstraction":
        self._args = new_args
        self._text_attribs = new_text_attribs
        self.update_text()

        attrib_info = [{"name": "COMMON"}]
        _, extra_attribs = self.get_all_valid_attribs({}, extra_attribs, attrib_info)
        self.add_extra_attribs(extra_attribs)
        write_stdout(
            "ObjectWarning:",
            self.name,
            ": edit : abstraction edited naively. if abstraction args affect"
            " inlets/outlets or abstraction has unique attributes, abstraction info"
            " must be imported using import_objs() function to reflect"
            " arg/attribute behaviors.",
        )
        return

    info = self.get_info()
    if not self.args_valid(self.name, new_args, info["args"]):
        write_stdout(self.name, "not edited")
        return
    self._args = new_args

    self._text_attribs, extra_attribs = self.get_all_valid_attribs(
        new_text_attribs, extra_attribs, info["attribs"]
    )
    self.update_ins_outs(info["in/out"], info["default"])
    self.add_extra_attribs(extra_attribs)
    self.update_text()


def link(self: MaxObject, link_file: str | None = None) -> None:
    """Link a file for a js object or abstraction."""
    known_obj_names = {name for group in self.known_objs.values() for name in group}
    allow_unknown_as_abstraction = (
        self._ref_file is None and self.name not in known_obj_names
    )
    if not (
        self.name == "js"
        or self._ref_file == "abstraction"
        or allow_unknown_as_abstraction
    ):
        write_stdout("ObjectError:", self.name, ": link : cannot be linked to a file")
        return

    if self.name == "js":
        self.link_js(link_file=link_file)
    else:
        self.link_abstraction(link_file=link_file)


def inspect(self: MaxObject) -> None:
    """Inspect the object."""
    del self
