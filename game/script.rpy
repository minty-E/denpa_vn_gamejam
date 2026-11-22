default textbox_style = "irl"
default game_time = "day"


init python:
    renpy.add_layer("mmo", above="master")

default md = "{font=assets/fonts/ARIALN.ttf}—{/font}"
default kw = "{font=assets/fonts/ARIALN.ttf}~{/font}"

default br1 = '[{space=3}'
default br2 = '{space=3}]'


define config.default_textshader = "typewriter"

define n = Character(None, kind=nvl_narrator)
define no = Character(None)
define cla = Character("Classmate A", kind=nvl, what_prefix = '"', what_suffix = '"')
define clb = Character("Classmate B", kind=nvl, what_prefix = '"', what_suffix = '"')
define son = Character("Sofia", kind=nvl, what_prefix = '"', what_suffix = '"')
define shn = Character("Sharlene", kind=nvl, what_prefix = '"', what_suffix = '"')
define shq = Character("{i}{b}Sharlene?{/b}{/i}", kind=adv)
define ssh = Character("Sofia & Sharlene", kind=nvl, what_prefix = '"', what_suffix = '"')

define so = Character("Sofia", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define sh = Character("Sharlene", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define shoko = Character("shokoichan", what_style="mmo_say_dialogue", what_prefix = '<', what_suffix = '>')
define sofiam = Character("sofiamagandz30", what_style="mmo_say_dialogue", what_prefix = '<', what_suffix = '>')
# added speakers
define som = Character("Sofia's Mother", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define shf = Character("Sharlene's Father", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define ca = Character("Classmate A", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define cb = Character("Classmate B", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define scma = Character("Schoolmate A", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define scmb = Character("Schoolmate B", who_prefix = "[br1]", who_suffix = "[br2]", what_prefix = '"', what_suffix = '"')
define mmo_console = Character("Console", what_style="mmo_say_dialogue")
define spiderlily = Character("Spiderlily", what_style="mmo_say_dialogue")


label start:

    call chapter_1_1 from _call_chapter_1_1   
    call chapter_1_2 from _call_chapter_1_2
    call chapter_1_3 from _call_chapter_1_3
    call chapter_1_4 from _call_chapter_1_4
    call chapter_1_5 from _call_chapter_1_5
    call chapter_1_6 from _call_chapter_1_6

    # new scenes
    call chapter_2_1 from _call_chapter_2_1
    call chapter_3_1 from _call_chapter_3_1
    call chapter_3_2 from _call_chapter_3_2
    call chapter_3_3 from _call_chapter_3_3
    call chapter_4_1 from _call_chapter_4_1
    call chapter_4_2 from _call_chapter_4_2
    call chapter_5_1 from _call_chapter_5_1
    call chapter_6_1 from _call_chapter_6_1
    call chapter_6_2 from _call_chapter_6_2
    call chapter_6_3 from _call_chapter_6_3
    call chapter_7_1 from _call_chapter_7_1

  

    return
