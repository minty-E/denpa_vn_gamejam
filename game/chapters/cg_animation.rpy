image black_screen = Solid("#000000")

image cg imagination2 = Movie(play="assets/cgs/cg2imagination.webm", start_image=Solid("#1b0707"), loop=True)
image cg imagination3 = Movie(play="assets/cgs/cg3imagination.webm", start_image=Solid("#1b0707"), loop=True)



style cg_cap_window is default:
    background Solid("#000000")
    padding (20, 12)

style cg_cap_text is default:
    font "assets/fonts/MS Gothic.ttf"
    size 28
    color "#ffffff"
    kerning 0.5
    line_spacing 4

define CG_CAPTION_DX = 0
define CG_CAPTION_DY = 0

define CG2_LINES = [
    ("The only one",                            120,  60),
    ("it didn't eat was me,",                   230, 150),
    ("'cus I could breathe in the water",       160, 240),
    ("much like he can,",                       120, 330),
    ("so he recognized that I was a friend,",   130, 420),
    ("one of his species.",                     200, 510),
]

# @sofive: doesnt work from here
define CG2_LINES_HAND = [
    ("I smiled",                                520, 140),
    ("and shook the siokoy's hand,",            380, 610),
]

define CG2_LINES_BODY = [
    ("while Sofia's disembodied body floated",   170, 150),
    ("around spewing blood from the headless neck.", 120, 600),
]


init python:

    def cg_caption(i, txt, x, y, cps=22):
        box = Window(
            Text(txt, style="cg_cap_text", slow_cps=cps, xmaximum=640),
            style="cg_cap_window",
            xpos=x + CG_CAPTION_DX,
            ypos=y + CG_CAPTION_DY,
            xanchor=0,
            yanchor=0,
        )

        renpy.show("cgcap%d" % i, what=box)

    def cg_caption_clear(n=16):
        for i in range(n):
            renpy.hide("cgcap%d" % i)

label blink(dur=0.13):

    scene black_screen
    $ renpy.pause(dur, hard=True)

    return

label cg_captions(lines, cps=22, gap=0.7, clear=True):
    $ renpy.config.skipping = None

    if clear:
        $ cg_caption_clear()

    $ cg_i = 0

    while cg_i < len(lines):
        $ cg_caption(cg_i, lines[cg_i][0], lines[cg_i][1], lines[cg_i][2], cps)
        $ cg_i += 1

        $ cg_delay = gap + len(lines[cg_i - 1][0]) * 0.035
        $ renpy.pause(cg_delay)

    return

label flicker_into(img, blinks=1, dur=0.08):

    $ renpy.config.skipping = None

    $ renpy.scene()
    $ renpy.show(img)
    $ renpy.pause(dur * 2.0, hard=True)

    while blinks > 0:
        $ renpy.show("black_screen", zorder=10)
        $ renpy.pause(dur, hard=True)
        $ renpy.hide("black_screen")
        $ renpy.pause(dur * 2.0, hard=True)
        $ blinks -= 1

    return



label imagination_cg:
    $ renpy.config.skipping = None #@sofive: failsafe
    $ quick_menu = False

    nvl clear
    window hide

    scene
    show cg imagination2
    with Fade(0.4, 0.0, 0.6, color="#000000")

    pause 0.8

    call cg_captions(CG2_LINES)
    call cg_captions(CG2_LINES_HAND)
    call cg_captions(CG2_LINES_BODY)

    scene black_screen
    $ renpy.pause(0.15, hard=True)
    nvl clear

    n "In my little vision, I declared the siokoy my new best friend, and that he was now my new Pomorimo-friend."

    nvl clear

    call flicker_into("cg imagination3")

    pause 2.5

    scene bg BATHROOM
    with Dissolve(0.4)
    $ quick_menu = True

    return
