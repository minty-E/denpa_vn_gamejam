default textbox_style = "irl"

define n = Character(None, kind=nvl_narrator)
define no = Character(None)
define cla = Character("Classmate A", kind=nvl)
define clb = Character("Classmate B", kind=nvl)
define son = Character("Sofia", kind=nvl)
define shn = Character("Sharlene", kind=nvl)

define so = Character("Sofia")
define sh = Character("Sharlene")
define shoko = Character("shokoichan", what_style="mmo_say_dialogue")
define sofiam = Character("sofiamagandz30", what_style="mmo_say_dialogue")
# added speakers
define ssh = Character("Sofia & Sharlene", kind=nvl)
define som = Character("Sofia's Mother")
define shf = Character("Sharlene's Father")
define ca = Character("Classmate A")
define cb = Character("Classmate B")
define scma = Character("Schoolmate A")
define scmb = Character("Schoolmate B")
define mmo_console = Character("Console", what_style="mmo_say_dialogue")
define spiderlily = Character("Spiderlily", what_style="mmo_say_dialogue")


label start:

    call chapter_1_1   
    call chapter_1_2
    call chapter_1_3
    call chapter_1_4
    call chapter_1_5

    # new scenes
    call chapter_2_1
    call chapter_3_1
    call chapter_3_2
    call chapter_3_3
    call chapter_4_1
    call chapter_4_2
    call chapter_5_1
    call chapter_6_1
    call chapter_6_2
    call chapter_6_3
    call chapter_7_1

  

    return
