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


label start:

    call chapter_1_1   
    call chapter_1_2
    call chapter_1_3
    call chapter_1_4
    call chapter_1_5


   

  

    return
