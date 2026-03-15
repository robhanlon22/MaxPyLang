"""Tests for patch object placement helpers."""

import pytest

from maxpylang import MaxObject, MaxPatch
from maxpylang.exceptions import UnknownObjectWarning


def test_place_check_args_rejects_invalid_inputs(capsys):
    patch = MaxPatch(verbose=False)

    with pytest.raises(AssertionError):
        patch.place_check_args(("button",), False, 1, None, None, "grid", "bad", None)
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button", "toggle"), True, 1, None, [1.0], "grid", [1, 1], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("button",), False, 1, None, None, "diagonal", [1, 1], None
        )

    num_objs, starting_pos = patch.place_check_args(
        ("button", "toggle"),
        True,
        [3],
        None,
        [0.5, 0.5],
        "random",
        [1, 1],
        "bad",
    )
    assert num_objs == 3
    assert starting_pos is None
    assert "starting position must be [x, y]" in capsys.readouterr().out


def test_place_check_args_handles_seeded_random_warning(capsys):
    patch = MaxPatch(verbose=False)
    num_objs, _ = patch.place_check_args(
        ("button", "toggle"), True, [3], 1, [0.5, 0.5], "random", [1, 1], None
    )
    assert num_objs == 3
    assert (
        "warning: randpick only uses the first element of num_objs to determine the number of objects picked"
        in capsys.readouterr().out
    )


def test_place_pick_objs_expands_and_randomly_selects():
    patch = MaxPatch(verbose=False)
    assert patch.place_pick_objs(
        ["toggle", "button"], False, [1, 2], None, None, False
    ) == [
        "toggle",
        "button",
        "button",
    ]

    picks = patch.place_pick_objs(["toggle", "button"], True, 4, 3, [0.5, 0.5], False)
    assert len(picks) == 4
    assert set(picks).issubset({"toggle", "button"})

    random_without_seed = patch.place_pick_objs(
        ["button", "toggle"], True, 2, None, [0.5, 0.5], False
    )
    assert len(random_without_seed) == 2


def test_place_check_args_supports_defaults_and_rejects_more_modes():
    patch = MaxPatch(verbose=False)

    assert patch.place_check_args(
        ("toggle",), False, None, None, None, "grid", [10, 20], [1, 2]
    ) == (1, [1, 2])
    assert (
        patch.place_check_args(
            ("toggle",), True, None, None, None, "random", [10, 20], None
        )[0]
        == 1
    )

    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, [1, 2], None, None, "grid", [10, 20], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, 1, None, None, "vertical", [10, 20], None
        )
    with pytest.raises(AssertionError):
        patch.place_check_args(
            ("toggle",), False, 1, None, None, "bogus", [10, 20], None
        )


def test_place_check_args_supports_custom_spacing_modes():
    patch = MaxPatch(verbose=False)

    custom_counts, custom_positions = patch.place_check_args(
        ("button", "toggle"),
        False,
        [1, 2],
        None,
        None,
        "custom",
        [[1, 1], [2, 2], [3, 3]],
        None,
    )
    assert custom_counts == [1, 2]
    assert custom_positions is None

    rand_custom_counts, _ = patch.place_check_args(
        ("button", "toggle"),
        True,
        2,
        None,
        [0.5, 0.5],
        "custom",
        [[1, 1], [2, 2]],
        None,
    )
    assert rand_custom_counts == 2


def test_place_main_layout_methods():
    patch = MaxPatch(verbose=False)

    grid = patch.place(
        "button",
        "toggle",
        num_objs=[1, 2],
        spacing_type="grid",
        spacing=[10, 10],
        verbose=False,
    )
    assert len(grid) == 3

    custom = patch.place(
        "number", spacing_type="custom", spacing=[[1, 2]], verbose=False
    )
    assert custom[0]._dict["box"]["patching_rect"][:2] == [1, 2]

    vertical = patch.place(
        "message", spacing_type="vertical", spacing=15, verbose=False
    )
    assert vertical[0]._dict["box"]["patching_rect"][1] == patch.curr_position[1]

    random = patch.place(
        "toggle", randpick=True, seed=1, spacing_type="random", verbose=False
    )
    assert random[0].name == "toggle"

    random_weighted = patch.place(
        "toggle",
        "button",
        randpick=True,
        num_objs=[2],
        seed=1,
        weights=[0.5, 0.5],
        spacing_type="random",
        verbose=False,
    )
    assert len(random_weighted) == 2

    seeded_in_place = patch.place(
        "toggle",
        randpick=True,
        num_objs=1,
        seed=None,
        spacing_type="random",
        verbose=False,
    )[0]
    assert seeded_in_place.name == "toggle"


def test_place_wraps_when_canvas_is_small():
    patch = MaxPatch(verbose=False)
    patch._patcher_dict["patcher"]["rect"][2] = 15
    patch.place_grid(["button", "toggle"], [10, 10], verbose=False)
    assert patch.curr_position == [10.0, 30.0]


def test_place_obj_and_get_obj_from_spec(capsys):
    patch = MaxPatch(verbose=False)
    placed = patch.place_obj("toggle", position=[1.0, 2.0], verbose=False)
    assert placed._dict["box"]["id"] == "obj-1"
    assert placed._dict["box"]["patching_rect"][:2] == [1.0, 2.0]
    assert placed.name == "toggle"

    assert patch.get_obj_from_spec("number").name == "number"
    assert patch.get_obj_from_spec(MaxObject("button")).name == "button"

    with pytest.raises(AssertionError):
        patch.get_obj_from_spec(object())

    with pytest.warns(UnknownObjectWarning, match="Unknown Max object"):
        unknown = patch.place("not-a-real-object", verbose=True)
    assert unknown[0].notknown() is True
