"""Tests for exposed MaxPatch helpers."""

import logging

from maxpylang import MaxPatch


def test_set_position_outputs_and_reorder_renumbers_objects(
    caplog: object,
) -> None:
    """Verify invalid positions report errors and reorder reindexes objects."""
    patch = MaxPatch(verbose=False)
    patch.place("toggle", verbose=False)[0]
    patch.place("number", verbose=False)[0]

    patch.set_position("bad", 1, from_place=True, verbose=True)
    assert "starting position must be specified" in caplog.text

    with caplog.at_level(logging.DEBUG, logger="maxpylang"):
        patch.set_position(5, 6, verbose=True)
    assert patch.curr_position == [5, 6]

    # create a gap in IDs and verify reorder fills it in.
    del patch.objs["obj-1"]
    patch.__dict__["_num_objs"] = 1
    caplog.clear()
    with caplog.at_level(logging.DEBUG, logger="maxpylang"):
        patch.reorder(verbose=True)
    assert patch.objs["obj-1"].name == "number"

    reorder_output = caplog.text
    assert "objects reordered" in reorder_output


def test_replace_handles_missing_and_existing_objects_and_preserves_connections(
    caplog: object,
) -> None:
    """Verify replace handles missing objects and preserves incoming/outgoing cords."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    patch.connect([source.outs[0], destination.ins[0]], verbose=False)

    patch.replace("obj-999", "message hello", verbose=True)
    assert "obj-999 does not exist, nothing changed" in caplog.text

    patch.replace("obj-1", "message replaced", retain=False, verbose=False)

    assert patch.objs["obj-1"].name == "message"
    assert destination.ins[0].sources == [patch.objs["obj-1"].outs[0]]


def test_inspect_returns_none_for_all_and_specific_objects(
    caplog: object,
) -> None:
    """Verify inspect returns None and does not print in test-mode."""
    patch = MaxPatch(verbose=False)
    obj = patch.place("toggle", verbose=False)[0]

    assert patch.inspect() is None
    assert patch.inspect("all") is None
    assert patch.inspect(obj.__dict__["_dict"]["box"]["id"]) is None

    assert not caplog.records
