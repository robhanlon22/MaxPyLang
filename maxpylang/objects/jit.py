"""Generated MaxObject stubs."""

from contextlib import redirect_stdout
from io import StringIO

from maxpylang.maxobject import MaxObject

__all__ = [
    "jit_3m",
    "jit_alphablend",
    "jit_altern",
    "jit_ameba",
    "jit_anim_drive",
    "jit_anim_node",
    "jit_anim_path",
    "jit_argb2ayuv",
    "jit_argb2grgb",
    "jit_argb2uyvy",
    "jit_avc",
    "jit_avg4",
    "jit_axis2quat",
    "jit_ayuv2argb",
    "jit_ayuv2luma",
    "jit_ayuv2uyvy",
    "jit_bfg",
    "jit_brass",
    "jit_brcosa",
    "jit_bsort",
    "jit_buffer_tilde",
    "jit_catch_tilde",
    "jit_change",
    "jit_charmap",
    "jit_chromakey",
    "jit_clip",
    "jit_coerce",
    "jit_colorspace",
    "jit_concat",
    "jit_convolve",
    "jit_conway",
    "jit_cycle",
    "jit_demultiplex",
    "jit_desktop",
    "jit_dimmap",
    "jit_dimop",
    "jit_displays",
    "jit_dx_grab",
    "jit_dx_videoout",
    "jit_eclipse",
    "jit_euler2quat",
    "jit_expr",
    "jit_fastblur",
    "jit_fft",
    "jit_fill",
    "jit_findbounds",
    "jit_fluoride",
    "jit_fprint",
    "jit_fpsgui",
    "jit_freeframe",
    "jit_gen",
    "jit_gencoord",
    "jit_gl_asyncread",
    "jit_gl_bfg",
    "jit_gl_camera",
    "jit_gl_cornerpin",
    "jit_gl_cubemap",
    "jit_gl_graph",
    "jit_gl_gridshape",
    "jit_gl_handle",
    "jit_gl_imageunit",
    "jit_gl_isosurf",
    "jit_gl_light",
    "jit_gl_lua",
    "jit_gl_material",
    "jit_gl_mesh",
    "jit_gl_model",
    "jit_gl_multiple",
    "jit_gl_node",
    "jit_gl_nurbs",
    "jit_gl_pass",
    "jit_gl_path",
    "jit_gl_physdraw",
    "jit_gl_picker",
    "jit_gl_pix",
    "jit_gl_plato",
    "jit_gl_render",
    "jit_gl_shader",
    "jit_gl_sketch",
    "jit_gl_skybox",
    "jit_gl_slab",
    "jit_gl_text",
    "jit_gl_text2d",
    "jit_gl_text3d",
    "jit_gl_texture",
    "jit_gl_videoplane",
    "jit_gl_volume",
    "jit_glop",
    "jit_glue",
    "jit_grab",
    "jit_gradient",
    "jit_graph",
    "jit_grgb2argb",
    "jit_hatch",
    "jit_hello",
    "jit_histogram",
    "jit_hsl2rgb",
    "jit_hue",
    "jit_iter",
    "jit_keyscreen",
    "jit_la_determinant",
    "jit_la_diagproduct",
    "jit_la_inverse",
    "jit_la_mult",
    "jit_la_trace",
    "jit_la_uppertri",
    "jit_lcd",
    "jit_linden",
    "jit_luma2ayuv",
    "jit_luma2uyvy",
    "jit_lumakey",
    "jit_map",
    "jit_matrix",
    "jit_matrixinfo",
    "jit_matrixset",
    "jit_mgraphics",
    "jit_movie",
    "jit_multiplex",
    "jit_mxform2d",
    "jit_net_recv",
    "jit_net_send",
    "jit_noise",
    "jit_normalize",
    "jit_obref",
    "jit_op",
    "jit_openexr",
    "jit_p_bounds",
    "jit_p_shiva",
    "jit_p_vishnu",
    "jit_pack",
    "jit_path",
    "jit_peek_tilde",
    "jit_phys_6dof",
    "jit_phys_barslide",
    "jit_phys_body",
    "jit_phys_conetwist",
    "jit_phys_ghost",
    "jit_phys_hinge",
    "jit_phys_multiple",
    "jit_phys_picker",
    "jit_phys_point2point",
    "jit_phys_world",
    "jit_pix",
    "jit_planeop",
    "jit_playlist",
    "jit_plot",
    "jit_plume",
    "jit_plur",
    "jit_poke_tilde",
    "jit_print",
    "jit_proxy",
    "jit_pwindow",
    "jit_pworld",
    "jit_qball",
    "jit_qfaker",
    "jit_qt_grab",
    "jit_qt_movie",
    "jit_qt_record",
    "jit_qt_videoout",
    "jit_quat",
    "jit_quat2axis",
    "jit_quat2euler",
    "jit_record",
    "jit_release_tilde",
    "jit_repos",
    "jit_resamp",
    "jit_reverse",
    "jit_rgb2hsl",
    "jit_rgb2luma",
    "jit_robcross",
    "jit_rota",
    "jit_roy",
    "jit_rubix",
    "jit_scalebias",
    "jit_scanoffset",
    "jit_scanslide",
    "jit_scanwrap",
    "jit_scissors",
    "jit_scope",
    "jit_shade",
    "jit_slide",
    "jit_sobel",
    "jit_spill",
    "jit_split",
    "jit_sprinkle",
    "jit_str_fromsymbol",
    "jit_str_op",
    "jit_str_regexp",
    "jit_str_tosymbol",
    "jit_streak",
    "jit_submatrix",
    "jit_textfile",
    "jit_thin",
    "jit_tiffany",
    "jit_traffic",
    "jit_transpose",
    "jit_turtle",
    "jit_uldl",
    "jit_unpack",
    "jit_uyvy2argb",
    "jit_uyvy2ayuv",
    "jit_uyvy2luma",
    "jit_vcr",
    "jit_wake",
    "jit_window",
    "jit_world",
    "jit_xfade",
    "mc_jit_peek_tilde",
]

_NAMES = {
    "jit_3m": "jit.3m",
    "jit_alphablend": "jit.alphablend",
    "jit_altern": "jit.altern",
    "jit_ameba": "jit.ameba",
    "jit_anim_drive": "jit.anim.drive",
    "jit_anim_node": "jit.anim.node",
    "jit_anim_path": "jit.anim.path",
    "jit_argb2ayuv": "jit.argb2ayuv",
    "jit_argb2grgb": "jit.argb2grgb",
    "jit_argb2uyvy": "jit.argb2uyvy",
    "jit_avc": "jit.avc",
    "jit_avg4": "jit.avg4",
    "jit_axis2quat": "jit.axis2quat",
    "jit_ayuv2argb": "jit.ayuv2argb",
    "jit_ayuv2luma": "jit.ayuv2luma",
    "jit_ayuv2uyvy": "jit.ayuv2uyvy",
    "jit_bfg": "jit.bfg",
    "jit_brass": "jit.brass",
    "jit_brcosa": "jit.brcosa",
    "jit_bsort": "jit.bsort",
    "jit_buffer_tilde": "jit.buffer~",
    "jit_catch_tilde": "jit.catch~",
    "jit_change": "jit.change",
    "jit_charmap": "jit.charmap",
    "jit_chromakey": "jit.chromakey",
    "jit_clip": "jit.clip",
    "jit_coerce": "jit.coerce",
    "jit_colorspace": "jit.colorspace",
    "jit_concat": "jit.concat",
    "jit_convolve": "jit.convolve",
    "jit_conway": "jit.conway",
    "jit_cycle": "jit.cycle",
    "jit_demultiplex": "jit.demultiplex",
    "jit_desktop": "jit.desktop",
    "jit_dimmap": "jit.dimmap",
    "jit_dimop": "jit.dimop",
    "jit_displays": "jit.displays",
    "jit_dx_grab": "jit.dx.grab",
    "jit_dx_videoout": "jit.dx.videoout",
    "jit_eclipse": "jit.eclipse",
    "jit_euler2quat": "jit.euler2quat",
    "jit_expr": "jit.expr",
    "jit_fastblur": "jit.fastblur",
    "jit_fft": "jit.fft",
    "jit_fill": "jit.fill",
    "jit_findbounds": "jit.findbounds",
    "jit_fluoride": "jit.fluoride",
    "jit_fprint": "jit.fprint",
    "jit_fpsgui": "jit.fpsgui",
    "jit_freeframe": "jit.freeframe",
    "jit_gen": "jit.gen",
    "jit_gencoord": "jit.gencoord",
    "jit_gl_asyncread": "jit.gl.asyncread",
    "jit_gl_bfg": "jit.gl.bfg",
    "jit_gl_camera": "jit.gl.camera",
    "jit_gl_cornerpin": "jit.gl.cornerpin",
    "jit_gl_cubemap": "jit.gl.cubemap",
    "jit_gl_graph": "jit.gl.graph",
    "jit_gl_gridshape": "jit.gl.gridshape",
    "jit_gl_handle": "jit.gl.handle",
    "jit_gl_imageunit": "jit.gl.imageunit",
    "jit_gl_isosurf": "jit.gl.isosurf",
    "jit_gl_light": "jit.gl.light",
    "jit_gl_lua": "jit.gl.lua",
    "jit_gl_material": "jit.gl.material",
    "jit_gl_mesh": "jit.gl.mesh",
    "jit_gl_model": "jit.gl.model",
    "jit_gl_multiple": "jit.gl.multiple",
    "jit_gl_node": "jit.gl.node",
    "jit_gl_nurbs": "jit.gl.nurbs",
    "jit_gl_pass": "jit.gl.pass",
    "jit_gl_path": "jit.gl.path",
    "jit_gl_physdraw": "jit.gl.physdraw",
    "jit_gl_picker": "jit.gl.picker",
    "jit_gl_pix": "jit.gl.pix",
    "jit_gl_plato": "jit.gl.plato",
    "jit_gl_render": "jit.gl.render",
    "jit_gl_shader": "jit.gl.shader",
    "jit_gl_sketch": "jit.gl.sketch",
    "jit_gl_skybox": "jit.gl.skybox",
    "jit_gl_slab": "jit.gl.slab",
    "jit_gl_text": "jit.gl.text",
    "jit_gl_text2d": "jit.gl.text2d",
    "jit_gl_text3d": "jit.gl.text3d",
    "jit_gl_texture": "jit.gl.texture",
    "jit_gl_videoplane": "jit.gl.videoplane",
    "jit_gl_volume": "jit.gl.volume",
    "jit_glop": "jit.glop",
    "jit_glue": "jit.glue",
    "jit_grab": "jit.grab",
    "jit_gradient": "jit.gradient",
    "jit_graph": "jit.graph",
    "jit_grgb2argb": "jit.grgb2argb",
    "jit_hatch": "jit.hatch",
    "jit_hello": "jit.hello",
    "jit_histogram": "jit.histogram",
    "jit_hsl2rgb": "jit.hsl2rgb",
    "jit_hue": "jit.hue",
    "jit_iter": "jit.iter",
    "jit_keyscreen": "jit.keyscreen",
    "jit_la_determinant": "jit.la.determinant",
    "jit_la_diagproduct": "jit.la.diagproduct",
    "jit_la_inverse": "jit.la.inverse",
    "jit_la_mult": "jit.la.mult",
    "jit_la_trace": "jit.la.trace",
    "jit_la_uppertri": "jit.la.uppertri",
    "jit_lcd": "jit.lcd",
    "jit_linden": "jit.linden",
    "jit_luma2ayuv": "jit.luma2ayuv",
    "jit_luma2uyvy": "jit.luma2uyvy",
    "jit_lumakey": "jit.lumakey",
    "jit_map": "jit.map",
    "jit_matrix": "jit.matrix",
    "jit_matrixinfo": "jit.matrixinfo",
    "jit_matrixset": "jit.matrixset",
    "jit_mgraphics": "jit.mgraphics",
    "jit_movie": "jit.movie",
    "jit_multiplex": "jit.multiplex",
    "jit_mxform2d": "jit.mxform2d",
    "jit_net_recv": "jit.net.recv",
    "jit_net_send": "jit.net.send",
    "jit_noise": "jit.noise",
    "jit_normalize": "jit.normalize",
    "jit_obref": "jit.obref",
    "jit_op": "jit.op",
    "jit_openexr": "jit.openexr",
    "jit_p_bounds": "jit.p.bounds",
    "jit_p_shiva": "jit.p.shiva",
    "jit_p_vishnu": "jit.p.vishnu",
    "jit_pack": "jit.pack",
    "jit_path": "jit.path",
    "jit_peek_tilde": "jit.peek~",
    "jit_phys_6dof": "jit.phys.6dof",
    "jit_phys_barslide": "jit.phys.barslide",
    "jit_phys_body": "jit.phys.body",
    "jit_phys_conetwist": "jit.phys.conetwist",
    "jit_phys_ghost": "jit.phys.ghost",
    "jit_phys_hinge": "jit.phys.hinge",
    "jit_phys_multiple": "jit.phys.multiple",
    "jit_phys_picker": "jit.phys.picker",
    "jit_phys_point2point": "jit.phys.point2point",
    "jit_phys_world": "jit.phys.world",
    "jit_pix": "jit.pix",
    "jit_planeop": "jit.planeop",
    "jit_playlist": "jit.playlist",
    "jit_plot": "jit.plot",
    "jit_plume": "jit.plume",
    "jit_plur": "jit.plur",
    "jit_poke_tilde": "jit.poke~",
    "jit_print": "jit.print",
    "jit_proxy": "jit.proxy",
    "jit_pwindow": "jit.pwindow",
    "jit_pworld": "jit.pworld",
    "jit_qball": "jit.qball",
    "jit_qfaker": "jit.qfaker",
    "jit_qt_grab": "jit.qt.grab",
    "jit_qt_movie": "jit.qt.movie",
    "jit_qt_record": "jit.qt.record",
    "jit_qt_videoout": "jit.qt.videoout",
    "jit_quat": "jit.quat",
    "jit_quat2axis": "jit.quat2axis",
    "jit_quat2euler": "jit.quat2euler",
    "jit_record": "jit.record",
    "jit_release_tilde": "jit.release~",
    "jit_repos": "jit.repos",
    "jit_resamp": "jit.resamp",
    "jit_reverse": "jit.reverse",
    "jit_rgb2hsl": "jit.rgb2hsl",
    "jit_rgb2luma": "jit.rgb2luma",
    "jit_robcross": "jit.robcross",
    "jit_rota": "jit.rota",
    "jit_roy": "jit.roy",
    "jit_rubix": "jit.rubix",
    "jit_scalebias": "jit.scalebias",
    "jit_scanoffset": "jit.scanoffset",
    "jit_scanslide": "jit.scanslide",
    "jit_scanwrap": "jit.scanwrap",
    "jit_scissors": "jit.scissors",
    "jit_scope": "jit.scope",
    "jit_shade": "jit.shade",
    "jit_slide": "jit.slide",
    "jit_sobel": "jit.sobel",
    "jit_spill": "jit.spill",
    "jit_split": "jit.split",
    "jit_sprinkle": "jit.sprinkle",
    "jit_str_fromsymbol": "jit.str.fromsymbol",
    "jit_str_op": "jit.str.op",
    "jit_str_regexp": "jit.str.regexp",
    "jit_str_tosymbol": "jit.str.tosymbol",
    "jit_streak": "jit.streak",
    "jit_submatrix": "jit.submatrix",
    "jit_textfile": "jit.textfile",
    "jit_thin": "jit.thin",
    "jit_tiffany": "jit.tiffany",
    "jit_traffic": "jit.traffic",
    "jit_transpose": "jit.transpose",
    "jit_turtle": "jit.turtle",
    "jit_uldl": "jit.uldl",
    "jit_unpack": "jit.unpack",
    "jit_uyvy2argb": "jit.uyvy2argb",
    "jit_uyvy2ayuv": "jit.uyvy2ayuv",
    "jit_uyvy2luma": "jit.uyvy2luma",
    "jit_vcr": "jit.vcr",
    "jit_wake": "jit.wake",
    "jit_window": "jit.window",
    "jit_world": "jit.world",
    "jit_xfade": "jit.xfade",
    "mc_jit_peek_tilde": "mc.jit.peek~",
}

_output = StringIO()
with redirect_stdout(_output):
    jit_3m = MaxObject("jit.3m")
    jit_3m.__doc__ = """
    jit.3m

    Attributes:
    max, mean, min
    """

    jit_alphablend = MaxObject("jit.alphablend")
    jit_alphablend.__doc__ = """
    jit.alphablend

    Attributes:
    mode
    """

    jit_altern = MaxObject("jit.altern")
    jit_altern.__doc__ = """
    jit.altern

    Attributes:
    bgcolor, colwidth, ignore_zero, rowheight, thresh, xinterval, yinterval
    """

    jit_ameba = MaxObject("jit.ameba")
    jit_ameba.__doc__ = """
    jit.ameba

    Attributes:
    gain, mode, x, y
    """

    jit_anim_drive = MaxObject("jit.anim.drive")
    jit_anim_drive.__doc__ = """
    jit.anim.drive

    Attributes:
    active, automatic, drawto, ease, easefunc, easein, easeout, evalreport, name,
    position, quat, scale, speed, spring_damp, spring_mass, spring_stiff,
    spring_thresh, ui_dict_layout, targetname, ui_listen, ui_map, ui_map_clone,
    ui_priority
    """

    jit_anim_node = MaxObject("jit.anim.node")
    jit_anim_node.__doc__ = """
    jit.anim.node

    Attributes:
    anchor, anim, animmode, automatic, direction, inherit_position, inherit_rotate,
    inherit_scale, invtransform, locklook, lockplane, lookat, movemode, name,
    parentpos, parentquat, parentrot, parentscale, position, quat, rotate,
    rotate_order, rotatexyz, scale, transform, tripod, turnmode, worlddir, worldpos,
    worldquat, worldrot, worldscale, worldtransform
    """

    jit_anim_path = MaxObject("jit.anim.path")
    jit_anim_path.__doc__ = """
    jit.anim.path

    Attributes:
    autohandles, automatic, closed, drawpath, drawto, duration, endreport, evalquat,
    evalreport, evalscale, interpmode, length, loop, loopreport, name, play,
    pointcount, position, quat, rate, scale, shortestrot, targetname, time, timemode
    """

    jit_argb2ayuv = MaxObject("jit.argb2ayuv")
    jit_argb2ayuv.__doc__ = """
    jit.argb2ayuv
    """

    jit_argb2grgb = MaxObject("jit.argb2grgb")
    jit_argb2grgb.__doc__ = """
    jit.argb2grgb
    """

    jit_argb2uyvy = MaxObject("jit.argb2uyvy")
    jit_argb2uyvy.__doc__ = """
    jit.argb2uyvy
    """

    jit_avc = MaxObject("jit.avc")
    jit_avc.__doc__ = """
    jit.avc
    """

    jit_avg4 = MaxObject("jit.avg4")
    jit_avg4.__doc__ = """
    jit.avg4

    Attributes:
    mode, x, y
    """

    jit_axis2quat = MaxObject("jit.axis2quat")
    jit_axis2quat.__doc__ = """
    jit.axis2quat

    Attributes:
    angleaxis, normalize, quat
    """

    jit_ayuv2argb = MaxObject("jit.ayuv2argb")
    jit_ayuv2argb.__doc__ = """
    jit.ayuv2argb
    """

    jit_ayuv2luma = MaxObject("jit.ayuv2luma")
    jit_ayuv2luma.__doc__ = """
    jit.ayuv2luma
    """

    jit_ayuv2uyvy = MaxObject("jit.ayuv2uyvy")
    jit_ayuv2uyvy.__doc__ = """
    jit.ayuv2uyvy
    """

    jit_bfg = MaxObject("jit.bfg")
    jit_bfg.__doc__ = """
    jit.bfg

    Attributes:
    align, autocenter, basis, classname, offset, origin, precision, rotation, scale,
    seed, weight
    """

    jit_brass = MaxObject("jit.brass")
    jit_brass.__doc__ = """
    jit.brass

    Attributes:
    atint, btint, gtint, mask, rtint
    """

    jit_brcosa = MaxObject("jit.brcosa")
    jit_brcosa.__doc__ = """
    jit.brcosa

    Attributes:
    brightness, contrast, saturation
    """

    jit_bsort = MaxObject("jit.bsort")
    jit_bsort.__doc__ = """
    jit.bsort

    Attributes:
    dimmode, maxiter, planemode, summode
    """

    jit_buffer_tilde = MaxObject("jit.buffer~")
    jit_buffer_tilde.__doc__ = """
    jit.buffer~

    Attributes:
    inputfirst, inputstart, outputfirst, outputlast, outputlength, outputstart,
    vizchecktime, vizfirst, vizheight, vizmode, vizlast, vizlength, vizmemoryratio,
    vizstart, vizwidth
    """

    jit_catch_tilde = MaxObject("jit.catch~")
    jit_catch_tilde.__doc__ = """
    jit.catch~

    Attributes:
    downsample, framesize, mode, trigdir, trigchan, trigthresh
    """

    jit_change = MaxObject("jit.change")
    jit_change.__doc__ = """
    jit.change

    Attributes:
    mode, report, thresh
    """

    jit_charmap = MaxObject("jit.charmap")
    jit_charmap.__doc__ = """
    jit.charmap
    """

    jit_chromakey = MaxObject("jit.chromakey")
    jit_chromakey.__doc__ = """
    jit.chromakey

    Attributes:
    alphaignore, color, fade, maxkey, minkey, mode, tol
    """

    jit_clip = MaxObject("jit.clip")
    jit_clip.__doc__ = """
    jit.clip

    Attributes:
    max, min
    """

    jit_coerce = MaxObject("jit.coerce")
    jit_coerce.__doc__ = """
    jit.coerce
    """

    jit_colorspace = MaxObject("jit.colorspace")
    jit_colorspace.__doc__ = """
    jit.colorspace

    Attributes:
    input, output
    """

    jit_concat = MaxObject("jit.concat")
    jit_concat.__doc__ = """
    jit.concat

    Attributes:
    autoclear, concatdim, mode, truncate
    """

    jit_convolve = MaxObject("jit.convolve")
    jit_convolve.__doc__ = """
    jit.convolve

    Attributes:
    boundmode, origin
    """

    jit_conway = MaxObject("jit.conway")
    jit_conway.__doc__ = """
    jit.conway

    Attributes:
    birthmark, deathmask, lifemask, neighborhood
    """

    jit_cycle = MaxObject("jit.cycle")
    jit_cycle.__doc__ = """
    jit.cycle

    Attributes:
    index, hi, mode, lo
    """

    jit_demultiplex = MaxObject("jit.demultiplex")
    jit_demultiplex.__doc__ = """
    jit.demultiplex

    Attributes:
    autoclear, demultiplexdim, scan_a, scan_b
    """

    jit_desktop = MaxObject("jit.desktop")
    jit_desktop.__doc__ = """
    jit.desktop

    Attributes:
    rect
    """

    jit_dimmap = MaxObject("jit.dimmap")
    jit_dimmap.__doc__ = """
    jit.dimmap

    Attributes:
    invert, map
    """

    jit_dimop = MaxObject("jit.dimop")
    jit_dimop.__doc__ = """
    jit.dimop

    Attributes:
    op, step
    """

    jit_displays = MaxObject("jit.displays")
    jit_displays.__doc__ = """
    jit.displays

    Attributes:
    resetmode
    """

    jit_dx_grab = MaxObject("jit.dx.grab")
    jit_dx_grab.__doc__ = """
    jit.dx.grab

    Attributes:
    backlight, bitrate, brightness, channels, colorenable, colormode, contrast,
    dropreport, dstrect, format, gain, gamma, hue, input, interp, resolution,
    samplerate, saturation, sharpness, snddevice, srcrect, unique, usedstrect,
    usesrcrect, vdevice, whitebalance, write_audio, write_video
    """

    jit_dx_videoout = MaxObject("jit.dx.videoout")
    jit_dx_videoout.__doc__ = """
    jit.dx.videoout
    """

    jit_eclipse = MaxObject("jit.eclipse")
    jit_eclipse.__doc__ = """
    jit.eclipse

    Attributes:
    blue, columns, green, inv, mode, op, red, rows, thresh, tint
    """

    jit_euler2quat = MaxObject("jit.euler2quat")
    jit_euler2quat.__doc__ = """
    jit.euler2quat

    Attributes:
    euler, normalize, quat, rotate_order
    """

    jit_expr = MaxObject("jit.expr")
    jit_expr.__doc__ = """
    jit.expr

    Attributes:
    cache, expr, inputs, precision, verbose
    """

    jit_fastblur = MaxObject("jit.fastblur")
    jit_fastblur.__doc__ = """
    jit.fastblur

    Attributes:
    center, mode, range, ring, ripple
    """

    jit_fft = MaxObject("jit.fft")
    jit_fft.__doc__ = """
    jit.fft

    Attributes:
    inverse
    """

    jit_fill = MaxObject("jit.fill")
    jit_fill.__doc__ = """
    jit.fill

    Attributes:
    matrix_name, plane, offset
    """

    jit_findbounds = MaxObject("jit.findbounds")
    jit_findbounds.__doc__ = """
    jit.findbounds

    Attributes:
    boundmax, boundmin, max, min
    """

    jit_fluoride = MaxObject("jit.fluoride")
    jit_fluoride.__doc__ = """
    jit.fluoride

    Attributes:
    glow, lum, mode, tol
    """

    jit_fprint = MaxObject("jit.fprint")
    jit_fprint.__doc__ = """
    jit.fprint

    Attributes:
    default_dir, defaultdir, coldelim, planedelim, precision, rowdelim, writemode
    """

    jit_fpsgui = MaxObject("jit.fpsgui")
    jit_fpsgui.__doc__ = """
    jit.fpsgui

    Attributes:
    bgcolor, bgcolor2, bordercolor, dim, fps, htextcolor, interval, mode, ms, name,
    planecount, style, textcolor, timeout, type, usetimeout
    """

    jit_freeframe = MaxObject("jit.freeframe")
    jit_freeframe.__doc__ = """
    jit.freeframe

    Attributes:
    fx, inmode, numparams, outmode
    """

    jit_gen = MaxObject("jit.gen")
    jit_gen.__doc__ = """
    jit.gen

    Attributes:
    dirty, gen, precision, t, title
    """

    jit_gencoord = MaxObject("jit.gencoord")
    jit_gencoord.__doc__ = """
    jit.gencoord

    Attributes:
    offset, scale
    """

    jit_gl_asyncread = MaxObject("jit.gl.asyncread")
    jit_gl_asyncread.__doc__ = """
    jit.gl.asyncread

    Attributes:
    matrixoutput, mode, out_name, texture
    """

    jit_gl_bfg = MaxObject("jit.gl.bfg")
    jit_gl_bfg.__doc__ = """
    jit.gl.bfg

    Attributes:
    activeinput, adapt, basis, basis.inner, basis.outer, colorize, colormode, depth,
    dim, dimscale, displaylist, distortion, edges, file, fractal_params, inputs,
    offset, out_name, outputs, palette, rect, rectangle, scale, shape, subdiv,
    texrect, time, type, voronoi_crackle, voronoi_jitter, voronoi_shade,
    voronoi_smooth, voronoise_amt, wrap, zoom
    """

    jit_gl_camera = MaxObject("jit.gl.camera")
    jit_gl_camera.__doc__ = """
    jit.gl.camera

    Attributes:
    adapt, capture, colormask, dim, direction, drawto, erase_color, far_clip, frustum,
    fsaa, layer, lens_angle, locklook, lookat, near_clip, ortho, out_name, out_names,
    proj_matrix, projection_mode, tripod, type, view_matrix, viewport,
    viewproj_matrix, vp_mode
    """

    jit_gl_cornerpin = MaxObject("jit.gl.cornerpin")
    jit_gl_cornerpin.__doc__ = """
    jit.gl.cornerpin

    Attributes:
    colormode, corner_color, corner_radius, cornermode, displaylist, drawcorners,
    enable_mouse, hover, interp, invert_corners, lower_left, lower_right, mousereport,
    preserve_aspect, rect_tex, texturename, ui_priority, upper_left, upper_right
    """

    jit_gl_cubemap = MaxObject("jit.gl.cubemap")
    jit_gl_cubemap.__doc__ = """
    jit.gl.cubemap

    Attributes:
    adapt, autotype, bordercolor, edge_length, file, filter, level, matrix_name,
    mipmap, type, wrap
    """

    jit_gl_graph = MaxObject("jit.gl.graph")
    jit_gl_graph.__doc__ = """
    jit.gl.graph

    Attributes:
    circpoints, radial, radialphase, radialradius
    """

    jit_gl_gridshape = MaxObject("jit.gl.gridshape")
    jit_gl_gridshape.__doc__ = """
    jit.gl.gridshape

    Attributes:
    cache_mode, dim, displaylist, gridmode, rad_minor, shape
    """

    jit_gl_handle = MaxObject("jit.gl.handle")
    jit_gl_handle.__doc__ = """
    jit.gl.handle

    Attributes:
    auto_handle, auto_rotate, auto_time, filters, hilite_color, hover, radius,
    rgb_axes, select_mode, tracking, ui_priority, visible
    """

    jit_gl_imageunit = MaxObject("jit.gl.imageunit")
    jit_gl_imageunit.__doc__ = """
    jit.gl.imageunit

    Attributes:
    activeinput, adapt, colormode, dim, dimscale, fx, inputs, out_name, paramsafe,
    thru, verbose
    """

    jit_gl_isosurf = MaxObject("jit.gl.isosurf")
    jit_gl_isosurf.__doc__ = """
    jit.gl.isosurf

    Attributes:
    autocolor, autonormals, dim, displaylist, epsilon, isolevel, mode, trianglecount
    """

    jit_gl_light = MaxObject("jit.gl.light")
    jit_gl_light.__doc__ = """
    jit.gl.light

    Attributes:
    ambient, atten_const, atten_linear, atten_quad, diffuse, direction, layer, lookat,
    shadowblur, shadowquality, shadowrange, shadows, shadowtexoutname, specular,
    spot_angle, spot_falloff, type, viewproj_matrix
    """

    jit_gl_lua = MaxObject("jit.gl.lua")
    jit_gl_lua.__doc__ = """
    jit.gl.lua

    Attributes:
    args, autowatch, file, gc, inlets, last_inlet, outlets, path
    """

    jit_gl_material = MaxObject("jit.gl.material")
    jit_gl_material.__doc__ = """
    jit.gl.material

    Attributes:
    darkness, diffuse_model, diffuse_size, diffuse_smooth, drawto, fog,
    heightmap_mode, override, roughness, shadow_eps, shadow_hard, shadow_radius,
    shadow_soft, specular_model, specular_size, specular_smooth, type
    """

    jit_gl_mesh = MaxObject("jit.gl.mesh")
    jit_gl_mesh.__doc__ = """
    jit.gl.mesh

    Attributes:
    auto_bitangents, auto_colors, auto_normals, auto_tangents, cache_mode, color_mode,
    draw_mode
    """

    jit_gl_model = MaxObject("jit.gl.model")
    jit_gl_model.__doc__ = """
    jit.gl.model

    Attributes:
    animblendmode, cache_mode, displaylist, drawgroup, drawskeleton, file,
    find_instances, fix_normals, gen_normals, gen_tangents, hasbones, material_mode,
    mode, nodeaxes, normalize, numanimations, numgroups, optimize, smoothing_angle,
    verbose
    """

    jit_gl_multiple = MaxObject("jit.gl.multiple")
    jit_gl_multiple.__doc__ = """
    jit.gl.multiple

    Attributes:
    dimparam, glparams, targetmode, targetname, texture
    """

    jit_gl_node = MaxObject("jit.gl.node")
    jit_gl_node.__doc__ = """
    jit.gl.node

    Attributes:
    adapt, capture, dim, erase_color, fsaa, out_name, out_names, type
    """

    jit_gl_nurbs = MaxObject("jit.gl.nurbs")
    jit_gl_nurbs.__doc__ = """
    jit.gl.nurbs

    Attributes:
    closed, ctlshow, dim, displaylist, order
    """

    jit_gl_pass = MaxObject("jit.gl.pass")
    jit_gl_pass.__doc__ = """
    jit.gl.pass

    Attributes:
    child, depth_drawto, file, out_name, quality
    """

    jit_gl_path = MaxObject("jit.gl.path")
    jit_gl_path.__doc__ = """
    jit.gl.path

    Attributes:
    autohandles, closed, displaylist, drawhandles, endcap, evalin, evalout,
    extrudescale, interpmode, joinstyle, normgen, pathstyle, pointcount, segments,
    texscale, texturemode
    """

    jit_gl_physdraw = MaxObject("jit.gl.physdraw")
    jit_gl_physdraw.__doc__ = """
    jit.gl.physdraw

    Attributes:
    constraintsize, contactsize, draw_aabb, draw_bodies, draw_worldbox, rgb, worldname
    """

    jit_gl_picker = MaxObject("jit.gl.picker")
    jit_gl_picker.__doc__ = """
    jit.gl.picker

    Attributes:
    filters, hover, ui_priority
    """

    jit_gl_pix = MaxObject("jit.gl.pix")
    jit_gl_pix.__doc__ = """
    jit.gl.pix

    Attributes:
    activeinput, adapt, colormode, depth, dim, dimscale, dirty, displaylist, edges,
    exportfolder, file, gen, inputs, out_name, outputs, rect, rectangle, thru, shape,
    subdiv, t, texrect, title, type, wrap
    """

    jit_gl_plato = MaxObject("jit.gl.plato")
    jit_gl_plato.__doc__ = """
    jit.gl.plato

    Attributes:
    shape
    """

    jit_gl_render = MaxObject("jit.gl.render")
    jit_gl_render.__doc__ = """
    jit.gl.render

    Attributes:
    accelerated, aux_buffers, camera, copy_texture, doublebuffer, draw_buffer, drawto,
    erase_color, erase_mode, far_clip, fsaa, geom_rows, high_res, lens_angle,
    light_ambient, light_diffuse, light_global_ambient, light_position,
    light_specular, lookat, near_clip, point_atten, point_fade, primitive, quality,
    rotate_order, shared_context, stereo, sync, up, verbose
    """

    jit_gl_shader = MaxObject("jit.gl.shader")
    jit_gl_shader.__doc__ = """
    jit.gl.shader

    Attributes:
    file, verbose
    """

    jit_gl_sketch = MaxObject("jit.gl.sketch")
    jit_gl_sketch.__doc__ = """
    jit.gl.sketch

    Attributes:
    autonormal, displaylist, immediate, pushstate
    """

    jit_gl_skybox = MaxObject("jit.gl.skybox")
    jit_gl_skybox.__doc__ = """
    jit.gl.skybox

    Attributes:
    displaylist, infinite
    """

    jit_gl_slab = MaxObject("jit.gl.slab")
    jit_gl_slab.__doc__ = """
    jit.gl.slab

    Attributes:
    activeinput, adapt, colormode, depth, dim, dimscale, displaylist, edges, file,
    inputs, out_name, outputs, rect, rectangle, thru, shape, subdiv, texrect, type,
    wrap
    """

    jit_gl_text = MaxObject("jit.gl.text")
    jit_gl_text.__doc__ = """
    jit.gl.text

    Attributes:
    align, depth, floatchomp, floatplaces, fontname, fontsize, leadscale, line_length,
    mode, plane, precision, screenmode, slant, tracking, weight
    """

    jit_gl_text2d = MaxObject("jit.gl.text2d")
    jit_gl_text2d.__doc__ = """
    jit.gl.text2d

    Attributes:
    align, depth, floatchomp, floatplaces, fontname, fontsize, leadscale, line_length,
    mode, plane, precision, screenmode, slant, tracking, weight
    """

    jit_gl_text3d = MaxObject("jit.gl.text3d")
    jit_gl_text3d.__doc__ = """
    jit.gl.text3d

    Attributes:
    align, depth, floatchomp, floatplaces, fontname, fontsize, leadscale, line_length,
    mode, plane, precision, screenmode, slant, tracking, weight
    """

    jit_gl_texture = MaxObject("jit.gl.texture")
    jit_gl_texture.__doc__ = """
    jit.gl.texture

    Attributes:
    adapt, anisotropy, apply, autoclear, autoscale, blendcolor, bordercolor,
    capture_buffer, capture_depthbits, capture_source, colormode, compare_func,
    compare_mode, compress, correction, debug, defaultimage, dim, dstdimend,
    dstdimstart, erase_color, file, filter, flip, function, mipmap, mode, offset,
    operand, priority, rectangle, thru, source, srcdimend, srcdimstart, texgen,
    texture_mode, type, usedstdim, usesrcdim, weight, wrap
    """

    jit_gl_videoplane = MaxObject("jit.gl.videoplane")
    jit_gl_videoplane.__doc__ = """
    jit.gl.videoplane

    Attributes:
    client_storage, colormode, dim, displaylist, gridmode, interp, nudge,
    preserve_aspect, rect_tex, tex_offset_x, tex_offset_y, tex_scale_x, tex_scale_y,
    texturename
    """

    jit_gl_volume = MaxObject("jit.gl.volume")
    jit_gl_volume.__doc__ = """
    jit.gl.volume

    Attributes:
    bounds, clip, clipangle, clipaxis, cubes, density, displaylist, distance, ds,
    exposure, intensity, mode, raycast_adapt, raycast_dim, samples, slices
    """

    jit_glop = MaxObject("jit.glop")
    jit_glop.__doc__ = """
    jit.glop

    Attributes:
    gain, mode
    """

    jit_glue = MaxObject("jit.glue")
    jit_glue.__doc__ = """
    jit.glue

    Attributes:
    columns, syncinlet, rows
    """

    jit_grab = MaxObject("jit.grab")
    jit_grab.__doc__ = """
    jit.grab

    Attributes:
    adapt, automatic, colormode, drawto, dstrect, engine, format, framerate,
    framereport, input, interp, output_texture, srcrect, texture_name, unique,
    usedstrect, usesrcrect, vdevice
    """

    jit_gradient = MaxObject("jit.gradient")
    jit_gradient.__doc__ = """
    jit.gradient

    Attributes:
    cheby, end, start
    """

    jit_graph = MaxObject("jit.graph")
    jit_graph.__doc__ = """
    jit.graph

    Attributes:
    brgb, clearit, frgb, height, mode, rangehi, rangelo
    """

    jit_grgb2argb = MaxObject("jit.grgb2argb")
    jit_grgb2argb.__doc__ = """
    jit.grgb2argb
    """

    jit_hatch = MaxObject("jit.hatch")
    jit_hatch.__doc__ = """
    jit.hatch

    Attributes:
    bgcolor, grid, thresh
    """

    jit_hello = MaxObject("jit.hello")
    jit_hello.__doc__ = """
    jit.hello

    Attributes:
    text
    """

    jit_histogram = MaxObject("jit.histogram")
    jit_histogram.__doc__ = """
    jit.histogram

    Attributes:
    autoclear, normalize, normval
    """

    jit_hsl2rgb = MaxObject("jit.hsl2rgb")
    jit_hsl2rgb.__doc__ = """
    jit.hsl2rgb
    """

    jit_hue = MaxObject("jit.hue")
    jit_hue.__doc__ = """
    jit.hue

    Attributes:
    hue_angle
    """

    jit_iter = MaxObject("jit.iter")
    jit_iter.__doc__ = """
    jit.iter

    Attributes:
    mode
    """

    jit_keyscreen = MaxObject("jit.keyscreen")
    jit_keyscreen.__doc__ = """
    jit.keyscreen

    Attributes:
    alpha, alphatol, blue, bluetol, green, greentol, key, mask, mode, red, redtol,
    target
    """

    jit_la_determinant = MaxObject("jit.la.determinant")
    jit_la_determinant.__doc__ = """
    jit.la.determinant

    Attributes:
    thresh
    """

    jit_la_diagproduct = MaxObject("jit.la.diagproduct")
    jit_la_diagproduct.__doc__ = """
    jit.la.diagproduct
    """

    jit_la_inverse = MaxObject("jit.la.inverse")
    jit_la_inverse.__doc__ = """
    jit.la.inverse

    Attributes:
    thresh
    """

    jit_la_mult = MaxObject("jit.la.mult")
    jit_la_mult.__doc__ = """
    jit.la.mult
    """

    jit_la_trace = MaxObject("jit.la.trace")
    jit_la_trace.__doc__ = """
    jit.la.trace
    """

    jit_la_uppertri = MaxObject("jit.la.uppertri")
    jit_la_uppertri.__doc__ = """
    jit.la.uppertri

    Attributes:
    swapcount, thresh
    """

    jit_lcd = MaxObject("jit.lcd")
    jit_lcd.__doc__ = """
    jit.lcd
    """

    jit_linden = MaxObject("jit.linden")
    jit_linden.__doc__ = """
    jit.linden

    Attributes:
    boundmode, ignore, leftbranch, production, rightbranch, wildcard
    """

    jit_luma2ayuv = MaxObject("jit.luma2ayuv")
    jit_luma2ayuv.__doc__ = """
    jit.luma2ayuv
    """

    jit_luma2uyvy = MaxObject("jit.luma2uyvy")
    jit_luma2uyvy.__doc__ = """
    jit.luma2uyvy
    """

    jit_lumakey = MaxObject("jit.lumakey")
    jit_lumakey.__doc__ = """
    jit.lumakey

    Attributes:
    ascale, bscale, fade, gscale, lum, maxkey, minkey, mode, rscale, tol
    """

    jit_map = MaxObject("jit.map")
    jit_map.__doc__ = """
    jit.map

    Attributes:
    clip, map
    """

    jit_matrix = MaxObject("jit.matrix")
    jit_matrix.__doc__ = """
    jit.matrix

    Attributes:
    adapt, dim, dimstride, dstdimend, dstdimstart, interp, name, planecount, planemap,
    thru, size, srcdimend, srcdimstart, usedstdim, usesrcdim, type
    """

    jit_matrixinfo = MaxObject("jit.matrixinfo")
    jit_matrixinfo.__doc__ = """
    jit.matrixinfo
    """

    jit_matrixset = MaxObject("jit.matrixset")
    jit_matrixset.__doc__ = """
    jit.matrixset

    Attributes:
    dim, dstdimend, dstdimstart, index, interp, matrixcount, planecount, planemap,
    thru, type, srcdimend, srcdimstart, usedstdim, usesrcdim
    """

    jit_mgraphics = MaxObject("jit.mgraphics")
    jit_mgraphics.__doc__ = """
    jit.mgraphics

    Attributes:
    autofill, dim, relative_coords, textfieldvisible
    """

    jit_movie = MaxObject("jit.movie")
    jit_movie.__doc__ = """
    jit.movie

    Attributes:
    adapt, automatic, autostart, cache_size, colormode, drawto, dstrect, duration,
    engine, fps, framecount, framereport, interp, loop, loopend, looppoints,
    looppoints_ms, looppoints_secs, loopreport, loopstart, milliseconds, movie_dim,
    moviedim, moviefile, moviename, moviepath, output_texture, position, rate,
    seconds, srcrect, texture_name, time, time_ms, time_secs, timescale, unique,
    usedstrect, usesrcrect, vol
    """

    jit_multiplex = MaxObject("jit.multiplex")
    jit_multiplex.__doc__ = """
    jit.multiplex

    Attributes:
    autoclear, mode, multiplexdim, scan_a, scan_b, truncate
    """

    jit_mxform2d = MaxObject("jit.mxform2d")
    jit_mxform2d.__doc__ = """
    jit.mxform2d

    Attributes:
    boundmode, interp, mxform, offset_x, offset_y
    """

    jit_net_recv = MaxObject("jit.net.recv")
    jit_net_recv.__doc__ = """
    jit.net.recv

    Attributes:
    connected, ip, port
    """

    jit_net_send = MaxObject("jit.net.send")
    jit_net_send.__doc__ = """
    jit.net.send

    Attributes:
    connected, host, ip, latency, nagle, port, report
    """

    jit_noise = MaxObject("jit.noise")
    jit_noise.__doc__ = """
    jit.noise

    Attributes:
    seed
    """

    jit_normalize = MaxObject("jit.normalize")
    jit_normalize.__doc__ = """
    jit.normalize

    Attributes:
    amp, global
    """

    jit_obref = MaxObject("jit.obref")
    jit_obref.__doc__ = """
    jit.obref
    """

    jit_op = MaxObject("jit.op")
    jit_op.__doc__ = """
    jit.op

    Attributes:
    op, val
    """

    jit_openexr = MaxObject("jit.openexr")
    jit_openexr.__doc__ = """
    jit.openexr

    Attributes:
    adjust, channels, defog, exposure, gamma, kneehigh, kneelow, normalize,
    outputfile, verbose
    """

    jit_p_bounds = MaxObject("jit.p.bounds")
    jit_p_bounds.__doc__ = """
    jit.p.bounds

    Attributes:
    bounds_hi, bounds_lo, mode, squish, squish_var
    """

    jit_p_shiva = MaxObject("jit.p.shiva")
    jit_p_shiva.__doc__ = """
    jit.p.shiva

    Attributes:
    emit, emit_var, init, init_var, life, life_var, mode
    """

    jit_p_vishnu = MaxObject("jit.p.vishnu")
    jit_p_vishnu.__doc__ = """
    jit.p.vishnu

    Attributes:
    force, mode, pitch, pitch_var, pos, pos_var, speed, speed_var, yaw, yaw_var
    """

    jit_pack = MaxObject("jit.pack")
    jit_pack.__doc__ = """
    jit.pack

    Attributes:
    index, jump, offset, plane
    """

    jit_path = MaxObject("jit.path")
    jit_path.__doc__ = """
    jit.path

    Attributes:
    autohandles, closed, dim, duration, evalmatrixmode, evalmatrixname,
    evalmatrixsize, grain, interpmode, length, loop, outmatrixname, play, pointcount,
    rate, thru, time, timemode, usetime
    """

    jit_peek_tilde = MaxObject("jit.peek~")
    jit_peek_tilde.__doc__ = """
    jit.peek~

    Attributes:
    interp, matrix_name, normalize, plane
    """

    jit_phys_6dof = MaxObject("jit.phys.6dof")
    jit_phys_6dof.__doc__ = """
    jit.phys.6dof

    Attributes:
    bias, body1, body2, collisions, enable, lowerlimit_ang, lowerlimit_lin,
    motorstrength, motorvelocity_ang, motorvelocity_lin, position1, position2, quat1,
    quat2, relaxation, rotate1, rotate2, rotatexyz1, rotatexyz2, spring_ang,
    spring_lin, springdamp_ang, springdamp_lin, springeq_ang, springeq_lin,
    springstiff_ang, springstiff_lin, strength, stretch, upperlimit_ang,
    upperlimit_lin, worldname, worldpos, worldquat
    """

    jit_phys_barslide = MaxObject("jit.phys.barslide")
    jit_phys_barslide.__doc__ = """
    jit.phys.barslide

    Attributes:
    body1, body2, collisions, damping, enable, linearposition, lowerlimit_ang,
    lowerlimit_lin, motorstrength_ang, motorstrength_lin, motorvelocity_ang,
    motorvelocity_lin, position1, position2, quat1, quat2, restitution, rotate1,
    rotate2, rotatexyz1, rotatexyz2, softness, strength, stretch, upperlimit_ang,
    upperlimit_lin, worldname, worldpos, worldquat
    """

    jit_phys_body = MaxObject("jit.phys.body")
    jit_phys_body.__doc__ = """
    jit.phys.body

    Attributes:
    anim, collisions, damping, enable, enable_sleep, filterclass, filters, force,
    forces_relative, friction, kinematic, local_scaling, mass, name, position, quat,
    reduce_hull, resetpos, resetquat, restitution, rolling_friction, rotate,
    rotate_order, rotatexyz, scale, send_scale, shape, targetname, torque,
    total_force, total_torque, velocity, velocity_ang, worldname
    """

    jit_phys_conetwist = MaxObject("jit.phys.conetwist")
    jit_phys_conetwist.__doc__ = """
    jit.phys.conetwist

    Attributes:
    bias, body1, body2, collisions, enable, position1, position2, quat1, quat2,
    relaxation, rotate1, rotate2, rotatexyz1, rotatexyz2, strength, stretch,
    swing1limit, swing2limit, twistlimit, worldname, worldpos, worldquat
    """

    jit_phys_ghost = MaxObject("jit.phys.ghost")
    jit_phys_ghost.__doc__ = """
    jit.phys.ghost

    Attributes:
    central_exp, central_force, central_mode, collision_mode, collisions, enable,
    filters, force, name, position, quat, rotate, rotate_order, rotatexyz, scale,
    shape, torque, worldname
    """

    jit_phys_hinge = MaxObject("jit.phys.hinge")
    jit_phys_hinge.__doc__ = """
    jit.phys.hinge

    Attributes:
    bias, body1, body2, collisions, enable, hingeangle, lowerlimit, motorstrength,
    motortarget, motorvelocity, position1, position2, quat1, quat2, relaxation,
    rotate1, rotate2, rotatexyz1, rotatexyz2, strength, stretch, upperlimit,
    worldname, worldpos, worldquat
    """

    jit_phys_multiple = MaxObject("jit.phys.multiple")
    jit_phys_multiple.__doc__ = """
    jit.phys.multiple

    Attributes:
    constraint, constraint_matrix, constraintoutname, damping, enable, enable_sleep,
    filterclass, filters, force, forces_relative, friction, kinematic, local_scaling,
    mass, name, physparams, posoutname, reduce_hull, restitution, rolling_friction,
    rotoutname, shape, shareshape, torque, worldname
    """

    jit_phys_picker = MaxObject("jit.phys.picker")
    jit_phys_picker.__doc__ = """
    jit.phys.picker

    Attributes:
    body, dynamics, enable, filterclass, filters, hover, local_position,
    output_positions, pickmode, position, strength, stretch, ui_priority, worldname
    """

    jit_phys_point2point = MaxObject("jit.phys.point2point")
    jit_phys_point2point.__doc__ = """
    jit.phys.point2point

    Attributes:
    body1, body2, collisions, enable, position1, position2, strength, stretch,
    worldname, worldpos, worldquat
    """

    jit_phys_world = MaxObject("jit.phys.world")
    jit_phys_world.__doc__ = """
    jit.phys.world

    Attributes:
    automatic, collision_mode, collisions, drawto, dynamics, enable, fixedtimestep,
    gravity, maxsubsteps, name, numcollisions, numthreads, raytest_mode, remove_plane,
    split_impulse, targetname, worldbox, worldbox_scale
    """

    jit_pix = MaxObject("jit.pix")
    jit_pix.__doc__ = """
    jit.pix

    Attributes:
    dirty, gen, precision, t, title
    """

    jit_planeop = MaxObject("jit.planeop")
    jit_planeop.__doc__ = """
    jit.planeop

    Attributes:
    op
    """

    jit_playlist = MaxObject("jit.playlist")
    jit_playlist.__doc__ = """
    jit.playlist

    Attributes:
    accentcolor, allowreorder, bgcolor, clipheight, color, drawto, elementcolor,
    expansion, loop, loopreport, output_texture, parameter_enable, parameter_mappable,
    reportprogress, selectioncolor, showname, style, textcolor
    """

    jit_plot = MaxObject("jit.plot")
    jit_plot.__doc__ = """
    jit.plot

    Attributes:
    brgb, clearit, frgb, height, width, xmax, xmin, ymax, ymin
    """

    jit_plume = MaxObject("jit.plume")
    jit_plume.__doc__ = """
    jit.plume

    Attributes:
    intervalmode, wrap, x_interval, xamount, xinterval, xoffset, y_interval, yamount,
    yinterval, yoffset
    """

    jit_plur = MaxObject("jit.plur")
    jit_plur.__doc__ = """
    jit.plur

    Attributes:
    colormode, gang, hi, lo, mode, scale, x_range, x_step, y_range, y_step
    """

    jit_poke_tilde = MaxObject("jit.poke~")
    jit_poke_tilde.__doc__ = """
    jit.poke~

    Attributes:
    matrix_name, normalize, plane
    """

    jit_print = MaxObject("jit.print")
    jit_print.__doc__ = """
    jit.print

    Attributes:
    coldelim, fieldwidth, info, mode, planedelim, precision, rowdelim, title, zeropad
    """

    jit_proxy = MaxObject("jit.proxy")
    jit_proxy.__doc__ = """
    jit.proxy

    Attributes:
    class, name
    """

    jit_pwindow = MaxObject("jit.pwindow")
    jit_pwindow.__doc__ = """
    jit.pwindow

    Attributes:
    border, bordercolor, colormode, depthbuffer, doublebuffer, dstrect, fsaa,
    idlemouse, interp, name, onscreen, pickray, planemap, shared, size, srcrect,
    stereo, sync, usedstrect, usesrcrect
    """

    jit_pworld = MaxObject("jit.pworld")
    jit_pworld.__doc__ = """
    jit.pworld

    Attributes:
    border, bordercolor, colormode, depthbuffer, doublebuffer, dstrect, enable, fps,
    fsaa, idlemouse, interp, name, onscreen, pickray, planemap, shared, size, srcrect,
    stereo, sync, usedstrect, usesrcrect
    """

    jit_qball = MaxObject("jit.qball")
    jit_qball.__doc__ = """
    jit.qball

    Attributes:
    mode
    """

    jit_qfaker = MaxObject("jit.qfaker")
    jit_qfaker.__doc__ = """
    jit.qfaker
    """

    jit_qt_grab = MaxObject("jit.qt.grab")
    jit_qt_grab.__doc__ = """
    jit.qt.grab

    Attributes:
    adapt, automatic, colormode, drawto, dstrect, engine, framerate, framereport,
    input, interp, output_texture, srcrect, texture_name, unique, usedstrect,
    usesrcrect, vdevice, format
    """

    jit_qt_movie = MaxObject("jit.qt.movie")
    jit_qt_movie.__doc__ = """
    jit.qt.movie

    Attributes:
    adapt, automatic, autostart, colormode, drawto, dstrect, duration, engine, fps,
    framecount, framereport, interp, loop, loopend, looppoints, loopreport, loopstart,
    movie_dim, moviedim, moviefile, moviename, moviepath, output_texture, rate,
    srcrect, texture_name, time, timescale, unique, usedstrect, usesrcrect, vol,
    time_secs, time_ms, seconds, position, milliseconds, looppoints_secs,
    looppoints_ms
    """

    jit_qt_record = MaxObject("jit.qt.record")
    jit_qt_record.__doc__ = """
    jit.qt.record

    Attributes:
    adapt, engine, preview, dstrect, interp, planemap, realtime, srcrect, time,
    usedstrect, usesrcrect, fps, codec
    """

    jit_qt_videoout = MaxObject("jit.qt.videoout")
    jit_qt_videoout.__doc__ = """
    jit.qt.videoout

    Attributes:
    codecquality, colormode, voc, vocmode
    """

    jit_quat = MaxObject("jit.quat")
    jit_quat.__doc__ = """
    jit.quat

    Attributes:
    inverse, normalize, quat1, quat2, quatout, xaxis, yaxis, zaxis
    """

    jit_quat2axis = MaxObject("jit.quat2axis")
    jit_quat2axis.__doc__ = """
    jit.quat2axis

    Attributes:
    angleaxis, normalize, quat
    """

    jit_quat2euler = MaxObject("jit.quat2euler")
    jit_quat2euler.__doc__ = """
    jit.quat2euler

    Attributes:
    euler, normalize, quat, rotate_order
    """

    jit_record = MaxObject("jit.record")
    jit_record.__doc__ = """
    jit.record

    Attributes:
    adapt, cache_size, codec, codeclist, dstrect, engine, fps, interp, planemap,
    preview, realtime, srcrect, time, usedstrect, usesrcrect
    """

    jit_release_tilde = MaxObject("jit.release~")
    jit_release_tilde.__doc__ = """
    jit.release~

    Attributes:
    mode, latency
    """

    jit_repos = MaxObject("jit.repos")
    jit_repos.__doc__ = """
    jit.repos

    Attributes:
    boundmode, interpbits, mode, offset_x, offset_y
    """

    jit_resamp = MaxObject("jit.resamp")
    jit_resamp.__doc__ = """
    jit.resamp

    Attributes:
    interp_x, interp_y, wrap, xscale, xshift, yscale, yshift
    """

    jit_reverse = MaxObject("jit.reverse")
    jit_reverse.__doc__ = """
    jit.reverse

    Attributes:
    immediate, reverse
    """

    jit_rgb2hsl = MaxObject("jit.rgb2hsl")
    jit_rgb2hsl.__doc__ = """
    jit.rgb2hsl

    Attributes:
    hoffset, hscale, loffset, lscale, soffset, sscale
    """

    jit_rgb2luma = MaxObject("jit.rgb2luma")
    jit_rgb2luma.__doc__ = """
    jit.rgb2luma

    Attributes:
    ascale, bscale, gscale, rscale
    """

    jit_robcross = MaxObject("jit.robcross")
    jit_robcross.__doc__ = """
    jit.robcross

    Attributes:
    thresh
    """

    jit_rota = MaxObject("jit.rota")
    jit_rota.__doc__ = """
    jit.rota

    Attributes:
    anchor_x, anchor_y, boundmode, cosoffset_x, cosoffset_y, cosscale_x, cosscale_y,
    interp, offset_x, offset_y, sinoffset_x, sinoffset_y, sinscale_x, sinscale_y,
    theta, thetaoffsetcos_x, thetaoffsetcos_y, thetaoffsetsin_x, thetaoffsetsin_y,
    thetascalecos_x, thetascalecos_y, thetascalesin_x, thetascalesin_y, zoom_x, zoom_y
    """

    jit_roy = MaxObject("jit.roy")
    jit_roy.__doc__ = """
    jit.roy

    Attributes:
    shades, x, y
    """

    jit_rubix = MaxObject("jit.rubix")
    jit_rubix.__doc__ = """
    jit.rubix

    Attributes:
    cols, dots, prob, probmono, rows
    """

    jit_scalebias = MaxObject("jit.scalebias")
    jit_scalebias.__doc__ = """
    jit.scalebias

    Attributes:
    abias, ascale, bbias, bias, bscale, gbias, gscale, mode, rbias, rscale, scale
    """

    jit_scanoffset = MaxObject("jit.scanoffset")
    jit_scanoffset.__doc__ = """
    jit.scanoffset

    Attributes:
    displacement_map, interp, mode, offset, scale
    """

    jit_scanslide = MaxObject("jit.scanslide")
    jit_scanslide.__doc__ = """
    jit.scanslide

    Attributes:
    dimmode, mode, offset, slide_down, slide_up
    """

    jit_scanwrap = MaxObject("jit.scanwrap")
    jit_scanwrap.__doc__ = """
    jit.scanwrap

    Attributes:
    mode
    """

    jit_scissors = MaxObject("jit.scissors")
    jit_scissors.__doc__ = """
    jit.scissors

    Attributes:
    columns, rows
    """

    jit_scope = MaxObject("jit.scope")
    jit_scope.__doc__ = """
    jit.scope

    Attributes:
    accum, accum_desat, bgcolor, border, colormode, dstrect, graphcolor, graphmode,
    hgraphcolor, hpopupbackgcolor, hpopupcolor, interp, mode, planemap,
    popupbackgcolor, popupcolor, size, srcrect, style
    """

    jit_shade = MaxObject("jit.shade")
    jit_shade.__doc__ = """
    jit.shade

    Attributes:
    max, min, mode
    """

    jit_slide = MaxObject("jit.slide")
    jit_slide.__doc__ = """
    jit.slide

    Attributes:
    slide_down, slide_up
    """

    jit_sobel = MaxObject("jit.sobel")
    jit_sobel.__doc__ = """
    jit.sobel

    Attributes:
    mode, thresh
    """

    jit_spill = MaxObject("jit.spill")
    jit_spill.__doc__ = """
    jit.spill

    Attributes:
    listlength, offset, plane
    """

    jit_split = MaxObject("jit.split")
    jit_split.__doc__ = """
    jit.split

    Attributes:
    autoclear, splitdim, splitpoint
    """

    jit_sprinkle = MaxObject("jit.sprinkle")
    jit_sprinkle.__doc__ = """
    jit.sprinkle

    Attributes:
    prob, x_range, y_range
    """

    jit_str_fromsymbol = MaxObject("jit.str.fromsymbol")
    jit_str_fromsymbol.__doc__ = """
    jit.str.fromsymbol
    """

    jit_str_op = MaxObject("jit.str.op")
    jit_str_op.__doc__ = """
    jit.str.op

    Attributes:
    end, multiline_in, multiline_out, op, start
    """

    jit_str_regexp = MaxObject("jit.str.regexp")
    jit_str_regexp.__doc__ = """
    jit.str.regexp

    Attributes:
    descriptor, re, substitute
    """

    jit_str_tosymbol = MaxObject("jit.str.tosymbol")
    jit_str_tosymbol.__doc__ = """
    jit.str.tosymbol

    Attributes:
    outsym
    """

    jit_streak = MaxObject("jit.streak")
    jit_streak.__doc__ = """
    jit.streak

    Attributes:
    direction, mode, prob, scale
    """

    jit_submatrix = MaxObject("jit.submatrix")
    jit_submatrix.__doc__ = """
    jit.submatrix

    Attributes:
    offset
    """

    jit_textfile = MaxObject("jit.textfile")
    jit_textfile.__doc__ = """
    jit.textfile

    Attributes:
    autoclear, defaultdir, convert, title
    """

    jit_thin = MaxObject("jit.thin")
    jit_thin.__doc__ = """
    jit.thin
    """

    jit_tiffany = MaxObject("jit.tiffany")
    jit_tiffany.__doc__ = """
    jit.tiffany

    Attributes:
    bgcolor, grid, xrange, xskip, yrange, yskip
    """

    jit_traffic = MaxObject("jit.traffic")
    jit_traffic.__doc__ = """
    jit.traffic
    """

    jit_transpose = MaxObject("jit.transpose")
    jit_transpose.__doc__ = """
    jit.transpose
    """

    jit_turtle = MaxObject("jit.turtle")
    jit_turtle.__doc__ = """
    jit.turtle

    Attributes:
    angle, clearmode, origin, scale
    """

    jit_uldl = MaxObject("jit.uldl")
    jit_uldl.__doc__ = """
    jit.uldl

    Attributes:
    defaultdir, convert, dir_list, dirlist, passive, password, percent, report,
    url_dl, url_ul, urldl, urlul, username
    """

    jit_unpack = MaxObject("jit.unpack")
    jit_unpack.__doc__ = """
    jit.unpack

    Attributes:
    jump, offset
    """

    jit_uyvy2argb = MaxObject("jit.uyvy2argb")
    jit_uyvy2argb.__doc__ = """
    jit.uyvy2argb

    Attributes:
    noalpha
    """

    jit_uyvy2ayuv = MaxObject("jit.uyvy2ayuv")
    jit_uyvy2ayuv.__doc__ = """
    jit.uyvy2ayuv

    Attributes:
    noalpha
    """

    jit_uyvy2luma = MaxObject("jit.uyvy2luma")
    jit_uyvy2luma.__doc__ = """
    jit.uyvy2luma
    """

    jit_vcr = MaxObject("jit.vcr")
    jit_vcr.__doc__ = """
    jit.vcr

    Attributes:
    adapt, cache_size, codec, codeclist, dstrect, engine, fps, interp, planemap,
    preview, realtime, srcrect, time, usedstrect, usesrcrect
    """

    jit_wake = MaxObject("jit.wake")
    jit_wake.__doc__ = """
    jit.wake

    Attributes:
    bdownbleed, bfb, bff, bgain, bleed, bleftbleed, brightbleed, bupbleed, fb, ff,
    gain, gdownbleed, gfb, gff, ggain, gleftbleed, grightbleed, gupbleed, normalize,
    rdownbleed, rfb, rff, rgain, rleftbleed, rrightbleed, rupbleed
    """

    jit_window = MaxObject("jit.window")
    jit_window.__doc__ = """
    jit.window

    Attributes:
    border, clamp, colormode, depthbuffer, doublebuffer, dstrect, floating, fsaa,
    fsmenubar, fullscreen, grow, idlemouse, interp, mousewheel, name, noaccel,
    pickray, planemap, pos, rect, shared, size, srcrect, stereo, sync, title,
    usedstrect, usesrcrect, visible
    """

    jit_world = MaxObject("jit.world")
    jit_world.__doc__ = """
    jit.world

    Attributes:
    border, auto_handle, enable, dim, displaylink, drawbang, drawto, capture,
    floating, fps, fsaa, fsmenubar, fullscreen, enable_cornerpin, erase_color,
    esc_fullscreen, interval, high_res, matrix_mode_async, output_matrix,
    output_texture, name, phys_worldname, position, ortho, preserve_aspect, size,
    rect, shared, sync, rotate, quat, rotatexyz, scale, windowposition, visible
    """

    jit_xfade = MaxObject("jit.xfade")
    jit_xfade.__doc__ = """
    jit.xfade

    Attributes:
    xfade
    """

    mc_jit_peek_tilde = MaxObject("mc.jit.peek~")
    mc_jit_peek_tilde.__doc__ = """
    mc.jit.peek~

    Attributes:
    interp, matrix_name, normalize, plane
    """


del _output
