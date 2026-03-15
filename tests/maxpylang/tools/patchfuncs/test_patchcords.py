"""Tests for patch cord operations."""

import pytest
from _pytest.capture import CaptureFixture

from maxpylang import MaxObject, MaxPatch


def test_connect_records_sources_and_destinations() -> None:
    """Verify connection updates source and destination endpoint lists."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]

    patch.connect([source.outs[0], destination.ins[0], [1.0, 2.0]], verbose=False)

    assert source.outs[0].destinations == [destination.ins[0]]
    assert destination.ins[0].sources == [source.outs[0]]
    assert destination.ins[0].midpoints == [[1.0, 2.0]]


def test_check_connection_format_and_typing() -> None:
    """Verify connection format assertions and typing validation."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    connection = [source.outs[0], destination.ins[0]]

    patch.connect(*[connection], verbose=False)
    assert patch.check_connection_typing([connection]) == [connection]

    patch.check_connection_format([connection])
    with pytest.raises(AssertionError):
        patch.check_connection_format([("bad", destination.ins[0], [])])
    with pytest.raises(AssertionError):
        patch.check_connection_format([("bad", destination.ins[0])])
    with pytest.raises(AssertionError):
        patch.check_connection_format([["bad", destination.ins[0], []]])


def test_check_connection_exists_reports_existing_and_missing(
    capsys: CaptureFixture[str],
) -> None:
    """Verify checks distinguish missing and existing connections."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    missing = [source.outs[0], destination.ins[0]]

    assert patch.check_connection_exists([missing]) == []
    assert "PatchError:" in capsys.readouterr().out

    patch.connect([source.outs[0], destination.ins[0]], verbose=False)
    assert patch.check_connection_exists([missing]) == [missing]


def test_check_connection_format_requires_midpoint_list() -> None:
    """Optional midpoint entries must be lists, not scalars."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    with pytest.raises(
        AssertionError,
        match="optional midpoints must be specified as list",
    ):
        patch.check_connection_format([[source.outs[0], destination.ins[0], "bad"]])


def test_swap_patchcords_moves_existing_connections() -> None:
    """Verify swapping a patch object rewires existing patchcord references."""
    patch = MaxPatch(verbose=False)
    old = patch.place("toggle", verbose=False)[0]
    source = patch.place("number", verbose=False)[0]
    destination = patch.place("message hello", verbose=False)[0]
    patch.connect(
        [source.outs[0], old.ins[0]],
        [old.outs[0], destination.ins[0]],
        verbose=False,
    )

    new = MaxObject("button")
    patch.swap_patchcords(new, old)
    assert source.outs[0].destinations[0].parent is new
    assert new.outs[0].destinations[0].parent is destination
