label chapter_3_2:

    nvl hide dissolve

    show mom smile at loc(300) with Dissolve(1.5)

    som "Yes, she's a very respectable girl. She worked day and night to get those awards!"

    shf "I wish my daughter could be more like yours!"

    show dad smile at loc(50) with Dissolve(1.5)

    shf "They're friends, so why don't they teach each other Mathematics? Sofia's always been better at it than her. It's a shame, because it's Shasha's lowest grade..."

    som "How about it, Sofia? Maybe Shasha's father could even pay you to be her tutor!"

    no "My mother erupts into laughter. Sharlene's father laughs with the joke, but it somehow feels like it doesn't reach his eyes. I stared directly at the sea creatures in front of me. Dead salmon, dead tuna, dead eel, dead urchin. Sharlene."

    no "She looked ashamed to even be sitting there. She hasn't taken a single piece of food either. I found it annoying that they chose to talk to me, and I wished that the sea creature in front of me would also drop dead."

    hide mom
    hide dad
    with Dissolve(1)
    with Pause(0.5)
    show sharlene casual upset at loc(500)
    show sofia a casual sismile at loc(-300)
    with Dissolve(1.5)  

    no "Sharlene always looks so easy to tease. It might be the only source of entertainment I have these days."

    show sofia b casual opsmile with Dissolve(1)
    so "I'd be glad to help her. She might even need to learn more than just math from me."

    so "Sh... Sharlene's never been the bright type, after all. But that's not inherently her fault."

    show sharlene sad with Dissolve(0.75)
    with Pause(0.25)
    show sofia b casual smile with Dissolve(0.5)

    no "Sharlene's eyes didn't reflect the light―in fact, they never did even in other places. That's because she always has her head at this awkward angle, looking down while trying to squint up."

    no "Someone taught her that eye contact was important and she always makes a point to remind me. Her eyes are squinting away."

    show sharlene b b_complain with easeinright
    sh "But Sofia wastes her time playing games with me..."
    show sharlene b b_complain at loc(200)
    show sofia b casual smile at loc(-500)
    with easeinright
    show mom mad at loc(400) with Dissolve(1.5)
    som "You―{w}"
    show sharlene b b_sad at loc(200)
    show sofia b casual neutral at loc(-500)
    with dissolve
    extend "you're not lying about my child again, are you?"
    show sharlene b_pathetic with Dissolve(2)
    no "Sharlene's face contorted in a way I haven't seen in a while. It was one of her funnier displays."

    show sharlene b_pathetic with vpunch
    sh "I wouldn't lie! Especially not to her mom!"

    sh "W-Why would I do that?{w=1} She's really good at Pomorimo Online!"

    som "Pomo... dear, what is she talking about...?"
    show sofia a casual fake at loc(-400) with easeinleft
    so "It's a pomodoro timer thing. For work habits?"
    show sharlene b_complain with dissolve
    sh "You―"

    no "I saw Sharlene doing that habit where she'd chew on the inside of her mouth. It always made her look like a bloated fish of sorts.{w}"
    hide sharlene with moveoutleft
    extend " She sinks away from the conversation and springs up abruptly from her seat. None of the adults react. They're used to her stupid outbursts."

    show sofia b casual clfrown at loc(-450) with easeinleft
    no "I was starting to feel even sicker from the smell invading my nostrils, and my legs stood up before I could explain to my mother what I was doing. Now I needed to act like I had some compassion."

    show sofia b casual worried at loc(-480) with easeinleft
    so "I'm just checking on her. Okay, mama?"
    show mom smile with Dissolve(1)
    som "That'd be good, yes. You manage to still be so kind even when she's so troublesome, Sofia."
    show sofia b casual sismile at loc(-500) with easeinleft
    so "... Hahaha."

    so "Of course."
    hide sofia with moveoutleft
    return
