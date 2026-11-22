label chapter_1_1:
    $ textbox_style = "irl"

    scene bg RECOG HALL GARDEN

    $ flash()
    n "{i}Snap!{/i}" # @sofive: camera flash and click @sfx

    # @sofive: @music: ionias5_10_ambient.mp3

    show sofia b casual neutral at loc(50, zom=0.75)
    with Dissolve(3)

    n "The flash annoyingly burnt into my retinas, and I could feel an arm awkwardly shifting up against me. A girl complained that I should move over. It made me want to plant my feet even firmer on the ground. Another flash popped; I squinted hard. I hated it, every single time."

    $ flash(hits=2)
    n "{i}Snap! Snap!{/i}"

    show classA frown at loc(-320) with dissolve
    cla "Would it kill them to stop taking photos?"

    
    show classB smile at loc(-100) with dissolve
    clb "You probably look ugly as hell in them... hahaha!"

    hide classB
    hide classA
    hide sofia
    with Fade(0.15, 0, 0.25, color="#fff")

    n "The flashing stopped.{w} The girls beside me ran quickly back to the crowd of adults, making sure to ignore my presence and run past every other person in the vicinity. I saw a girl bump into another.{w=.5}"
    show sofia b casual neutral at loc(-80) with hpunch
    extend " One of them stomped on my shoe."
    
    nvl clear

    n "My shoes, which my mother had kindly bought for me just for {i}this{/i} specific occasion. I thought of the satisfaction that entered my heart when I went to the shoe outlet with my family and saw this pair. They scoffed and said it didn't suit me, but once I put them on and looked at my feet in the mirror, their tune changed completely. They're like fools who easily bend to my whims. Really, I loved them for it."
    show sofia a casual mock at loc(-200,120, zom=1.25)
    with Dissolve(1)
    extend "I stared dead ahead at the girl who stomped on my brand-new doll shoes. Their shine had dulled a bit. She saw me staring ahead at her, and I scoffed as visibly as I could. Quickly, she turned away."
    show sofia casual silook at loc(-265, 170, zom=1.35)
    with Dissolve(0.25)
    n "I didn't care, and I was hoping she[md]Angela, from the other class over[md]would look like an ugly brute in her photos so that her male crush would think she looked absolutely detestable in them. She most likely was, anyway, because the way she angled her head made her buccal fat crush against her neck in such a way that would make her cry if she saw it."
    nvl clear
    hide sofia with dissolve
    n "I checked the photos on my mama's phone.{w} Really, this outdoor setting didn't need flash, and it only made the photo so much uglier. It was the halfwit's father that wouldn't stop using the flash on his phone[md]nobody taught him how to turn it off, and nobody in the vicinity cared. They shot him dirty looks, I saw, I saw it all! But they didn't care."

    n "They wanted it to end as much as I did, so they snapped away on their poorly made Androids and beat up digital cameras.{w}"
    show sofia casual disgust
    with Dissolve(0.25)
    extend " I saw the halfwit's crooked smile in the photo. I almost wanted to puke."
    nvl clear
    n "When I turned my head up from the screen,{w=1}"
    show sofia b casual neutral at loc(100)
    show sharlene a1 casual side_look at loc(550)
    with Fade(0.25, 0, 0.25)
    extend "she was there,{w=.5} and her real life counterpart was just as if not more awful than the one on the screen. Even on special occasions, she never bothered to fix her hair, and her pin had become lopsided from how rowdy she was. Hairs stuck out like static electricity were affecting them.{p} She didn't come bare-faced, but it's obvious that her mother did her make-up last minute. She chose an outfit that was ill-fitted. It sparkled bright blue, and I thought it was one of those tacky department store dresses her mother would buy for her. Lacking taste might be genetic. I don't know why she crawled up to me. I wanted to squash her again like a bug, but I let the thought go, because I didn't want to ruin one of the only good occasions I got to have these days."

    nvl clear

    return