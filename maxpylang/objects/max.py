"""Generated MaxObject stubs."""

from contextlib import redirect_stdout
from io import StringIO

from maxpylang.maxobject import MaxObject

__all__ = [
    "abs_",
    "absolutepath",
    "accum",
    "acos",
    "acosh",
    "active",
    "anal",
    "append",
    "asin",
    "asinh",
    "atan",
    "atan2",
    "atanh",
    "atodb",
    "atoi",
    "attrui",
    "autopattr",
    "bag",
    "bangbang",
    "bendin",
    "bendout",
    "bgcolor",
    "bitand",
    "bitor",
    "bline",
    "bondo",
    "borax",
    "bpatcher",
    "bucket",
    "buddy",
    "button",
    "capture",
    "cartopol",
    "change",
    "chooser",
    "clip",
    "clocker",
    "closebang",
    "coll",
    "colorpicker",
    "combine",
    "comment",
    "conformpath",
    "console",
    "cos",
    "cosh",
    "counter",
    "cpuclock",
    "crosspatch",
    "ctlin",
    "ctlout",
    "cycle",
    "date",
    "dbtoa",
    "decide",
    "decode",
    "defer",
    "deferlow",
    "delay",
    "detonate",
    "dial",
    "dialog",
    "dict_",
    "dict_deserialize",
    "dict_group",
    "dict_iter",
    "dict_join",
    "dict_pack",
    "dict_print",
    "dict_route",
    "dict_serialize",
    "dict_slice",
    "dict_strip",
    "dict_unpack",
    "dict_view",
    "div",
    "dropfile",
    "drunk",
    "equals",
    "error",
    "expr",
    "filedate",
    "filein",
    "filepath",
    "filewatch",
    "float_",
    "flonum",
    "flush",
    "folder",
    "follow",
    "fontlist",
    "forward",
    "fpic",
    "freebang",
    "fromsymbol",
    "fswap",
    "ftom",
    "funbuff",
    "function",
    "funnel",
    "gate",
    "gestalt",
    "getattr_",
    "grab",
    "greaterthan",
    "greaterthaneq",
    "gswitch",
    "gswitch2",
    "hi",
    "hint",
    "histo",
    "hover",
    "if_",
    "imovie",
    "incdec",
    "inlet",
    "int_",
    "itable",
    "iter_",
    "itoa",
    "jit_cellblock",
    "join",
    "js",
    "jstrigger",
    "jsui",
    "jweb",
    "key",
    "keyup",
    "kslider",
    "lcd",
    "led",
    "lessthan",
    "lessthaneq",
    "line",
    "linedrive",
    "listfunnel",
    "loadbang",
    "loadmess",
    "logand",
    "logor",
    "makenote",
    "mappings",
    "match",
    "matrix",
    "matrixctrl",
    "maximum",
    "maxurl",
    "mc_function",
    "mc_getattr",
    "mc_line",
    "mean",
    "menubar",
    "message",
    "metro",
    "midiflush",
    "midiformat",
    "midiin",
    "midiinfo",
    "midiout",
    "midiparse",
    "minimum",
    "minus",
    "modifiers",
    "modulo",
    "mousefilter",
    "mousestate",
    "movie",
    "mpeconfig",
    "mpeformat",
    "mpeparse",
    "mtof",
    "mtr",
    "multirange",
    "multislider",
    "mxj",
    "next_",
    "nodes",
    "notein",
    "noteout",
    "notequals",
    "nrpnin",
    "nrpnout",
    "nslider",
    "number",
    "numkey",
    "offer",
    "onebang",
    "onecopy",
    "opendialog",
    "outlet",
    "pack",
    "pak",
    "panel",
    "past",
    "patcher",
    "patcherargs",
    "pattr",
    "pattrforward",
    "pattrhub",
    "pattrmarker",
    "pattrstorage",
    "pcontrol",
    "peak",
    "pgmin",
    "pgmout",
    "pictctrl",
    "pictslider",
    "pipe",
    "playbar",
    "plus",
    "poltocar",
    "poly",
    "polyin",
    "polymidiin",
    "polyout",
    "pong",
    "pow_",
    "prepend",
    "preset",
    "print_",
    "prob",
    "project",
    "pv",
    "pvar",
    "qlim",
    "qlist",
    "qmetro",
    "quickthresh",
    "radiogroup",
    "random",
    "rdiv",
    "receive",
    "regexp",
    "relativepath",
    "rminus",
    "round_",
    "route",
    "routepass",
    "router",
    "rpnin",
    "rpnout",
    "rslider",
    "rtin",
    "savebang",
    "savedialog",
    "scale",
    "screensize",
    "select",
    "send",
    "seq",
    "serial",
    "setclock",
    "shiftleft",
    "shiftright",
    "sin",
    "sinh",
    "slide",
    "slider",
    "speedlim",
    "spell",
    "split",
    "spray",
    "sprintf",
    "sqrt",
    "standalone",
    "stripnote",
    "strippath",
    "substitute",
    "suckah",
    "suspend",
    "sustain",
    "swap",
    "swatch",
    "switch",
    "sxformat",
    "sysexin",
    "tab",
    "table",
    "tan",
    "tanh",
    "tempo",
    "text",
    "textbutton",
    "textedit",
    "themecolor",
    "thispatcher",
    "thresh",
    "timepoint",
    "timer",
    "times",
    "togedge",
    "toggle",
    "tosymbol",
    "touchin",
    "touchout",
    "translate",
    "transport",
    "trigger",
    "trough",
    "ubutton",
    "udpreceive",
    "udpsend",
    "umenu",
    "universal",
    "unjoin",
    "unpack",
    "urn",
    "uzi",
    "value",
    "vdp",
    "vexpr",
    "vstscan",
    "when",
    "xbendin",
    "xbendout",
    "xctlin",
    "xctlout",
    "xmidiin",
    "xnotein",
    "xnoteout",
    "zl",
    "zl_change",
    "zl_compare",
    "zl_delace",
    "zl_ecils",
    "zl_filter",
    "zl_group",
    "zl_indexmap",
    "zl_iter",
    "zl_join",
    "zl_lace",
    "zl_len",
    "zl_lookup",
    "zl_median",
    "zl_mth",
    "zl_nth",
    "zl_queue",
    "zl_reg",
    "zl_rev",
    "zl_rot",
    "zl_scramble",
    "zl_sect",
    "zl_slice",
    "zl_sort",
    "zl_stack",
    "zl_stream",
    "zl_sub",
    "zl_sum",
    "zl_swap",
    "zl_thin",
    "zl_union",
    "zl_unique",
    "zmap",
]

_NAMES = {
    "abs_": "abs",
    "absolutepath": "absolutepath",
    "accum": "accum",
    "acos": "acos",
    "acosh": "acosh",
    "active": "active",
    "anal": "anal",
    "append": "append",
    "asin": "asin",
    "asinh": "asinh",
    "atan": "atan",
    "atan2": "atan2",
    "atanh": "atanh",
    "atodb": "atodb",
    "atoi": "atoi",
    "attrui": "attrui",
    "autopattr": "autopattr",
    "bag": "bag",
    "bangbang": "bangbang",
    "bendin": "bendin",
    "bendout": "bendout",
    "bgcolor": "bgcolor",
    "bitand": "bitand",
    "bitor": "bitor",
    "bline": "bline",
    "bondo": "bondo",
    "borax": "borax",
    "bpatcher": "bpatcher",
    "bucket": "bucket",
    "buddy": "buddy",
    "button": "button",
    "capture": "capture",
    "cartopol": "cartopol",
    "change": "change",
    "chooser": "chooser",
    "clip": "clip",
    "clocker": "clocker",
    "closebang": "closebang",
    "coll": "coll",
    "colorpicker": "colorpicker",
    "combine": "combine",
    "comment": "comment",
    "conformpath": "conformpath",
    "console": "console",
    "cos": "cos",
    "cosh": "cosh",
    "counter": "counter",
    "cpuclock": "cpuclock",
    "crosspatch": "crosspatch",
    "ctlin": "ctlin",
    "ctlout": "ctlout",
    "cycle": "cycle",
    "date": "date",
    "dbtoa": "dbtoa",
    "decide": "decide",
    "decode": "decode",
    "defer": "defer",
    "deferlow": "deferlow",
    "delay": "delay",
    "detonate": "detonate",
    "dial": "dial",
    "dialog": "dialog",
    "dict_": "dict",
    "dict_deserialize": "dict.deserialize",
    "dict_group": "dict.group",
    "dict_iter": "dict.iter",
    "dict_join": "dict.join",
    "dict_pack": "dict.pack",
    "dict_print": "dict.print",
    "dict_route": "dict.route",
    "dict_serialize": "dict.serialize",
    "dict_slice": "dict.slice",
    "dict_strip": "dict.strip",
    "dict_unpack": "dict.unpack",
    "dict_view": "dict.view",
    "div": "div",
    "dropfile": "dropfile",
    "drunk": "drunk",
    "equals": "equals",
    "error": "error",
    "expr": "expr",
    "filedate": "filedate",
    "filein": "filein",
    "filepath": "filepath",
    "filewatch": "filewatch",
    "float_": "float",
    "flonum": "flonum",
    "flush": "flush",
    "folder": "folder",
    "follow": "follow",
    "fontlist": "fontlist",
    "forward": "forward",
    "fpic": "fpic",
    "freebang": "freebang",
    "fromsymbol": "fromsymbol",
    "fswap": "fswap",
    "ftom": "ftom",
    "funbuff": "funbuff",
    "function": "function",
    "funnel": "funnel",
    "gate": "gate",
    "gestalt": "gestalt",
    "getattr_": "getattr",
    "grab": "grab",
    "greaterthan": "greaterthan",
    "greaterthaneq": "greaterthaneq",
    "gswitch": "gswitch",
    "gswitch2": "gswitch2",
    "hi": "hi",
    "hint": "hint",
    "histo": "histo",
    "hover": "hover",
    "if_": "if",
    "imovie": "imovie",
    "incdec": "incdec",
    "inlet": "inlet",
    "int_": "int",
    "itable": "itable",
    "iter_": "iter",
    "itoa": "itoa",
    "jit_cellblock": "jit.cellblock",
    "join": "join",
    "js": "js",
    "jstrigger": "jstrigger",
    "jsui": "jsui",
    "jweb": "jweb",
    "key": "key",
    "keyup": "keyup",
    "kslider": "kslider",
    "lcd": "lcd",
    "led": "led",
    "lessthan": "lessthan",
    "lessthaneq": "lessthaneq",
    "line": "line",
    "linedrive": "linedrive",
    "listfunnel": "listfunnel",
    "loadbang": "loadbang",
    "loadmess": "loadmess",
    "logand": "logand",
    "logor": "logor",
    "makenote": "makenote",
    "mappings": "mappings",
    "match": "match",
    "matrix": "matrix",
    "matrixctrl": "matrixctrl",
    "maximum": "maximum",
    "maxurl": "maxurl",
    "mc_function": "mc.function",
    "mc_getattr": "mc.getattr",
    "mc_line": "mc.line",
    "mean": "mean",
    "menubar": "menubar",
    "message": "message",
    "metro": "metro",
    "midiflush": "midiflush",
    "midiformat": "midiformat",
    "midiin": "midiin",
    "midiinfo": "midiinfo",
    "midiout": "midiout",
    "midiparse": "midiparse",
    "minimum": "minimum",
    "minus": "minus",
    "modifiers": "modifiers",
    "modulo": "modulo",
    "mousefilter": "mousefilter",
    "mousestate": "mousestate",
    "movie": "movie",
    "mpeconfig": "mpeconfig",
    "mpeformat": "mpeformat",
    "mpeparse": "mpeparse",
    "mtof": "mtof",
    "mtr": "mtr",
    "multirange": "multirange",
    "multislider": "multislider",
    "mxj": "mxj",
    "next_": "next",
    "nodes": "nodes",
    "notein": "notein",
    "noteout": "noteout",
    "notequals": "notequals",
    "nrpnin": "nrpnin",
    "nrpnout": "nrpnout",
    "nslider": "nslider",
    "number": "number",
    "numkey": "numkey",
    "offer": "offer",
    "onebang": "onebang",
    "onecopy": "onecopy",
    "opendialog": "opendialog",
    "outlet": "outlet",
    "pack": "pack",
    "pak": "pak",
    "panel": "panel",
    "past": "past",
    "patcher": "patcher",
    "patcherargs": "patcherargs",
    "pattr": "pattr",
    "pattrforward": "pattrforward",
    "pattrhub": "pattrhub",
    "pattrmarker": "pattrmarker",
    "pattrstorage": "pattrstorage",
    "pcontrol": "pcontrol",
    "peak": "peak",
    "pgmin": "pgmin",
    "pgmout": "pgmout",
    "pictctrl": "pictctrl",
    "pictslider": "pictslider",
    "pipe": "pipe",
    "playbar": "playbar",
    "plus": "plus",
    "poltocar": "poltocar",
    "poly": "poly",
    "polyin": "polyin",
    "polymidiin": "polymidiin",
    "polyout": "polyout",
    "pong": "pong",
    "pow_": "pow",
    "prepend": "prepend",
    "preset": "preset",
    "print_": "print",
    "prob": "prob",
    "project": "project",
    "pv": "pv",
    "pvar": "pvar",
    "qlim": "qlim",
    "qlist": "qlist",
    "qmetro": "qmetro",
    "quickthresh": "quickthresh",
    "radiogroup": "radiogroup",
    "random": "random",
    "rdiv": "rdiv",
    "receive": "receive",
    "regexp": "regexp",
    "relativepath": "relativepath",
    "rminus": "rminus",
    "round_": "round",
    "route": "route",
    "routepass": "routepass",
    "router": "router",
    "rpnin": "rpnin",
    "rpnout": "rpnout",
    "rslider": "rslider",
    "rtin": "rtin",
    "savebang": "savebang",
    "savedialog": "savedialog",
    "scale": "scale",
    "screensize": "screensize",
    "select": "select",
    "send": "send",
    "seq": "seq",
    "serial": "serial",
    "setclock": "setclock",
    "shiftleft": "shiftleft",
    "shiftright": "shiftright",
    "sin": "sin",
    "sinh": "sinh",
    "slide": "slide",
    "slider": "slider",
    "speedlim": "speedlim",
    "spell": "spell",
    "split": "split",
    "spray": "spray",
    "sprintf": "sprintf",
    "sqrt": "sqrt",
    "standalone": "standalone",
    "stripnote": "stripnote",
    "strippath": "strippath",
    "substitute": "substitute",
    "suckah": "suckah",
    "suspend": "suspend",
    "sustain": "sustain",
    "swap": "swap",
    "swatch": "swatch",
    "switch": "switch",
    "sxformat": "sxformat",
    "sysexin": "sysexin",
    "tab": "tab",
    "table": "table",
    "tan": "tan",
    "tanh": "tanh",
    "tempo": "tempo",
    "text": "text",
    "textbutton": "textbutton",
    "textedit": "textedit",
    "themecolor": "themecolor",
    "thispatcher": "thispatcher",
    "thresh": "thresh",
    "timepoint": "timepoint",
    "timer": "timer",
    "times": "times",
    "togedge": "togedge",
    "toggle": "toggle",
    "tosymbol": "tosymbol",
    "touchin": "touchin",
    "touchout": "touchout",
    "translate": "translate",
    "transport": "transport",
    "trigger": "trigger",
    "trough": "trough",
    "ubutton": "ubutton",
    "udpreceive": "udpreceive",
    "udpsend": "udpsend",
    "umenu": "umenu",
    "universal": "universal",
    "unjoin": "unjoin",
    "unpack": "unpack",
    "urn": "urn",
    "uzi": "uzi",
    "value": "value",
    "vdp": "vdp",
    "vexpr": "vexpr",
    "vstscan": "vstscan",
    "when": "when",
    "xbendin": "xbendin",
    "xbendout": "xbendout",
    "xctlin": "xctlin",
    "xctlout": "xctlout",
    "xmidiin": "xmidiin",
    "xnotein": "xnotein",
    "xnoteout": "xnoteout",
    "zl": "zl",
    "zl_change": "zl.change",
    "zl_compare": "zl.compare",
    "zl_delace": "zl.delace",
    "zl_ecils": "zl.ecils",
    "zl_filter": "zl.filter",
    "zl_group": "zl.group",
    "zl_indexmap": "zl.indexmap",
    "zl_iter": "zl.iter",
    "zl_join": "zl.join",
    "zl_lace": "zl.lace",
    "zl_len": "zl.len",
    "zl_lookup": "zl.lookup",
    "zl_median": "zl.median",
    "zl_mth": "zl.mth",
    "zl_nth": "zl.nth",
    "zl_queue": "zl.queue",
    "zl_reg": "zl.reg",
    "zl_rev": "zl.rev",
    "zl_rot": "zl.rot",
    "zl_scramble": "zl.scramble",
    "zl_sect": "zl.sect",
    "zl_slice": "zl.slice",
    "zl_sort": "zl.sort",
    "zl_stack": "zl.stack",
    "zl_stream": "zl.stream",
    "zl_sub": "zl.sub",
    "zl_sum": "zl.sum",
    "zl_swap": "zl.swap",
    "zl_thin": "zl.thin",
    "zl_union": "zl.union",
    "zl_unique": "zl.unique",
    "zmap": "zmap",
}

_output = StringIO()
with redirect_stdout(_output):
    abs_ = MaxObject("abs")
    abs_.__doc__ = """
    abs

    Args:
    format (number, optional)
    """

    absolutepath = MaxObject("absolutepath")
    absolutepath.__doc__ = """
    absolutepath
    """

    accum = MaxObject("accum")
    accum.__doc__ = """
    accum

    Args:
    initial (int, float, optional)
    """

    acos = MaxObject("acos")
    acos.__doc__ = """
    acos

    Args:
    initial-value (int, float, optional)
    """

    acosh = MaxObject("acosh")
    acosh.__doc__ = """
    acosh

    Args:
    initial-value (int, float, optional)
    """

    active = MaxObject("active")
    active.__doc__ = """
    active
    """

    anal = MaxObject("anal")
    anal.__doc__ = """
    anal

    Args:
    input-limit (int, optional)
    """

    append = MaxObject("append")
    append.__doc__ = """
    append

    Args:
    appended-message (any, optional)
    """

    asin = MaxObject("asin")
    asin.__doc__ = """
    asin

    Args:
    initial-value (int, float, optional)
    """

    asinh = MaxObject("asinh")
    asinh.__doc__ = """
    asinh

    Args:
    initial-value (int, float, optional)
    """

    atan = MaxObject("atan")
    atan.__doc__ = """
    atan

    Args:
    initial-value (int, float, optional)
    """

    atan2 = MaxObject("atan2")
    atan2.__doc__ = """
    atan2

    Args:
    x-value (number, optional)
    """

    atanh = MaxObject("atanh")
    atanh.__doc__ = """
    atanh

    Args:
    initial-value (int, float, optional)
    """

    atodb = MaxObject("atodb")
    atodb.__doc__ = """
    atodb
    """

    atoi = MaxObject("atoi")
    atoi.__doc__ = """
    atoi

    Attributes:
    utf8
    """

    attrui = MaxObject("attrui")
    attrui.__doc__ = """
    attrui

    Attributes:
    align, arrowcolor, attr, attr_display, attrfilter, bgcolor, bgcolor2, bordercolor,
    displaymode, htricolor, lock, menu_display, orientation, parameter_enable,
    parameter_mappable, paramonly, rounded, showcaption, storeinpreset, style,
    text_width, textcolor, textjustification, tricolor
    """

    autopattr = MaxObject("autopattr")
    autopattr.__doc__ = """
    autopattr

    Args:
    name (symbol, optional)

    Attributes:
    autoname, autorestore, dirty, greedy, name
    """

    bag = MaxObject("bag")
    bag.__doc__ = """
    bag

    Args:
    duplicate-flag (symbol, optional)
    """

    bangbang = MaxObject("bangbang")
    bangbang.__doc__ = """
    bangbang

    Args:
    outlets (number, optional)
    """

    bendin = MaxObject("bendin")
    bendin.__doc__ = """
    bendin

    Args:
    port-and-channel (symbol, required)
    channel (int, required)
    port (symbol, optional)
    midi-device (symbol, optional)

    Attributes:
    matchport, name
    """

    bendout = MaxObject("bendout")
    bendout.__doc__ = """
    bendout

    Args:
    port-and-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    midi-device (symbol, optional)

    Attributes:
    matchport, name
    """

    bgcolor = MaxObject("bgcolor")
    bgcolor.__doc__ = """
    bgcolor

    Args:
    red (int, optional)
    green (int, optional)
    blue (int, optional)
    """

    bitand = MaxObject("bitand")
    bitand.__doc__ = """
    bitand

    Args:
    initial-value (int, optional)
    """

    bitor = MaxObject("bitor")
    bitor.__doc__ = """
    bitor

    Args:
    initial-value (int, optional)
    """

    bline = MaxObject("bline")
    bline.__doc__ = """
    bline

    Args:
    initial-value (number, optional)
    """

    bondo = MaxObject("bondo")
    bondo.__doc__ = """
    bondo

    Args:
    inlets-outlets (int, optional)
    delay (int, optional)
    list-flag (symbol, optional)
    """

    borax = MaxObject("borax")
    borax.__doc__ = """
    borax
    """

    bpatcher = MaxObject("bpatcher")
    bpatcher.__doc__ = """
    bpatcher

    Attributes:
    args, bgcolor, embed, name
    """

    bucket = MaxObject("bucket")
    bucket.__doc__ = """
    bucket

    Args:
    outlets (int, optional)
    output-flag (int, optional)
    """

    buddy = MaxObject("buddy")
    buddy.__doc__ = """
    buddy

    Args:
    inlets (int, optional)
    """

    button = MaxObject("button")
    button.__doc__ = """
    button

    Attributes:
    bgcolor, blinkcolor, blinktime, fgcolor, outlinecolor, parameter_enable,
    parameter_mappable, style
    """

    capture = MaxObject("capture")
    capture.__doc__ = """
    capture

    Args:
    maximum (int, optional)
    display-format (symbol, optional)

    Attributes:
    listout, precision, size
    """

    cartopol = MaxObject("cartopol")
    cartopol.__doc__ = """
    cartopol
    """

    change = MaxObject("change")
    change.__doc__ = """
    change

    Args:
    initial-value (int, float, optional)
    mode (symbol, optional)
    """

    chooser = MaxObject("chooser")
    chooser.__doc__ = """
    chooser

    Attributes:
    autopopulate, bgcolor, collection, depth, enabledrag, factorycontent, filekind,
    filtertext, headerheight, headerlabel, items, keynavigate, margin, multiselect,
    parameter_enable, parameter_mappable, prefix, prefix_mode, preview, selectedclick,
    selectioncolor, showdotfiles, stripecolor, style, textcolor, types,
    useselectioncolor
    """

    clip = MaxObject("clip")
    clip.__doc__ = """
    clip

    Args:
    minimum (number, optional)
    maximum (number, optional)

    Attributes:
    mode
    """

    clocker = MaxObject("clocker")
    clocker.__doc__ = """
    clocker

    Args:
    time-interval (int, symbol, float, required)

    Attributes:
    active, autostart, autostarttime, defer, interval, quantize, transport
    """

    closebang = MaxObject("closebang")
    closebang.__doc__ = """
    closebang
    """

    coll = MaxObject("coll")
    coll.__doc__ = """
    coll

    Args:
    name (symbol, optional)
    no-search (any, optional)

    Attributes:
    embed, precision
    """

    colorpicker = MaxObject("colorpicker")
    colorpicker.__doc__ = """
    colorpicker

    Attributes:
    compatibility, currentcolor
    """

    combine = MaxObject("combine")
    combine.__doc__ = """
    combine

    Args:
    inlets (any, optional)

    Attributes:
    padding, triggers
    """

    comment = MaxObject("comment")
    comment.__doc__ = """
    comment

    Attributes:
    bgcolor, bubble, bubblepoint, bubbleside, bubbletextmargin, bubbleusescolors,
    style, suppressinlet, underline
    """

    conformpath = MaxObject("conformpath")
    conformpath.__doc__ = """
    conformpath

    Args:
    pathstyle (symbol, optional)
    pathtype (symbol, optional)
    """

    console = MaxObject("console")
    console.__doc__ = """
    console

    Attributes:
    classfilter, patcherfilter, showonlyerrors, textfilter
    """

    cos = MaxObject("cos")
    cos.__doc__ = """
    cos

    Args:
    initial-value (int, float, optional)
    """

    cosh = MaxObject("cosh")
    cosh.__doc__ = """
    cosh

    Args:
    initial-value (int, float, optional)
    """

    counter = MaxObject("counter")
    counter.__doc__ = """
    counter

    Args:
    options (int, optional)

    Attributes:
    carryflag, compatmode
    """

    cpuclock = MaxObject("cpuclock")
    cpuclock.__doc__ = """
    cpuclock
    """

    crosspatch = MaxObject("crosspatch")
    crosspatch.__doc__ = """
    crosspatch

    Attributes:
    allowdisabled, bgcolor, candycane, candycane2, candycane3, candycane4, candycane5,
    candycane6, candycane7, candycane8, candymode, colorlabels, connectacrossdividers,
    dividercolor, dividers, embed, exclusive, gaincaption, gaindragmode, gainradius,
    gainstyle, incolormap, initialgain, inlabels, labelheight, labelwidth, linecolor,
    maxgain, numins, numouts, outcolormap, outlabels, overgaincolor, parameter_enable,
    parameter_mappable, preservegain, showgain, showlabels, style, textcolor
    """

    ctlin = MaxObject("ctlin")
    ctlin.__doc__ = """
    ctlin

    Args:
    port (symbol, optional)
    device (symbol, optional)
    ctrllr-channel (list, optional)

    Attributes:
    matchport, name
    """

    ctlout = MaxObject("ctlout")
    ctlout.__doc__ = """
    ctlout

    Args:
    port (symbol, optional)
    device (symbol, optional)
    ctrllr-channel (list, optional)

    Attributes:
    matchport, name
    """

    cycle = MaxObject("cycle")
    cycle.__doc__ = """
    cycle

    Args:
    outlets (int, optional)
    mode (int, optional)
    """

    date = MaxObject("date")
    date.__doc__ = """
    date
    """

    dbtoa = MaxObject("dbtoa")
    dbtoa.__doc__ = """
    dbtoa
    """

    decide = MaxObject("decide")
    decide.__doc__ = """
    decide

    Args:
    seed (int, optional)
    """

    decode = MaxObject("decode")
    decode.__doc__ = """
    decode

    Args:
    outlets (int, optional)
    outlets (float, optional)
    """

    defer = MaxObject("defer")
    defer.__doc__ = """
    defer
    """

    deferlow = MaxObject("deferlow")
    deferlow.__doc__ = """
    deferlow
    """

    delay = MaxObject("delay")
    delay.__doc__ = """
    delay

    Args:
    time (any, required)

    Attributes:
    delaytime, quantize
    """

    detonate = MaxObject("detonate")
    detonate.__doc__ = """
    detonate

    Args:
    label (symbol, required)
    """

    dial = MaxObject("dial")
    dial.__doc__ = """
    dial

    Attributes:
    bgcolor, clip, degrees, fgcolor, floatoutput, min, mode, mult, needlecolor,
    outlinecolor, parameter_enable, parameter_mappable, size, style, thickness,
    vtracking
    """

    dialog = MaxObject("dialog")
    dialog.__doc__ = """
    dialog

    Args:
    label (symbol, optional)

    Attributes:
    label, mask, mode
    """

    dict_ = MaxObject("dict")
    dict_.__doc__ = """
    dict

    Args:
    name (symbol, optional)
    filename (symbol, optional)

    Attributes:
    embed, name, parameter_enable, parameter_mappable, quiet
    """

    dict_deserialize = MaxObject("dict.deserialize")
    dict_deserialize.__doc__ = """
    dict.deserialize

    Args:
    name (symbol, optional)

    Attributes:
    name
    """

    dict_group = MaxObject("dict.group")
    dict_group.__doc__ = """
    dict.group

    Args:
    name (symbol, optional)

    Attributes:
    name
    """

    dict_iter = MaxObject("dict.iter")
    dict_iter.__doc__ = """
    dict.iter
    """

    dict_join = MaxObject("dict.join")
    dict_join.__doc__ = """
    dict.join

    Args:
    default-values (list, optional)
    """

    dict_pack = MaxObject("dict.pack")
    dict_pack.__doc__ = """
    dict.pack

    Args:
    name (symbol, optional)
    default-values (list, optional)

    Attributes:
    keys, name, triggers
    """

    dict_print = MaxObject("dict.print")
    dict_print.__doc__ = """
    dict.print

    Args:
    identifier (any, optional)
    """

    dict_route = MaxObject("dict.route")
    dict_route.__doc__ = """
    dict.route

    Args:
    default-values (list, optional)
    """

    dict_serialize = MaxObject("dict.serialize")
    dict_serialize.__doc__ = """
    dict.serialize

    Attributes:
    compress, mode
    """

    dict_slice = MaxObject("dict.slice")
    dict_slice.__doc__ = """
    dict.slice

    Attributes:
    keys
    """

    dict_strip = MaxObject("dict.strip")
    dict_strip.__doc__ = """
    dict.strip

    Args:
    keys (list, optional)

    Attributes:
    keys
    """

    dict_unpack = MaxObject("dict.unpack")
    dict_unpack.__doc__ = """
    dict.unpack

    Args:
    name (symbol, optional)
    default-values (list, optional)

    Attributes:
    keys
    """

    dict_view = MaxObject("dict.view")
    dict_view.__doc__ = """
    dict.view

    Attributes:
    bgcolor, stripecolor, style, textcolor
    """

    div = MaxObject("div")
    div.__doc__ = """
    div

    Args:
    initial (int, float, optional)
    """

    dropfile = MaxObject("dropfile")
    dropfile.__doc__ = """
    dropfile

    Attributes:
    border, bordercolor, folderslash, rounded, types
    """

    drunk = MaxObject("drunk")
    drunk.__doc__ = """
    drunk

    Args:
    maximum value (int, optional)
    step size (int, optional)
    """

    equals = MaxObject("equals")
    equals.__doc__ = """
    equals

    Args:
    comparison-value (int, float, optional)

    Attributes:
    fuzzy
    """

    error = MaxObject("error")
    error.__doc__ = """
    error

    Args:
    on (int, optional)
    """

    expr = MaxObject("expr")
    expr.__doc__ = """
    expr

    Args:
    expression (list, required)
    constant (number, required)
    inlet-format (symbol, required)
    table-info (, required)
    (other) (symbol, required)
    """

    filedate = MaxObject("filedate")
    filedate.__doc__ = """
    filedate
    """

    filein = MaxObject("filein")
    filein.__doc__ = """
    filein

    Args:
    filename (symbol, optional)
    spool (symbol, optional)
    """

    filepath = MaxObject("filepath")
    filepath.__doc__ = """
    filepath

    Args:
    path-type (symbol, required)
    preference (int, optional)
    """

    filewatch = MaxObject("filewatch")
    filewatch.__doc__ = """
    filewatch

    Args:
    filename (symbol, optional)
    """

    float_ = MaxObject("float")
    float_.__doc__ = """
    float

    Args:
    initial-value (float, optional)
    """

    flonum = MaxObject("flonum")
    flonum.__doc__ = """
    flonum

    Attributes:
    bgcolor, bordercolor, cantchange, hbgcolor, htextcolor, htricolor, maximum,
    minimum, mouseup, numdecimalplaces, outputonclick, parameter_enable, textcolor,
    triangle, tricolor, triscale
    """

    flush = MaxObject("flush")
    flush.__doc__ = """
    flush
    """

    folder = MaxObject("folder")
    folder.__doc__ = """
    folder

    Args:
    pathname (symbol, optional)
    """

    follow = MaxObject("follow")
    follow.__doc__ = """
    follow

    Args:
    filename (symbol, optional)
    """

    fontlist = MaxObject("fontlist")
    fontlist.__doc__ = """
    fontlist

    Args:
    font-type (symbol, optional)
    """

    forward = MaxObject("forward")
    forward.__doc__ = """
    forward

    Args:
    receiver (symbol, optional)
    """

    fpic = MaxObject("fpic")
    fpic.__doc__ = """
    fpic

    Attributes:
    alpha, autofit, destrect, embed, forceaspect, pic, xoffset, yoffset
    """

    freebang = MaxObject("freebang")
    freebang.__doc__ = """
    freebang
    """

    fromsymbol = MaxObject("fromsymbol")
    fromsymbol.__doc__ = """
    fromsymbol

    Attributes:
    separator
    """

    fswap = MaxObject("fswap")
    fswap.__doc__ = """
    fswap

    Args:
    initial (int, float, optional)
    """

    ftom = MaxObject("ftom")
    ftom.__doc__ = """
    ftom

    Args:
    format (float, optional)

    Attributes:
    base
    """

    funbuff = MaxObject("funbuff")
    funbuff.__doc__ = """
    funbuff

    Args:
    filename (symbol, optional)
    """

    function = MaxObject("function")
    function.__doc__ = """
    function

    Attributes:
    autosustain, bgcolor, bordercolor, clickadd, clickmove, clicksustain, cursor,
    cursorcolor, domain, grid, gridcolor, gridstep_x, gridstep_y, legend, linecolor,
    linethickness, mode, mousemode, mousereport, outputmode, parameter_enable,
    parameter_mappable, pointalign, pointcolor, pointsize, range, snap2grid, style,
    sustaincolor, textcolor, zoom_x, zoom_y
    """

    funnel = MaxObject("funnel")
    funnel.__doc__ = """
    funnel

    Args:
    inlets (int, optional)
    offset (int, optional)
    """

    gate = MaxObject("gate")
    gate.__doc__ = """
    gate

    Args:
    outlets (int, optional)
    initial-state (int, optional)
    """

    gestalt = MaxObject("gestalt")
    gestalt.__doc__ = """
    gestalt

    Attributes:
    outputmode, selector
    """

    getattr_ = MaxObject("getattr")
    getattr_.__doc__ = """
    getattr

    Args:
    attribute (symbol, optional)

    Attributes:
    attr, listen, prefix
    """

    grab = MaxObject("grab")
    grab.__doc__ = """
    grab

    Args:
    number-of-outlets (int, optional)
    receive-name (symbol, optional)
    """

    greaterthan = MaxObject("greaterthan")
    greaterthan.__doc__ = """
    greaterthan

    Args:
    initial-comparison-value (number, optional)
    """

    greaterthaneq = MaxObject("greaterthaneq")
    greaterthaneq.__doc__ = """
    greaterthaneq

    Args:
    comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    gswitch = MaxObject("gswitch")
    gswitch.__doc__ = """
    gswitch

    Attributes:
    bgcolor, color, inputs, int, parameter_enable, parameter_mappable, style,
    switchcolor
    """

    gswitch2 = MaxObject("gswitch2")
    gswitch2.__doc__ = """
    gswitch2

    Attributes:
    bgcolor, color, int, outputs, parameter_enable, parameter_mappable, style,
    switchcolor
    """

    hi = MaxObject("hi")
    hi.__doc__ = """
    hi

    Args:
    device (symbol, optional)
    """

    hint = MaxObject("hint")
    hint.__doc__ = """
    hint

    Attributes:
    delay, enabled
    """

    histo = MaxObject("histo")
    histo.__doc__ = """
    histo

    Args:
    size (int, optional)
    """

    hover = MaxObject("hover")
    hover.__doc__ = """
    hover

    Attributes:
    mode
    """

    if_ = MaxObject("if")
    if_.__doc__ = """
    if

    Args:
    if (symbol, required)
    then, else (symbol, required)
    $i1, $f1, $s1 (symbol, required)
    send (symbol, required)
    out2 (symbol, required)
    """

    imovie = MaxObject("imovie")
    imovie.__doc__ = """
    imovie

    Attributes:
    autofit, border, moviedim, name
    """

    incdec = MaxObject("incdec")
    incdec.__doc__ = """
    incdec

    Attributes:
    bgcolor, bordercolor, elementcolor, fgcolor, increment, parameter_enable,
    parameter_mappable, style
    """

    inlet = MaxObject("inlet")
    inlet.__doc__ = """
    inlet

    Attributes:
    comment, cool, style, tricolor
    """

    int_ = MaxObject("int")
    int_.__doc__ = """
    int

    Args:
    initial-value (number, optional)
    """

    itable = MaxObject("itable")
    itable.__doc__ = """
    itable

    Args:
    tablename (symbol, required)

    Attributes:
    autohint, bgcolor, bgcolor2, bordercolor, embed, legend, linecolor, name,
    notename, parameter_enable, parameter_mappable, pointcolor, range, selectioncolor,
    signed, size, style, textcolor, tool
    """

    iter_ = MaxObject("iter")
    iter_.__doc__ = """
    iter
    """

    itoa = MaxObject("itoa")
    itoa.__doc__ = """
    itoa

    Attributes:
    utf8
    """

    jit_cellblock = MaxObject("jit.cellblock")
    jit_cellblock.__doc__ = """
    jit.cellblock

    Attributes:
    automouse, bblend, bgcolor, border, bordercolor, colhead, cols, colwidth,
    datadirty, fblend, fgcolor, grid, gridlinecolor, hcellcolor, headercolor, hscroll,
    hsync, interval, just, neverdirty, outmode, precision, readonly, rowhead,
    rowheight, rows, savemode, sccolor, selmode, selsync, sgcolor, signalmode,
    signalusecols, stcolor, textcolor, vscroll, vsync
    """

    join = MaxObject("join")
    join.__doc__ = """
    join

    Args:
    inlets (int, required)

    Attributes:
    triggers
    """

    js = MaxObject("js")
    js.__doc__ = """
    js

    Args:
    filename (symbol, optional)
    inlets-outlets (list, optional)
    jsarguments (list, optional)

    Attributes:
    parameter_enable, parameter_mappable
    """

    jstrigger = MaxObject("jstrigger")
    jstrigger.__doc__ = """
    jstrigger

    Args:
    sequential-Javascript-instructions (symbol, number, required)
    """

    jsui = MaxObject("jsui")
    jsui.__doc__ = """
    jsui

    Attributes:
    border, filename, jsarguments, nofsaa, parameter_enable, parameter_mappable
    """

    jweb = MaxObject("jweb")
    jweb.__doc__ = """
    jweb

    Attributes:
    rendermode, url
    """

    key = MaxObject("key")
    key.__doc__ = """
    key
    """

    keyup = MaxObject("keyup")
    keyup.__doc__ = """
    keyup
    """

    kslider = MaxObject("kslider")
    kslider.__doc__ = """
    kslider

    Attributes:
    blackkeycolor, bordercolor, hkeycolor, inputmode, mode, offset, parameter_enable,
    parameter_mappable, range, selectioncolor, style, whitekeycolor
    """

    lcd = MaxObject("lcd")
    lcd.__doc__ = """
    lcd

    Attributes:
    bgtransparent, border, enablesprites, idle, local
    """

    led = MaxObject("led")
    led.__doc__ = """
    led

    Attributes:
    bgcolor, blinktime, offcolor, oncolor, parameter_enable, parameter_mappable,
    style, thickness, useoffcolor
    """

    lessthan = MaxObject("lessthan")
    lessthan.__doc__ = """
    lessthan

    Args:
    initial-comparison-value (number, optional)
    """

    lessthaneq = MaxObject("lessthaneq")
    lessthaneq.__doc__ = """
    lessthaneq

    Args:
    intitial-value (number, optional)

    Attributes:
    fuzzy
    """

    line = MaxObject("line")
    line.__doc__ = """
    line

    Args:
    initial (number, optional)
    grain (number, optional)

    Attributes:
    compatmode, floatoutput, grain, maxpoints
    """

    linedrive = MaxObject("linedrive")
    linedrive.__doc__ = """
    linedrive

    Args:
    input (number, required)
    output (number, required)
    curve (number, required)
    delay (int, required)
    """

    listfunnel = MaxObject("listfunnel")
    listfunnel.__doc__ = """
    listfunnel

    Args:
    offset (int, optional)
    """

    loadbang = MaxObject("loadbang")
    loadbang.__doc__ = """
    loadbang
    """

    loadmess = MaxObject("loadmess")
    loadmess.__doc__ = """
    loadmess

    Args:
    message (symbol, required)

    Attributes:
    defer
    """

    logand = MaxObject("logand")
    logand.__doc__ = """
    logand

    Args:
    comparison-value (int, optional)
    """

    logor = MaxObject("logor")
    logor.__doc__ = """
    logor

    Args:
    comparison-value (int, optional)
    """

    makenote = MaxObject("makenote")
    makenote.__doc__ = """
    makenote

    Args:
    velocity (number, optional)
    duration (number, optional)
    channel (number, optional)

    Attributes:
    duration, repeatmode
    """

    mappings = MaxObject("mappings")
    mappings.__doc__ = """
    mappings

    Attributes:
    file
    """

    match = MaxObject("match")
    match.__doc__ = """
    match

    Args:
    match-list (list, required)
    """

    matrix = MaxObject("matrix")
    matrix.__doc__ = """
    matrix

    Args:
    number-of-inputs (int, optional)
    number-of-outputs (int, optional)
    default-connect-gain (float, optional)

    Attributes:
    defaultgain, inhibit, inrange, outscale, scalemode
    """

    matrixctrl = MaxObject("matrixctrl")
    matrixctrl.__doc__ = """
    matrixctrl

    Attributes:
    active, autosize, bgcolor, bkgndpict, cellpict, clickedimage, clickvalue, color,
    columns, dialmode, dialtracking, elementcolor, horizontalmargin,
    horizontalspacing, imagemask, inactiveimage, invisiblebkgnd, one/column,
    one/matrix, one/row, parameter_enable, parameter_mappable, range, rows, scale,
    style, verticalmargin, verticalspacing
    """

    maximum = MaxObject("maximum")
    maximum.__doc__ = """
    maximum

    Args:
    initial (int, float, optional)
    """

    maxurl = MaxObject("maxurl")
    maxurl.__doc__ = """
    maxurl

    Args:
    thread count (int, optional)
    """

    mc_function = MaxObject("mc.function")
    mc_function.__doc__ = """
    mc.function

    Attributes:
    autosustain, bgcolor, bordercolor, candycane, candycane2, candycane3, candycane4,
    candycane5, candycane6, candycane7, candycane8, chans, clickadd, clickinactive,
    clickmove, clicksustain, cursor, cursorcolor, displaychan, domain, grid,
    gridcolor, gridstep_x, gridstep_y, legend, linecolor, linethickness, mode,
    mousemode, mousereport, outputmode, parameter_enable, parameter_mappable,
    pointalign, pointcolor, pointsize, range, snap2grid, style, sustaincolor,
    textcolor, zoom_x, zoom_y
    """

    mc_getattr = MaxObject("mc.getattr")
    mc_getattr.__doc__ = """
    mc.getattr

    Args:
    attribute (symbol, optional)

    Attributes:
    attr, listen, prefix
    """

    mc_line = MaxObject("mc.line")
    mc_line.__doc__ = """
    mc.line

    Args:
    initial (number, optional)
    grain (number, optional)

    Attributes:
    compatmode, floatoutput, grain, maxpoints
    """

    mean = MaxObject("mean")
    mean.__doc__ = """
    mean
    """

    menubar = MaxObject("menubar")
    menubar.__doc__ = """
    menubar

    Args:
    display and behavior (int, optional)
    """

    message = MaxObject("message")
    message.__doc__ = """
    message

    Attributes:
    bgcolor, bgcolor2, bgfillcolor, dontreplace, gradient, style
    """

    metro = MaxObject("metro")
    metro.__doc__ = """
    metro

    Args:
    interval (number, optional)

    Attributes:
    active, autostart, autostarttime, defer, interval, quantize, transport
    """

    midiflush = MaxObject("midiflush")
    midiflush.__doc__ = """
    midiflush
    """

    midiformat = MaxObject("midiformat")
    midiformat.__doc__ = """
    midiformat

    Args:
    initial-MIDI-channel-number (int, optional)
    initial-MIDI-channel-number (float, optional)

    Attributes:
    hires
    """

    midiin = MaxObject("midiin")
    midiin.__doc__ = """
    midiin

    Args:
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    midiinfo = MaxObject("midiinfo")
    midiinfo.__doc__ = """
    midiinfo

    Attributes:
    autopollcontrollers, autopollinput, autopolloutput
    """

    midiout = MaxObject("midiout")
    midiout.__doc__ = """
    midiout

    Args:
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    midiparse = MaxObject("midiparse")
    midiparse.__doc__ = """
    midiparse

    Attributes:
    hires
    """

    minimum = MaxObject("minimum")
    minimum.__doc__ = """
    minimum

    Args:
    initial (int, float, optional)
    """

    minus = MaxObject("minus")
    minus.__doc__ = """
    minus

    Args:
    initial (number, optional)
    """

    modifiers = MaxObject("modifiers")
    modifiers.__doc__ = """
    modifiers

    Args:
    rate (int, optional)
    """

    modulo = MaxObject("modulo")
    modulo.__doc__ = """
    modulo

    Args:
    initial-value (int, optional)
    """

    mousefilter = MaxObject("mousefilter")
    mousefilter.__doc__ = """
    mousefilter
    """

    mousestate = MaxObject("mousestate")
    mousestate.__doc__ = """
    mousestate
    """

    movie = MaxObject("movie")
    movie.__doc__ = """
    movie

    Args:
    filename (symbol, optional)

    Attributes:
    autofit, border, name
    """

    mpeconfig = MaxObject("mpeconfig")
    mpeconfig.__doc__ = """
    mpeconfig

    Attributes:
    chanrange, masterchan
    """

    mpeformat = MaxObject("mpeformat")
    mpeformat.__doc__ = """
    mpeformat

    Args:
    channels (int, required)

    Attributes:
    chanrange, masterchan, zone
    """

    mpeparse = MaxObject("mpeparse")
    mpeparse.__doc__ = """
    mpeparse

    Attributes:
    hires, index, strict
    """

    mtof = MaxObject("mtof")
    mtof.__doc__ = """
    mtof

    Attributes:
    base
    """

    mtr = MaxObject("mtr")
    mtr.__doc__ = """
    mtr

    Args:
    tracks (int, optional)

    Attributes:
    autostart, autostarttime, bindto, embed, length, loop, mode, nextmode, quantize,
    selection, speed, sync, trackspeed, transport
    """

    multirange = MaxObject("multirange")
    multirange.__doc__ = """
    multirange

    Attributes:
    bgcolor, color, domain, elementcolor, legend, parameter_enable,
    parameter_mappable, range, style, textcolor
    """

    multislider = MaxObject("multislider")
    multislider.__doc__ = """
    multislider

    Attributes:
    bgcolor, border_bottom, border_left, border_right, border_top, bordercolor,
    candicane2, candicane3, candicane4, candicane5, candicane6, candicane7,
    candicane8, candycane, compatibility, contdata, drawpeaks, ghostbar, orientation,
    parameter_enable, parameter_mappable, peakcolor, setminmax, setstyle, settype,
    signed, size, slidercolor, spacing, style, thickness
    """

    mxj = MaxObject("mxj")
    mxj.__doc__ = """
    mxj

    Args:
    Java-class (symbol, required)
    attributes (list, required)
    """

    next_ = MaxObject("next")
    next_.__doc__ = """
    next
    """

    nodes = MaxObject("nodes")
    nodes.__doc__ = """
    nodes

    Attributes:
    bgcolor, bordercolor, candycane, candycane2, candycane3, candycane4, candycane5,
    candycane6, candycane7, candycane8, clickmoveinactive, disabledalpha, displayknob,
    filternodeschanges, knobbordercolor, knobcolor, knobpict, knobsize, mousemode,
    nodecolor, nodenumber, nodesnames, nsize, parameter_enable, parameter_mappable,
    pointcolor, style, textcolor, xplace, yplace
    """

    notein = MaxObject("notein")
    notein.__doc__ = """
    notein

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    noteout = MaxObject("noteout")
    noteout.__doc__ = """
    noteout

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    notequals = MaxObject("notequals")
    notequals.__doc__ = """
    notequals

    Args:
    initial-comparison-value (int, float, optional)

    Attributes:
    fuzzy
    """

    nrpnin = MaxObject("nrpnin")
    nrpnin.__doc__ = """
    nrpnin

    Args:
    param-channel (list, optional)

    Attributes:
    hires, permissive
    """

    nrpnout = MaxObject("nrpnout")
    nrpnout.__doc__ = """
    nrpnout

    Args:
    parameter-channel (list, optional)

    Attributes:
    hires, running
    """

    nslider = MaxObject("nslider")
    nslider.__doc__ = """
    nslider

    Attributes:
    bgcolor, bordercolor, clefs, fgcolor, mode, parameter_enable, parameter_mappable,
    rounded, staffs, style
    """

    number = MaxObject("number")
    number.__doc__ = """
    number

    Attributes:
    bgcolor, bordercolor, cantchange, format, hbgcolor, htextcolor, htricolor,
    maximum, minimum, mousefilter, numdecimalplaces, outputonclick, parameter_enable,
    parameter_mappable, style, textcolor, triangle, tricolor, triscale
    """

    numkey = MaxObject("numkey")
    numkey.__doc__ = """
    numkey

    Args:
    format (float, optional)
    """

    offer = MaxObject("offer")
    offer.__doc__ = """
    offer
    """

    onebang = MaxObject("onebang")
    onebang.__doc__ = """
    onebang

    Args:
    initialization (int, optional)
    """

    onecopy = MaxObject("onecopy")
    onecopy.__doc__ = """
    onecopy
    """

    opendialog = MaxObject("opendialog")
    opendialog.__doc__ = """
    opendialog

    Args:
    folder (symbol, optional)
    soundfile (symbol, optional)
    file-types (symbol, optional)
    """

    outlet = MaxObject("outlet")
    outlet.__doc__ = """
    outlet

    Attributes:
    comment, style, tricolor
    """

    pack = MaxObject("pack")
    pack.__doc__ = """
    pack

    Args:
    list-elements (any, optional)
    """

    pak = MaxObject("pak")
    pak.__doc__ = """
    pak

    Args:
    list-elements (any, optional)
    """

    panel = MaxObject("panel")
    panel.__doc__ = """
    panel

    Attributes:
    angle, arrow_orientation, bgcolor, bgfillcolor, border, bordercolor, drag_window,
    grad1, grad2, horizontal_direction, mode, rounded, shadow, shape, style,
    vertical_direction
    """

    past = MaxObject("past")
    past.__doc__ = """
    past

    Args:
    list (list, required)
    number (int, required)
    """

    patcher = MaxObject("patcher")
    patcher.__doc__ = """
    patcher

    Args:
    subpatch (symbol, optional)

    Attributes:
    accentcolor, assistshowspatchername, bgcolor, bgfillcolor, bottomtoolbarpinned,
    boxanimatetime, clearcolor, color, defaultfocusbox, description, digest,
    editing_bgcolor, elementcolor, enablehscroll, enabletransparentbgwithtitlebar,
    enablevscroll, filepath, fontface, fontname, fontsize, globalpatchername,
    gridonopen, gridsize, gridsnaponopen, helpsidebarclosed, isolateaudio,
    lefttoolbarpinned, locked_bgcolor, objectsnaponopen, openinpresentation, openrect,
    patchlinecolor, righttoolbarpinned, selectioncolor, showontab, stripecolor, style,
    subpatcher_template, tags, tallnewobj, textcolor, textcolor_inverse,
    textjustification, title, toolbarvisible, toptoolbarpinned, workspacedisabled
    """

    patcherargs = MaxObject("patcherargs")
    patcherargs.__doc__ = """
    patcherargs

    Args:
    defaults (int, symbol, float, required)
    """

    pattr = MaxObject("pattr")
    pattr.__doc__ = """
    pattr

    Args:
    name (symbol, optional)

    Attributes:
    autorestore, bindto, default_active, default_interp, default_priority, dirty,
    initial, invisible, parameter_enable, parameter_mappable, thru, type
    """

    pattrforward = MaxObject("pattrforward")
    pattrforward.__doc__ = """
    pattrforward

    Args:
    target (symbol, optional)

    Attributes:
    send
    """

    pattrhub = MaxObject("pattrhub")
    pattrhub.__doc__ = """
    pattrhub

    Attributes:
    patcher
    """

    pattrmarker = MaxObject("pattrmarker")
    pattrmarker.__doc__ = """
    pattrmarker

    Args:
    name (symbol, required)

    Attributes:
    invisible, name
    """

    pattrstorage = MaxObject("pattrstorage")
    pattrstorage.__doc__ = """
    pattrstorage

    Args:
    name (symbol, optional)

    Attributes:
    activewritemode, autopattr_vis, autorestore, autowatch, backupmode, changemode,
    client_rect, dirty, fileusagemode, flat, greedy, notifymode, outputmode,
    parameter_enable, parameter_mappable, paraminitmode, savemode, storage_rect,
    subscribemode
    """

    pcontrol = MaxObject("pcontrol")
    pcontrol.__doc__ = """
    pcontrol
    """

    peak = MaxObject("peak")
    peak.__doc__ = """
    peak

    Args:
    format (float, optional)
    """

    pgmin = MaxObject("pgmin")
    pgmin.__doc__ = """
    pgmin

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name, zerobased
    """

    pgmout = MaxObject("pgmout")
    pgmout.__doc__ = """
    pgmout

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name, zerobased
    """

    pictctrl = MaxObject("pictctrl")
    pictctrl.__doc__ = """
    pictctrl

    Attributes:
    active, clickedimage, clickincrement, clip, degrees, frames, imagemask,
    inactiveimage, mode, multiplier, name, offset, parameter_enable,
    parameter_mappable, range, ratio, snap, threshold, trackcircular, trackhorizontal,
    tracking, trackvertical
    """

    pictslider = MaxObject("pictslider")
    pictslider.__doc__ = """
    pictslider

    Attributes:
    active, bgcolor, bkgnddrag, bkgndpict, bkgndsize, bottommargin, bottomvalue,
    clickedimage, color, elementcolor, horizontaltracking, imagemask, inactiveimage,
    invisiblebkgnd, jump, knobpict, leftmargin, leftvalue, movehorizontal,
    movevertical, parameter_enable, parameter_mappable, rightmargin, rightvalue,
    scaleknob, style, topmargin, topvalue, verticaltracking
    """

    pipe = MaxObject("pipe")
    pipe.__doc__ = """
    pipe

    Args:
    initialization (list, optional)

    Attributes:
    clock, delaytime, quantize
    """

    playbar = MaxObject("playbar")
    playbar.__doc__ = """
    playbar

    Attributes:
    bgcolor, color, disabledcolor, hideloop, hiderwff, refreshrate, selectioncolor,
    style
    """

    plus = MaxObject("plus")
    plus.__doc__ = """
    plus

    Args:
    initial (int, float, optional)
    """

    poltocar = MaxObject("poltocar")
    poltocar.__doc__ = """
    poltocar
    """

    poly = MaxObject("poly")
    poly.__doc__ = """
    poly

    Args:
    voices (number, optional)
    steal-mode (int, optional)
    """

    polyin = MaxObject("polyin")
    polyin.__doc__ = """
    polyin

    Args:
    port-channel (list, required)
    key-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    polymidiin = MaxObject("polymidiin")
    polymidiin.__doc__ = """
    polymidiin
    """

    polyout = MaxObject("polyout")
    polyout.__doc__ = """
    polyout

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    pong = MaxObject("pong")
    pong.__doc__ = """
    pong

    Args:
    low-value (float, optional)
    high-value (float, optional)

    Attributes:
    mode, range
    """

    pow_ = MaxObject("pow")
    pow_.__doc__ = """
    pow

    Args:
    exponent (int, float, optional)
    """

    prepend = MaxObject("prepend")
    prepend.__doc__ = """
    prepend

    Args:
    message (symbol, required)
    """

    preset = MaxObject("preset")
    preset.__doc__ = """
    preset

    Attributes:
    active1, active2, bgcolor, bordercolor, bubblesize, circlecolor, clicked1,
    clicked2, embed, emptycolor, margin, paramonly, pattrstorage, showtrack, spacing,
    stored1, stored2, style, textcolor
    """

    print_ = MaxObject("print")
    print_.__doc__ = """
    print

    Args:
    identifier (any, optional)

    Attributes:
    deltatime, floatprecision, level, popup, time
    """

    prob = MaxObject("prob")
    prob.__doc__ = """
    prob

    Attributes:
    embed
    """

    project = MaxObject("project")
    project.__doc__ = """
    project

    Attributes:
    amxdtype, autolocalize, autoorganize, browsertext, devpath, devpathtype,
    hideprojectwindow, readonly, showdependencies, sortmode
    """

    pv = MaxObject("pv")
    pv.__doc__ = """
    pv

    Args:
    name (symbol, required)
    message (any, optional)
    """

    pvar = MaxObject("pvar")
    pvar.__doc__ = """
    pvar

    Args:
    object-name (symbol, optional)
    number-of-outlets (int, optional)
    """

    qlim = MaxObject("qlim")
    qlim.__doc__ = """
    qlim

    Args:
    minimum (int, required)

    Attributes:
    defer, quantize, threshold, usurp
    """

    qlist = MaxObject("qlist")
    qlist.__doc__ = """
    qlist
    """

    qmetro = MaxObject("qmetro")
    qmetro.__doc__ = """
    qmetro

    Args:
    interval (number, optional)

    Attributes:
    active, autostart, autostarttime, defer, interval, quantize, transport
    """

    quickthresh = MaxObject("quickthresh")
    quickthresh.__doc__ = """
    quickthresh

    Args:
    threshold (number, optional)
    fudge (number, optional)
    extension (number, optional)
    """

    radiogroup = MaxObject("radiogroup")
    radiogroup.__doc__ = """
    radiogroup

    Attributes:
    activecolor, bgcolor, elementcolor, enabled, flagmode, inactive, inactivecolor,
    itemtype, offset, parameter_enable, parameter_mappable, selection, shape, size,
    style
    """

    random = MaxObject("random")
    random.__doc__ = """
    random

    Args:
    range (int, optional)
    seed (int, optional)

    Attributes:
    classic
    """

    rdiv = MaxObject("rdiv")
    rdiv.__doc__ = """
    rdiv

    Args:
    divisor (number, optional)
    """

    receive = MaxObject("receive")
    receive.__doc__ = """
    receive

    Args:
    name (symbol, optional)
    """

    regexp = MaxObject("regexp")
    regexp.__doc__ = """
    regexp

    Args:
    expression (symbol, optional)
    substitution (symbol, optional)

    Attributes:
    re, substitute, tosymbol
    """

    relativepath = MaxObject("relativepath")
    relativepath.__doc__ = """
    relativepath
    """

    rminus = MaxObject("rminus")
    rminus.__doc__ = """
    rminus

    Args:
    value (int, float, optional)
    """

    round_ = MaxObject("round")
    round_.__doc__ = """
    round

    Args:
    multiple (number, optional)

    Attributes:
    nearest
    """

    route = MaxObject("route")
    route.__doc__ = """
    route

    Args:
    selectors (any, optional)
    """

    routepass = MaxObject("routepass")
    routepass.__doc__ = """
    routepass

    Args:
    selectors (any, optional)
    """

    router = MaxObject("router")
    router.__doc__ = """
    router

    Args:
    inlets (int, required)
    outlets (int, required)
    """

    rpnin = MaxObject("rpnin")
    rpnin.__doc__ = """
    rpnin

    Args:
    param-channel (list, optional)

    Attributes:
    hires, permissive
    """

    rpnout = MaxObject("rpnout")
    rpnout.__doc__ = """
    rpnout

    Args:
    parameter-channel (list, optional)

    Attributes:
    hires, running
    """

    rslider = MaxObject("rslider")
    rslider.__doc__ = """
    rslider

    Attributes:
    bgcolor, bordercolor, drawline, fgcolor, floatoutput, listmode, min, mult,
    orientation, parameter_enable, parameter_mappable, size, style, thickness
    """

    rtin = MaxObject("rtin")
    rtin.__doc__ = """
    rtin

    Args:
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    savebang = MaxObject("savebang")
    savebang.__doc__ = """
    savebang
    """

    savedialog = MaxObject("savedialog")
    savedialog.__doc__ = """
    savedialog

    Args:
    filetypes (symbol, optional)
    """

    scale = MaxObject("scale")
    scale.__doc__ = """
    scale

    Args:
    input-low (number, optional)
    input-high (number, optional)
    output-low (number, optional)
    output-high (number, optional)
    exponential (float, optional)

    Attributes:
    classic
    """

    screensize = MaxObject("screensize")
    screensize.__doc__ = """
    screensize
    """

    select = MaxObject("select")
    select.__doc__ = """
    select

    Args:
    inlet (int, required)
    selectors (any, optional)

    Attributes:
    fuzzy, matchfloat
    """

    send = MaxObject("send")
    send.__doc__ = """
    send

    Args:
    name (symbol, required)
    """

    seq = MaxObject("seq")
    seq.__doc__ = """
    seq

    Args:
    filename (symbol, optional)

    Attributes:
    overridetempo, sequencetempo, tempo
    """

    serial = MaxObject("serial")
    serial.__doc__ = """
    serial

    Args:
    portname (symbol, required)
    port (symbol, optional)
    rate (int, optional)
    data (int, optional)
    stop (int, optional)
    parity (int, symbol, optional)

    Attributes:
    autoopen, baud, bufsize, chunk, databits, defer, drain, dtr, parity, poll,
    serport, stopbits, xonxoff
    """

    setclock = MaxObject("setclock")
    setclock.__doc__ = """
    setclock

    Args:
    name (symbol, required)
    mode (symbol, required)
    multiplier (float, required)
    """

    shiftleft = MaxObject("shiftleft")
    shiftleft.__doc__ = """
    shiftleft

    Args:
    initial-value (int, optional)
    """

    shiftright = MaxObject("shiftright")
    shiftright.__doc__ = """
    shiftright

    Args:
    initial-value (int, optional)
    """

    sin = MaxObject("sin")
    sin.__doc__ = """
    sin

    Args:
    initial-value (int, float, optional)
    """

    sinh = MaxObject("sinh")
    sinh.__doc__ = """
    sinh

    Args:
    initial-value (int, float, optional)
    """

    slide = MaxObject("slide")
    slide.__doc__ = """
    slide

    Args:
    slide-up (float, optional)
    slide-down-value (float, optional)
    """

    slider = MaxObject("slider")
    slider.__doc__ = """
    slider

    Attributes:
    bgcolor, bordercolor, elementcolor, floatoutput, knobcolor, knobshape, min, mult,
    orientation, parameter_enable, parameter_mappable, relative, size, style,
    thickness
    """

    speedlim = MaxObject("speedlim")
    speedlim.__doc__ = """
    speedlim

    Args:
    delta-time (int, symbol, float, optional)

    Attributes:
    defer, quantize, threshold, usurp
    """

    spell = MaxObject("spell")
    spell.__doc__ = """
    spell

    Args:
    size (int, optional)
    character (int, optional)
    """

    split = MaxObject("split")
    split.__doc__ = """
    split

    Args:
    minimum (number, required)
    maximum (number, required)
    """

    spray = MaxObject("spray")
    spray.__doc__ = """
    spray

    Args:
    outlets (int, optional)
    offset (int, optional)
    listmode (int, optional)
    """

    sprintf = MaxObject("sprintf")
    sprintf.__doc__ = """
    sprintf

    Args:
    format (symbol, required)
    symout (symbol, optional)
    """

    sqrt = MaxObject("sqrt")
    sqrt.__doc__ = """
    sqrt

    Args:
    initial (int, float, optional)
    """

    standalone = MaxObject("standalone")
    standalone.__doc__ = """
    standalone

    Attributes:
    allwindowsactive, appicon_mac, appicon_win, bundleidentifier,
    cantclosetoplevelpatchers, cefsupport, copysupport, database, gensupport,
    noloadbangdefeating, overdrive, preffilename, searchformissingfiles,
    statusvisible, usesearchpath
    """

    stripnote = MaxObject("stripnote")
    stripnote.__doc__ = """
    stripnote
    """

    strippath = MaxObject("strippath")
    strippath.__doc__ = """
    strippath
    """

    substitute = MaxObject("substitute")
    substitute.__doc__ = """
    substitute

    Args:
    match (any, optional)
    replacement (any, optional)
    mode (any, optional)
    """

    suckah = MaxObject("suckah")
    suckah.__doc__ = """
    suckah

    Attributes:
    boundmode, compatibility, outputalpha
    """

    suspend = MaxObject("suspend")
    suspend.__doc__ = """
    suspend
    """

    sustain = MaxObject("sustain")
    sustain.__doc__ = """
    sustain

    Attributes:
    repeatmode, sustain
    """

    swap = MaxObject("swap")
    swap.__doc__ = """
    swap

    Args:
    initial (number, optional)
    """

    swatch = MaxObject("swatch")
    swatch.__doc__ = """
    swatch

    Attributes:
    compatibility, parameter_enable, parameter_mappable, saturation
    """

    switch = MaxObject("switch")
    switch.__doc__ = """
    switch

    Args:
    inlets (int, optional)
    initial (int, optional)
    """

    sxformat = MaxObject("sxformat")
    sxformat.__doc__ = """
    sxformat

    Args:
    SysEx (list, required)
    """

    sysexin = MaxObject("sysexin")
    sysexin.__doc__ = """
    sysexin

    Args:
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    tab = MaxObject("tab")
    tab.__doc__ = """
    tab

    Attributes:
    activesafe, bgcolor, border, bordercolor, borderoncolor, button, clicktabcolor,
    clicktextcolor, colorselectedtext, contrastactivetab, fadetime, fadeunselect,
    gradient, hovertabcolor, hovertextcolor, htabcolor, htextcolor, margin, mode,
    multiline, parameter_enable, parameter_mappable, rounded, segmented, spacing_x,
    spacing_y, style, tabcolor, tabs, textcolor, truncate, valign
    """

    table = MaxObject("table")
    table.__doc__ = """
    table

    Args:
    name (symbol, optional)

    Attributes:
    embed, name, notename, parameter_enable, parameter_mappable, range, signed, size
    """

    tan = MaxObject("tan")
    tan.__doc__ = """
    tan

    Args:
    initial-value (int, float, optional)
    """

    tanh = MaxObject("tanh")
    tanh.__doc__ = """
    tanh

    Args:
    initial-value (int, float, optional)
    """

    tempo = MaxObject("tempo")
    tempo.__doc__ = """
    tempo

    Args:
    tempo (int, float, optional)
    """

    text = MaxObject("text")
    text.__doc__ = """
    text

    Args:
    filename (symbol, required)

    Attributes:
    precision
    """

    textbutton = MaxObject("textbutton")
    textbutton.__doc__ = """
    textbutton

    Attributes:
    active, align, bgcolor, bgoncolor, bgovercolor, bgoveroncolor, blinktime, border,
    bordercolor, borderoncolor, fontlink, legacytextcolor, mode, outputmode,
    parameter_enable, parameter_mappable, rounded, spacing_x, spacing_y, style, text,
    textcolor, texton, textoncolor, textovercolor, textoveroncolor, tosymbol,
    truncate, underline, usebgoncolor, usetextovercolor
    """

    textedit = MaxObject("textedit")
    textedit.__doc__ = """
    textedit

    Attributes:
    autoscroll, bangmode, bgcolor, border, bordercolor, clickmode, keymode, lines,
    nosymquotes, outputmode, parameter_enable, parameter_mappable, readonly, rounded,
    separator, style, tabmode, textcolor, wordwrap
    """

    themecolor = MaxObject("themecolor")
    themecolor.__doc__ = """
    themecolor

    Args:
    UI element name (symbol, required)

    Attributes:
    color
    """

    thispatcher = MaxObject("thispatcher")
    thispatcher.__doc__ = """
    thispatcher
    """

    thresh = MaxObject("thresh")
    thresh.__doc__ = """
    thresh

    Args:
    threshold (int, optional)
    threshold-time (float, optional)
    """

    timepoint = MaxObject("timepoint")
    timepoint.__doc__ = """
    timepoint

    Args:
    time (int, symbol, float, required)

    Attributes:
    time, transport
    """

    timer = MaxObject("timer")
    timer.__doc__ = """
    timer

    Attributes:
    format, transport
    """

    times = MaxObject("times")
    times.__doc__ = """
    times

    Args:
    initial (int, float, optional)
    """

    togedge = MaxObject("togedge")
    togedge.__doc__ = """
    togedge
    """

    toggle = MaxObject("toggle")
    toggle.__doc__ = """
    toggle

    Attributes:
    bgcolor, bordercolor, checkedcolor, parameter_enable, parameter_mappable, style,
    thickness, uncheckedcolor
    """

    tosymbol = MaxObject("tosymbol")
    tosymbol.__doc__ = """
    tosymbol

    Attributes:
    separator
    """

    touchin = MaxObject("touchin")
    touchin.__doc__ = """
    touchin

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    touchout = MaxObject("touchout")
    touchout.__doc__ = """
    touchout

    Args:
    port-channel (list, required)
    channel (int, required)
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    translate = MaxObject("translate")
    translate.__doc__ = """
    translate

    Args:
    input-format (symbol, optional)
    output-format (symbol, optional)

    Attributes:
    in, listen, mode, out, transport
    """

    transport = MaxObject("transport")
    transport.__doc__ = """
    transport

    Attributes:
    clocksource, name, resetbarcount, tempo
    """

    trigger = MaxObject("trigger")
    trigger.__doc__ = """
    trigger

    Args:
    formats (symbol, optional)
    constant (any, optional)
    """

    trough = MaxObject("trough")
    trough.__doc__ = """
    trough

    Args:
    value (float, optional)
    """

    ubutton = MaxObject("ubutton")
    ubutton.__doc__ = """
    ubutton

    Attributes:
    dragtrack, hilite, hltcolor, parameter_enable, parameter_mappable, rounded, stay,
    toggle
    """

    udpreceive = MaxObject("udpreceive")
    udpreceive.__doc__ = """
    udpreceive

    Args:
    port (int, required)
    full-packet (symbol, optional)

    Attributes:
    quiet
    """

    udpsend = MaxObject("udpsend")
    udpsend.__doc__ = """
    udpsend

    Args:
    host (symbol, required)
    port (int, required)
    """

    umenu = MaxObject("umenu")
    umenu.__doc__ = """
    umenu

    Attributes:
    align, allowdrag, applycolors, arrow, arrowbgcolor, arrowcolor, arrowframe,
    arrowlink, autopopulate, bgcolor, bgcolor2, bgfillcolor, collection, color, depth,
    discolor, elementcolor, framecolor, hltcolor, items, labelclick, menumode,
    parameter_enable, parameter_mappable, pattrmode, prefix, prefix_mode, rounded,
    showdotfiles, style, textcolor, textcolor2, togcolor, truncate, types, underline
    """

    universal = MaxObject("universal")
    universal.__doc__ = """
    universal

    Args:
    mode (int, optional)

    Attributes:
    descend
    """

    unjoin = MaxObject("unjoin")
    unjoin.__doc__ = """
    unjoin

    Args:
    outlets (int, required)

    Attributes:
    outsize
    """

    unpack = MaxObject("unpack")
    unpack.__doc__ = """
    unpack

    Args:
    list-elements (any, optional)
    """

    urn = MaxObject("urn")
    urn.__doc__ = """
    urn

    Args:
    limit (int, optional)
    seed (int, optional)
    """

    uzi = MaxObject("uzi")
    uzi.__doc__ = """
    uzi

    Args:
    initial (int, optional)
    base (int, optional)
    """

    value = MaxObject("value")
    value.__doc__ = """
    value

    Args:
    name (symbol, required)
    initial (any, optional)
    """

    vdp = MaxObject("vdp")
    vdp.__doc__ = """
    vdp
    """

    vexpr = MaxObject("vexpr")
    vexpr.__doc__ = """
    vexpr

    Args:
    expression (list, required)
    constant (number, required)
    format (symbol, required)
    table (symbol, required)
    (other) (symbol, required)

    Attributes:
    maxsize, scalarmode
    """

    vstscan = MaxObject("vstscan")
    vstscan.__doc__ = """
    vstscan
    """

    when = MaxObject("when")
    when.__doc__ = """
    when

    Args:
    transport (symbol, required)

    Attributes:
    transport
    """

    xbendin = MaxObject("xbendin")
    xbendin.__doc__ = """
    xbendin

    Args:
    channel (int, optional)
    xbendin2 (symbol, optional)
    """

    xbendout = MaxObject("xbendout")
    xbendout.__doc__ = """
    xbendout

    Args:
    xbendout2 (symbol, required)
    channel (int, optional)
    """

    xctlin = MaxObject("xctlin")
    xctlin.__doc__ = """
    xctlin

    Args:
    ctrllr-channel (list, optional)

    Attributes:
    lsbfirst
    """

    xctlout = MaxObject("xctlout")
    xctlout.__doc__ = """
    xctlout

    Args:
    ctrllr-channel (list, optional)

    Attributes:
    lsbfirst, running
    """

    xmidiin = MaxObject("xmidiin")
    xmidiin.__doc__ = """
    xmidiin

    Args:
    port (symbol, optional)
    device (symbol, optional)

    Attributes:
    matchport, name
    """

    xnotein = MaxObject("xnotein")
    xnotein.__doc__ = """
    xnotein

    Args:
    channel (int, optional)
    """

    xnoteout = MaxObject("xnoteout")
    xnoteout.__doc__ = """
    xnoteout

    Args:
    channel (int, optional)
    """

    zl = MaxObject("zl")
    zl.__doc__ = """
    zl

    Args:
    mode (symbol, required)
    length (int, optional)
    function-int (int, optional)
    function-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_change = MaxObject("zl.change")
    zl_change.__doc__ = """
    zl.change

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_compare = MaxObject("zl.compare")
    zl_compare.__doc__ = """
    zl.compare

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_delace = MaxObject("zl.delace")
    zl_delace.__doc__ = """
    zl.delace

    Attributes:
    zlmaxsize
    """

    zl_ecils = MaxObject("zl.ecils")
    zl_ecils.__doc__ = """
    zl.ecils

    Args:
    size (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_filter = MaxObject("zl.filter")
    zl_filter.__doc__ = """
    zl.filter

    Args:
    filter (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_group = MaxObject("zl.group")
    zl_group.__doc__ = """
    zl.group

    Args:
    initial-size (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_indexmap = MaxObject("zl.indexmap")
    zl_indexmap.__doc__ = """
    zl.indexmap

    Args:
    initial-index (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_iter = MaxObject("zl.iter")
    zl_iter.__doc__ = """
    zl.iter

    Args:
    initial-size (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_join = MaxObject("zl.join")
    zl_join.__doc__ = """
    zl.join

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_lace = MaxObject("zl.lace")
    zl_lace.__doc__ = """
    zl.lace

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_len = MaxObject("zl.len")
    zl_len.__doc__ = """
    zl.len

    Attributes:
    zlmaxsize
    """

    zl_lookup = MaxObject("zl.lookup")
    zl_lookup.__doc__ = """
    zl.lookup

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_median = MaxObject("zl.median")
    zl_median.__doc__ = """
    zl.median

    Attributes:
    zlmaxsize
    """

    zl_mth = MaxObject("zl.mth")
    zl_mth.__doc__ = """
    zl.mth

    Args:
    initial-index (int, optional)
    index-sub (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_nth = MaxObject("zl.nth")
    zl_nth.__doc__ = """
    zl.nth

    Args:
    initial-index (int, optional)
    index-sub (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_queue = MaxObject("zl.queue")
    zl_queue.__doc__ = """
    zl.queue

    Attributes:
    zlmaxsize
    """

    zl_reg = MaxObject("zl.reg")
    zl_reg.__doc__ = """
    zl.reg

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_rev = MaxObject("zl.rev")
    zl_rev.__doc__ = """
    zl.rev

    Attributes:
    zlmaxsize
    """

    zl_rot = MaxObject("zl.rot")
    zl_rot.__doc__ = """
    zl.rot

    Args:
    distance (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_scramble = MaxObject("zl.scramble")
    zl_scramble.__doc__ = """
    zl.scramble

    Args:
    initial-list (list, optional)

    Attributes:
    zlmaxsize
    """

    zl_sect = MaxObject("zl.sect")
    zl_sect.__doc__ = """
    zl.sect

    Args:
    initial-list (list, required)

    Attributes:
    zlmaxsize
    """

    zl_slice = MaxObject("zl.slice")
    zl_slice.__doc__ = """
    zl.slice

    Args:
    initial-size (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_sort = MaxObject("zl.sort")
    zl_sort.__doc__ = """
    zl.sort

    Args:
    order (int, optional)

    Attributes:
    zlmaxsize
    """

    zl_stack = MaxObject("zl.stack")
    zl_stack.__doc__ = """
    zl.stack

    Attributes:
    zlmaxsize
    """

    zl_stream = MaxObject("zl.stream")
    zl_stream.__doc__ = """
    zl.stream

    Args:
    initial-length (int, required)

    Attributes:
    zlmaxsize
    """

    zl_sub = MaxObject("zl.sub")
    zl_sub.__doc__ = """
    zl.sub

    Args:
    initial-list (list, required)

    Attributes:
    zlmaxsize
    """

    zl_sum = MaxObject("zl.sum")
    zl_sum.__doc__ = """
    zl.sum

    Attributes:
    zlmaxsize
    """

    zl_swap = MaxObject("zl.swap")
    zl_swap.__doc__ = """
    zl.swap

    Args:
    initial-swap (list, required)

    Attributes:
    zlmaxsize
    """

    zl_thin = MaxObject("zl.thin")
    zl_thin.__doc__ = """
    zl.thin

    Attributes:
    zlmaxsize
    """

    zl_union = MaxObject("zl.union")
    zl_union.__doc__ = """
    zl.union

    Args:
    initial-list (list, required)

    Attributes:
    zlmaxsize
    """

    zl_unique = MaxObject("zl.unique")
    zl_unique.__doc__ = """
    zl.unique

    Args:
    initial-list (list, required)

    Attributes:
    zlmaxsize
    """

    zmap = MaxObject("zmap")
    zmap.__doc__ = """
    zmap

    Args:
    minimum-input (number, required)
    maximum-input (number, required)
    minimum-output (number, required)
    maximum-output (number, required)
    """


del _output
