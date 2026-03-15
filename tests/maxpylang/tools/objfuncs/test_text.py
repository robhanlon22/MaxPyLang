"""Tests for objfuncs.text helpers."""

from maxpylang import MaxObject


def test_parse_text_splits_name_args_and_attribs() -> None:
    """Verify parse_text returns parsed name, args, and text attributes."""
    obj = MaxObject("message")
    name, args, text_attribs = obj.parse_text("message 1 2.5 hello @size 3 4")

    assert name == "message"
    assert args == [1, 2.5, "hello"]
    assert text_attribs == {"size": ["3", "4"]}


def test_parse_text_keeps_empty_attribute_values() -> None:
    """Verify attribute flags without values are preserved as empty arrays."""
    obj = MaxObject("message")
    name, args, text_attribs = obj.parse_text("message 1 2.5 hello @size")

    assert name == "message"
    assert args == [1, 2.5, "hello"]
    assert text_attribs == {"size": []}


def test_update_and_get_text_roundtrip() -> None:
    """Verify attribute updates are reflected in serialized object text."""
    obj = MaxObject("message")
    obj.edit(text="message 1 hello @fontsize 12 @style", text_add="replace")

    assert obj.get_text() == " 1 hello @fontsize 12 @style"
    obj.update_text()
    assert obj.raw_dict["box"]["text"] == " 1 hello @fontsize 12 @style"
