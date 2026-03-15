"""Tests for patchcord operations."""

import pytest

from maxpylang import MaxObject, MaxPatch


def test_connect_records_sources_and_destinations():
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]

    patch.connect([source.outs[0], destination.ins[0], [1.0, 2.0]], verbose=False)

    assert source.outs[0].destinations == [destination.ins[0]]
    assert destination.ins[0].sources == [source.outs[0]]
    assert destination.ins[0].midpoints == [[1.0, 2.0]]


def test_check_connection_format_and_typing():
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


def test_check_connection_exists_reports_existing_and_missing(capsys):
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    missing = [source.outs[0], destination.ins[0]]

    assert patch.check_connection_exists([missing]) == []
    assert "PatchError:" in capsys.readouterr().out

    patch.connect([source.outs[0], destination.ins[0]], verbose=False)
    assert patch.check_connection_exists([missing]) == [missing]


def test_swap_patchcords_moves_existing_connections():
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
