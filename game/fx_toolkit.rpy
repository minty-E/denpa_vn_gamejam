image cg CRT = "assets/cgs/cg_CRT.png"
image cg SCENE1 = "assets/cgs/cg_SCENE1.png"
image cg SCENE2 = "assets/cgs/cg_SCENE2.png"
image cg LAYOUT = "assets/cgs/cg_LAYOUT.png"


init -10 python:

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

            /* one wave across the screen, drifting */
            lv_uv.x += sin(lv_uv.y * u_wave_freq * 6.2832 + lv_ph) * u_wave_depth * 0.010 * lv_a;
            lv_uv.y += cos(lv_uv.x * u_wave_freq * 4.3982 - lv_ph * 0.8) * u_wave_depth * 0.008 * lv_a;

            gl_FragColor = texture2D(tex0, clamp(lv_uv, 0.002, 0.998));
        """)

    renpy.register_shader(
        "vn.static",
        variables="""
            uniform float u_static_amount;
            uniform float u_static_grain;
            uniform float u_static_roll;
            uniform float u_time;
            uniform vec2 u_model_size;
        """,
        fragment_300="""
            vec2 lv_px = floor(v_tex_coord * u_model_size.xy / 2.0);
            float lv_n = fract(sin(dot(lv_px, vec2(12.9898, 78.233)) + floor(u_time * 24.0) * 0.731) * 43758.5453);
            float lv_n2 = fract(lv_n * 7.0 + u_time);
            float lv_lum = mix(lv_n, lv_n2, 0.35) * u_static_grain;

            /* vertical hold: a rolling dark bar with a bright edge under it */
            float lv_roll = fract(v_tex_coord.y + u_time * u_static_roll);
            float lv_bar = smoothstep(0.0, 0.05, lv_roll) * (1.0 - smoothstep(0.05, 0.16, lv_roll));
            lv_lum *= 1.0 - 0.55 * lv_bar;
            lv_lum += 0.20 * smoothstep(0.97, 1.0, lv_roll);

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
        """
        Fire a full-screen camera flash over the scene, the say/NVL box and the
        quick menu. The screen is torn down first so a second call restarts the
        animation instead of reusing the finished one.

            $ flash()
            $ flash(hits=2)
            $ flash(hold=0.25, peak=1.0, dur=0.6)
        """
        renpy.hide_screen("fxflash")
        renpy.show_screen("fxflash_screen", _tag="fxflash", hold=hold, dur=dur, peak=peak, hits=hits)


image fx_noise = Solid("#000000")

transform fx_static(amount=1.0, grain=1.0, roll=0.22):
    mesh True
    shader "vn.static"
    u_static_amount amount
    u_static_grain grain
    u_static_roll roll
    pause 0
    repeat

transform fx_static_burst(hold=0.18):
    mesh True
    shader "vn.static"
    u_static_grain 1.0
    u_static_roll 0.22
    u_static_amount 0.0
    linear 0.03 u_static_amount 1.0
    pause hold
    linear 0.06 u_static_amount 0.0

transform fx_static_fade(amount=1.0, dur=1.4):
    mesh True
    shader "vn.static"
    u_static_grain 1.0
    u_static_roll 0.22
    u_static_amount amount
    linear dur u_static_amount 0.0

transform fx_static_in(dur=0.9, grain=1.0, roll=0.22):
    mesh True
    shader "vn.static"
    u_static_grain grain
    u_static_roll roll
    u_static_amount 0.0
    linear dur u_static_amount 1.0
    block:
        pause 0
        repeat
