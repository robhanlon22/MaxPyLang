"""Tests for objfuncs.makexlets helpers."""

from maxpylang import MaxObject


def test_make_xlets_and_parse_io_num_rules():
    obj = MaxObject("button")
    obj._dict["box"]["numinlets"] = 1
    obj._dict["box"]["numoutlets"] = 2
    obj._dict["box"]["outlettype"] = ["", "signal"]
    obj.make_xlets_from_self_dict()
    assert len(obj.ins) == 1
    assert [outlet.types for outlet in obj.outs] == ["any", "signal"]

    obj._args = [5, "x", 3]
    assert obj.parse_io_num([{"argtype": "n", "index": "all", "add_amt": 1}], 0) == 3
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
        == 4
    )
    assert obj.parse_io_num([{"argtype": "any", "index": 99}], 7) == 7
    assert (
        obj.parse_io_num([{"argtype": "any", "index": 0, "comparitor": "< 0"}], 9) == 9
    )


def test_update_xlet_typing_respects_defaults_and_overrides():
    trigger = MaxObject("button")
    trigger._dict["box"]["numinlets"] = 1
    trigger._dict["box"]["numoutlets"] = 1
    trigger._dict["box"]["outlettype"] = [""]
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
    assert trigger._dict["box"]["outlettype"] == ["float"]


def test_parse_io_typing_handles_default_and_dict_rules():
    obj = MaxObject("button")
    obj._args = ["b", "i", "s"]
    assert obj.parse_io_typing("signal", 2) == ["signal", "signal"]
    assert obj.parse_io_typing("trigger_out", 3) == ["bang", "int", ""]
    obj._args = ["7", "f", "x"]
    assert obj.parse_io_typing("unpack_out", 3) == ["int", "float", ""]
    assert obj.parse_io_typing(
        {"default": "any", "first": [1, "int"], "last": [1, "float"]},
        3,
    ) == ["int", "any", "float"]


def test_update_ins_outs_cleans_removed_xlets_and_connections(capsys):
    obj = MaxObject("button")
    obj._dict["box"]["numoutlets"] = 2
    obj._dict["box"]["outlettype"] = ["", ""]
    obj.make_xlets_from_self_dict()

    receiver = MaxObject("number")
    receiver.ins[0]._sources.append(obj.outs[1])
    receiver.ins[0]._midpoints.append([1.0, 2.0])
    obj.outs[1]._destinations.append(receiver.ins[0])

    obj._args = [0]
    obj.update_ins_outs(
        {"numoutlets": [{"argtype": "any", "index": 0, "type": {"default": ""}}]},
        default_info={},
    )
    assert obj.outs == []
    assert "Patchcord removed" in capsys.readouterr().out


def test_xlet_add_remove_updates_counts_and_parsing():
    obj = MaxObject("button")
    obj._dict["box"]["numoutlets"] = 1
    obj._dict["box"]["outlettype"] = [""]
    obj.make_xlets_from_self_dict()

    obj.add_xlets(2, "numoutlets")
    assert len(obj.outs) == 3
    obj.remove_xlets(2, "numoutlets")
    assert len(obj.outs) == 1

    obj._dict["box"]["numinlets"] = 3
    obj._dict["box"]["numoutlets"] = 1
    obj.make_xlets_from_self_dict()
    obj._args = [2, "x"]
    obj.update_ins_outs(
        {
            "numinlets": [{"argtype": "n", "index": 0, "type": {"default": ""}}],
            "numoutlets": [{"argtype": "any", "index": "all", "type": {"default": ""}}],
        },
        default_info={},
    )
    assert len(obj.ins) == 2
    assert len(obj.outs) == 2


def test_remove_xlets_detaches_sources_from_removed_inlets(capsys):
    source = MaxObject("button")
    target = MaxObject("button")
    target._dict["box"]["numinlets"] = 2
    target._dict["box"]["numoutlets"] = 1
    target._dict["box"]["outlettype"] = [""]
    target.make_xlets_from_self_dict()

    source.outs[0]._destinations.append(target.ins[1])
    target.ins[1]._sources.append(source.outs[0])
    target.ins[1]._midpoints.append(None)

    target.remove_xlets(1, "numinlets")

    assert source.outs[0].destinations == []
    assert "Patchcord removed" in capsys.readouterr().out


def test_update_ins_outs_updates_vst_save_state():
    obj = MaxObject("button")
    obj._name = "vst~"
    obj._args = [2]
    obj._dict["box"]["numoutlets"] = 1
    obj._dict["box"]["outlettype"] = [""]
    obj._dict["box"]["save"] = ["prefix", ";"]
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

    assert obj._dict["box"]["numoutlets"] == 2
    assert obj._dict["box"]["save"] == ["prefix", 2, ";"]
