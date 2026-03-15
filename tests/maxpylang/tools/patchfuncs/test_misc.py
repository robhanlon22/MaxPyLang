"""Tests for miscellaneous MaxPatch helpers."""

from maxpylang import MaxPatch


def test_add_barebones_obj_appends_to_patcher_dict():
    patch = MaxPatch(verbose=False)
    patch.add_barebones_obj("cycle~")

    boxes = patch._patcher_dict["patcher"]["boxes"]
    assert len(boxes) == 1
    assert boxes[0]["box"]["maxclass"] == "newobj"
    assert boxes[0]["box"]["text"] == "cycle~"
    assert patch.num_objs == 0
