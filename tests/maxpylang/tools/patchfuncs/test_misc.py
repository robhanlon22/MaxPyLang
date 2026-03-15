"""Tests for miscellaneous patch helper behavior."""

from maxpylang import MaxPatch


def test_add_barebones_obj_appends_to_patcher_dict() -> None:
    """Verify barebones object insertion stores box data."""
    patch = MaxPatch(verbose=False)
    patch.add_barebones_obj("cycle~")

    boxes = patch.__dict__["_patcher_dict"]["patcher"]["boxes"]
    assert len(boxes) == 1
    assert boxes[0]["box"]["maxclass"] == "newobj"
    assert boxes[0]["box"]["text"] == "cycle~"
    assert patch.num_objs == 0
