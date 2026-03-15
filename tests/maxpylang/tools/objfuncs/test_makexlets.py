"""Tests for objfuncs.makexlets helpers."""

from _pytest.capture import CaptureFixture

from maxpylang import MaxObject

_NUM_INLETS = 1
_NUM_OUTLETS = 2
_NUM_CONNECTIONS = 2
_INDEX_ALL = "all"
_DEFAULT_INLET_COUNT = 2
_ADD_AMOUNT = 1
_INDEX_OUT_OF_RANGE = 99
_NEGATIVE_COMPARE_NUM = 9
_FALLBACK_COMPARE_NUM = 7
_FILLER_COUNT = 4
_SECOND_DEFAULT_COUNT = 2
_OUT_OF_RANGE_INDEX = 7


def test_make_xlets_and_parse_io_num_rules() -> None:
    """Verify inlet/outlet generation and numeric parsing rules."""
    obj = MaxObject("button")
    obj.__dict__["_dict"]["box"]["numinlets"] = _NUM_INLETS
    obj.__dict__["_dict"]["box"]["numoutlets"] = _NUM_OUTLETS
    obj.__dict__["_dict"]["box"]["outlettype"] = ["", "signal"]
    obj.make_xlets_from_self_dict()
    assert len(obj.ins) == _NUM_INLETS
    assert [outlet.types for outlet in obj.outs] == ["any", "signal"]

    obj.__dict__["_args"] = [5, "x", _DEFAULT_INLET_COUNT]
    assert (
        obj.parse_io_num(
            [{"argtype": "n", "index": _INDEX_ALL, "add_amt": _ADD_AMOUNT}], 0
        )
        == _FILLER_COUNT
    )
    assert (
        obj.parse_io_num(
            [
                {
                    "argtype": "any",
                    "index": 0,
                    "acc_vals": [1, 4, 8],
                    "comparitor": "> 0",
                }
            ],
            0,
        )
        == _FILLER_COUNT
    )
    assert (
        obj.parse_io_num(
            [{"argtype": "any", "index": _INDEX_OUT_OF_RANGE}], _OUT_OF_RANGE_INDEX
        )
        == _OUT_OF_RANGE_INDEX
    )
    assert (
        obj.parse_io_num(
            [{"argtype": "any", "index": 0, "comparitor": "< 0"}], _NEGATIVE_COMPARE_NUM
        )
        == _FALLBACK_COMPARE_NUM
    )


def test_update_xlet_typing_respects_defaults_and_overrides() -> None:
    """Verify default and override types flow through outlet typing."""
    trigger = MaxObject("button")
    trigger.__dict__["_dict"]["box"]["numinlets"] = _NUM_INLETS
    trigger.__dict__["_dict"]["box"]["numoutlets"] = 1
    trigger.__dict__["_dict"]["box"]["outlettype"] = [""]
    trigger.make_xlets_from_self_dict()
    trigger.update_xlet_typing(
        {
            "numinlets": [{}],
            "numoutlets": [{"type": {"default": "", "last": [1, "float"]}}],
        },
        "numoutlets",
        1,
    )
    assert trigger.outs[0].types == "float"
    assert trigger.__dict__["_dict"]["box"]["outlettype"] == ["float"]


def test_parse_io_typing_handles_default_and_dict_rules() -> None:
    """Verify io typing supports symbolic and numeric parsing."""
    obj = MaxObject("button")
    obj.__dict__["_args"] = ["b", "i", "s"]
    assert obj.parse_io_typing("signal", 2) == ["signal", "signal"]
    assert obj.parse_io_typing("trigger_out", 3) == ["bang", "int", ""]
    obj.__dict__["_args"] = ["7", "f", "x"]
    assert obj.parse_io_typing("unpack_out", 3) == ["int", "float", ""]
    assert obj.parse_io_typing(
        {"default": "any", "first": [1, "int"], "last": [1, "float"]},
        3,
    ) == ["int", "any", "float"]


def test_update_ins_outs_cleans_removed_xlets_and_connections(
    capsys: CaptureFixture[str],
) -> None:
    """Verify removed xlets and their cord references are cleaned."""
    obj = MaxObject("button")
    obj.__dict__["_dict"]["box"]["numoutlets"] = 2
    obj.__dict__["_dict"]["box"]["outlettype"] = ["", ""]
    obj.make_xlets_from_self_dict()

    receiver = MaxObject("number")
    receiver.ins[0].__dict__["_sources"].append(obj.outs[1])
    receiver.ins[0].__dict__["_midpoints"].append([1.0, 2.0])
    obj.outs[1].__dict__["_destinations"].append(receiver.ins[0])

    obj.__dict__["_args"] = [0]
    obj.update_ins_outs(
        {"numoutlets": [{"argtype": "any", "index": 0, "type": {"default": ""}}]},
        default_info={},
    )
    assert obj.outs == []
    assert "Patchcord removed" in capsys.readouterr().out


def test_xlet_add_remove_updates_counts_and_parsing() -> None:
    """Verify explicit add/remove xlet operations update counts."""
    obj = MaxObject("button")
    obj.__dict__["_dict"]["box"]["numoutlets"] = 1
    obj.__dict__["_dict"]["box"]["outlettype"] = [""]
    obj.make_xlets_from_self_dict()

    obj.add_xlets(2, "numoutlets")
    assert len(obj.outs) == _NUM_CONNECTIONS + 1
    obj.remove_xlets(2, "numoutlets")
    assert len(obj.outs) == 1

    obj.__dict__["_dict"]["box"]["numinlets"] = 3
    obj.__dict__["_dict"]["box"]["numoutlets"] = 1
    obj.make_xlets_from_self_dict()
    obj.__dict__["_args"] = [2, "x"]
    obj.update_ins_outs(
        {
            "numinlets": [{"argtype": "n", "index": 0, "type": {"default": ""}}],
            "numoutlets": [
                {"argtype": "any", "index": _INDEX_ALL, "type": {"default": ""}}
            ],
        },
        default_info={},
    )
    assert len(obj.ins) == _SECOND_DEFAULT_COUNT
    assert len(obj.outs) == _SECOND_DEFAULT_COUNT


def test_remove_xlets_detaches_sources_from_removed_inlets(
    capsys: CaptureFixture[str],
) -> None:
    """Verify removing inlets detaches attached source connections."""
    source = MaxObject("button")
    target = MaxObject("button")
    target.__dict__["_dict"]["box"]["numinlets"] = 2
    target.__dict__["_dict"]["box"]["numoutlets"] = 1
    target.__dict__["_dict"]["box"]["outlettype"] = [""]
    target.make_xlets_from_self_dict()

    source.outs[0].__dict__["_destinations"].append(target.ins[1])
    target.ins[1].__dict__["_sources"].append(source.outs[0])
    target.ins[1].__dict__["_midpoints"].append(None)

    target.remove_xlets(1, "numinlets")

    assert source.outs[0].destinations == []
    assert "Patchcord removed" in capsys.readouterr().out


def test_update_ins_outs_updates_vst_save_state() -> None:
    """Verify vst save list updates when outlets are updated."""
    obj = MaxObject("button")
    obj.__dict__["_name"] = "vst~"
    obj.__dict__["_args"] = [2]
    obj.__dict__["_dict"]["box"]["numoutlets"] = 1
    obj.__dict__["_dict"]["box"]["outlettype"] = [""]
    obj.__dict__["_dict"]["box"]["save"] = ["prefix", ";"]
    obj.make_xlets_from_self_dict()

    obj.update_ins_outs(
        {
            "numoutlets": [
                {
                    "argtype": "any",
                    "index": 0,
                    "type": {"default": "", "first": [1, "int"]},
                }
            ]
        },
        default_info={},
    )

    assert obj.__dict__["_dict"]["box"]["numoutlets"] == _SECOND_DEFAULT_COUNT
    assert obj.__dict__["_dict"]["box"]["save"] == ["prefix", 2, ";"]
