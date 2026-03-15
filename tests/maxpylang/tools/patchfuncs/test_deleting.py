"""Tests for patch deletion helpers."""

import pytest
from _pytest.capture import CaptureFixture

from maxpylang import MaxPatch


def test_delete_get_extra_cords_collects_attached_connections() -> None:
    """Verify extra cords from deletion include connected endpoints."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]

    patch.connect([source.outs[0], destination.ins[0]], verbose=False)

    extra = patch.delete_get_extra_cords(source.__dict__["_dict"]["box"]["id"])
    assert len(extra) == 1
    assert extra[0] == [source.outs[0], destination.ins[0]]

    assert destination.ins[0].sources == [source.outs[0]]
    assert source.outs[0].destinations == [destination.ins[0]]


def test_delete_objs_remove_objects_and_report_missing(
    capsys: CaptureFixture[str],
) -> None:
    """Verify remove by id handles both present and missing entries."""
    patch = MaxPatch(verbose=False)
    left = patch.place("toggle", verbose=False)[0]
    right = patch.place("number", verbose=False)[0]
    patch.connect([left.outs[0], right.ins[0]], verbose=False)

    patch.delete_objs(left.__dict__["_dict"]["box"]["id"], verbose=True)

    assert left.__dict__["_dict"]["box"]["id"] not in patch.objs
    assert right.ins[0].sources == []
    assert patch.num_objs == 1

    patch.delete_objs("not-found", verbose=True)
    assert "delete error: not-found not in patch" in capsys.readouterr().out


def test_delete_cords_updates_connections_and_silently_skips_missing(
    capsys: CaptureFixture[str],
) -> None:
    """Verify deleting cords drops endpoints and handles missing ones safely."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    patch.connect([source.outs[0], destination.ins[0], [1.0, 2.0]], verbose=False)

    patch.delete_cords([source.outs[0], destination.ins[0]], verbose=True)
    assert destination.ins[0].sources == []
    assert source.outs[0].destinations == []
    assert "disconnected:" in capsys.readouterr().out


def test_delete_removes_attachments_and_objects_in_one_call(
    capsys: CaptureFixture[str],
) -> None:
    """Verify combined object/cord deletion keeps structure consistent."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    target = patch.place("number", verbose=False)[0]
    patch.connect([source.outs[0], target.ins[0]], verbose=False)

    patch.delete(
        objs=["not-in-patch"],
        cords=[[source.outs[0], target.ins[0]]],
        verbose=True,
    )
    output = capsys.readouterr().out
    assert "delete error: not-in-patch not in patch" in output
    assert target.ins[0].sources == []
    assert source.__dict__["_dict"]["box"]["id"] in patch.objs
    assert target.__dict__["_dict"]["box"]["id"] in patch.objs

    patch.delete(
        objs=[target.__dict__["_dict"]["box"]["id"]],
        cords=[],
        verbose=True,
    )
    assert target.__dict__["_dict"]["box"]["id"] not in patch.objs


def test_delete_requires_string_identifiers() -> None:
    """Non-string object identifiers should trigger an assertion."""
    patch = MaxPatch(verbose=False)
    assert patch.delete_get_extra_cords("missing") == []
    with pytest.raises(
        AssertionError,
        match="objects to delete must be given as strings",
    ):
        patch.delete(objs=[123], verbose=False)


def test_delete_cords_requires_valid_pairs() -> None:
    """Cord deletion expects (Outlet, Inlet) tuples."""
    patch = MaxPatch(verbose=False)
    with pytest.raises(AssertionError, match="cords must be specified as"):
        patch.delete_cords(["wrong", "pair"], verbose=False)
