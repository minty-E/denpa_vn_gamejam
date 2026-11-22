label chapter_1_5:
    nvl clear
    show sofia a casual tlsmile2 at loc(750)
    show sharlene casual b_smile at loc(600)
    with easeinright

    n "My parents watch us talk and assume that we’re having a friendly time.{w}"
    show dad smile at loc(-60)
    show mom smile at loc(-160)
    with Dissolve(2)
    extend " They start to approach me, and I feel relief. I turn my head back to Sharlene and I swear to god that she’s laughing at me. Her ugly crooked smile is plastered again on her face."
    show sofia a casual fake
    with Dissolve(0.25)
    extend " I wanted to slap her until she’d stop making that face."
    show sofia a casual silook
    with dissolve
    extend " I surveyed the area again. There’s those brute girls from the other section, one of them kissing up to that boy from the grade above us. The way his head is shaved is so lopsided. I saw the little dandruff flakes in his hair. I counted them. There’s about one, two, then five, maybe seven of these little imps in the area. I don’t care. 
    {w}"
    extend " I checked again to see if they were staring at me.{w=.5} I stomp my foot 3 times to assess if they are. If I correctly stomp it, then they aren’t."
    show sofia a casual silook with vpunch
    extend "{w=1} One."
    show sofia a casual silook with vpunch
    extend " {w=1}Two."
    show sofia a casual silook with vpunch
    extend " {w=1}Three."
    show sharlene a1 casual neutral
    hide dad
    hide mom
    with Dissolve(1)
    extend " {w=1.5}They aren’t. It’s a good thing they aren’t, because I felt Sharlene’s disgusting stare boring into me, and I wanted it to stop badly."
    show sofia b casual smile at loc(750)
    show sharlene a2 casual bracing
    n "I raise my hand again. She shields her head preemptively, and it feels like we’re playing out a pre-programmed sequence."

    nvl clear

    n "I smack her head and count every smack, because 6 smacks means that she’ll stop. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "One.{w} "
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Two. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Three. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend  "Four. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Five. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Six. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Seven. {w}"
    extend "I went over 6. I went over 6. I have to do it again, so I pause briefly, then I hit again.{w}"
    show sofia b casual neutral
    with Dissolve(2)
    with Pause(3)
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "One. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Two. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Three. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "Four. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    extend "I stopped.{w}"
    show sofia b casual mad with Dissolve(2)
    extend " I hesitated because I saw the red swell up in her face again, and I saw her staring at me listlessly like some sort of dead fish. I heard people clamoring around me, but I needed to get it correct."
    show sofia a casual shadow with Dissolve(0.5)
    with Pause(1)
    show sofia b casual rage with Dissolve(2)
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.10
    extend "One. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.20
    extend "Two. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.30
    extend "Three. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.40
    extend "Four. {w=3}"
    extend "I stop briefly,{w=.5} but continue.{w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.50
    extend "Five. {w}"
    show sharlene with vpunch
    show sharlene a2 casual sad with hpunch
    show image Solid("#ff0000"):
        alpha 0.60
    extend "Six. {w}"
    scene bg RECOG HALL GARDEN
    show image Solid("#ff0000"):
        alpha 0.05
    show sofia b casual rage
    with Dissolve(3)
    extend "Then my hand freezes in the air.{w=1} The writhing fish below me then finally stops writhing, but I still see the rise and fall of its chest. I can’t believe it’s not dead. I see maggots crawling out of its exposed ribcages, too. I push it off."
    nvl clear
    show layer master at fx_wave_rise(0.12, 0.85, 3.0, 2.5)
    with Dissolve(8)
    n "I heard a piercing scream{w=1} "
    show sofia b casual shock
    with hpunch
    extend "then realized the voice is coming out of my own throat, because I felt something writhing on my hands."
    show sofia b casual tweak with Dissolve(3)
    n "I don’t want to be here. {w=0.4}I don’t want to be here! {w=0.4}I don’t want to be here! {w=0.4}I don’t want to be here!{w=.4}{nw}"
    show layer master at fx_wave_hit(1.0, 0.45, 0.08, 0.5, 2.5)
    with Dissolve(3)
    n "Somebody’s hand is brusquely grabbing my arm! {w=0.3}I don’t want to be here! {w=0.2}I don’t want to be here!" 

    # @sofive: probably do something with {w} in the counting sequence here

    show layer master at fx_wave(0.45, 2.5)
    with Dissolve(5)

    scene black
    with Dissolve(0.25)

    n "I get wrestled away from the sequence. My wish is granted but whoever it is that grabbed me, I wanted dead.{w} I wanted them dead so bad.{w=1} The rotten fish on the ground is smiling at me.{w=1} It didn’t actually stop smiling.{w=1.5} She tells me something."

    show layer master at fx_wave(0.70, 2.5)
    show fx_noise at fx_static_in(1.1)
    $ renpy.pause(1.5, hard=True)
    nvl clear
    return