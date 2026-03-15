"""Tests for objfuncs.text helpers."""

from maxpylang import MaxObject


def test_parse_text_splits_name_args_and_attribs():
    obj = MaxObject("message")
    name, args, text_attribs = obj.parse_text("message 1 2.5 hello @size 3 4")

    assert name == "message"
    assert args == [1, 2.5, "hello"]
    assert text_attribs == {"size": ["3", "4"]}


def test_parse_text_keeps_empty_attribute_values():
    obj = MaxObject("message")
    name, args, text_attribs = obj.parse_text("message 1 2.5 hello @size")

    assert name == "message"
    assert args == [1, 2.5, "hello"]
    assert text_attribs == {"size": []}


def test_update_and_get_text_roundtrip():
    obj = MaxObject("button")
    obj._name = "message"
    obj._args = [1, "hello"]
    obj._text_attribs = {"fontsize": ["12"], "style": None}

    assert obj.get_text() == " 1 hello @fontsize 12 @style"
    obj.update_text()
    assert obj._dict["box"]["text"] == " 1 hello @fontsize 12 @style"
