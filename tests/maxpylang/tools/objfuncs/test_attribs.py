"""Tests for objfuncs.attribs helpers."""

from types import SimpleNamespace

from maxpylang import MaxObject


def test_add_and_get_extra_attribs():
    obj = MaxObject("button")
    obj.add_extra_attribs({"presentation": 1})
    extra = obj.get_extra_attribs()
    assert extra["presentation"] == 1


def test_remove_bad_attribs_filtering_and_messages(capsys):
    obj = MaxObject("message")
    cleaned = obj.remove_bad_attribs(
        {
            "fontsize": 12,
            "unknown": ["x"],
            "patching_rect": [1, 2],
            "empty": [],
            "wrong_type": ["large"],
        },
        [
            {"name": "fontsize", "type": "float", "size": 1},
            {"name": "patching_rect", "type": "float", "size": 4},
            {"name": "COMMON"},
            {"name": "wrong_type", "type": "float", "size": 1},
        ],
    )
    assert cleaned == {"fontsize": 12, "empty": []}
    attrib_output = capsys.readouterr().out
    assert "not a valid attribute argument" in attrib_output
    assert "requires 4 arguments" in attrib_output
    assert "requires arguments of type float" in attrib_output
    assert "no argument given for attribute empty" in attrib_output


def test_remove_bad_attribs_accepts_string_sizes_and_keeps_valid_scalar_fields():
    obj = MaxObject("message")
    cleaned = obj.remove_bad_attribs(
        {
            "good": [1],
            "noval": [],
            "bad": [1],
            "small": [1],
            "wrong": ["x"],
        },
        [
            {"name": "good", "type": "int", "size": "1"},
            {"name": "small", "type": "int", "size": "2"},
            {"name": "wrong", "type": "int", "size": "1"},
        ],
    )
    assert cleaned == {"good": [1], "noval": []}


def test_get_all_valid_attribs_with_common_box_fields():
    obj = MaxObject("message")
    attrib_specs = [
        {"name": "fontsize", "type": "float", "size": 1},
        {"name": "COMMON"},
    ]
    text_attribs, extra_attribs = obj.get_all_valid_attribs(
        {"fontsize": ["14"]},
        {"patching_rect": [1, 2, 3, 4], "bogus": ["x"]},
        attrib_specs,
    )
    assert text_attribs == {"fontsize": ["14"]}
    assert extra_attribs["patching_rect"] == [1, 2, 3, 4]
    assert "bogus" not in extra_attribs


def test_retain_attribs_calls_edit_with_other_attribs():
    source = SimpleNamespace(get_extra_attribs=lambda: {"presentation": 2})
    target = MaxObject("message")
    called = {}

    def fake_edit(**kwargs):
        called.update(kwargs)

    target.edit = fake_edit
    target.retain_attribs(source)
    assert called == {"presentation": 2}
