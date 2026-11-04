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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    n "{i}Snap!{/i}"

    n "The flash annoyingly burnt into my retinas, and I could feel an arm awkwardly shifting up against me. A girl complained that I should move over. It made me want to plant my feet even firmer on the ground. Another flash popped; I squinted hard. I hated it, every single time."

    n "{i}Snap! Snap!{/i}"

    cla "\"Would it kill them to stop taking photos?\""

    clb "\"You probably look ugly as hell in them... hahaha!\""

    n "The flashing stopped. The girls beside me ran quickly back to the crowd of adults, making sure to ignore my presence and run past every other person in the vicinity. I saw a girl bump into another. One of them stomped on my shoe."

    nvl clear

    n "My shoes, which my mother had kindly bought for me just for {i}this{/i} specific occasion. I thought of the satisfaction that entered my heart when I went to the shoe outlet with my family and saw this pair. They scoffed and said it didn't suit me, but once I put them on and looked at my feet in the mirror, their tune changed completely. They're like fools who easily bend to my whims. Really, I loved them for it. I stared dead ahead at the girl who stomped on my brand-new doll shoes. Their shine had dulled a bit. She saw me staring ahead at her, and I scoffed as visibly as I could. Quickly, she turned away."

    n "I didn't care, and I was hoping her—Angela, from the other class over—would look like an ugly brute in her photos so that her male crush would think she looked absolutely detestable in them. She most likely was, anyway, because the way she angled her head made her buccal fat crush against her neck in such a way that would make her cry if she saw it."

    n "I checked the photos on my mama's phone. Really, this outdoor setting didn't need flash, and it only made the photo so much uglier. It was the halfwit's father that wouldn't stop using the flash on his phone–nobody taught him how to turn it off, and nobody in the vicinity cared. They shot him dirty looks, I saw, I saw it all! But they didn't care."

    nvl clear

    n "They wanted it to end as much as I did, so they snapped away on their poorly made Androids and beat up digital cameras. I saw the halfwit's crooked smile in the photo. I almost wanted to puke."

    n "When I turned my head up from the screen, she was there, and her real life counterpart was just as if not more awful than the one on the screen. Even on special occasions, she never bothered to fix her hair, and her pin had become lopsided from how rowdy she was. Hairs stuck out like static electricity were affecting them. She didn't come bare-faced, but it's obvious that her mother did her make-up last minute. She chose an outfit that was ill-fitted. It sparkled bright blue, and I thought it was one of those tacky department store dresses her mother would buy for her. Lacking taste might be genetic. I don't know why she crawled up to me. I wanted to squash her again like a bug, but I let the thought go, because I didn't want to ruin one of the only good occasions I got to have these days."

    nvl hide dissolve

    sh "\"So, first honors, huh? You really know how to persevere-\""

    so "\"Don't even start with me, Shokoy.\""

    no "She tilted her head in that so-awful cartoony manner that I always hated. She then put a hand on her chin. It's like real life is a joke to this seawater creature."

    sh "\"Don't think this is the end of me, Sofia-sama!\""

    sh "\"They always say the underdogs win when you expect them to the least. I've got a steadfast heart and all the dokidoki in the world to carry me, so I'm gonna blast through third, and waaay into first.\""

    sh "\"You're noooooot gonna be ready for it.\""

    so "\"Do you think I care if you get first honors? I don't think even the rest of the student body cares.\""

    sh "\"I guess, but I wanna prove you guys' theory about me having alien maggots in my brain wrong.\""

    sh "\"Tried to check, BTW. I looked at my ear in the mirror 'n there was nothing.\""

    sh "\"‘Coz if there were, there'd be white stuff wriggling out.\""

    nvl clear

    n "I tried so hard to ignore her. She's unbearable to talk to, she says the most unbearable things, and she makes nods to things that frankly I don't even care to think of. Regrettably, I know what she's talking about half the time. Our parents made us watch TV all the time, and she had the expensive kind. Cable. I have cable at my home, too, but I don't care to click through any of the channels. I already have my home computer to attend to. She'd always put the anime channel on cable. We'd do the stupid dances together and sing the songs in broken pretend-foreign-language. I still have notebooks with those Pretty Beat stickers she gave me on the front. When I tried to peel them off the covers were only damaged, so I kept them in a drawer, covered in ash and perhaps growing mold. One of the notebooks had a lopsided drawing of hers in it. I only broke them open again to use as scratch paper for my math homework."

    n "Sharlene plays with her hands in the most anxious way. It's like watching a small animal. Whenever she's not rubbing the skin on her fingers against her palm, she's scratching at every piece of loose skin she can find. She picks and I notice this every time, but she has the hands of a brute. Crackled, peeled skin at the edges of all of her nails. She always picks at them even when they're already bleeding. She was picking at them again. The red seeped out and her hands floated up to bite on the already bleeding hangnail. I swear I caught myself involuntarily dry hacking."

    nvl clear

    n "I raised my palm to slap her hand away from her face. She didn't even react. At some point, she stopped reacting strongly. She always cried before when I would hurt her in any way, even when it was just dumb things like accidentally ribbing her or accidentally catching my nails in her hair. She'd cry and scream so loud her parents thought I was killing her."

    n "Sometimes, I don't think they’re wrong. I've tried to kill her so many times in my mind, already."

    son "\"You're disgusting.\""

    son "\"Does your blood taste good to you? Are dead skin cells part of your essential diet? Is that why you do that?\""

    return
