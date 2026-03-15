"""Generated MaxObject stubs."""

from contextlib import redirect_stdout
from io import StringIO

from maxpylang.maxobject import MaxObject

__all__ = [
    "_2d_wave_tilde",
    "abs_tilde",
    "acos_tilde",
    "acosh_tilde",
    "adc_tilde",
    "adoutput_tilde",
    "adsr_tilde",
    "adstatus",
    "allpass_tilde",
    "amxd_tilde",
    "asin_tilde",
    "asinh_tilde",
    "atan2_tilde",
    "atan_tilde",
    "atanh_tilde",
    "atodb_tilde",
    "average_tilde",
    "avg_tilde",
    "begin_tilde",
    "biquad_tilde",
    "bitand_tilde",
    "bitnot_tilde",
    "bitor_tilde",
    "bitsafe_tilde",
    "bitshift_tilde",
    "bitxor_tilde",
    "buffer_tilde",
    "buffir_tilde",
    "capture_tilde",
    "cartopol_tilde",
    "cascade_tilde",
    "change_tilde",
    "click_tilde",
    "clip_tilde",
    "comb_tilde",
    "cos_tilde",
    "cosh_tilde",
    "cosx_tilde",
    "count_tilde",
    "cross_tilde",
    "curve_tilde",
    "cycle_tilde",
    "dac_tilde",
    "dbtoa_tilde",
    "degrade_tilde",
    "delay_tilde",
    "delta_tilde",
    "deltaclip_tilde",
    "div_tilde",
    "downsamp_tilde",
    "dspstate_tilde",
    "dsptime_tilde",
    "edge_tilde",
    "equals_tilde",
    "ezadc_tilde",
    "ezdac_tilde",
    "fbinshift_tilde",
    "fffb_tilde",
    "fft_tilde",
    "fftin_tilde",
    "fftinfo_tilde",
    "fftout_tilde",
    "filtercoeff_tilde",
    "filterdesign",
    "filterdetail",
    "filtergraph_tilde",
    "frame_tilde",
    "frameaccum_tilde",
    "frameaverage_tilde",
    "framedelta_tilde",
    "framesmooth_tilde",
    "framesnap_tilde",
    "freqshift_tilde",
    "ftom_tilde",
    "fzero_tilde",
    "gain_tilde",
    "gate_tilde",
    "gen",
    "gen_tilde",
    "gizmo_tilde",
    "greaterthan_tilde",
    "greaterthaneq_tilde",
    "gridmeter_tilde",
    "groove_tilde",
    "hilbert_tilde",
    "hostcontrol_tilde",
    "hostphasor_tilde",
    "hostsync_tilde",
    "ifft_tilde",
    "in_",
    "in_tilde",
    "index_tilde",
    "info_tilde",
    "ioscbank_tilde",
    "kink_tilde",
    "lessthan_tilde",
    "lessthaneq_tilde",
    "levelmeter_tilde",
    "limi_tilde",
    "line_tilde",
    "log_tilde",
    "lookup_tilde",
    "lores_tilde",
    "matrix_tilde",
    "maximum_tilde",
    "mc_2d_wave_tilde",
    "mc_abs_tilde",
    "mc_acos_tilde",
    "mc_acosh_tilde",
    "mc_adc_tilde",
    "mc_adsr_tilde",
    "mc_allpass_tilde",
    "mc_amxd_tilde",
    "mc_apply_tilde",
    "mc_asin_tilde",
    "mc_asinh_tilde",
    "mc_assign",
    "mc_atan_tilde",
    "mc_atanh_tilde",
    "mc_atodb_tilde",
    "mc_average_tilde",
    "mc_avg_tilde",
    "mc_bands_tilde",
    "mc_biquad_tilde",
    "mc_bitand_tilde",
    "mc_bitnot_tilde",
    "mc_bitor_tilde",
    "mc_bitsafe_tilde",
    "mc_bitxor_tilde",
    "mc_buffir_tilde",
    "mc_cartopol_tilde",
    "mc_cascade_tilde",
    "mc_cell",
    "mc_change_tilde",
    "mc_channelcount_tilde",
    "mc_chord_tilde",
    "mc_click_tilde",
    "mc_clip_tilde",
    "mc_comb_tilde",
    "mc_combine_tilde",
    "mc_cos_tilde",
    "mc_cosh_tilde",
    "mc_cosx_tilde",
    "mc_count_tilde",
    "mc_cross_tilde",
    "mc_curve_tilde",
    "mc_cycle_tilde",
    "mc_dac_tilde",
    "mc_dbtoa_tilde",
    "mc_degrade_tilde",
    "mc_deinterleave_tilde",
    "mc_delay_tilde",
    "mc_delta_tilde",
    "mc_deltaclip_tilde",
    "mc_div_tilde",
    "mc_downsamp_tilde",
    "mc_dup_tilde",
    "mc_edge_tilde",
    "mc_equals_tilde",
    "mc_evolve_tilde",
    "mc_ezadc_tilde",
    "mc_ezdac_tilde",
    "mc_fffb_tilde",
    "mc_fft_tilde",
    "mc_filtercoeff_tilde",
    "mc_frameaccum_tilde",
    "mc_frameaverage_tilde",
    "mc_framedelta_tilde",
    "mc_framesmooth_tilde",
    "mc_freqshift_tilde",
    "mc_ftom_tilde",
    "mc_fzero_tilde",
    "mc_gain_tilde",
    "mc_gate_tilde",
    "mc_gen",
    "mc_gen_tilde",
    "mc_generate_tilde",
    "mc_gradient_tilde",
    "mc_greaterthan_tilde",
    "mc_greaterthaneq_tilde",
    "mc_groove_tilde",
    "mc_hilbert_tilde",
    "mc_ifft_tilde",
    "mc_in_tilde",
    "mc_index_tilde",
    "mc_interleave_tilde",
    "mc_kink_tilde",
    "mc_lessthan_tilde",
    "mc_lessthaneq_tilde",
    "mc_limi_tilde",
    "mc_line_tilde",
    "mc_list_tilde",
    "mc_log_tilde",
    "mc_lookup_tilde",
    "mc_lores_tilde",
    "mc_makelist",
    "mc_matrix_tilde",
    "mc_maximum_tilde",
    "mc_midiplayer_tilde",
    "mc_minimum_tilde",
    "mc_minmax_tilde",
    "mc_minus_tilde",
    "mc_mixdown_tilde",
    "mc_modulo_tilde",
    "mc_mstosamps_tilde",
    "mc_mtof_tilde",
    "mc_noise_tilde",
    "mc_normalize_tilde",
    "mc_noteallocator_tilde",
    "mc_notequals_tilde",
    "mc_number_tilde",
    "mc_omx_4band_tilde",
    "mc_omx_5band_tilde",
    "mc_omx_comp_tilde",
    "mc_omx_peaklim_tilde",
    "mc_onepole_tilde",
    "mc_op_tilde",
    "mc_out_tilde",
    "mc_overdrive_tilde",
    "mc_pack_tilde",
    "mc_pattern_tilde",
    "mc_peakamp_tilde",
    "mc_peek_tilde",
    "mc_pfft_tilde",
    "mc_phasegroove_tilde",
    "mc_phaseshift_tilde",
    "mc_phasewrap_tilde",
    "mc_phasor_tilde",
    "mc_pink_tilde",
    "mc_pitchshift_tilde",
    "mc_play_tilde",
    "mc_playlist_tilde",
    "mc_plus_tilde",
    "mc_plusequals_tilde",
    "mc_poltocar_tilde",
    "mc_poly_tilde",
    "mc_pong_tilde",
    "mc_pow_tilde",
    "mc_ramp_tilde",
    "mc_rampsmooth_tilde",
    "mc_rand_tilde",
    "mc_range_tilde",
    "mc_rate_tilde",
    "mc_rdiv_tilde",
    "mc_receive_tilde",
    "mc_record_tilde",
    "mc_rect_tilde",
    "mc_resize_tilde",
    "mc_reson_tilde",
    "mc_retune_tilde",
    "mc_rminus_tilde",
    "mc_round_tilde",
    "mc_route",
    "mc_sah_tilde",
    "mc_sampstoms_tilde",
    "mc_sash_tilde",
    "mc_saw_tilde",
    "mc_scale_tilde",
    "mc_selector_tilde",
    "mc_send_tilde",
    "mc_separate_tilde",
    "mc_seq_tilde",
    "mc_sfplay_tilde",
    "mc_sfrecord_tilde",
    "mc_shape_tilde",
    "mc_sig_tilde",
    "mc_sinh_tilde",
    "mc_sinx_tilde",
    "mc_slide_tilde",
    "mc_snapshot_tilde",
    "mc_snowfall_tilde",
    "mc_snowphasor_tilde",
    "mc_spike_tilde",
    "mc_sqrt_tilde",
    "mc_stash_tilde",
    "mc_stereo_tilde",
    "mc_stutter_tilde",
    "mc_subdiv_tilde",
    "mc_svf_tilde",
    "mc_swing_tilde",
    "mc_sync_tilde",
    "mc_table_tilde",
    "mc_tanh_tilde",
    "mc_tanx_tilde",
    "mc_tapin_tilde",
    "mc_tapout_tilde",
    "mc_target",
    "mc_targetlist",
    "mc_teeth_tilde",
    "mc_thresh_tilde",
    "mc_times_tilde",
    "mc_train_tilde",
    "mc_transpose_tilde",
    "mc_trapezoid_tilde",
    "mc_tri_tilde",
    "mc_triangle_tilde",
    "mc_trunc_tilde",
    "mc_twist_tilde",
    "mc_unpack_tilde",
    "mc_updown_tilde",
    "mc_vectral_tilde",
    "mc_voiceallocator_tilde",
    "mc_vst_tilde",
    "mc_wave_tilde",
    "mc_what_tilde",
    "mc_where_tilde",
    "mc_zerox_tilde",
    "mc_zigzag_tilde",
    "mcs_2d_wave_tilde",
    "mcs_amxd_tilde",
    "mcs_fffb_tilde",
    "mcs_gate_tilde",
    "mcs_gen_tilde",
    "mcs_groove_tilde",
    "mcs_limi_tilde",
    "mcs_matrix_tilde",
    "mcs_play_tilde",
    "mcs_poly_tilde",
    "mcs_selector_tilde",
    "mcs_sig_tilde",
    "mcs_tapout_tilde",
    "mcs_vst_tilde",
    "mcs_wave_tilde",
    "meter_tilde",
    "minimum_tilde",
    "minmax_tilde",
    "minus_tilde",
    "modulo_tilde",
    "mstosamps_tilde",
    "mtof_tilde",
    "mute_tilde",
    "mxj_tilde",
    "noise_tilde",
    "normalize_tilde",
    "notequals_tilde",
    "number_tilde",
    "omx_4band_tilde",
    "omx_5band_tilde",
    "omx_comp_tilde",
    "omx_peaklim_tilde",
    "onepole_tilde",
    "oscbank_tilde",
    "out",
    "out_tilde",
    "overdrive_tilde",
    "pass_tilde",
    "peakamp_tilde",
    "peek_tilde",
    "pfft_tilde",
    "phasegroove_tilde",
    "phaseshift_tilde",
    "phasewrap_tilde",
    "phasor_tilde",
    "pink_tilde",
    "pitchshift_tilde",
    "play_tilde",
    "playlist_tilde",
    "plot_tilde",
    "plugin_tilde",
    "plugout_tilde",
    "plugphasor_tilde",
    "plugreceive_tilde",
    "plugsend_tilde",
    "plugsync_tilde",
    "plus_tilde",
    "plusequals_tilde",
    "poke_tilde",
    "poltocar_tilde",
    "poly_tilde",
    "polybuffer_tilde",
    "pong_tilde",
    "pow_tilde",
    "ramp_tilde",
    "rampsmooth_tilde",
    "rand_tilde",
    "rate_tilde",
    "rdiv_tilde",
    "receive_tilde",
    "record_tilde",
    "rect_tilde",
    "reson_tilde",
    "retune_tilde",
    "rewire_tilde",
    "rminus_tilde",
    "round_tilde",
    "sah_tilde",
    "sampstoms_tilde",
    "sash_tilde",
    "saw_tilde",
    "scale_tilde",
    "scope_tilde",
    "selector_tilde",
    "send_tilde",
    "seq_tilde",
    "sfinfo_tilde",
    "sflist_tilde",
    "sfplay_tilde",
    "sfrecord_tilde",
    "shape_tilde",
    "sig_tilde",
    "sinh_tilde",
    "sinx_tilde",
    "slide_tilde",
    "snapshot_tilde",
    "snowfall_tilde",
    "spectroscope_tilde",
    "spike_tilde",
    "sqrt_tilde",
    "stash_tilde",
    "stretch_tilde",
    "stutter_tilde",
    "subdiv_tilde",
    "svf_tilde",
    "swing_tilde",
    "sync_tilde",
    "table_tilde",
    "tanh_tilde",
    "tanx_tilde",
    "tapin_tilde",
    "tapout_tilde",
    "techno_tilde",
    "teeth_tilde",
    "thispoly_tilde",
    "thresh_tilde",
    "times_tilde",
    "train_tilde",
    "trapezoid_tilde",
    "tri_tilde",
    "triangle_tilde",
    "trunc_tilde",
    "twist_tilde",
    "typeroute_tilde",
    "updown_tilde",
    "vectral_tilde",
    "vst_tilde",
    "wave_tilde",
    "waveform_tilde",
    "what_tilde",
    "where_tilde",
    "windowed_fft_tilde",
    "zerox_tilde",
    "zigzag_tilde",
    "zplane_tilde",
]

_NAMES = {
    "_2d_wave_tilde": "2d.wave~",
    "abs_tilde": "abs~",
    "acos_tilde": "acos~",
    "acosh_tilde": "acosh~",
    "adc_tilde": "adc~",
    "adoutput_tilde": "adoutput~",
    "adsr_tilde": "adsr~",
    "adstatus": "adstatus",
    "allpass_tilde": "allpass~",
    "amxd_tilde": "amxd~",
    "asin_tilde": "asin~",
    "asinh_tilde": "asinh~",
    "atan2_tilde": "atan2~",
    "atan_tilde": "atan~",
    "atanh_tilde": "atanh~",
    "atodb_tilde": "atodb~",
    "average_tilde": "average~",
    "avg_tilde": "avg~",
    "begin_tilde": "begin~",
    "biquad_tilde": "biquad~",
    "bitand_tilde": "bitand~",
    "bitnot_tilde": "bitnot~",
    "bitor_tilde": "bitor~",
    "bitsafe_tilde": "bitsafe~",
    "bitshift_tilde": "bitshift~",
    "bitxor_tilde": "bitxor~",
    "buffer_tilde": "buffer~",
    "buffir_tilde": "buffir~",
    "capture_tilde": "capture~",
    "cartopol_tilde": "cartopol~",
    "cascade_tilde": "cascade~",
    "change_tilde": "change~",
    "click_tilde": "click~",
    "clip_tilde": "clip~",
    "comb_tilde": "comb~",
    "cos_tilde": "cos~",
    "cosh_tilde": "cosh~",
    "cosx_tilde": "cosx~",
    "count_tilde": "count~",
    "cross_tilde": "cross~",
    "curve_tilde": "curve~",
    "cycle_tilde": "cycle~",
    "dac_tilde": "dac~",
    "dbtoa_tilde": "dbtoa~",
    "degrade_tilde": "degrade~",
    "delay_tilde": "delay~",
    "delta_tilde": "delta~",
    "deltaclip_tilde": "deltaclip~",
    "div_tilde": "div~",
    "downsamp_tilde": "downsamp~",
    "dspstate_tilde": "dspstate~",
    "dsptime_tilde": "dsptime~",
    "edge_tilde": "edge~",
    "equals_tilde": "equals~",
    "ezadc_tilde": "ezadc~",
    "ezdac_tilde": "ezdac~",
    "fbinshift_tilde": "fbinshift~",
    "fffb_tilde": "fffb~",
    "fft_tilde": "fft~",
    "fftin_tilde": "fftin~",
    "fftinfo_tilde": "fftinfo~",
    "fftout_tilde": "fftout~",
    "filtercoeff_tilde": "filtercoeff~",
    "filterdesign": "filterdesign",
    "filterdetail": "filterdetail",
    "filtergraph_tilde": "filtergraph~",
    "frame_tilde": "frame~",
    "frameaccum_tilde": "frameaccum~",
    "frameaverage_tilde": "frameaverage~",
    "framedelta_tilde": "framedelta~",
    "framesmooth_tilde": "framesmooth~",
    "framesnap_tilde": "framesnap~",
    "freqshift_tilde": "freqshift~",
    "ftom_tilde": "ftom~",
    "fzero_tilde": "fzero~",
    "gain_tilde": "gain~",
    "gate_tilde": "gate~",
    "gen": "gen",
    "gen_tilde": "gen~",
    "gizmo_tilde": "gizmo~",
    "greaterthan_tilde": "greaterthan~",
    "greaterthaneq_tilde": "greaterthaneq~",
    "gridmeter_tilde": "gridmeter~",
    "groove_tilde": "groove~",
    "hilbert_tilde": "hilbert~",
    "hostcontrol_tilde": "hostcontrol~",
    "hostphasor_tilde": "hostphasor~",
    "hostsync_tilde": "hostsync~",
    "ifft_tilde": "ifft~",
    "in_": "in",
    "in_tilde": "in~",
    "index_tilde": "index~",
    "info_tilde": "info~",
    "ioscbank_tilde": "ioscbank~",
    "kink_tilde": "kink~",
    "lessthan_tilde": "lessthan~",
    "lessthaneq_tilde": "lessthaneq~",
    "levelmeter_tilde": "levelmeter~",
    "limi_tilde": "limi~",
    "line_tilde": "line~",
    "log_tilde": "log~",
    "lookup_tilde": "lookup~",
    "lores_tilde": "lores~",
    "matrix_tilde": "matrix~",
    "maximum_tilde": "maximum~",
    "mc_2d_wave_tilde": "mc.2d.wave~",
    "mc_abs_tilde": "mc.abs~",
    "mc_acos_tilde": "mc.acos~",
    "mc_acosh_tilde": "mc.acosh~",
    "mc_adc_tilde": "mc.adc~",
    "mc_adsr_tilde": "mc.adsr~",
    "mc_allpass_tilde": "mc.allpass~",
    "mc_amxd_tilde": "mc.amxd~",
    "mc_apply_tilde": "mc.apply~",
    "mc_asin_tilde": "mc.asin~",
    "mc_asinh_tilde": "mc.asinh~",
    "mc_assign": "mc.assign",
    "mc_atan_tilde": "mc.atan~",
    "mc_atanh_tilde": "mc.atanh~",
    "mc_atodb_tilde": "mc.atodb~",
    "mc_average_tilde": "mc.average~",
    "mc_avg_tilde": "mc.avg~",
    "mc_bands_tilde": "mc.bands~",
    "mc_biquad_tilde": "mc.biquad~",
    "mc_bitand_tilde": "mc.bitand~",
    "mc_bitnot_tilde": "mc.bitnot~",
    "mc_bitor_tilde": "mc.bitor~",
    "mc_bitsafe_tilde": "mc.bitsafe~",
    "mc_bitxor_tilde": "mc.bitxor~",
    "mc_buffir_tilde": "mc.buffir~",
    "mc_cartopol_tilde": "mc.cartopol~",
    "mc_cascade_tilde": "mc.cascade~",
    "mc_cell": "mc.cell",
    "mc_change_tilde": "mc.change~",
    "mc_channelcount_tilde": "mc.channelcount~",
    "mc_chord_tilde": "mc.chord~",
    "mc_click_tilde": "mc.click~",
    "mc_clip_tilde": "mc.clip~",
    "mc_comb_tilde": "mc.comb~",
    "mc_combine_tilde": "mc.combine~",
    "mc_cos_tilde": "mc.cos~",
    "mc_cosh_tilde": "mc.cosh~",
    "mc_cosx_tilde": "mc.cosx~",
    "mc_count_tilde": "mc.count~",
    "mc_cross_tilde": "mc.cross~",
    "mc_curve_tilde": "mc.curve~",
    "mc_cycle_tilde": "mc.cycle~",
    "mc_dac_tilde": "mc.dac~",
    "mc_dbtoa_tilde": "mc.dbtoa~",
    "mc_degrade_tilde": "mc.degrade~",
    "mc_deinterleave_tilde": "mc.deinterleave~",
    "mc_delay_tilde": "mc.delay~",
    "mc_delta_tilde": "mc.delta~",
    "mc_deltaclip_tilde": "mc.deltaclip~",
    "mc_div_tilde": "mc.div~",
    "mc_downsamp_tilde": "mc.downsamp~",
    "mc_dup_tilde": "mc.dup~",
    "mc_edge_tilde": "mc.edge~",
    "mc_equals_tilde": "mc.equals~",
    "mc_evolve_tilde": "mc.evolve~",
    "mc_ezadc_tilde": "mc.ezadc~",
    "mc_ezdac_tilde": "mc.ezdac~",
    "mc_fffb_tilde": "mc.fffb~",
    "mc_fft_tilde": "mc.fft~",
    "mc_filtercoeff_tilde": "mc.filtercoeff~",
    "mc_frameaccum_tilde": "mc.frameaccum~",
    "mc_frameaverage_tilde": "mc.frameaverage~",
    "mc_framedelta_tilde": "mc.framedelta~",
    "mc_framesmooth_tilde": "mc.framesmooth~",
    "mc_freqshift_tilde": "mc.freqshift~",
    "mc_ftom_tilde": "mc.ftom~",
    "mc_fzero_tilde": "mc.fzero~",
    "mc_gain_tilde": "mc.gain~",
    "mc_gate_tilde": "mc.gate~",
    "mc_gen": "mc.gen",
    "mc_gen_tilde": "mc.gen~",
    "mc_generate_tilde": "mc.generate~",
    "mc_gradient_tilde": "mc.gradient~",
    "mc_greaterthan_tilde": "mc.greaterthan~",
    "mc_greaterthaneq_tilde": "mc.greaterthaneq~",
    "mc_groove_tilde": "mc.groove~",
    "mc_hilbert_tilde": "mc.hilbert~",
    "mc_ifft_tilde": "mc.ifft~",
    "mc_in_tilde": "mc.in~",
    "mc_index_tilde": "mc.index~",
    "mc_interleave_tilde": "mc.interleave~",
    "mc_kink_tilde": "mc.kink~",
    "mc_lessthan_tilde": "mc.lessthan~",
    "mc_lessthaneq_tilde": "mc.lessthaneq~",
    "mc_limi_tilde": "mc.limi~",
    "mc_line_tilde": "mc.line~",
    "mc_list_tilde": "mc.list~",
    "mc_log_tilde": "mc.log~",
    "mc_lookup_tilde": "mc.lookup~",
    "mc_lores_tilde": "mc.lores~",
    "mc_makelist": "mc.makelist",
    "mc_matrix_tilde": "mc.matrix~",
    "mc_maximum_tilde": "mc.maximum~",
    "mc_midiplayer_tilde": "mc.midiplayer~",
    "mc_minimum_tilde": "mc.minimum~",
    "mc_minmax_tilde": "mc.minmax~",
    "mc_minus_tilde": "mc.minus~",
    "mc_mixdown_tilde": "mc.mixdown~",
    "mc_modulo_tilde": "mc.modulo~",
    "mc_mstosamps_tilde": "mc.mstosamps~",
    "mc_mtof_tilde": "mc.mtof~",
    "mc_noise_tilde": "mc.noise~",
    "mc_normalize_tilde": "mc.normalize~",
    "mc_noteallocator_tilde": "mc.noteallocator~",
    "mc_notequals_tilde": "mc.notequals~",
    "mc_number_tilde": "mc.number~",
    "mc_omx_4band_tilde": "mc.omx.4band~",
    "mc_omx_5band_tilde": "mc.omx.5band~",
    "mc_omx_comp_tilde": "mc.omx.comp~",
    "mc_omx_peaklim_tilde": "mc.omx.peaklim~",
    "mc_onepole_tilde": "mc.onepole~",
    "mc_op_tilde": "mc.op~",
    "mc_out_tilde": "mc.out~",
    "mc_overdrive_tilde": "mc.overdrive~",
    "mc_pack_tilde": "mc.pack~",
    "mc_pattern_tilde": "mc.pattern~",
    "mc_peakamp_tilde": "mc.peakamp~",
    "mc_peek_tilde": "mc.peek~",
    "mc_pfft_tilde": "mc.pfft~",
    "mc_phasegroove_tilde": "mc.phasegroove~",
    "mc_phaseshift_tilde": "mc.phaseshift~",
    "mc_phasewrap_tilde": "mc.phasewrap~",
    "mc_phasor_tilde": "mc.phasor~",
    "mc_pink_tilde": "mc.pink~",
    "mc_pitchshift_tilde": "mc.pitchshift~",
    "mc_play_tilde": "mc.play~",
    "mc_playlist_tilde": "mc.playlist~",
    "mc_plus_tilde": "mc.plus~",
    "mc_plusequals_tilde": "mc.plusequals~",
    "mc_poltocar_tilde": "mc.poltocar~",
    "mc_poly_tilde": "mc.poly~",
    "mc_pong_tilde": "mc.pong~",
    "mc_pow_tilde": "mc.pow~",
    "mc_ramp_tilde": "mc.ramp~",
    "mc_rampsmooth_tilde": "mc.rampsmooth~",
    "mc_rand_tilde": "mc.rand~",
    "mc_range_tilde": "mc.range~",
    "mc_rate_tilde": "mc.rate~",
    "mc_rdiv_tilde": "mc.rdiv~",
    "mc_receive_tilde": "mc.receive~",
    "mc_record_tilde": "mc.record~",
    "mc_rect_tilde": "mc.rect~",
    "mc_resize_tilde": "mc.resize~",
    "mc_reson_tilde": "mc.reson~",
    "mc_retune_tilde": "mc.retune~",
    "mc_rminus_tilde": "mc.rminus~",
    "mc_round_tilde": "mc.round~",
    "mc_route": "mc.route",
    "mc_sah_tilde": "mc.sah~",
    "mc_sampstoms_tilde": "mc.sampstoms~",
    "mc_sash_tilde": "mc.sash~",
    "mc_saw_tilde": "mc.saw~",
    "mc_scale_tilde": "mc.scale~",
    "mc_selector_tilde": "mc.selector~",
    "mc_send_tilde": "mc.send~",
    "mc_separate_tilde": "mc.separate~",
    "mc_seq_tilde": "mc.seq~",
    "mc_sfplay_tilde": "mc.sfplay~",
    "mc_sfrecord_tilde": "mc.sfrecord~",
    "mc_shape_tilde": "mc.shape~",
    "mc_sig_tilde": "mc.sig~",
    "mc_sinh_tilde": "mc.sinh~",
    "mc_sinx_tilde": "mc.sinx~",
    "mc_slide_tilde": "mc.slide~",
    "mc_snapshot_tilde": "mc.snapshot~",
    "mc_snowfall_tilde": "mc.snowfall~",
    "mc_snowphasor_tilde": "mc.snowphasor~",
    "mc_spike_tilde": "mc.spike~",
    "mc_sqrt_tilde": "mc.sqrt~",
    "mc_stash_tilde": "mc.stash~",
    "mc_stereo_tilde": "mc.stereo~",
    "mc_stutter_tilde": "mc.stutter~",
    "mc_subdiv_tilde": "mc.subdiv~",
    "mc_svf_tilde": "mc.svf~",
    "mc_swing_tilde": "mc.swing~",
    "mc_sync_tilde": "mc.sync~",
    "mc_table_tilde": "mc.table~",
    "mc_tanh_tilde": "mc.tanh~",
    "mc_tanx_tilde": "mc.tanx~",
    "mc_tapin_tilde": "mc.tapin~",
    "mc_tapout_tilde": "mc.tapout~",
    "mc_target": "mc.target",
    "mc_targetlist": "mc.targetlist",
    "mc_teeth_tilde": "mc.teeth~",
    "mc_thresh_tilde": "mc.thresh~",
    "mc_times_tilde": "mc.times~",
    "mc_train_tilde": "mc.train~",
    "mc_transpose_tilde": "mc.transpose~",
    "mc_trapezoid_tilde": "mc.trapezoid~",
    "mc_tri_tilde": "mc.tri~",
    "mc_triangle_tilde": "mc.triangle~",
    "mc_trunc_tilde": "mc.trunc~",
    "mc_twist_tilde": "mc.twist~",
    "mc_unpack_tilde": "mc.unpack~",
    "mc_updown_tilde": "mc.updown~",
    "mc_vectral_tilde": "mc.vectral~",
    "mc_voiceallocator_tilde": "mc.voiceallocator~",
    "mc_vst_tilde": "mc.vst~",
    "mc_wave_tilde": "mc.wave~",
    "mc_what_tilde": "mc.what~",
    "mc_where_tilde": "mc.where~",
    "mc_zerox_tilde": "mc.zerox~",
    "mc_zigzag_tilde": "mc.zigzag~",
    "mcs_2d_wave_tilde": "mcs.2d.wave~",
    "mcs_amxd_tilde": "mcs.amxd~",
    "mcs_fffb_tilde": "mcs.fffb~",
    "mcs_gate_tilde": "mcs.gate~",
    "mcs_gen_tilde": "mcs.gen~",
    "mcs_groove_tilde": "mcs.groove~",
    "mcs_limi_tilde": "mcs.limi~",
    "mcs_matrix_tilde": "mcs.matrix~",
    "mcs_play_tilde": "mcs.play~",
    "mcs_poly_tilde": "mcs.poly~",
    "mcs_selector_tilde": "mcs.selector~",
    "mcs_sig_tilde": "mcs.sig~",
    "mcs_tapout_tilde": "mcs.tapout~",
    "mcs_vst_tilde": "mcs.vst~",
    "mcs_wave_tilde": "mcs.wave~",
    "meter_tilde": "meter~",
    "minimum_tilde": "minimum~",
    "minmax_tilde": "minmax~",
    "minus_tilde": "minus~",
    "modulo_tilde": "modulo~",
    "mstosamps_tilde": "mstosamps~",
    "mtof_tilde": "mtof~",
    "mute_tilde": "mute~",
    "mxj_tilde": "mxj~",
    "noise_tilde": "noise~",
    "normalize_tilde": "normalize~",
    "notequals_tilde": "notequals~",
    "number_tilde": "number~",
    "omx_4band_tilde": "omx.4band~",
    "omx_5band_tilde": "omx.5band~",
    "omx_comp_tilde": "omx.comp~",
    "omx_peaklim_tilde": "omx.peaklim~",
    "onepole_tilde": "onepole~",
    "oscbank_tilde": "oscbank~",
    "out": "out",
    "out_tilde": "out~",
    "overdrive_tilde": "overdrive~",
    "pass_tilde": "pass~",
    "peakamp_tilde": "peakamp~",
    "peek_tilde": "peek~",
    "pfft_tilde": "pfft~",
    "phasegroove_tilde": "phasegroove~",
    "phaseshift_tilde": "phaseshift~",
    "phasewrap_tilde": "phasewrap~",
    "phasor_tilde": "phasor~",
    "pink_tilde": "pink~",
    "pitchshift_tilde": "pitchshift~",
    "play_tilde": "play~",
    "playlist_tilde": "playlist~",
    "plot_tilde": "plot~",
    "plugin_tilde": "plugin~",
    "plugout_tilde": "plugout~",
    "plugphasor_tilde": "plugphasor~",
    "plugreceive_tilde": "plugreceive~",
    "plugsend_tilde": "plugsend~",
    "plugsync_tilde": "plugsync~",
    "plus_tilde": "plus~",
    "plusequals_tilde": "plusequals~",
    "poke_tilde": "poke~",
    "poltocar_tilde": "poltocar~",
    "poly_tilde": "poly~",
    "polybuffer_tilde": "polybuffer~",
    "pong_tilde": "pong~",
    "pow_tilde": "pow~",
    "ramp_tilde": "ramp~",
    "rampsmooth_tilde": "rampsmooth~",
    "rand_tilde": "rand~",
    "rate_tilde": "rate~",
    "rdiv_tilde": "rdiv~",
    "receive_tilde": "receive~",
    "record_tilde": "record~",
    "rect_tilde": "rect~",
    "reson_tilde": "reson~",
    "retune_tilde": "retune~",
    "rewire_tilde": "rewire~",
    "rminus_tilde": "rminus~",
    "round_tilde": "round~",
    "sah_tilde": "sah~",
    "sampstoms_tilde": "sampstoms~",
    "sash_tilde": "sash~",
    "saw_tilde": "saw~",
    "scale_tilde": "scale~",
    "scope_tilde": "scope~",
    "selector_tilde": "selector~",
    "send_tilde": "send~",
    "seq_tilde": "seq~",
    "sfinfo_tilde": "sfinfo~",
    "sflist_tilde": "sflist~",
    "sfplay_tilde": "sfplay~",
    "sfrecord_tilde": "sfrecord~",
    "shape_tilde": "shape~",
    "sig_tilde": "sig~",
    "sinh_tilde": "sinh~",
    "sinx_tilde": "sinx~",
    "slide_tilde": "slide~",
    "snapshot_tilde": "snapshot~",
    "snowfall_tilde": "snowfall~",
    "spectroscope_tilde": "spectroscope~",
    "spike_tilde": "spike~",
    "sqrt_tilde": "sqrt~",
    "stash_tilde": "stash~",
    "stretch_tilde": "stretch~",
    "stutter_tilde": "stutter~",
    "subdiv_tilde": "subdiv~",
    "svf_tilde": "svf~",
    "swing_tilde": "swing~",
    "sync_tilde": "sync~",
    "table_tilde": "table~",
    "tanh_tilde": "tanh~",
    "tanx_tilde": "tanx~",
    "tapin_tilde": "tapin~",
    "tapout_tilde": "tapout~",
    "techno_tilde": "techno~",
    "teeth_tilde": "teeth~",
    "thispoly_tilde": "thispoly~",
    "thresh_tilde": "thresh~",
    "times_tilde": "times~",
    "train_tilde": "train~",
    "trapezoid_tilde": "trapezoid~",
    "tri_tilde": "tri~",
    "triangle_tilde": "triangle~",
    "trunc_tilde": "trunc~",
    "twist_tilde": "twist~",
    "typeroute_tilde": "typeroute~",
    "updown_tilde": "updown~",
    "vectral_tilde": "vectral~",
    "vst_tilde": "vst~",
    "wave_tilde": "wave~",
    "waveform_tilde": "waveform~",
    "what_tilde": "what~",
    "where_tilde": "where~",
    "windowed_fft_tilde": "windowed-fft~",
    "zerox_tilde": "zerox~",
    "zigzag_tilde": "zigzag~",
    "zplane_tilde": "zplane~",
}

_output = StringIO()
with redirect_stdout(_output):
    _2d_wave_tilde = MaxObject("2d.wave~")
    _2d_wave_tilde.__doc__ = """
    2d.wave~

    Args:
    buffer-name (symbol, required)
    start and end-points (number, optional)
    number-of-output-channels (int, optional)
    rows (int, optional)
    """

    abs_tilde = MaxObject("abs~")
    abs_tilde.__doc__ = """
    abs~
    """

    acos_tilde = MaxObject("acos~")
    acos_tilde.__doc__ = """
    acos~
    """

    acosh_tilde = MaxObject("acosh~")
    acosh_tilde.__doc__ = """
    acosh~
    """

    adc_tilde = MaxObject("adc~")
    adc_tilde.__doc__ = """
    adc~

    Args:
    inputs (int, optional)
    """

    adoutput_tilde = MaxObject("adoutput~")
    adoutput_tilde.__doc__ = """
    adoutput~

    Args:
    audiodriver-output-channels (int, optional)
    """

    adsr_tilde = MaxObject("adsr~")
    adsr_tilde.__doc__ = """
    adsr~

    Args:
    attack (float, optional)
    decay (float, optional)
    sustain (float, optional)
    release (float, optional)

    Attributes:
    attack, decay, legato, maxsustain, release, retrigger, sustain, triggermode
    """

    adstatus = MaxObject("adstatus")
    adstatus.__doc__ = """
    adstatus

    Args:
    Controllable-settings: (symbol, required)
    """

    allpass_tilde = MaxObject("allpass~")
    allpass_tilde.__doc__ = """
    allpass~

    Args:
    max-delay (float, optional)
    initial-delay (float, optional)
    gain (float, optional)
    """

    amxd_tilde = MaxObject("amxd~")
    amxd_tilde.__doc__ = """
    amxd~

    Args:
    devicename (symbol, required)

    Attributes:
    active, annotation_name, autosave, autosize, mcisolate, parameter_enable,
    parameter_mappable, patchername, realtime_params, showheader
    """

    asin_tilde = MaxObject("asin~")
    asin_tilde.__doc__ = """
    asin~
    """

    asinh_tilde = MaxObject("asinh~")
    asinh_tilde.__doc__ = """
    asinh~
    """

    atan2_tilde = MaxObject("atan2~")
    atan2_tilde.__doc__ = """
    atan2~
    """

    atan_tilde = MaxObject("atan~")
    atan_tilde.__doc__ = """
    atan~
    """

    atanh_tilde = MaxObject("atanh~")
    atanh_tilde.__doc__ = """
    atanh~
    """

    atodb_tilde = MaxObject("atodb~")
    atodb_tilde.__doc__ = """
    atodb~
    """

    average_tilde = MaxObject("average~")
    average_tilde.__doc__ = """
    average~

    Args:
    max-averaging-interval (int, optional)
    averaging-mode (symbol, optional)

    Attributes:
    mode
    """

    avg_tilde = MaxObject("avg~")
    avg_tilde.__doc__ = """
    avg~
    """

    begin_tilde = MaxObject("begin~")
    begin_tilde.__doc__ = """
    begin~
    """

    biquad_tilde = MaxObject("biquad~")
    biquad_tilde.__doc__ = """
    biquad~

    Args:
    a0 (float, required)
    a1 (float, required)
    a2 (float, required)
    b1 (float, required)
    b2 (float, required)

    Attributes:
    smooth
    """

    bitand_tilde = MaxObject("bitand~")
    bitand_tilde.__doc__ = """
    bitand~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    bitnot_tilde = MaxObject("bitnot~")
    bitnot_tilde.__doc__ = """
    bitnot~

    Args:
    operational-mode (int, optional)

    Attributes:
    mode
    """

    bitor_tilde = MaxObject("bitor~")
    bitor_tilde.__doc__ = """
    bitor~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    bitsafe_tilde = MaxObject("bitsafe~")
    bitsafe_tilde.__doc__ = """
    bitsafe~
    """

    bitshift_tilde = MaxObject("bitshift~")
    bitshift_tilde.__doc__ = """
    bitshift~

    Args:
    number-of-bits/direction-of-shift (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    bitxor_tilde = MaxObject("bitxor~")
    bitxor_tilde.__doc__ = """
    bitxor~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    buffer_tilde = MaxObject("buffer~")
    buffer_tilde.__doc__ = """
    buffer~

    Args:
    name (symbol, required)
    filename (symbol, optional)
    duration (number, optional)
    channels (int, optional)

    Attributes:
    dither, filetype, format, quantization, samps, size
    """

    buffir_tilde = MaxObject("buffir~")
    buffir_tilde.__doc__ = """
    buffir~

    Args:
    buffer-name (symbol, required)
    read-offset (int, float, optional)
    read-duration (int, float, optional)
    """

    capture_tilde = MaxObject("capture~")
    capture_tilde.__doc__ = """
    capture~

    Args:
    behavioral-flag (f) (symbol, optional)
    maximum-samples (int, optional)
    signal-vector-indices (up to 10 ints) (list, optional)
    """

    cartopol_tilde = MaxObject("cartopol~")
    cartopol_tilde.__doc__ = """
    cartopol~
    """

    cascade_tilde = MaxObject("cascade~")
    cascade_tilde.__doc__ = """
    cascade~
    """

    change_tilde = MaxObject("change~")
    change_tilde.__doc__ = """
    change~
    """

    click_tilde = MaxObject("click~")
    click_tilde.__doc__ = """
    click~

    Args:
    wavetable-values (list, optional)
    """

    clip_tilde = MaxObject("clip~")
    clip_tilde.__doc__ = """
    clip~

    Args:
    minimum (float, optional)
    maximum (float, optional)

    Attributes:
    mode
    """

    comb_tilde = MaxObject("comb~")
    comb_tilde.__doc__ = """
    comb~

    Args:
    max-delay (float, optional)
    initial-delay (float, optional)
    gain-coefficient (float, optional)
    feedforward-coefficient (float, optional)
    feedback-coefficient (float, optional)
    """

    cos_tilde = MaxObject("cos~")
    cos_tilde.__doc__ = """
    cos~
    """

    cosh_tilde = MaxObject("cosh~")
    cosh_tilde.__doc__ = """
    cosh~
    """

    cosx_tilde = MaxObject("cosx~")
    cosx_tilde.__doc__ = """
    cosx~
    """

    count_tilde = MaxObject("count~")
    count_tilde.__doc__ = """
    count~

    Args:
    initial-value (int, optional)
    count-limit (int, optional)
    enable (int, optional)
    autoreset-state (int, optional)

    Attributes:
    autoreset
    """

    cross_tilde = MaxObject("cross~")
    cross_tilde.__doc__ = """
    cross~

    Args:
    cutoff-frequency (float, required)
    """

    curve_tilde = MaxObject("curve~")
    curve_tilde.__doc__ = """
    curve~

    Args:
    initial-value (number, optional)
    curve-parameter (number, optional)

    Attributes:
    maxpoints, shapemode
    """

    cycle_tilde = MaxObject("cycle~")
    cycle_tilde.__doc__ = """
    cycle~

    Args:
    frequency (number, optional)
    buffer-name (symbol, optional)
    sample-offset (int, optional)

    Attributes:
    buffer, buffer_offset, buffer_sizeinsamps, frequency, phase
    """

    dac_tilde = MaxObject("dac~")
    dac_tilde.__doc__ = """
    dac~

    Args:
    outputs (int, symbol, optional)
    """

    dbtoa_tilde = MaxObject("dbtoa~")
    dbtoa_tilde.__doc__ = """
    dbtoa~
    """

    degrade_tilde = MaxObject("degrade~")
    degrade_tilde.__doc__ = """
    degrade~

    Args:
    resampling-frequency-ratio (float, optional)
    number-of-quantization-bits (int, optional)
    """

    delay_tilde = MaxObject("delay~")
    delay_tilde.__doc__ = """
    delay~

    Args:
    maximum-delay-memory (int, required)
    initial-delay-time (list, optional)
    ramp-time (int, optional)

    Attributes:
    delay
    """

    delta_tilde = MaxObject("delta~")
    delta_tilde.__doc__ = """
    delta~
    """

    deltaclip_tilde = MaxObject("deltaclip~")
    deltaclip_tilde.__doc__ = """
    deltaclip~

    Args:
    minimum-slope-value (float, optional)
    minimum and maximum-slope-values (float, optional)
    """

    div_tilde = MaxObject("div~")
    div_tilde.__doc__ = """
    div~

    Args:
    initial-divisor (number, optional)
    """

    downsamp_tilde = MaxObject("downsamp~")
    downsamp_tilde.__doc__ = """
    downsamp~

    Args:
    downsampled-rate (number, optional)
    """

    dspstate_tilde = MaxObject("dspstate~")
    dspstate_tilde.__doc__ = """
    dspstate~
    """

    dsptime_tilde = MaxObject("dsptime~")
    dsptime_tilde.__doc__ = """
    dsptime~
    """

    edge_tilde = MaxObject("edge~")
    edge_tilde.__doc__ = """
    edge~
    """

    equals_tilde = MaxObject("equals~")
    equals_tilde.__doc__ = """
    equals~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    ezadc_tilde = MaxObject("ezadc~")
    ezadc_tilde.__doc__ = """
    ezadc~

    Attributes:
    bgcolor, border, bordercolor, color, elementcolor, local, offgradcolor1,
    offgradcolor2, ongradcolor1, ongradcolor2, style
    """

    ezdac_tilde = MaxObject("ezdac~")
    ezdac_tilde.__doc__ = """
    ezdac~

    Attributes:
    bgcolor, border, bordercolor, color, elementcolor, local, offgradcolor1,
    offgradcolor2, ongradcolor1, ongradcolor2, style
    """

    fbinshift_tilde = MaxObject("fbinshift~")
    fbinshift_tilde.__doc__ = """
    fbinshift~

    Args:
    frequency-shift (int, required)
    frequency-shift (float, optional)
    """

    fffb_tilde = MaxObject("fffb~")
    fffb_tilde.__doc__ = """
    fffb~

    Args:
    number-of-filters (int, required)
    1st-filter-frequency (float, optional)
    filter-frequency-ratios (float) (float, optional)
    Q (list, optional)
    harmonic-series-flag (H) (symbol, optional)
    """

    fft_tilde = MaxObject("fft~")
    fft_tilde.__doc__ = """
    fft~

    Args:
    number-of-FFT-samples (int, optional)
    spectral-frame-size (int, optional)
    phase (int, optional)
    """

    fftin_tilde = MaxObject("fftin~")
    fftin_tilde.__doc__ = """
    fftin~

    Args:
    inlet-assignment (int, required)
    window-envelope-function (symbol, optional)
    """

    fftinfo_tilde = MaxObject("fftinfo~")
    fftinfo_tilde.__doc__ = """
    fftinfo~
    """

    fftout_tilde = MaxObject("fftout~")
    fftout_tilde.__doc__ = """
    fftout~

    Args:
    outlet-assignment (int, required)
    window-envelope-function (symbol, optional)
    """

    filtercoeff_tilde = MaxObject("filtercoeff~")
    filtercoeff_tilde.__doc__ = """
    filtercoeff~

    Args:
    default-filter-type (symbol, optional)
    resampling-factor (int, optional)
    """

    filterdesign = MaxObject("filterdesign")
    filterdesign.__doc__ = """
    filterdesign

    Attributes:
    frequency, name, order, passband_ripple, response, samplerate, sos_output,
    stopband_attenuation, tf_output, topology, units, zpk_output
    """

    filterdetail = MaxObject("filterdetail")
    filterdetail.__doc__ = """
    filterdetail

    Attributes:
    numpoints
    """

    filtergraph_tilde = MaxObject("filtergraph~")
    filtergraph_tilde.__doc__ = """
    filtergraph~

    Attributes:
    autoout, bgcolor, bordercolor, bwidthcolor, curvecolor, dbdisplay, display_flat,
    domain, edit_Q, edit_amp, edit_analog, edit_displaydot, edit_filter, edit_freq,
    edit_gainmode, edit_maxQ, edit_maxamp, edit_maxfreq, edit_minQ, edit_minamp,
    edit_minfreq, edit_mode, fgcolor, fullspect, hbwidthcolor, hcurvecolor, hfgcolor,
    linmarkers, logamp, logfreq, logmarkers, markercolor, nfilters, numdisplay,
    parameter_enable, parameter_mappable, phasespect, range, style, textcolor
    """

    frame_tilde = MaxObject("frame~")
    frame_tilde.__doc__ = """
    frame~
    """

    frameaccum_tilde = MaxObject("frameaccum~")
    frameaccum_tilde.__doc__ = """
    frameaccum~

    Args:
    phasewrap-flag (0 or nonzero) (int, optional)
    """

    frameaverage_tilde = MaxObject("frameaverage~")
    frameaverage_tilde.__doc__ = """
    frameaverage~

    Attributes:
    framecount, framesize
    """

    framedelta_tilde = MaxObject("framedelta~")
    framedelta_tilde.__doc__ = """
    framedelta~
    """

    framesmooth_tilde = MaxObject("framesmooth~")
    framesmooth_tilde.__doc__ = """
    framesmooth~

    Attributes:
    framesize, smoothness
    """

    framesnap_tilde = MaxObject("framesnap~")
    framesnap_tilde.__doc__ = """
    framesnap~

    Args:
    interval (int, optional)

    Attributes:
    active, interval
    """

    freqshift_tilde = MaxObject("freqshift~")
    freqshift_tilde.__doc__ = """
    freqshift~

    Args:
    frequency-shift (int, required)
    frequency-shift (float, optional)
    """

    ftom_tilde = MaxObject("ftom~")
    ftom_tilde.__doc__ = """
    ftom~

    Attributes:
    base
    """

    fzero_tilde = MaxObject("fzero~")
    fzero_tilde.__doc__ = """
    fzero~

    Attributes:
    freqmax, freqmin, onsetamp, onsetlist, onsetperiod, onsetpitch, period, size,
    threshold
    """

    gain_tilde = MaxObject("gain~")
    gain_tilde.__doc__ = """
    gain~

    Attributes:
    bgcolor, bordercolor, inc, interp, interpinlet, knobcolor, multislider,
    orientation, parameter_enable, parameter_mappable, relative, scale, size,
    stripecolor, style
    """

    gate_tilde = MaxObject("gate~")
    gate_tilde.__doc__ = """
    gate~

    Args:
    number-of-outlets (int, optional)
    initial-open-outlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    gen = MaxObject("gen")
    gen.__doc__ = """
    gen

    Args:
    patcher-name (symbol, optional)

    Attributes:
    active, autoexport, cpu, cpumeasure, dumpoutlet, exportfolder, exportname,
    exportnotifier, exportscript, exportscriptargs, gen, hot, interval, nocache, poll,
    title
    """

    gen_tilde = MaxObject("gen~")
    gen_tilde.__doc__ = """
    gen~

    Args:
    patcher-name (symbol, optional)

    Attributes:
    autoexport, cpu, cpumeasure, dumpoutlet, exportfolder, exportname, exportnotifier,
    exportscript, exportscriptargs, gen, nocache, poll, title
    """

    gizmo_tilde = MaxObject("gizmo~")
    gizmo_tilde.__doc__ = """
    gizmo~

    Args:
    default-pitch-scalar (int, float, optional)
    """

    greaterthan_tilde = MaxObject("greaterthan~")
    greaterthan_tilde.__doc__ = """
    greaterthan~

    Args:
    initial-comparison-value (number, optional)
    """

    greaterthaneq_tilde = MaxObject("greaterthaneq~")
    greaterthaneq_tilde.__doc__ = """
    greaterthaneq~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    gridmeter_tilde = MaxObject("gridmeter~")
    gridmeter_tilde.__doc__ = """
    gridmeter~

    Attributes:
    attack, bgcolor, cellheight, cellwidth, color, columns, contrast, dividersize,
    elementcolor, hotcolor, interval, range, release, style
    """

    groove_tilde = MaxObject("groove~")
    groove_tilde.__doc__ = """
    groove~

    Args:
    buffer-name (symbol, required)
    number-of-outputs (int, optional)

    Attributes:
    basictuning, followglobaltempo, formant, formantcorrection, lock, loop, loopend,
    loopinterp, loopstart, mode, name, originallength, originaltempo, phase,
    pitchcorrection, pitchshift, pitchshiftcent, quality, slurtime, timestretch,
    transport
    """

    hilbert_tilde = MaxObject("hilbert~")
    hilbert_tilde.__doc__ = """
    hilbert~
    """

    hostcontrol_tilde = MaxObject("hostcontrol~")
    hostcontrol_tilde.__doc__ = """
    hostcontrol~
    """

    hostphasor_tilde = MaxObject("hostphasor~")
    hostphasor_tilde.__doc__ = """
    hostphasor~
    """

    hostsync_tilde = MaxObject("hostsync~")
    hostsync_tilde.__doc__ = """
    hostsync~
    """

    ifft_tilde = MaxObject("ifft~")
    ifft_tilde.__doc__ = """
    ifft~

    Args:
    IFFT-points (int, optional)
    """

    in_ = MaxObject("in")
    in_.__doc__ = """
    in

    Args:
    inlet-number/positioning (int, required)

    Attributes:
    attr_comment
    """

    in_tilde = MaxObject("in~")
    in_tilde.__doc__ = """
    in~

    Args:
    inlet-number (int, required)

    Attributes:
    attr_comment, chans
    """

    index_tilde = MaxObject("index~")
    index_tilde.__doc__ = """
    index~

    Args:
    buffer-name (symbol, required)
    buffer-channel-to-index (int, optional)
    """

    info_tilde = MaxObject("info~")
    info_tilde.__doc__ = """
    info~

    Args:
    buffer-name (symbol, optional)
    """

    ioscbank_tilde = MaxObject("ioscbank~")
    ioscbank_tilde.__doc__ = """
    ioscbank~

    Args:
    number-of-oscillators (int, optional)
    frequency-smoothing-factor (int, optional)
    amplitude-smoothing-factor (int, optional)
    """

    kink_tilde = MaxObject("kink~")
    kink_tilde.__doc__ = """
    kink~

    Args:
    slope-multiplier (float, optional)
    """

    lessthan_tilde = MaxObject("lessthan~")
    lessthan_tilde.__doc__ = """
    lessthan~

    Args:
    initial-comparison-value (int, float, optional)
    """

    lessthaneq_tilde = MaxObject("lessthaneq~")
    lessthaneq_tilde.__doc__ = """
    lessthaneq~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    levelmeter_tilde = MaxObject("levelmeter~")
    levelmeter_tilde.__doc__ = """
    levelmeter~

    Attributes:
    attack, bgcolor, bordercolor, coolcolor, displaychan, fgcolor, hotcolor,
    inactivealpha, interval, markercolor, markers, markersused, needlecolor, offset,
    overloadcolor, range, release, rounded, style, tepidcolor, warmcolor
    """

    limi_tilde = MaxObject("limi~")
    limi_tilde.__doc__ = """
    limi~

    Args:
    channel_count (int, optional)
    buffer_size (int, optional)

    Attributes:
    bypass, dcblock, lookahead, mode, postamp, preamp, release, threshold
    """

    line_tilde = MaxObject("line~")
    line_tilde.__doc__ = """
    line~

    Args:
    initial-value (int, float, optional)

    Attributes:
    maxpoints
    """

    log_tilde = MaxObject("log~")
    log_tilde.__doc__ = """
    log~

    Args:
    logarithmic-base (number, optional)
    """

    lookup_tilde = MaxObject("lookup~")
    lookup_tilde.__doc__ = """
    lookup~

    Args:
    buffer-name (symbol, required)
    sample-offset (int, optional)
    """

    lores_tilde = MaxObject("lores~")
    lores_tilde.__doc__ = """
    lores~

    Args:
    cutoff (number, optional)
    resonance (number, optional)

    Attributes:
    cutoff, resonance
    """

    matrix_tilde = MaxObject("matrix~")
    matrix_tilde.__doc__ = """
    matrix~

    Args:
    inlets (int, required)
    outlets (int, required)
    default-connect-gain (float, optional)

    Attributes:
    ramp
    """

    maximum_tilde = MaxObject("maximum~")
    maximum_tilde.__doc__ = """
    maximum~

    Args:
    initial-comparison-value (number, optional)
    """

    mc_2d_wave_tilde = MaxObject("mc.2d.wave~")
    mc_2d_wave_tilde.__doc__ = """
    mc.2d.wave~

    Args:
    buffer-name (symbol, required)
    start and end-points (number, optional)
    number-of-output-channels (int, optional)
    rows (int, optional)
    """

    mc_abs_tilde = MaxObject("mc.abs~")
    mc_abs_tilde.__doc__ = """
    mc.abs~
    """

    mc_acos_tilde = MaxObject("mc.acos~")
    mc_acos_tilde.__doc__ = """
    mc.acos~
    """

    mc_acosh_tilde = MaxObject("mc.acosh~")
    mc_acosh_tilde.__doc__ = """
    mc.acosh~
    """

    mc_adc_tilde = MaxObject("mc.adc~")
    mc_adc_tilde.__doc__ = """
    mc.adc~

    Args:
    inputs (symbol, optional)
    """

    mc_adsr_tilde = MaxObject("mc.adsr~")
    mc_adsr_tilde.__doc__ = """
    mc.adsr~

    Args:
    attack (float, optional)
    decay (float, optional)
    sustain (float, optional)
    release (float, optional)

    Attributes:
    attack, decay, legato, maxsustain, release, retrigger, sustain, triggermode
    """

    mc_allpass_tilde = MaxObject("mc.allpass~")
    mc_allpass_tilde.__doc__ = """
    mc.allpass~

    Args:
    max-delay (float, optional)
    initial-delay (float, optional)
    gain (float, optional)
    """

    mc_amxd_tilde = MaxObject("mc.amxd~")
    mc_amxd_tilde.__doc__ = """
    mc.amxd~

    Args:
    devicename (symbol, required)

    Attributes:
    active, annotation_name, autosave, autosize, mcisolate, parameter_enable,
    parameter_mappable, patchername, realtime_params, showheader
    """

    mc_apply_tilde = MaxObject("mc.apply~")
    mc_apply_tilde.__doc__ = """
    mc.apply~

    Args:
    channels (int, optional)

    Attributes:
    chans, functions, ramptime
    """

    mc_asin_tilde = MaxObject("mc.asin~")
    mc_asin_tilde.__doc__ = """
    mc.asin~
    """

    mc_asinh_tilde = MaxObject("mc.asinh~")
    mc_asinh_tilde.__doc__ = """
    mc.asinh~
    """

    mc_assign = MaxObject("mc.assign")
    mc_assign.__doc__ = """
    mc.assign

    Attributes:
    chans, delays, density, mode, pattern, pos
    """

    mc_atan_tilde = MaxObject("mc.atan~")
    mc_atan_tilde.__doc__ = """
    mc.atan~
    """

    mc_atanh_tilde = MaxObject("mc.atanh~")
    mc_atanh_tilde.__doc__ = """
    mc.atanh~
    """

    mc_atodb_tilde = MaxObject("mc.atodb~")
    mc_atodb_tilde.__doc__ = """
    mc.atodb~
    """

    mc_average_tilde = MaxObject("mc.average~")
    mc_average_tilde.__doc__ = """
    mc.average~

    Args:
    max-averaging-interval (int, optional)
    averaging-mode (symbol, optional)

    Attributes:
    mode
    """

    mc_avg_tilde = MaxObject("mc.avg~")
    mc_avg_tilde.__doc__ = """
    mc.avg~
    """

    mc_bands_tilde = MaxObject("mc.bands~")
    mc_bands_tilde.__doc__ = """
    mc.bands~

    Args:
    number-of-bands (int, required)
    """

    mc_biquad_tilde = MaxObject("mc.biquad~")
    mc_biquad_tilde.__doc__ = """
    mc.biquad~

    Args:
    a0 (float, required)
    a1 (float, required)
    a2 (float, required)
    b1 (float, required)
    b2 (float, required)

    Attributes:
    smooth
    """

    mc_bitand_tilde = MaxObject("mc.bitand~")
    mc_bitand_tilde.__doc__ = """
    mc.bitand~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    mc_bitnot_tilde = MaxObject("mc.bitnot~")
    mc_bitnot_tilde.__doc__ = """
    mc.bitnot~

    Args:
    operational-mode (int, optional)

    Attributes:
    mode
    """

    mc_bitor_tilde = MaxObject("mc.bitor~")
    mc_bitor_tilde.__doc__ = """
    mc.bitor~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    mc_bitsafe_tilde = MaxObject("mc.bitsafe~")
    mc_bitsafe_tilde.__doc__ = """
    mc.bitsafe~
    """

    mc_bitxor_tilde = MaxObject("mc.bitxor~")
    mc_bitxor_tilde.__doc__ = """
    mc.bitxor~

    Args:
    bitmask (int, optional)
    operational-mode (int, optional)

    Attributes:
    mode
    """

    mc_buffir_tilde = MaxObject("mc.buffir~")
    mc_buffir_tilde.__doc__ = """
    mc.buffir~

    Args:
    buffer-name (symbol, required)
    read-offset (int, float, optional)
    read-duration (int, float, optional)
    """

    mc_cartopol_tilde = MaxObject("mc.cartopol~")
    mc_cartopol_tilde.__doc__ = """
    mc.cartopol~
    """

    mc_cascade_tilde = MaxObject("mc.cascade~")
    mc_cascade_tilde.__doc__ = """
    mc.cascade~
    """

    mc_cell = MaxObject("mc.cell")
    mc_cell.__doc__ = """
    mc.cell

    Attributes:
    columns, constant, message, numeric, row
    """

    mc_change_tilde = MaxObject("mc.change~")
    mc_change_tilde.__doc__ = """
    mc.change~
    """

    mc_channelcount_tilde = MaxObject("mc.channelcount~")
    mc_channelcount_tilde.__doc__ = """
    mc.channelcount~
    """

    mc_chord_tilde = MaxObject("mc.chord~")
    mc_chord_tilde.__doc__ = """
    mc.chord~

    Args:
    channels (int, optional)

    Attributes:
    allocmode, busymapname, chans, embed, extendmode, inputmode, offmode, triggermode,
    usebusymap
    """

    mc_click_tilde = MaxObject("mc.click~")
    mc_click_tilde.__doc__ = """
    mc.click~

    Args:
    wavetable-values (list, optional)
    """

    mc_clip_tilde = MaxObject("mc.clip~")
    mc_clip_tilde.__doc__ = """
    mc.clip~

    Args:
    minimum (float, optional)
    maximum (float, optional)

    Attributes:
    mode
    """

    mc_comb_tilde = MaxObject("mc.comb~")
    mc_comb_tilde.__doc__ = """
    mc.comb~

    Args:
    max-delay (float, optional)
    initial-delay (float, optional)
    gain-coefficient (float, optional)
    feedforward-coefficient (float, optional)
    feedback-coefficient (float, optional)
    """

    mc_combine_tilde = MaxObject("mc.combine~")
    mc_combine_tilde.__doc__ = """
    mc.combine~

    Args:
    number-of-inlets (int, optional)

    Attributes:
    chans
    """

    mc_cos_tilde = MaxObject("mc.cos~")
    mc_cos_tilde.__doc__ = """
    mc.cos~
    """

    mc_cosh_tilde = MaxObject("mc.cosh~")
    mc_cosh_tilde.__doc__ = """
    mc.cosh~
    """

    mc_cosx_tilde = MaxObject("mc.cosx~")
    mc_cosx_tilde.__doc__ = """
    mc.cosx~
    """

    mc_count_tilde = MaxObject("mc.count~")
    mc_count_tilde.__doc__ = """
    mc.count~

    Args:
    initial-value (int, optional)
    count-limit (int, optional)
    enable (int, optional)
    autoreset-state (int, optional)

    Attributes:
    autoreset
    """

    mc_cross_tilde = MaxObject("mc.cross~")
    mc_cross_tilde.__doc__ = """
    mc.cross~

    Args:
    cutoff-frequency (float, required)
    """

    mc_curve_tilde = MaxObject("mc.curve~")
    mc_curve_tilde.__doc__ = """
    mc.curve~

    Args:
    initial-value (number, optional)
    curve-parameter (number, optional)

    Attributes:
    maxpoints, shapemode
    """

    mc_cycle_tilde = MaxObject("mc.cycle~")
    mc_cycle_tilde.__doc__ = """
    mc.cycle~

    Args:
    frequency (number, optional)
    buffer-name (symbol, optional)
    sample-offset (int, optional)

    Attributes:
    buffer, buffer_offset, buffer_sizeinsamps, frequency, phase
    """

    mc_dac_tilde = MaxObject("mc.dac~")
    mc_dac_tilde.__doc__ = """
    mc.dac~

    Args:
    outputs (symbol, optional)
    """

    mc_dbtoa_tilde = MaxObject("mc.dbtoa~")
    mc_dbtoa_tilde.__doc__ = """
    mc.dbtoa~
    """

    mc_degrade_tilde = MaxObject("mc.degrade~")
    mc_degrade_tilde.__doc__ = """
    mc.degrade~

    Args:
    resampling-frequency-ratio (float, optional)
    number-of-quantization-bits (int, optional)
    """

    mc_deinterleave_tilde = MaxObject("mc.deinterleave~")
    mc_deinterleave_tilde.__doc__ = """
    mc.deinterleave~

    Args:
    outputs (int, optional)
    """

    mc_delay_tilde = MaxObject("mc.delay~")
    mc_delay_tilde.__doc__ = """
    mc.delay~

    Args:
    maximum-delay-memory (int, required)
    initial-delay-time (list, optional)
    ramp-time (int, optional)

    Attributes:
    delay
    """

    mc_delta_tilde = MaxObject("mc.delta~")
    mc_delta_tilde.__doc__ = """
    mc.delta~
    """

    mc_deltaclip_tilde = MaxObject("mc.deltaclip~")
    mc_deltaclip_tilde.__doc__ = """
    mc.deltaclip~

    Args:
    minimum-slope-value (float, optional)
    minimum and maximum-slope-values (float, optional)
    """

    mc_div_tilde = MaxObject("mc.div~")
    mc_div_tilde.__doc__ = """
    mc.div~

    Args:
    initial-divisor (number, optional)
    """

    mc_downsamp_tilde = MaxObject("mc.downsamp~")
    mc_downsamp_tilde.__doc__ = """
    mc.downsamp~

    Args:
    downsampled-rate (number, optional)
    """

    mc_dup_tilde = MaxObject("mc.dup~")
    mc_dup_tilde.__doc__ = """
    mc.dup~

    Args:
    channel count (int, optional)

    Attributes:
    chans
    """

    mc_edge_tilde = MaxObject("mc.edge~")
    mc_edge_tilde.__doc__ = """
    mc.edge~
    """

    mc_equals_tilde = MaxObject("mc.equals~")
    mc_equals_tilde.__doc__ = """
    mc.equals~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    mc_evolve_tilde = MaxObject("mc.evolve~")
    mc_evolve_tilde.__doc__ = """
    mc.evolve~

    Args:
    chans (int, required)

    Attributes:
    chans, inclusive
    """

    mc_ezadc_tilde = MaxObject("mc.ezadc~")
    mc_ezadc_tilde.__doc__ = """
    mc.ezadc~

    Attributes:
    bgcolor, border, bordercolor, color, elementcolor, local, offgradcolor1,
    offgradcolor2, ongradcolor1, ongradcolor2, style
    """

    mc_ezdac_tilde = MaxObject("mc.ezdac~")
    mc_ezdac_tilde.__doc__ = """
    mc.ezdac~

    Attributes:
    bgcolor, border, bordercolor, color, elementcolor, local, offgradcolor1,
    offgradcolor2, ongradcolor1, ongradcolor2, style
    """

    mc_fffb_tilde = MaxObject("mc.fffb~")
    mc_fffb_tilde.__doc__ = """
    mc.fffb~

    Args:
    number-of-filters (int, required)
    1st-filter-frequency (float, optional)
    filter-frequency-ratios (float) (float, optional)
    Q (list, optional)
    harmonic-series-flag (H) (symbol, optional)
    """

    mc_fft_tilde = MaxObject("mc.fft~")
    mc_fft_tilde.__doc__ = """
    mc.fft~

    Args:
    number-of-FFT-samples (int, optional)
    spectral-frame-size (int, optional)
    phase (int, optional)
    """

    mc_filtercoeff_tilde = MaxObject("mc.filtercoeff~")
    mc_filtercoeff_tilde.__doc__ = """
    mc.filtercoeff~

    Args:
    default-filter-type (symbol, optional)
    resampling-factor (int, optional)
    """

    mc_frameaccum_tilde = MaxObject("mc.frameaccum~")
    mc_frameaccum_tilde.__doc__ = """
    mc.frameaccum~

    Args:
    phasewrap-flag (0 or nonzero) (int, optional)
    """

    mc_frameaverage_tilde = MaxObject("mc.frameaverage~")
    mc_frameaverage_tilde.__doc__ = """
    mc.frameaverage~

    Attributes:
    framecount, framesize
    """

    mc_framedelta_tilde = MaxObject("mc.framedelta~")
    mc_framedelta_tilde.__doc__ = """
    mc.framedelta~
    """

    mc_framesmooth_tilde = MaxObject("mc.framesmooth~")
    mc_framesmooth_tilde.__doc__ = """
    mc.framesmooth~

    Attributes:
    framesize, smoothness
    """

    mc_freqshift_tilde = MaxObject("mc.freqshift~")
    mc_freqshift_tilde.__doc__ = """
    mc.freqshift~

    Args:
    frequency-shift (int, required)
    frequency-shift (float, optional)
    """

    mc_ftom_tilde = MaxObject("mc.ftom~")
    mc_ftom_tilde.__doc__ = """
    mc.ftom~

    Attributes:
    base
    """

    mc_fzero_tilde = MaxObject("mc.fzero~")
    mc_fzero_tilde.__doc__ = """
    mc.fzero~

    Attributes:
    freqmax, freqmin, onsetamp, onsetlist, onsetperiod, onsetpitch, period, size,
    threshold
    """

    mc_gain_tilde = MaxObject("mc.gain~")
    mc_gain_tilde.__doc__ = """
    mc.gain~

    Attributes:
    bgcolor, bordercolor, inc, interp, interpinlet, knobcolor, multislider,
    orientation, parameter_enable, parameter_mappable, relative, scale, size,
    stripecolor, style
    """

    mc_gate_tilde = MaxObject("mc.gate~")
    mc_gate_tilde.__doc__ = """
    mc.gate~

    Args:
    number-of-outlets (int, optional)
    initial-open-outlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    mc_gen = MaxObject("mc.gen")
    mc_gen.__doc__ = """
    mc.gen

    Args:
    patcher-name (symbol, optional)

    Attributes:
    active, autoexport, cpu, cpumeasure, dumpoutlet, exportfolder, exportname,
    exportnotifier, exportscript, exportscriptargs, gen, hot, interval, nocache, poll,
    title
    """

    mc_gen_tilde = MaxObject("mc.gen~")
    mc_gen_tilde.__doc__ = """
    mc.gen~

    Args:
    patcher-name (symbol, optional)

    Attributes:
    autoexport, cpu, cpumeasure, dumpoutlet, exportfolder, exportname, exportnotifier,
    exportscript, exportscriptargs, gen, nocache, poll, title
    """

    mc_generate_tilde = MaxObject("mc.generate~")
    mc_generate_tilde.__doc__ = """
    mc.generate~

    Args:
    initial-parameter-1 (float, optional)
    initial-parameter-2 (float, optional)
    initial-parameter-3 (float, optional)

    Attributes:
    chans, op, p1, p2, p3, ramptime
    """

    mc_gradient_tilde = MaxObject("mc.gradient~")
    mc_gradient_tilde.__doc__ = """
    mc.gradient~

    Args:
    chans (int, required)

    Attributes:
    chans, mode
    """

    mc_greaterthan_tilde = MaxObject("mc.greaterthan~")
    mc_greaterthan_tilde.__doc__ = """
    mc.greaterthan~

    Args:
    initial-comparison-value (number, optional)
    """

    mc_greaterthaneq_tilde = MaxObject("mc.greaterthaneq~")
    mc_greaterthaneq_tilde.__doc__ = """
    mc.greaterthaneq~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    mc_groove_tilde = MaxObject("mc.groove~")
    mc_groove_tilde.__doc__ = """
    mc.groove~

    Args:
    buffer-name (symbol, required)
    number-of-outputs (int, optional)

    Attributes:
    basictuning, followglobaltempo, formant, formantcorrection, lock, loop, loopend,
    loopinterp, loopstart, mode, name, originallength, originaltempo, phase,
    pitchcorrection, pitchshift, pitchshiftcent, quality, slurtime, timestretch,
    transport
    """

    mc_hilbert_tilde = MaxObject("mc.hilbert~")
    mc_hilbert_tilde.__doc__ = """
    mc.hilbert~
    """

    mc_ifft_tilde = MaxObject("mc.ifft~")
    mc_ifft_tilde.__doc__ = """
    mc.ifft~

    Args:
    IFFT-points (int, optional)
    """

    mc_in_tilde = MaxObject("mc.in~")
    mc_in_tilde.__doc__ = """
    mc.in~

    Args:
    starting-inlet-number (int, required)

    Attributes:
    attr_comment, chans
    """

    mc_index_tilde = MaxObject("mc.index~")
    mc_index_tilde.__doc__ = """
    mc.index~

    Args:
    buffer-name (symbol, required)
    buffer-channel-to-index (int, optional)
    """

    mc_interleave_tilde = MaxObject("mc.interleave~")
    mc_interleave_tilde.__doc__ = """
    mc.interleave~

    Args:
    inputs (int, optional)
    """

    mc_kink_tilde = MaxObject("mc.kink~")
    mc_kink_tilde.__doc__ = """
    mc.kink~

    Args:
    slope-multiplier (float, optional)
    """

    mc_lessthan_tilde = MaxObject("mc.lessthan~")
    mc_lessthan_tilde.__doc__ = """
    mc.lessthan~

    Args:
    initial-comparison-value (int, float, optional)
    """

    mc_lessthaneq_tilde = MaxObject("mc.lessthaneq~")
    mc_lessthaneq_tilde.__doc__ = """
    mc.lessthaneq~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    mc_limi_tilde = MaxObject("mc.limi~")
    mc_limi_tilde.__doc__ = """
    mc.limi~

    Args:
    channel_count (int, optional)
    buffer_size (int, optional)

    Attributes:
    bypass, dcblock, lookahead, mode, postamp, preamp, release, threshold
    """

    mc_line_tilde = MaxObject("mc.line~")
    mc_line_tilde.__doc__ = """
    mc.line~

    Args:
    initial-value (int, float, optional)

    Attributes:
    maxpoints
    """

    mc_list_tilde = MaxObject("mc.list~")
    mc_list_tilde.__doc__ = """
    mc.list~

    Args:
    initial values (list, required)

    Attributes:
    chans
    """

    mc_log_tilde = MaxObject("mc.log~")
    mc_log_tilde.__doc__ = """
    mc.log~

    Args:
    logarithmic-base (number, optional)
    """

    mc_lookup_tilde = MaxObject("mc.lookup~")
    mc_lookup_tilde.__doc__ = """
    mc.lookup~

    Args:
    buffer-name (symbol, required)
    sample-offset (int, optional)
    """

    mc_lores_tilde = MaxObject("mc.lores~")
    mc_lores_tilde.__doc__ = """
    mc.lores~

    Args:
    cutoff (number, optional)
    resonance (number, optional)

    Attributes:
    cutoff, resonance
    """

    mc_makelist = MaxObject("mc.makelist")
    mc_makelist.__doc__ = """
    mc.makelist

    Attributes:
    mode, voices
    """

    mc_matrix_tilde = MaxObject("mc.matrix~")
    mc_matrix_tilde.__doc__ = """
    mc.matrix~

    Args:
    inlets (int, required)
    outlets (int, required)
    default-connect-gain (float, optional)

    Attributes:
    ramp
    """

    mc_maximum_tilde = MaxObject("mc.maximum~")
    mc_maximum_tilde.__doc__ = """
    mc.maximum~

    Args:
    initial-comparison-value (number, optional)
    """

    mc_midiplayer_tilde = MaxObject("mc.midiplayer~")
    mc_midiplayer_tilde.__doc__ = """
    mc.midiplayer~

    Attributes:
    chanmod, defaultdur, defaultnote, defaultvelocity, mpemode, playzero, triggermode,
    velcurve
    """

    mc_minimum_tilde = MaxObject("mc.minimum~")
    mc_minimum_tilde.__doc__ = """
    mc.minimum~

    Args:
    initial-comparison-value (number, optional)
    """

    mc_minmax_tilde = MaxObject("mc.minmax~")
    mc_minmax_tilde.__doc__ = """
    mc.minmax~
    """

    mc_minus_tilde = MaxObject("mc.minus~")
    mc_minus_tilde.__doc__ = """
    mc.minus~

    Args:
    initial-subtraction-value (number, optional)
    """

    mc_mixdown_tilde = MaxObject("mc.mixdown~")
    mc_mixdown_tilde.__doc__ = """
    mc.mixdown~

    Args:
    output-channel-count (int, optional)

    Attributes:
    activechans, autogain, busymapname, chans, linearpanmode, linearpanscalefactor,
    pancontrolmode, usebusymap
    """

    mc_modulo_tilde = MaxObject("mc.modulo~")
    mc_modulo_tilde.__doc__ = """
    mc.modulo~

    Args:
    initial-divisor (number, optional)
    """

    mc_mstosamps_tilde = MaxObject("mc.mstosamps~")
    mc_mstosamps_tilde.__doc__ = """
    mc.mstosamps~
    """

    mc_mtof_tilde = MaxObject("mc.mtof~")
    mc_mtof_tilde.__doc__ = """
    mc.mtof~

    Attributes:
    base
    """

    mc_noise_tilde = MaxObject("mc.noise~")
    mc_noise_tilde.__doc__ = """
    mc.noise~

    Attributes:
    classic
    """

    mc_normalize_tilde = MaxObject("mc.normalize~")
    mc_normalize_tilde.__doc__ = """
    mc.normalize~

    Args:
    initial-maximum-output-amplitude (float, optional)
    """

    mc_noteallocator_tilde = MaxObject("mc.noteallocator~")
    mc_noteallocator_tilde.__doc__ = """
    mc.noteallocator~

    Args:
    voice count (int, optional)

    Attributes:
    direct, hires, mpemode, name, steal, voices
    """

    mc_notequals_tilde = MaxObject("mc.notequals~")
    mc_notequals_tilde.__doc__ = """
    mc.notequals~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    mc_number_tilde = MaxObject("mc.number~")
    mc_number_tilde.__doc__ = """
    mc.number~

    Attributes:
    bgcolor, bgcolor2, bordercolor, chans, color, displaychan, ft1, hbgcolor,
    htextcolor, interval, maximum, minimum, monitormode, numdecimalplaces, sigoutmode,
    style, textcolor
    """

    mc_omx_4band_tilde = MaxObject("mc.omx.4band~")
    mc_omx_4band_tilde.__doc__ = """
    mc.omx.4band~
    """

    mc_omx_5band_tilde = MaxObject("mc.omx.5band~")
    mc_omx_5band_tilde.__doc__ = """
    mc.omx.5band~
    """

    mc_omx_comp_tilde = MaxObject("mc.omx.comp~")
    mc_omx_comp_tilde.__doc__ = """
    mc.omx.comp~
    """

    mc_omx_peaklim_tilde = MaxObject("mc.omx.peaklim~")
    mc_omx_peaklim_tilde.__doc__ = """
    mc.omx.peaklim~
    """

    mc_onepole_tilde = MaxObject("mc.onepole~")
    mc_onepole_tilde.__doc__ = """
    mc.onepole~

    Args:
    center-frequency (float, optional)
    Hz/linear/radians (symbol, optional)
    """

    mc_op_tilde = MaxObject("mc.op~")
    mc_op_tilde.__doc__ = """
    mc.op~

    Attributes:
    op
    """

    mc_out_tilde = MaxObject("mc.out~")
    mc_out_tilde.__doc__ = """
    mc.out~

    Args:
    starting-outlet-number (int, required)

    Attributes:
    attr_comment, chans
    """

    mc_overdrive_tilde = MaxObject("mc.overdrive~")
    mc_overdrive_tilde.__doc__ = """
    mc.overdrive~

    Args:
    drive-factor (int, required)
    drive-factor (float, optional)
    """

    mc_pack_tilde = MaxObject("mc.pack~")
    mc_pack_tilde.__doc__ = """
    mc.pack~

    Args:
    size (int, required)

    Attributes:
    chans
    """

    mc_pattern_tilde = MaxObject("mc.pattern~")
    mc_pattern_tilde.__doc__ = """
    mc.pattern~

    Args:
    channels (int, required)

    Attributes:
    autorecord, chans, defaultmute, defaultquantize, defaultramp, defaultwrap, embed,
    immediate, in, individual, ref
    """

    mc_peakamp_tilde = MaxObject("mc.peakamp~")
    mc_peakamp_tilde.__doc__ = """
    mc.peakamp~

    Args:
    ms-output-interval (int, optional)

    Attributes:
    interval, signed
    """

    mc_peek_tilde = MaxObject("mc.peek~")
    mc_peek_tilde.__doc__ = """
    mc.peek~

    Args:
    buffer-name (symbol, required)
    buffer-channel (int, optional)
    clipping-enable-flag (int, optional)
    """

    mc_pfft_tilde = MaxObject("mc.pfft~")
    mc_pfft_tilde.__doc__ = """
    mc.pfft~

    Args:
    subpatch-name (symbol, required)
    FFT-size (int, optional)
    overlap-factor (hop-size-denominator) (int, optional)
    start-onset (int, optional)
    full-spectrum-flag (0 or nonzero) (int, optional)
    'args' and list-of-argument-values (symbol, optional)
    """

    mc_phasegroove_tilde = MaxObject("mc.phasegroove~")
    mc_phasegroove_tilde.__doc__ = """
    mc.phasegroove~

    Attributes:
    conflict
    """

    mc_phaseshift_tilde = MaxObject("mc.phaseshift~")
    mc_phaseshift_tilde.__doc__ = """
    mc.phaseshift~

    Args:
    frequency (number, optional)
    q (number, optional)
    """

    mc_phasewrap_tilde = MaxObject("mc.phasewrap~")
    mc_phasewrap_tilde.__doc__ = """
    mc.phasewrap~
    """

    mc_phasor_tilde = MaxObject("mc.phasor~")
    mc_phasor_tilde.__doc__ = """
    mc.phasor~

    Args:
    initial-frequency (list, optional)

    Attributes:
    frequency, jitter, limit, lock, phaseoffset, syncupdate, transport
    """

    mc_pink_tilde = MaxObject("mc.pink~")
    mc_pink_tilde.__doc__ = """
    mc.pink~
    """

    mc_pitchshift_tilde = MaxObject("mc.pitchshift~")
    mc_pitchshift_tilde.__doc__ = """
    mc.pitchshift~

    Args:
    channels (int, optional)

    Attributes:
    constantlatency, enabled, pitchshift, pitchshiftcent, quality, reportlatency,
    usecents
    """

    mc_play_tilde = MaxObject("mc.play~")
    mc_play_tilde.__doc__ = """
    mc.play~

    Args:
    buffer-name (symbol, required)
    number-of-output-channels (int, optional)

    Attributes:
    interptime, loop, loopinterp
    """

    mc_playlist_tilde = MaxObject("mc.playlist~")
    mc_playlist_tilde.__doc__ = """
    mc.playlist~

    Attributes:
    accentcolor, allowreorder, basictuning, bgcolor, channelcount, chans, clipheight,
    color, elementcolor, expansion, followglobaltempo, formant, formantcorrection,
    loop, loopreport, mode, name, originallength, originaltempo, parameter_enable,
    parameter_mappable, pitchcorrection, pitchshift, pitchshiftcent, quality,
    reportprogress, selectioncolor, showname, slurtime, speed, style, textcolor,
    timestretch, waveformdisplay
    """

    mc_plus_tilde = MaxObject("mc.plus~")
    mc_plus_tilde.__doc__ = """
    mc.plus~

    Args:
    initial-offset (number, optional)
    """

    mc_plusequals_tilde = MaxObject("mc.plusequals~")
    mc_plusequals_tilde.__doc__ = """
    mc.plusequals~

    Args:
    initial-sum (float, optional)
    """

    mc_poltocar_tilde = MaxObject("mc.poltocar~")
    mc_poltocar_tilde.__doc__ = """
    mc.poltocar~
    """

    mc_poly_tilde = MaxObject("mc.poly~")
    mc_poly_tilde.__doc__ = """
    mc.poly~

    Args:
    patcher-name (symbol, required)
    number-of-instances (int, optional)
    local and flag (0 or 1) (symbol, optional)
    'up' and up-sampling-factor (symbol, optional)
    'down' and down-sampling factor (symbol, optional)
    'args' and list-of-argument-values (symbol, optional)

    Attributes:
    args, legacynotemode, midimode, mpemode, parallel, patchername, replicate,
    resampling, steal, target, voices, vs, zone
    """

    mc_pong_tilde = MaxObject("mc.pong~")
    mc_pong_tilde.__doc__ = """
    mc.pong~

    Args:
    folding-mode (int, optional)
    low-value (float, optional)
    high-value (float, optional)

    Attributes:
    mode, range
    """

    mc_pow_tilde = MaxObject("mc.pow~")
    mc_pow_tilde.__doc__ = """
    mc.pow~

    Args:
    base-value (number, optional)
    """

    mc_ramp_tilde = MaxObject("mc.ramp~")
    mc_ramp_tilde.__doc__ = """
    mc.ramp~

    Args:
    duration (float, optional)

    Attributes:
    curve, duration, end, interval, mode, reset, retrigger, start
    """

    mc_rampsmooth_tilde = MaxObject("mc.rampsmooth~")
    mc_rampsmooth_tilde.__doc__ = """
    mc.rampsmooth~

    Args:
    ramp-up-samples (int, optional)
    ramp-down-samples (int, optional)

    Attributes:
    rampdown, rampup
    """

    mc_rand_tilde = MaxObject("mc.rand~")
    mc_rand_tilde.__doc__ = """
    mc.rand~

    Args:
    initial-frequency (number, optional)
    """

    mc_range_tilde = MaxObject("mc.range~")
    mc_range_tilde.__doc__ = """
    mc.range~

    Args:
    size (int, required)

    Attributes:
    chans, hi, inclusive, lo, reflection
    """

    mc_rate_tilde = MaxObject("mc.rate~")
    mc_rate_tilde.__doc__ = """
    mc.rate~

    Args:
    multiplier (float, optional)
    sync-mode-flag (int, optional)

    Attributes:
    sync
    """

    mc_rdiv_tilde = MaxObject("mc.rdiv~")
    mc_rdiv_tilde.__doc__ = """
    mc.rdiv~

    Args:
    initial-divisor (number, optional)
    """

    mc_receive_tilde = MaxObject("mc.receive~")
    mc_receive_tilde.__doc__ = """
    mc.receive~

    Args:
    object-name (symbol, required)
    channel-count (int, optional)

    Attributes:
    chans, name
    """

    mc_record_tilde = MaxObject("mc.record~")
    mc_record_tilde.__doc__ = """
    mc.record~

    Args:
    buffer-name (symbol, required)
    input-channels (int, optional)

    Attributes:
    append, loop, loopend, loopstart, transport
    """

    mc_rect_tilde = MaxObject("mc.rect~")
    mc_rect_tilde.__doc__ = """
    mc.rect~

    Args:
    frequency (number, optional)
    pulse-width (number, optional)
    """

    mc_resize_tilde = MaxObject("mc.resize~")
    mc_resize_tilde.__doc__ = """
    mc.resize~

    Args:
    channels (int, required)

    Attributes:
    chans, replicate, select
    """

    mc_reson_tilde = MaxObject("mc.reson~")
    mc_reson_tilde.__doc__ = """
    mc.reson~

    Args:
    initial-gain (float, optional)
    center-frequency (float, optional)
    Q (float, optional)

    Attributes:
    cf, gain, q
    """

    mc_retune_tilde = MaxObject("mc.retune~")
    mc_retune_tilde.__doc__ = """
    mc.retune~

    Args:
    standard pitch (int, required)

    Attributes:
    correction_ambience_threshold, correction_amount, correction_bypass,
    correction_threshold, enablednotes, notebase, notelist, pitchdetection, quality,
    reportlatency, retune, use_16bit, windowsize
    """

    mc_rminus_tilde = MaxObject("mc.rminus~")
    mc_rminus_tilde.__doc__ = """
    mc.rminus~

    Args:
    initial-subtraction-value (number, optional)
    """

    mc_round_tilde = MaxObject("mc.round~")
    mc_round_tilde.__doc__ = """
    mc.round~

    Args:
    int or float (number, optional)

    Attributes:
    nearest
    """

    mc_route = MaxObject("mc.route")
    mc_route.__doc__ = """
    mc.route

    Args:
    Outlets (int, optional)
    """

    mc_sah_tilde = MaxObject("mc.sah~")
    mc_sah_tilde.__doc__ = """
    mc.sah~

    Args:
    initial-trigger-value (number, optional)

    Attributes:
    duration, thresh, triggermode
    """

    mc_sampstoms_tilde = MaxObject("mc.sampstoms~")
    mc_sampstoms_tilde.__doc__ = """
    mc.sampstoms~
    """

    mc_sash_tilde = MaxObject("mc.sash~")
    mc_sash_tilde.__doc__ = """
    mc.sash~

    Attributes:
    advancelevel, dir, maxsize, mode, samplelevel, size
    """

    mc_saw_tilde = MaxObject("mc.saw~")
    mc_saw_tilde.__doc__ = """
    mc.saw~

    Args:
    initial-frequency (number, optional)
    """

    mc_scale_tilde = MaxObject("mc.scale~")
    mc_scale_tilde.__doc__ = """
    mc.scale~

    Args:
    minimum-in-value (number, required)
    maximum-in-value (number, required)
    minimum-out-value (number, required)
    maximum-out-value (number, required)
    scaling-curve (float, optional)

    Attributes:
    classic
    """

    mc_selector_tilde = MaxObject("mc.selector~")
    mc_selector_tilde.__doc__ = """
    mc.selector~

    Args:
    number-of-inputs (int, optional)
    initially-open-inlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    mc_send_tilde = MaxObject("mc.send~")
    mc_send_tilde.__doc__ = """
    mc.send~

    Args:
    object-name (symbol, required)
    channel-count (int, optional)

    Attributes:
    chans, name
    """

    mc_separate_tilde = MaxObject("mc.separate~")
    mc_separate_tilde.__doc__ = """
    mc.separate~

    Args:
    channels per outlet (int, optional)

    Attributes:
    chans
    """

    mc_seq_tilde = MaxObject("mc.seq~")
    mc_seq_tilde.__doc__ = """
    mc.seq~
    """

    mc_sfplay_tilde = MaxObject("mc.sfplay~")
    mc_sfplay_tilde.__doc__ = """
    mc.sfplay~

    Args:
    sflist-object-name (symbol, optional)
    number-of-output-channels (int, optional)
    buffer-size (int, optional)
    position-outlet-flag (int, optional)
    object-reference-name (symbol, optional)

    Attributes:
    audiofile, basictuning, chans, followglobaltempo, formant, formantcorrection,
    loop, mode, name, originallength, originaltempo, pitchcorrection, pitchshift,
    pitchshiftcent, quality, slurtime, speed, timestretch
    """

    mc_sfrecord_tilde = MaxObject("mc.sfrecord~")
    mc_sfrecord_tilde.__doc__ = """
    mc.sfrecord~

    Args:
    number-of-channels (int, optional)
    buffer-size (int, optional)

    Attributes:
    bitdepth, dither, nchans, quantization, resample, sortloop
    """

    mc_shape_tilde = MaxObject("mc.shape~")
    mc_shape_tilde.__doc__ = """
    mc.shape~

    Attributes:
    constant, curvemode
    """

    mc_sig_tilde = MaxObject("mc.sig~")
    mc_sig_tilde.__doc__ = """
    mc.sig~

    Args:
    initial-output-value (number, optional)
    """

    mc_sinh_tilde = MaxObject("mc.sinh~")
    mc_sinh_tilde.__doc__ = """
    mc.sinh~
    """

    mc_sinx_tilde = MaxObject("mc.sinx~")
    mc_sinx_tilde.__doc__ = """
    mc.sinx~
    """

    mc_slide_tilde = MaxObject("mc.slide~")
    mc_slide_tilde.__doc__ = """
    mc.slide~

    Args:
    slide-up (float, optional)
    slide-down (float, optional)

    Attributes:
    slidedown, slideup
    """

    mc_snapshot_tilde = MaxObject("mc.snapshot~")
    mc_snapshot_tilde.__doc__ = """
    mc.snapshot~

    Args:
    reporting-interval (list, optional)

    Attributes:
    active, interval
    """

    mc_snowfall_tilde = MaxObject("mc.snowfall~")
    mc_snowfall_tilde.__doc__ = """
    mc.snowfall~

    Args:
    dimenions (int, optional)

    Attributes:
    boundarymode, dimensions, direction, directiondev, endmode, endvalue, energyramp,
    initial, initialdev, interval, intervaldev, max, min, scalemax, scalemin, squish,
    wanderprob
    """

    mc_snowphasor_tilde = MaxObject("mc.snowphasor~")
    mc_snowphasor_tilde.__doc__ = """
    mc.snowphasor~

    Attributes:
    busymapname, chans, interval, intervalcycle, intervaldev, mode, perchantriggers,
    prob, probdev, rampdev, ramptime, rate, ratedev, threshold, usebusymap
    """

    mc_spike_tilde = MaxObject("mc.spike~")
    mc_spike_tilde.__doc__ = """
    mc.spike~

    Args:
    refractory-period (int, float, optional)
    """

    mc_sqrt_tilde = MaxObject("mc.sqrt~")
    mc_sqrt_tilde.__doc__ = """
    mc.sqrt~
    """

    mc_stash_tilde = MaxObject("mc.stash~")
    mc_stash_tilde.__doc__ = """
    mc.stash~

    Args:
    sample-thresh (float, optional)
    advance-thresh (float, optional)

    Attributes:
    advancelevel, advancetriggermode, dir, duration, interp, maxsize, mode,
    samplelevel, sampletriggermode, size, writemode
    """

    mc_stereo_tilde = MaxObject("mc.stereo~")
    mc_stereo_tilde.__doc__ = """
    mc.stereo~

    Attributes:
    activechans, autogain, busymapname, chans, linearpanmode, linearpanscalefactor,
    pancontrolmode, usebusymap
    """

    mc_stutter_tilde = MaxObject("mc.stutter~")
    mc_stutter_tilde.__doc__ = """
    mc.stutter~

    Args:
    max-buffer-length (int, required)
    initial-buffer-size (int, required)
    trigger-polarity (int, required)
    number-of-copied-samples (int, required)
    number-of-outputs (int, optional)
    """

    mc_subdiv_tilde = MaxObject("mc.subdiv~")
    mc_subdiv_tilde.__doc__ = """
    mc.subdiv~

    Args:
    subdivisions (int, required)

    Attributes:
    div, lockprob, pattern, prob, silentmode, syncupdate
    """

    mc_svf_tilde = MaxObject("mc.svf~")
    mc_svf_tilde.__doc__ = """
    mc.svf~

    Args:
    center-frequency (float, optional)
    resonance (float, optional)
    Hz (symbol, optional)
    linear (symbol, optional)
    radians (symbol, optional)
    """

    mc_swing_tilde = MaxObject("mc.swing~")
    mc_swing_tilde.__doc__ = """
    mc.swing~

    Args:
    swing (float, optional)

    Attributes:
    swing, syncupdate
    """

    mc_sync_tilde = MaxObject("mc.sync~")
    mc_sync_tilde.__doc__ = """
    mc.sync~

    Attributes:
    rtport
    """

    mc_table_tilde = MaxObject("mc.table~")
    mc_table_tilde.__doc__ = """
    mc.table~

    Attributes:
    embed, extend, inmap, inputmode, interp, name, outscale, parameter_enable,
    parameter_mappable, range, signed, size, triggermode
    """

    mc_tanh_tilde = MaxObject("mc.tanh~")
    mc_tanh_tilde.__doc__ = """
    mc.tanh~
    """

    mc_tanx_tilde = MaxObject("mc.tanx~")
    mc_tanx_tilde.__doc__ = """
    mc.tanx~
    """

    mc_tapin_tilde = MaxObject("mc.tapin~")
    mc_tapin_tilde.__doc__ = """
    mc.tapin~

    Args:
    maximum-delay (number, optional)
    """

    mc_tapout_tilde = MaxObject("mc.tapout~")
    mc_tapout_tilde.__doc__ = """
    mc.tapout~

    Args:
    initial-delay (number, optional)

    Attributes:
    unique
    """

    mc_target = MaxObject("mc.target")
    mc_target.__doc__ = """
    mc.target

    Args:
    prepend (symbol, optional)
    initial voice (int, optional)

    Attributes:
    append, prepend
    """

    mc_targetlist = MaxObject("mc.targetlist")
    mc_targetlist.__doc__ = """
    mc.targetlist

    Args:
    prepend (symbol, optional)
    voice index (int, optional)
    inlet count (int, optional)

    Attributes:
    listmode
    """

    mc_teeth_tilde = MaxObject("mc.teeth~")
    mc_teeth_tilde.__doc__ = """
    mc.teeth~

    Args:
    feedforward-delay (float, optional)
    feedback-delay (float, optional)
    gain (float, optional)
    feedforward-gain (float, optional)
    feedback-gain (float, optional)
    """

    mc_thresh_tilde = MaxObject("mc.thresh~")
    mc_thresh_tilde.__doc__ = """
    mc.thresh~

    Args:
    low/reset-threshold (float, required)
    high/set-threshold (float, required)
    """

    mc_times_tilde = MaxObject("mc.times~")
    mc_times_tilde.__doc__ = """
    mc.times~

    Args:
    initial-multiplier (number, optional)
    """

    mc_train_tilde = MaxObject("mc.train~")
    mc_train_tilde.__doc__ = """
    mc.train~

    Args:
    inter-pulse-interval (number, optional)
    pulse-width (number, optional)
    phase (number, optional)

    Attributes:
    interval, phase, resetmode, width
    """

    mc_transpose_tilde = MaxObject("mc.transpose~")
    mc_transpose_tilde.__doc__ = """
    mc.transpose~

    Args:
    inlets (int, optional)
    outlets (int, optional)
    """

    mc_trapezoid_tilde = MaxObject("mc.trapezoid~")
    mc_trapezoid_tilde.__doc__ = """
    mc.trapezoid~

    Args:
    ramp-up (float, optional)
    ramp-down (float, optional)

    Attributes:
    hi, lo
    """

    mc_tri_tilde = MaxObject("mc.tri~")
    mc_tri_tilde.__doc__ = """
    mc.tri~

    Args:
    initial-frequency (number, optional)
    duty-cycle (float, optional)
    """

    mc_triangle_tilde = MaxObject("mc.triangle~")
    mc_triangle_tilde.__doc__ = """
    mc.triangle~

    Args:
    peak-value-phase-offset (float, optional)

    Attributes:
    hi, lo
    """

    mc_trunc_tilde = MaxObject("mc.trunc~")
    mc_trunc_tilde.__doc__ = """
    mc.trunc~
    """

    mc_twist_tilde = MaxObject("mc.twist~")
    mc_twist_tilde.__doc__ = """
    mc.twist~

    Attributes:
    curve, interval, shapemode, syncupdate
    """

    mc_unpack_tilde = MaxObject("mc.unpack~")
    mc_unpack_tilde.__doc__ = """
    mc.unpack~

    Args:
    size (int, required)
    """

    mc_updown_tilde = MaxObject("mc.updown~")
    mc_updown_tilde.__doc__ = """
    mc.updown~

    Attributes:
    down, level, up
    """

    mc_vectral_tilde = MaxObject("mc.vectral~")
    mc_vectral_tilde.__doc__ = """
    mc.vectral~

    Args:
    vector-size (int, optional)
    """

    mc_voiceallocator_tilde = MaxObject("mc.voiceallocator~")
    mc_voiceallocator_tilde.__doc__ = """
    mc.voiceallocator~

    Args:
    voice count (int, optional)

    Attributes:
    initialbusystate, name, steal, voices
    """

    mc_vst_tilde = MaxObject("mc.vst~")
    mc_vst_tilde.__doc__ = """
    mc.vst~

    Args:
    number-of-inputs/outputs (int, optional)
    VST-plugin-filename (symbol, optional)
    preset-effects-name (symbol, optional)

    Attributes:
    annotation_name, autosave, bypass, enablehscroll, enablevscroll, genericeditor,
    mcisolate, parameter_enable, parameter_mappable, prefer, valuemode
    """

    mc_wave_tilde = MaxObject("mc.wave~")
    mc_wave_tilde.__doc__ = """
    mc.wave~

    Args:
    buffer-name (symbol, required)
    start-point (number, optional)
    end-point (number, optional)
    number-of-output-channels (int, optional)

    Attributes:
    interp, interp_bias, interp_tension
    """

    mc_what_tilde = MaxObject("mc.what~")
    mc_what_tilde.__doc__ = """
    mc.what~

    Args:
    values (list, optional)

    Attributes:
    matches, syncupdate, triggermode
    """

    mc_where_tilde = MaxObject("mc.where~")
    mc_where_tilde.__doc__ = """
    mc.where~
    """

    mc_zerox_tilde = MaxObject("mc.zerox~")
    mc_zerox_tilde.__doc__ = """
    mc.zerox~

    Args:
    click-volume (float, optional)
    """

    mc_zigzag_tilde = MaxObject("mc.zigzag~")
    mc_zigzag_tilde.__doc__ = """
    mc.zigzag~

    Args:
    initial-value (int, float, optional)

    Attributes:
    loopmode, maxpoints, mode
    """

    mcs_2d_wave_tilde = MaxObject("mcs.2d.wave~")
    mcs_2d_wave_tilde.__doc__ = """
    mcs.2d.wave~

    Args:
    buffer-name (symbol, required)
    start and end-points (number, optional)
    number-of-output-channels (int, optional)
    rows (int, optional)
    """

    mcs_amxd_tilde = MaxObject("mcs.amxd~")
    mcs_amxd_tilde.__doc__ = """
    mcs.amxd~

    Args:
    devicename (symbol, required)

    Attributes:
    active, annotation_name, autosize, mcisolate, parameter_enable, patchername,
    showheader
    """

    mcs_fffb_tilde = MaxObject("mcs.fffb~")
    mcs_fffb_tilde.__doc__ = """
    mcs.fffb~

    Args:
    number-of-filters (int, required)
    1st-filter-frequency (float, optional)
    filter-frequency-ratios (float) (float, optional)
    Q (list, optional)
    harmonic-series-flag (H) (symbol, optional)
    """

    mcs_gate_tilde = MaxObject("mcs.gate~")
    mcs_gate_tilde.__doc__ = """
    mcs.gate~

    Args:
    number-of-outlets (int, optional)
    initial-open-outlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    mcs_gen_tilde = MaxObject("mcs.gen~")
    mcs_gen_tilde.__doc__ = """
    mcs.gen~

    Args:
    patcher-name (symbol, optional)

    Attributes:
    autoexport, cpu, cpumeasure, dumpoutlet, exportfolder, exportname, exportnotifier,
    exportscript, exportscriptargs, gen, nocache, poll, title
    """

    mcs_groove_tilde = MaxObject("mcs.groove~")
    mcs_groove_tilde.__doc__ = """
    mcs.groove~

    Args:
    buffer-name (symbol, required)
    number-of-outputs (int, optional)

    Attributes:
    basictuning, followglobaltempo, formant, formantcorrection, lock, loop, loopend,
    loopinterp, loopstart, mode, name, originallength, originaltempo, phase,
    pitchcorrection, pitchshift, pitchshiftcent, quality, slurtime, timestretch,
    transport
    """

    mcs_limi_tilde = MaxObject("mcs.limi~")
    mcs_limi_tilde.__doc__ = """
    mcs.limi~

    Args:
    channel_count (int, optional)
    buffer_size (int, optional)

    Attributes:
    bypass, dcblock, lookahead, mode, postamp, preamp, release, threshold
    """

    mcs_matrix_tilde = MaxObject("mcs.matrix~")
    mcs_matrix_tilde.__doc__ = """
    mcs.matrix~

    Args:
    inlets (int, required)
    outlets (int, required)
    default-connect-gain (float, optional)

    Attributes:
    numouts, ramp
    """

    mcs_play_tilde = MaxObject("mcs.play~")
    mcs_play_tilde.__doc__ = """
    mcs.play~

    Args:
    buffer-name (symbol, required)
    number-of-output-channels (int, optional)

    Attributes:
    interptime, loop, loopinterp
    """

    mcs_poly_tilde = MaxObject("mcs.poly~")
    mcs_poly_tilde.__doc__ = """
    mcs.poly~

    Args:
    patcher-name (symbol, required)
    number-of-instances (int, optional)
    local and flag (0 or 1) (symbol, optional)
    'up' and up-sampling-factor (symbol, optional)
    'down' and down-sampling factor (symbol, optional)
    'args' and list-of-argument-values (symbol, optional)

    Attributes:
    args, legacynotemode, midimode, mpemode, parallel, patchername, replicate,
    resampling, steal, target, voices, vs, zone
    """

    mcs_selector_tilde = MaxObject("mcs.selector~")
    mcs_selector_tilde.__doc__ = """
    mcs.selector~

    Args:
    number-of-inputs (int, optional)
    initially-open-inlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    mcs_sig_tilde = MaxObject("mcs.sig~")
    mcs_sig_tilde.__doc__ = """
    mcs.sig~

    Args:
    initial-output-value (number, optional)

    Attributes:
    chans
    """

    mcs_tapout_tilde = MaxObject("mcs.tapout~")
    mcs_tapout_tilde.__doc__ = """
    mcs.tapout~

    Args:
    initial-delay (number, optional)

    Attributes:
    unique
    """

    mcs_vst_tilde = MaxObject("mcs.vst~")
    mcs_vst_tilde.__doc__ = """
    mcs.vst~

    Args:
    number-of-inputs/outputs (int, optional)
    VST-plugin-filename (symbol, optional)
    preset-effects-name (symbol, optional)

    Attributes:
    annotation_name, autosave, bypass, enablehscroll, enablevscroll, genericeditor,
    mcisolate, parameter_enable, parameter_mappable, prefer, valuemode
    """

    mcs_wave_tilde = MaxObject("mcs.wave~")
    mcs_wave_tilde.__doc__ = """
    mcs.wave~

    Args:
    buffer-name (symbol, required)
    start-point (number, optional)
    end-point (number, optional)
    number-of-output-channels (int, optional)

    Attributes:
    interp, interp_bias, interp_tension
    """

    meter_tilde = MaxObject("meter~")
    meter_tilde.__doc__ = """
    meter~

    Attributes:
    bgcolor, bordercolor, coldcolor, dbperled, hotcolor, interval, monotone, nhotleds,
    ntepidleds, numleds, nwarmleds, offcolor, oncolor, orientation, overloadcolor,
    style, tepidcolor, warmcolor
    """

    minimum_tilde = MaxObject("minimum~")
    minimum_tilde.__doc__ = """
    minimum~

    Args:
    initial-comparison-value (number, optional)
    """

    minmax_tilde = MaxObject("minmax~")
    minmax_tilde.__doc__ = """
    minmax~
    """

    minus_tilde = MaxObject("minus~")
    minus_tilde.__doc__ = """
    minus~

    Args:
    initial-subtraction-value (number, optional)
    """

    modulo_tilde = MaxObject("modulo~")
    modulo_tilde.__doc__ = """
    modulo~

    Args:
    initial-divisor (number, optional)
    """

    mstosamps_tilde = MaxObject("mstosamps~")
    mstosamps_tilde.__doc__ = """
    mstosamps~
    """

    mtof_tilde = MaxObject("mtof~")
    mtof_tilde.__doc__ = """
    mtof~

    Attributes:
    base
    """

    mute_tilde = MaxObject("mute~")
    mute_tilde.__doc__ = """
    mute~
    """

    mxj_tilde = MaxObject("mxj~")
    mxj_tilde.__doc__ = """
    mxj~

    Args:
    Java-class (symbol, required)
    attributes (list, required)
    """

    noise_tilde = MaxObject("noise~")
    noise_tilde.__doc__ = """
    noise~

    Attributes:
    classic
    """

    normalize_tilde = MaxObject("normalize~")
    normalize_tilde.__doc__ = """
    normalize~

    Args:
    initial-maximum-output-amplitude (float, optional)
    """

    notequals_tilde = MaxObject("notequals~")
    notequals_tilde.__doc__ = """
    notequals~

    Args:
    initial-comparison-value (number, optional)

    Attributes:
    fuzzy
    """

    number_tilde = MaxObject("number~")
    number_tilde.__doc__ = """
    number~

    Attributes:
    bgcolor, bgcolor2, bordercolor, ft1, hbgcolor, htextcolor, interval, maximum,
    minimum, monitormode, numdecimalplaces, sigoutmode, style, textcolor
    """

    omx_4band_tilde = MaxObject("omx.4band~")
    omx_4band_tilde.__doc__ = """
    omx.4band~
    """

    omx_5band_tilde = MaxObject("omx.5band~")
    omx_5band_tilde.__doc__ = """
    omx.5band~
    """

    omx_comp_tilde = MaxObject("omx.comp~")
    omx_comp_tilde.__doc__ = """
    omx.comp~
    """

    omx_peaklim_tilde = MaxObject("omx.peaklim~")
    omx_peaklim_tilde.__doc__ = """
    omx.peaklim~
    """

    onepole_tilde = MaxObject("onepole~")
    onepole_tilde.__doc__ = """
    onepole~

    Args:
    center-frequency (float, optional)
    Hz/linear/radians (symbol, optional)
    """

    oscbank_tilde = MaxObject("oscbank~")
    oscbank_tilde.__doc__ = """
    oscbank~

    Args:
    number-of-oscillators (int, optional)
    frequency-smoothing-factor (samples) (int, optional)
    amplitude-smoothing-factor (samples) (int, optional)
    lookup-table-size (samples) (int, optional)
    """

    out = MaxObject("out")
    out.__doc__ = """
    out

    Attributes:
    attr_comment
    """

    out_tilde = MaxObject("out~")
    out_tilde.__doc__ = """
    out~

    Args:
    outlet-number (int, required)

    Attributes:
    attr_comment, chans
    """

    overdrive_tilde = MaxObject("overdrive~")
    overdrive_tilde.__doc__ = """
    overdrive~

    Args:
    drive-factor (int, required)
    drive-factor (float, optional)
    """

    pass_tilde = MaxObject("pass~")
    pass_tilde.__doc__ = """
    pass~
    """

    peakamp_tilde = MaxObject("peakamp~")
    peakamp_tilde.__doc__ = """
    peakamp~

    Args:
    ms-output-interval (int, optional)

    Attributes:
    interval, signed
    """

    peek_tilde = MaxObject("peek~")
    peek_tilde.__doc__ = """
    peek~

    Args:
    buffer-name (symbol, required)
    buffer-channel (int, optional)
    clipping-enable-flag (int, optional)
    """

    pfft_tilde = MaxObject("pfft~")
    pfft_tilde.__doc__ = """
    pfft~

    Args:
    subpatch-name (symbol, required)
    FFT-size (int, optional)
    overlap-factor (hop-size-denominator) (int, optional)
    start-onset (int, optional)
    full-spectrum-flag (0 or nonzero) (int, optional)
    'args' and list-of-argument-values (symbol, optional)
    """

    phasegroove_tilde = MaxObject("phasegroove~")
    phasegroove_tilde.__doc__ = """
    phasegroove~

    Attributes:
    conflict
    """

    phaseshift_tilde = MaxObject("phaseshift~")
    phaseshift_tilde.__doc__ = """
    phaseshift~

    Args:
    frequency (number, optional)
    q (number, optional)
    """

    phasewrap_tilde = MaxObject("phasewrap~")
    phasewrap_tilde.__doc__ = """
    phasewrap~
    """

    phasor_tilde = MaxObject("phasor~")
    phasor_tilde.__doc__ = """
    phasor~

    Args:
    initial-frequency (list, optional)

    Attributes:
    frequency, jitter, limit, lock, phaseoffset, syncupdate, transport
    """

    pink_tilde = MaxObject("pink~")
    pink_tilde.__doc__ = """
    pink~
    """

    pitchshift_tilde = MaxObject("pitchshift~")
    pitchshift_tilde.__doc__ = """
    pitchshift~

    Args:
    channels (int, optional)

    Attributes:
    constantlatency, enabled, pitchshift, pitchshiftcent, quality, reportlatency,
    usecents
    """

    play_tilde = MaxObject("play~")
    play_tilde.__doc__ = """
    play~

    Args:
    buffer-name (symbol, required)
    number-of-output-channels (int, optional)

    Attributes:
    interptime, loop, loopinterp
    """

    playlist_tilde = MaxObject("playlist~")
    playlist_tilde.__doc__ = """
    playlist~

    Attributes:
    accentcolor, allowreorder, basictuning, bgcolor, channelcount, chans, clipheight,
    color, elementcolor, expansion, followglobaltempo, formant, formantcorrection,
    loop, loopreport, mode, name, originallength, originaltempo, parameter_enable,
    parameter_mappable, pitchcorrection, pitchshift, pitchshiftcent, quality,
    reportprogress, selectioncolor, showname, slurtime, speed, style, textcolor,
    timestretch, waveformdisplay
    """

    plot_tilde = MaxObject("plot~")
    plot_tilde.__doc__ = """
    plot~

    Attributes:
    applyfont, audioframerate, audioframesize, bgcolor, domainlabel, fontname,
    fontsize, gridcolor, gridorigincolor, margins, numplots, numpoints, rangelabel,
    thinmode, thinthresh, thinto
    """

    plugin_tilde = MaxObject("plugin~")
    plugin_tilde.__doc__ = """
    plugin~

    Args:
    input-channels (list, optional)

    Attributes:
    chans
    """

    plugout_tilde = MaxObject("plugout~")
    plugout_tilde.__doc__ = """
    plugout~

    Args:
    output-channel-destination (int, optional)

    Attributes:
    chans
    """

    plugphasor_tilde = MaxObject("plugphasor~")
    plugphasor_tilde.__doc__ = """
    plugphasor~
    """

    plugreceive_tilde = MaxObject("plugreceive~")
    plugreceive_tilde.__doc__ = """
    plugreceive~

    Args:
    object-name (symbol, required)
    """

    plugsend_tilde = MaxObject("plugsend~")
    plugsend_tilde.__doc__ = """
    plugsend~

    Args:
    object-name (symbol, required)
    """

    plugsync_tilde = MaxObject("plugsync~")
    plugsync_tilde.__doc__ = """
    plugsync~
    """

    plus_tilde = MaxObject("plus~")
    plus_tilde.__doc__ = """
    plus~

    Args:
    initial-offset (number, optional)
    """

    plusequals_tilde = MaxObject("plusequals~")
    plusequals_tilde.__doc__ = """
    plusequals~

    Args:
    initial-sum (float, optional)
    """

    poke_tilde = MaxObject("poke~")
    poke_tilde.__doc__ = """
    poke~

    Args:
    buffer-object-name (symbol, required)
    channel-number (int, optional)
    """

    poltocar_tilde = MaxObject("poltocar~")
    poltocar_tilde.__doc__ = """
    poltocar~
    """

    poly_tilde = MaxObject("poly~")
    poly_tilde.__doc__ = """
    poly~

    Args:
    patcher-name (symbol, required)
    number-of-instances (int, optional)
    local and flag (0 or 1) (symbol, optional)
    'up' and up-sampling-factor (symbol, optional)
    'down' and down-sampling factor (symbol, optional)
    'args' and list-of-argument-values (symbol, optional)

    Attributes:
    args, legacynotemode, midimode, mpemode, parallel, patchername, replicate,
    resampling, steal, target, voices, vs, zone
    """

    polybuffer_tilde = MaxObject("polybuffer~")
    polybuffer_tilde.__doc__ = """
    polybuffer~

    Args:
    name (symbol, required)

    Attributes:
    embed, quiet
    """

    pong_tilde = MaxObject("pong~")
    pong_tilde.__doc__ = """
    pong~

    Args:
    folding-mode (int, optional)
    low-value (float, optional)
    high-value (float, optional)

    Attributes:
    mode, range
    """

    pow_tilde = MaxObject("pow~")
    pow_tilde.__doc__ = """
    pow~

    Args:
    base-value (number, optional)
    """

    ramp_tilde = MaxObject("ramp~")
    ramp_tilde.__doc__ = """
    ramp~

    Args:
    duration (float, optional)

    Attributes:
    curve, duration, end, interval, mode, reset, retrigger, start
    """

    rampsmooth_tilde = MaxObject("rampsmooth~")
    rampsmooth_tilde.__doc__ = """
    rampsmooth~

    Args:
    ramp-up-samples (int, optional)
    ramp-down-samples (int, optional)

    Attributes:
    rampdown, rampup
    """

    rand_tilde = MaxObject("rand~")
    rand_tilde.__doc__ = """
    rand~

    Args:
    initial-frequency (number, optional)
    """

    rate_tilde = MaxObject("rate~")
    rate_tilde.__doc__ = """
    rate~

    Args:
    multiplier (float, optional)
    sync-mode-flag (int, optional)

    Attributes:
    sync
    """

    rdiv_tilde = MaxObject("rdiv~")
    rdiv_tilde.__doc__ = """
    rdiv~

    Args:
    initial-divisor (number, optional)
    """

    receive_tilde = MaxObject("receive~")
    receive_tilde.__doc__ = """
    receive~

    Args:
    object-name (symbol, required)

    Attributes:
    chans, name
    """

    record_tilde = MaxObject("record~")
    record_tilde.__doc__ = """
    record~

    Args:
    buffer-name (symbol, required)
    input-channels (int, optional)

    Attributes:
    append, loop, loopend, loopstart, transport
    """

    rect_tilde = MaxObject("rect~")
    rect_tilde.__doc__ = """
    rect~

    Args:
    frequency (number, optional)
    pulse-width (number, optional)
    """

    reson_tilde = MaxObject("reson~")
    reson_tilde.__doc__ = """
    reson~

    Args:
    initial-gain (float, optional)
    center-frequency (float, optional)
    Q (float, optional)

    Attributes:
    cf, gain, q
    """

    retune_tilde = MaxObject("retune~")
    retune_tilde.__doc__ = """
    retune~

    Args:
    standard pitch (int, required)

    Attributes:
    correction_ambience_threshold, correction_amount, correction_bypass,
    correction_threshold, enablednotes, notebase, notelist, pitchdetection, quality,
    reportlatency, retune, use_16bit, windowsize
    """

    rewire_tilde = MaxObject("rewire~")
    rewire_tilde.__doc__ = """
    rewire~

    Args:
    device (symbol, optional)
    outputs (int, optional)
    """

    rminus_tilde = MaxObject("rminus~")
    rminus_tilde.__doc__ = """
    rminus~

    Args:
    initial-subtraction-value (number, optional)
    """

    round_tilde = MaxObject("round~")
    round_tilde.__doc__ = """
    round~

    Args:
    int or float (number, optional)

    Attributes:
    nearest
    """

    sah_tilde = MaxObject("sah~")
    sah_tilde.__doc__ = """
    sah~

    Args:
    initial-trigger-value (number, optional)

    Attributes:
    duration, thresh, triggermode
    """

    sampstoms_tilde = MaxObject("sampstoms~")
    sampstoms_tilde.__doc__ = """
    sampstoms~
    """

    sash_tilde = MaxObject("sash~")
    sash_tilde.__doc__ = """
    sash~

    Attributes:
    advancelevel, dir, maxsize, mode, samplelevel, size
    """

    saw_tilde = MaxObject("saw~")
    saw_tilde.__doc__ = """
    saw~

    Args:
    initial-frequency (number, optional)
    """

    scale_tilde = MaxObject("scale~")
    scale_tilde.__doc__ = """
    scale~

    Args:
    minimum-in-value (number, required)
    maximum-in-value (number, required)
    minimum-out-value (number, required)
    maximum-out-value (number, required)
    scaling-curve (float, optional)

    Attributes:
    classic
    """

    scope_tilde = MaxObject("scope~")
    scope_tilde.__doc__ = """
    scope~

    Attributes:
    automatic, bgcolor, bordercolor, bufsize, calccount, delay, displaychan,
    displaysinglechannel, drawstyle, fgcolor, gridcolor, inactivealpha, range,
    rounded, style, trigger, triglevel
    """

    selector_tilde = MaxObject("selector~")
    selector_tilde.__doc__ = """
    selector~

    Args:
    number-of-inputs (int, optional)
    initially-open-inlet (int, optional)

    Attributes:
    ramptime, stepmode
    """

    send_tilde = MaxObject("send~")
    send_tilde.__doc__ = """
    send~

    Args:
    object-name (symbol, required)

    Attributes:
    name
    """

    seq_tilde = MaxObject("seq~")
    seq_tilde.__doc__ = """
    seq~
    """

    sfinfo_tilde = MaxObject("sfinfo~")
    sfinfo_tilde.__doc__ = """
    sfinfo~

    Args:
    filename (symbol, optional)
    """

    sflist_tilde = MaxObject("sflist~")
    sflist_tilde.__doc__ = """
    sflist~

    Args:
    object-name (symbol, required)
    buffer-size (int, optional)

    Attributes:
    name
    """

    sfplay_tilde = MaxObject("sfplay~")
    sfplay_tilde.__doc__ = """
    sfplay~

    Args:
    sflist-object-name (symbol, optional)
    number-of-output-channels (int, optional)
    buffer-size (int, optional)
    position-outlet-flag (int, optional)
    object-reference-name (symbol, optional)

    Attributes:
    audiofile, basictuning, chans, followglobaltempo, formant, formantcorrection,
    loop, mode, name, originallength, originaltempo, pitchcorrection, pitchshift,
    pitchshiftcent, quality, slurtime, speed, timestretch
    """

    sfrecord_tilde = MaxObject("sfrecord~")
    sfrecord_tilde.__doc__ = """
    sfrecord~

    Args:
    number-of-input-channels (int, optional)
    buffer-size (int, optional)

    Attributes:
    bitdepth, dither, nchans, quantization, resample, sortloop
    """

    shape_tilde = MaxObject("shape~")
    shape_tilde.__doc__ = """
    shape~

    Attributes:
    constant, curvemode
    """

    sig_tilde = MaxObject("sig~")
    sig_tilde.__doc__ = """
    sig~

    Args:
    initial-output-value (number, optional)
    """

    sinh_tilde = MaxObject("sinh~")
    sinh_tilde.__doc__ = """
    sinh~
    """

    sinx_tilde = MaxObject("sinx~")
    sinx_tilde.__doc__ = """
    sinx~
    """

    slide_tilde = MaxObject("slide~")
    slide_tilde.__doc__ = """
    slide~

    Args:
    slide-up (float, optional)
    slide-down (float, optional)

    Attributes:
    slidedown, slideup
    """

    snapshot_tilde = MaxObject("snapshot~")
    snapshot_tilde.__doc__ = """
    snapshot~

    Args:
    reporting-interval (list, optional)

    Attributes:
    active, interval
    """

    snowfall_tilde = MaxObject("snowfall~")
    snowfall_tilde.__doc__ = """
    snowfall~

    Args:
    dimenions (int, optional)

    Attributes:
    boundarymode, dimensions, direction, directiondev, endmode, endvalue, energyramp,
    initial, initialdev, interval, intervaldev, max, min, scalemax, scalemin, squish,
    wanderprob
    """

    spectroscope_tilde = MaxObject("spectroscope~")
    spectroscope_tilde.__doc__ = """
    spectroscope~

    Attributes:
    bgcolor, border, bordercolor, curvecolor, displaychan, domain, fgcolor, interval,
    logamp, logfreq, markercolor, monochrome, orientation, phasespect, range, rounded,
    scroll, sono, sonohicolor, sonolocolor, sonomedcolor, sonomedhicolor,
    sonomedlocolor, sonomonobgcolor, sonomonofgcolor, style
    """

    spike_tilde = MaxObject("spike~")
    spike_tilde.__doc__ = """
    spike~

    Args:
    refractory-period (int, float, optional)
    """

    sqrt_tilde = MaxObject("sqrt~")
    sqrt_tilde.__doc__ = """
    sqrt~
    """

    stash_tilde = MaxObject("stash~")
    stash_tilde.__doc__ = """
    stash~

    Args:
    sample-thresh (float, optional)
    advance-thresh (float, optional)

    Attributes:
    advancelevel, advancetriggermode, dir, duration, interp, maxsize, mode,
    samplelevel, sampletriggermode, size, writemode
    """

    stretch_tilde = MaxObject("stretch~")
    stretch_tilde.__doc__ = """
    stretch~

    Args:
    buffer-name (symbol, required)

    Attributes:
    basictuning, followglobaltempo, formant, formantcorrection, mode, originallength,
    originaltempo, pitchcorrection, pitchshift, pitchshiftcent, progress_enable,
    quality, readagain, slurtime, stretch
    """

    stutter_tilde = MaxObject("stutter~")
    stutter_tilde.__doc__ = """
    stutter~

    Args:
    max-buffer-length (int, required)
    initial-buffer-size (int, required)
    trigger-polarity (int, required)
    number-of-copied-samples (int, required)
    number-of-outputs (int, optional)
    """

    subdiv_tilde = MaxObject("subdiv~")
    subdiv_tilde.__doc__ = """
    subdiv~

    Args:
    subdivisions (int, required)

    Attributes:
    div, lockprob, pattern, prob, silentmode, syncupdate
    """

    svf_tilde = MaxObject("svf~")
    svf_tilde.__doc__ = """
    svf~

    Args:
    center-frequency (float, optional)
    resonance (float, optional)
    Hz (symbol, optional)
    linear (symbol, optional)
    radians (symbol, optional)
    """

    swing_tilde = MaxObject("swing~")
    swing_tilde.__doc__ = """
    swing~

    Args:
    swing (float, optional)

    Attributes:
    swing, syncupdate
    """

    sync_tilde = MaxObject("sync~")
    sync_tilde.__doc__ = """
    sync~

    Attributes:
    rtport
    """

    table_tilde = MaxObject("table~")
    table_tilde.__doc__ = """
    table~

    Attributes:
    embed, extend, inmap, inputmode, interp, name, outscale, parameter_enable,
    parameter_mappable, range, signed, size, triggermode
    """

    tanh_tilde = MaxObject("tanh~")
    tanh_tilde.__doc__ = """
    tanh~
    """

    tanx_tilde = MaxObject("tanx~")
    tanx_tilde.__doc__ = """
    tanx~
    """

    tapin_tilde = MaxObject("tapin~")
    tapin_tilde.__doc__ = """
    tapin~

    Args:
    maximum-delay (number, optional)
    """

    tapout_tilde = MaxObject("tapout~")
    tapout_tilde.__doc__ = """
    tapout~

    Args:
    initial-delay (number, optional)

    Attributes:
    unique
    """

    techno_tilde = MaxObject("techno~")
    techno_tilde.__doc__ = """
    techno~
    """

    teeth_tilde = MaxObject("teeth~")
    teeth_tilde.__doc__ = """
    teeth~

    Args:
    feedforward-delay (float, optional)
    feedback-delay (float, optional)
    gain (float, optional)
    feedforward-gain (float, optional)
    feedback-gain (float, optional)
    """

    thispoly_tilde = MaxObject("thispoly~")
    thispoly_tilde.__doc__ = """
    thispoly~
    """

    thresh_tilde = MaxObject("thresh~")
    thresh_tilde.__doc__ = """
    thresh~

    Args:
    low/reset-threshold (float, required)
    high/set-threshold (float, required)
    """

    times_tilde = MaxObject("times~")
    times_tilde.__doc__ = """
    times~

    Args:
    initial-multiplier (number, optional)
    """

    train_tilde = MaxObject("train~")
    train_tilde.__doc__ = """
    train~

    Args:
    inter-pulse-interval (number, optional)
    pulse-width (number, optional)
    phase (number, optional)

    Attributes:
    interval, phase, resetmode, width
    """

    trapezoid_tilde = MaxObject("trapezoid~")
    trapezoid_tilde.__doc__ = """
    trapezoid~

    Args:
    ramp-up (float, optional)
    ramp-down (float, optional)

    Attributes:
    hi, lo
    """

    tri_tilde = MaxObject("tri~")
    tri_tilde.__doc__ = """
    tri~

    Args:
    initial-frequency (number, optional)
    duty-cycle (float, optional)
    """

    triangle_tilde = MaxObject("triangle~")
    triangle_tilde.__doc__ = """
    triangle~

    Args:
    peak-value-phase-offset (float, optional)

    Attributes:
    hi, lo
    """

    trunc_tilde = MaxObject("trunc~")
    trunc_tilde.__doc__ = """
    trunc~
    """

    twist_tilde = MaxObject("twist~")
    twist_tilde.__doc__ = """
    twist~

    Attributes:
    curve, interval, shapemode, syncupdate
    """

    typeroute_tilde = MaxObject("typeroute~")
    typeroute_tilde.__doc__ = """
    typeroute~
    """

    updown_tilde = MaxObject("updown~")
    updown_tilde.__doc__ = """
    updown~

    Attributes:
    down, level, up
    """

    vectral_tilde = MaxObject("vectral~")
    vectral_tilde.__doc__ = """
    vectral~

    Args:
    vector-size (int, optional)
    """

    vst_tilde = MaxObject("vst~")
    vst_tilde.__doc__ = """
    vst~

    Args:
    number-of-inputs/outputs (int, optional)
    VST-plugin-filename (symbol, optional)
    preset-effects-name (symbol, optional)

    Attributes:
    annotation_name, autosave, bypass, enablehscroll, enablevscroll, genericeditor,
    mcisolate, parameter_enable, parameter_mappable, prefer, valuemode
    """

    wave_tilde = MaxObject("wave~")
    wave_tilde.__doc__ = """
    wave~

    Args:
    buffer-name (symbol, required)
    start-point (number, optional)
    end-point (number, optional)
    number-of-output-channels (int, optional)

    Attributes:
    interp, interp_bias, interp_tension
    """

    waveform_tilde = MaxObject("waveform~")
    waveform_tilde.__doc__ = """
    waveform~

    Attributes:
    allowdrag, attr_bpm, beats, bgcolor, bordercolor, buffername, chanoffset,
    clipdraw, grid, gridcolor, invert, labelbgcolor, labels, labeltextcolor,
    linecolor, norulerclick, offset, outmode, quiet, selectalpha, selectioncolor,
    setmode, setunit, snapto, style, ticks, vlabels, voffset, vticks, vzoom,
    waveformcolor, zoom_orientation
    """

    what_tilde = MaxObject("what~")
    what_tilde.__doc__ = """
    what~

    Args:
    values (list, optional)

    Attributes:
    matches, syncupdate, triggermode
    """

    where_tilde = MaxObject("where~")
    where_tilde.__doc__ = """
    where~
    """

    windowed_fft_tilde = MaxObject("windowed-fft~")
    windowed_fft_tilde.__doc__ = """
    windowed-fft~

    Args:
    number-of-FFT-samples (int, required)
    """

    zerox_tilde = MaxObject("zerox~")
    zerox_tilde.__doc__ = """
    zerox~

    Args:
    click-volume (float, optional)
    """

    zigzag_tilde = MaxObject("zigzag~")
    zigzag_tilde.__doc__ = """
    zigzag~

    Args:
    initial-value (int, float, optional)

    Attributes:
    loopmode, maxpoints, mode
    """

    zplane_tilde = MaxObject("zplane~")
    zplane_tilde.__doc__ = """
    zplane~

    Attributes:
    axiscolor, bgcolor, bordercolor, circlebordercolor, fgcolor, gridlinecolor,
    hlcolor, order, pconstrain, polezerocolor, rounded, style
    """


del _output
