label chapter_3_3:

    scene bg JP RESTROOM
    with Fade(1, 1.5, 1)

    no "{i}Creak...{/i}"

    no "As soon as I walked in, the fishy, rotten smell was even stronger. But now it also smelled of someone's urine. It was even more miserable than the pigpen outside. When I saw Sharlene, it was like she completely changed."

    no "She wasn't even wearing the same expression she did earlier. In fact, she looked irritatingly calm."

    show sharlene a2 bracing at loc(400) with dissolve

    sh "Holy fuck.{w}"
    show sofia a casual silook at loc(-400) with Dissolve(1)
    extend " I feel like my eye's going to bulge out of my skull from how itchy it feels."
    show sofia a casual neutral1 at loc(-350) with easeinright
    show sharlene a2 surprised with dissolve
    with Pause(.5)
    so "...Itchy?"

    no "Our gazes briefly met in the mirror. Sharlene was pulling down on her right bottom eyelid, and I could see the red flesh peeking out from under. It looked red and a bit swollen. She blew in the snot in her nose, and that's how I knew she came in here just to cry again."

    no "Though the swollenness of her eye felt unnatural. It looked like it was going to leak pus at any moment."

    sh "Yeah. I got gunk from the fish in my eye. There's probably a contagious virus in it now."
    sh "Nay...{w}"
    show sharlene a1 proud at loc(360) with easeinleft
    extend " that's my evil eye.{w=.5} I've been granted powers to banish evil."
    show sofia a casual disgust at loc(-400) with easeinright

    sh "And if you stare into it too hard your eyes are gonna fall off."

    no "An ugly smile creeps onto her face. Even just now I've already had enough of her antics, so I turned my back to the mirror, arms folded together. It felt like it'd be so satisfying to stomp on her foot and remind her of her idiocy, but I held back."
    show sofia a casual silook with dissolve
    so "You are genuinely an idiot."

    no "An unpleasant sensation was starting to crawl up my spine. I had to swallow it down. I had to. It would be a complete detriment if it snaked itself into my gut."
    show sharlene a1 nervous_smile with dissolve
    sh "Haha.{w=.5} You're going to school tomorrow?"
    show sofia a casual neutral2 with Dissolve(0.25)

    so "Of course?"

    sh "Kuya Kang on the TV said the weather's rain tomorrow."

    show sharlene a1 frustrated

    sh "So if you come you're gonna get eaten by the siokoy."

    show sharlene a1 creep_smile with Dissolve(1.5)
    with Pause(.5)
    show sharlene a1 creep_smile at loc(300) with easeinleft
    show sofia a casual surp
    sh "You're probably its favourite snack."
    show sofia a casual mad
    so "Fuck you, Shokoy."
    show sofia a casual mad at loc(-300) with easeinright
    show sofia a casual mad with vpunch
    with Pause(0.25)
    show sharlene nervous_smile with hpunch
    show sharlene nervous_smile at loc(400) with moveinright
    no "I stomp on her foot and elbow her. She doesn't even respond in an interesting way. All I hear is a scoff, and my nerves quiet down unceremoniously. I couldn't get entertainment out of this even if I wanted to."

    so "Did it ever occur to you that this is why people think you're going to kill everyone?"

    show sharlene b b_fosmile with dissolve
    sh "You guys are also fucking stupid. It's just an old tale, like a yokai's tale. They don't hurt you if you don't do anything stupid."
    show sofia a casual silook with Dissolve(.75)
    so "I don't even know why I bother to tell you these things."
    show sharlene b b_pathetic at loc(250) with easeinleft
    sh "It's `cause you're my friend!"

    sh "We're friends! Even if the siokoy eats you we're friends.{w=1} Okay?"
    scene black
    with Dissolve(1)
    no "I felt her body temperature crush against mine as she tried to nudge me into responding.{w} I hated feeling it,{w=.5} for every second that passed."
    scene black
    with Dissolve(1)
    with Pause(1.5)

    return
