image cg CRT = "assets/cgs/cg_CRT.png"
image cg SCENE1 = "assets/cgs/cg_SCENE1.png"
image cg SCENE2 = "assets/cgs/cg_SCENE2.png"
image cg LAYOUT = "assets/cgs/cg_LAYOUT.png"


init python:

    renpy.register_shader(
        "vn.wave",
        variables="""
            uniform float u_wave_amount;
            uniform float u_wave_depth;
            uniform float u_wave_freq;
            uniform float u_wave_speed;
            uniform float u_wave_margin;
            uniform float u_time;
        """,
        fragment_300="""
            float lv_a = clamp(u_wave_amount, 0.0, 1.0);
            vec2 lv_uv = (v_tex_coord - vec2(0.5)) * u_wave_margin + vec2(0.5);
            float lv_ph = u_time * u_wave_speed;

            lv_uv.x += sin(lv_uv.y * u_wave_freq * 6.2832 + lv_ph) * u_wave_depth * 0.010 * lv_a;
            lv_uv.y += cos(lv_uv.x * u_wave_freq * 4.3982 - lv_ph * 0.8) * u_wave_depth * 0.008 * lv_a;

            gl_FragColor = texture2D(tex0, clamp(lv_uv, 0.002, 0.998));
        """)

    


    renpy.register_shader(
        "vn.static", #@sofive: new and better imp of tv static hopefully, credit/inspiration: https://github.com/kws/tv-static
        variables="""
            uniform float u_static_amount;
            uniform float u_static_lines;
            uniform float u_time;
            uniform vec2 u_model_size;
        """,
        fragment_300="""
            float lv_t = mod(u_time, 100.0) + 1.0;
            float lv_aspect = u_model_size.x / u_model_size.y;
            vec2 lv_grid = vec2(u_static_lines * lv_aspect, u_static_lines);
            vec2 lv_uv = (floor(v_tex_coord * lv_grid) + 0.5) / lv_grid;

            float lv_lum = fract(sin(dot(lv_uv * lv_t, vec2(12.9898, 78.233))) * 43758.5453);
            lv_lum += fract(sin(dot(vec2(lv_t, lv_uv.y), vec2(12.9898, 78.233))) * 43758.5453) * 0.1;

            lv_lum += sin(lv_uv.y * 800.0 + lv_t * 50.0) * 0.05;

            float lv_a = clamp(u_static_amount, 0.0, 1.0);
            gl_FragColor = vec4(vec3(clamp(lv_lum, 0.0, 1.0)) * lv_a, lv_a);
        """)


transform fx_wave(amount=0.6, depth=1.0, freq=1.15, speed=0.85, margin=0.94):
    mesh True
    shader "vn.wave"
    u_wave_amount amount
    u_wave_depth depth
    u_wave_freq freq
    u_wave_speed speed
    u_wave_margin margin
    pause 0
    repeat

transform fx_wave_rise(start=0.0, target=0.85, dur=6.0, depth=1.0, freq=1.15, speed=0.85, margin=0.94):
    mesh True
    shader "vn.wave"
    u_wave_amount start
    u_wave_depth depth
    u_wave_freq freq
    u_wave_speed speed
    u_wave_margin margin
    linear dur u_wave_amount target
    block:
        pause 0
        repeat

transform fx_wave_hit(peak=1.0, base=0.3, hold=0.06, recover=0.5, depth=1.0, margin=0.94):
    mesh True
    shader "vn.wave"
    u_wave_depth depth
    u_wave_freq 1.15
    u_wave_speed 0.85
    u_wave_margin margin
    u_wave_amount base
    linear 0.04 u_wave_amount peak
    pause hold
    linear recover u_wave_amount base
    block:
        pause 0
        repeat

transform fx_blur(amount=6.0, dur=0.4):
    blur 0
    linear dur blur amount

transform fx_sway(amount=5, period=5.0):
    block:
        linear period xoffset amount yoffset -amount
        linear period xoffset -amount yoffset amount
        repeat


image fx_white = Solid("#ffffff")

transform fx_flash_double(peak=1.0):
    alpha 0.0
    linear 0.02 alpha peak
    linear 0.10 alpha 0.0
    pause 0.06
    linear 0.02 alpha peak
    linear 0.30 alpha 0.0

transform fx_flash_burn(peak=1.0, hold=0.10, dur=0.45):
    alpha 0.0
    linear 0.03 alpha peak
    pause hold
    linear dur alpha 0.0

screen fxflash_screen(hold=0.06, dur=0.36, peak=1.0, hits=1):
    zorder 100
    if hits >= 2:
        add Solid("#ffffff", xysize=(config.screen_width, config.screen_height)) at fx_flash_double(peak)
    else:
        add Solid("#ffffff", xysize=(config.screen_width, config.screen_height)) at fx_flash_burn(peak, hold, dur)

init python:

    def flash(hold=0.06, dur=0.36, peak=1.0, hits=1):
        renpy.hide_screen("fxflash")
        renpy.show_screen("fxflash_screen", _tag="fxflash", hold=hold, dur=dur, peak=peak, hits=hits)


image fx_noise = Solid("#000000")

transform fx_static(amount=1.0, lines=120.0):
    mesh True
    shader "vn.static"
    u_static_amount amount
    u_static_lines lines
    #u_static_roll roll
    pause 0
    repeat

transform fx_static_burst(hold=0.18, lines=120.0):
    mesh True
    shader "vn.static"
    u_static_lines lines
    #u_static_roll 0.20
    u_static_amount 0.0
    linear 0.03 u_static_amount 1.0
    pause hold
    linear 0.06 u_static_amount 0.0

transform fx_static_fade(amount=1.0, dur=1.4, lines=120.0):
    mesh True
    shader "vn.static"
    u_static_lines lines
    #u_static_roll 0.20
    u_static_amount amount
    linear dur u_static_amount 0.0

transform fx_static_in(dur=0.9, lines=120.0):
    mesh True
    shader "vn.static"
    u_static_lines lines
    #u_static_roll roll
    u_static_amount 0.0
    linear dur u_static_amount 1.0
    block:
        pause 0
        repeat
