label chapter_4_1:

    image intro = Text("{font=assets/fonts/Jersey20.ttf}{size=350}{space=80}DAY 1{/size}{/font}{size=150}\n{font=assets/fonts/ARIALN.ttf}ALGOR{space=180}MORTIS")
    show intro at center
    with Dissolve(3)
    with Pause(1.5)
    hide intro with Dissolve(2)

    scene bg MMO VILLAGE
    with Dissolve(1.5)

    show shokoi neutral at mmo_loc(0)
    show sofmg neutral at mmo_loc(550)
    with Dissolve(0.5)

    $ textbox_style = "mmo"

    shoko "lolz you didnt chat 4 like 3 minutes"

    shoko "idiot that falls asleep on her desk XD"

    hide sofmg

    mmo_console "[[10:12:04PM] sofiamagandz30 disconnected from your party."

    mmo_console "[[10:12:04PM] sofiamagandz30 joined the World Hub."

    mmo_console "[[10:12:05PM] You sent a party request to sofiamagandz30."

    show shokoi scared shade

    shoko "if u dont respond ill be sooooooo upset"

    show shokoi smug -shade

    shoko "soffffff xdddd"
    show sofmg smile1 at mmo_loc(550) with log_in

    sofiam "im here idiot"

    show sofmg shade smile2
    sofiam "somebody fucked up the router line"
    show shokoi lol cloud
    shoko "mayb it wuz ur dad again ( ´ ▽ ` )"

    show shokoi smile -cloud
    show sofmg neutral -shade

    mmo_console "[[10:12:06PM] sofiamagandz30 accepted your party request."

    mmo_console "[[10:12:06PM] shokoichan requested to move to area Crystal Dungeon. [[Server: MIDNIGHT] Yes No"

    show sofmg pout

    sofiam "im so sick of crystal dungeon. youre so boring"

    show shokoi sad

    shoko "me needz an item from crystal dungeon T_T"

    show sofmg neutral

    sofiam "k"

    show sofmg silook
    show shokoi sismile

    sofiam "at least im getting wep exp"
    $ lsn=renpy.random.randint(1, 5)
    scene LS with Dissolve(1)

    mmo_console "[[10:12:14M] Connecting to server: MIDNIGHT..."

    mmo_console "[[10:12:15PM] Moving to Crystal Dungeon..."

    scene LS

    $renpy.pause(2, hard=True)

    scene black with Dissolve(2)

    return
