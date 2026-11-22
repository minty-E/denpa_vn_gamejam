label chapter_6_3:
    scene bg HALLWAY
    with CropMove(0.5, "wiperight")

    show sofia a nowform silook with Dissolve(1)

    no "When I make it out to the hallway, my first instinct is to just keep marching farther and farther away from that putrid place. I knew they looked at me like I was the same kind of animal that Sharlene was. They've been doing it ever since she started talking my ear off about Pomorimo and some other dumb shit during recess."
    no "I don't remember when that was. That's how long ago this charade has been going. I kept telling her to stay away from me, but she kept insisting that she doesn't see any reason to be apart from me. That I'm just being cold because I'm surrendering to the \"opinions of others\"."
    no "I knew at that moment I should've screamed at her just to make it clear to her where our distinctions lay. It could've been as simple as {i}you are not my friend and I am above you and I will not be bullied by some adolescent dimwits all because you want to tell me about games and cartoons{/i}."
    no "I felt my blood boiling just thinking about what I could've said to her.{w}"

    show sofia a nowform neutral2 with Dissolve(2)
    extend "{w=.5} I can fix it.{w=.5} I can probably still fix this."

    no "My feet felt so heavy, but each forced impact of my shoe was satisfying. I knew, at least, that people would be scared of me.{w}"
    show sofia a nowform mad at loc(800) with easeinright
    extend " That's right. If they can't accept me, they should at least fear me. This way, I don't have to be below dirt―"

    sh "I pray I'll be believin' in tomorrow..."

    scene bg HALLWAY
    show sharlene b now_uniform b_sad at loc(600)
    with Dissolve(3)

    show sofia b nowform pathetic at loc (-400)
    with Dissolve(2)

    so "......"

    no "Sharlene's throat started moving in an obscenely gross way. I could tell she was trying to keep {i}something back{/i}, because she swallows her spit and her face contorts some ways before it finally starts looking dumb. She does that awful finger fidgeting thing she likes to do."

    show sharlene b now_uniform b_pathetic
    sh "Hi."

    show sofia b nowform clfrown with Dissolve(.25)

    so "........."

    no "She stepped out of the comfort room―actually, even just thinking about that feels obscene. I don't even want to imagine what she was doing there and I have no interest in it. She behaved the way the outcasts in her cartoons always did."
    no "She would take to eating lunch and playing games and drawing in the fucking comfort room stall of all things. She also did some other things but I don't want to bother thinking about it right now. All I know is that her wrist is completely spotless and that she's only holding that chewed-up notebook in her right hand."
    no "She gripped it harder and it started looking even more banged up. I didn't know why I had to run into her now. It didn't do anything for my already awful mood. I could probably kill her right now and it would be so much better."
    no "In fact, she could start killing me and that would already be heaps more exciting than this sham of a school."

    show sofia b nowform pathetic at loc(-300) with easeinleft
    so "Where's your siokoy?"

    show sharlene b now_uniform b_shocked at loc(650) with easeinright
    sh "My wha...?"

    show sofia b nowform mad at loc(-250) with easeinright

    so "Tch.{w=1} You know.{w=.5} The siokoy that's going to eat the whole school?"

    show sharlene b now_uniform b_wismile with Dissolve(3)

    no "Her face contorted into an ugly grin. She laughs.{w}" 

    show sofia b nowform shock at loc (-325) with easeinright

    extend " She takes way too long laughing at what I said that at this point I feel like she has nothing valuable to offer me."

    sh "{i}It's me!{/i}"

    no "I already knew she was going to say it but it didn't make it any less infuriating."
    show sofia b nowform shock at loc (-300) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    no "I step closer.{w}"
    show sofia b nowform shock at loc (-275) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend " Once.{w}"
    show sofia b nowform shock at loc (-250) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend " Twice.{w}"
    show sofia b nowform shock at loc (-225) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend "I see Sharlene twitch a bit for every step further I took, and I saw her throat moving again.{w}"
    show sofia b nowform shock at loc (-200) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend " She tries to laugh me off but her laugh turns into a snicker."
    show sofia b nowform shock at loc (-175) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    no "A snicker?{w} "
    show sofia b nowform shock at loc (-150) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend "Was she mocking me?{w} "
    show sofia b nowform shock at loc (-125) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend "I think she is, because the last thing I see{w=1}"
    show sofia b nowform shock at loc (-100) with easeinright
    show sharlene b now_uniform b_wismile with hpunch
    extend " before she takes off like an animal is her disgusting smirk.{w} "
    hide sharlene b now_uniform b_wismile with moveoutright
    show sofia b nowform shock at loc (-75) with easeinright
    extend "She turned right back into the comfort room.{w=.75} That's her mistake."

    return
