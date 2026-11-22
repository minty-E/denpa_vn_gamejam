label chapter_1_2:
    hide screen nvl
    with dissolve

    show sharlene casual smug:
        xoffset -60
    with easeinright
    show sofia a casual silook:
        xoffset -5
    with easeinright

    $renpy.transition(dissolve, layer="screen", always=True)
    sh "So, first honors, huh? You really know how to persevere-{w=.25}{nw}"
    show sofia b casual frown
    with vpunch
    so "Don't even start with me, Shokoy."

    no "She tilted her head in that so-awful cartoony manner that I always hated. She then put a hand on her chin. It's like real life is a joke to this seawater creature."

    show sharlene b casual b_awkward:
        xoffset 20
    with easeinleft
    sh "Don't think this is the end of me, Sofia-sama!"

    show sofia b casual neutral:
        xoffset 10
    with easeinleft

    sh "They always say the underdogs win when you expect them to the least. I've got a steadfast heart and all the dokidoki in the world to carry me, so I'm gonna blast through third, and waaay into first."

    show sharlene b casual b_smile
    with dissolve

    sh "You're noooooot gonna be ready for it."

    show sofia b casual frown
    with Dissolve(0.15)

    so "Do you think I care if you get first honors? I don't think even the rest of the student body cares."

    sh "I guess, but I wanna prove you guys' theory about me having alien maggots in my brain wrong."

    sh "Tried to check, BTW. I looked at my ear in the mirror 'n there was nothing."

    show sharlene a1 casual proud:
        xoffset -30
    with easeinleft

    sh "‘Coz if there were, there'd be white stuff wriggling out."

    return