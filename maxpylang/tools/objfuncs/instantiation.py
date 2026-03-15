"""Instantiation helpers for `MaxObject`."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectDict = dict[str, Any]
SerializedObject = dict[str, Any]


def build_from_specs(
    self: MaxObject,
    text: str,
    extra_attribs: ObjectDict,
    *,
    abstraction: bool = False,
    io_counts: tuple[int | None, int | None] = (None, None),
) -> None:
    """Build an object from in-box text and extra attributes."""
    inlets, outlets = io_counts
    self._name, self._args, self._text_attribs = self.parse_text(text)

    if abstraction:
        self._ref_file = "abstraction"
        self.create_declared_abstraction(text, inlets or 0, outlets or 0, extra_attribs)
        return

    ref_file = self.get_ref(self._name)
    if ref_file == "not_found":
        self._ref_file = None
        self._dict = self.unknown_obj_dict
        self.update_text()
        return

    if ref_file == "abstraction":
        self._ref_file = ref_file
        self.create_abstraction(text=text, extra_attribs=extra_attribs, from_dict=False)
        return

    info = self.get_info(ref_file)
    if not self.args_valid(self._name, self._args, info["args"]):
        self._ref_file = None
        self._dict = self.unknown_obj_dict
        self.update_text()
        return

    self._ref_file = ref_file
    self._dict = info["default"]
    self._text_attribs, extra_attribs = self.get_all_valid_attribs(
        self._text_attribs, extra_attribs, info["attribs"]
    )
    self.make_xlets_from_self_dict()
    self.update_ins_outs(info["in/out"], info["default"])
    self.add_extra_attribs(extra_attribs)
    self.update_text()

    if self.name == "js":
        self.create_js(from_dict=False)


def build_from_dict(self: MaxObject, given_dict: object) -> None:
    """Build an object from a serialized Max box dictionary."""
    obj_dict = cast("SerializedObject", given_dict)
    box_dict = cast("SerializedObject", obj_dict["box"])
    if box_dict["maxclass"] == "newobj":
        self._name, self._args, self._text_attribs = self.parse_text(
            str(box_dict["text"])
        )
    else:
        self._name = str(box_dict["maxclass"])

    self._ref_file = self.get_ref(self._name)
    if self._ref_file == "not_found":
        self._ref_file = None

    self._dict = obj_dict
    if self._ref_file == "abstraction":
        self.create_abstraction(from_dict=True)
        return

    if self.name == "js":
        self.create_js(from_dict=True)
    self.make_xlets_from_self_dict()
