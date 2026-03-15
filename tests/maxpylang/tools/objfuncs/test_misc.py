"""Tests for objfuncs.misc helpers."""

from types import SimpleNamespace

from maxpylang.tools.objfuncs import misc as obj_misc


def test_obj_misc_notknown_and_repr():
    unknown = SimpleNamespace(
        _ref_file=None,
        name="cycle~",
        _dict={"box": {"text": "cycle~ 440"}},
    )
    known = SimpleNamespace(
        _ref_file="ref-file",
        name="button",
        _dict={"box": {"maxclass": "button"}},
    )

    assert obj_misc.notknown(unknown) is True
    assert obj_misc.notknown(known) is False
    assert obj_misc.__repr__(unknown) == "cycle~ [cycle~ 440]"
    assert obj_misc.__repr__(known) == "button [button]"
