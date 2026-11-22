init -1 python:
    SHAR_A = "assets/sprites/SHARLENE_POSE_A1_A2"
    SHAR_B = "assets/sprites/SHARLENE_POSE_B"

transform sprite_fix:
    zoom 0.95

transform sprite_fix_new:
    zoom 0.95
    xoffset -12
    yoffset -25

transform sprite_fix_s:
    xoffset 106
    yoffset -170
transform mmo_loc(posx=0, posy=160, zom=0.35):
    xoffset posx
    yoffset posy
    zoom zom

transform mmo_fix:
    xoffset 170

transform thrash(rate=0.090):
    linear rate xoffset 2 yoffset -6
    linear rate xoffset -2.8 yoffset -2
    linear rate xoffset 2.8 yoffset -2
    linear rate xoffset -2 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat

transform hit_loop:
    ease 0.08 offset (-20, 0)
    ease 0.08 offset (+40, 0)
    ease 0.09 offset (0, 0)
    pause 0.5
    ease 0.08 offset (0, +20)
    ease 0.08 offset (0, -40)
    ease 0.09 offset (0, 0)
    pause 0.5
    repeat


define log_in = ComposeTransition(CropMove(1, "wipeup"), before=Pixellate(.25, 3), after=Dissolve(.75))


# OVERWORLD

######### SHARLANE
image shar_a1_casual       = SHAR_A + "/SHAR_A1/OUTFITS/SHAR CASUAL A1.png"
image shar_a1_housewear    = SHAR_A + "/SHAR_A1/OUTFITS/SHAR HOUSEWEAR A1.png"
image shar_a1_now_uniform  = SHAR_A + "/SHAR_A1/OUTFITS/SHAR NOW UNIFORM A1.png"
image shar_a1_then_uniform = SHAR_A + "/SHAR_A1/OUTFITS/SHAR THEN UNIFORM A1.png"

image shar_a2_casual       = SHAR_A + "/SHAR_A2/OUTFITS/SHAR CASUAL A2.png"
image shar_a2_housewear    = SHAR_A + "/SHAR_A2/OUTFITS/SHAR HOUSEWEAR A2.png"
image shar_a2_then_uniform = SHAR_A + "/SHAR_A2/OUTFITS/SHAR THEN UNIFORM A2.png"

image shar_a2_hands = SHAR_A + "/SHAR_A2/SHAR HANDS OVER FACE A2.png"
image shar_head_a  = SHAR_A + "/SHAR HEAD A.png"
image shar_head_a_shadow = SHAR_A + "/SHAR HEAD WITH SHADOW A.png"

image shar_b_casual      = SHAR_B + "/OUTFITS/SHAR CASUAL B.png"
image shar_b_housewear   = SHAR_B + "/OUTFITS/SHAR HOUSEWEAR B.png"
image shar_b_now_uniform = SHAR_B + "/OUTFITS/SHAR NOW UNIFORM B.png"
image shar_head_b        = SHAR_B + "/SHAR HEAD B.png"

image shar_a_neutral        = SHAR_A + "/EXPRESSIONS/UPSET/SHAR NEUTRAL A.png"
image shar_a_neutral_2      = SHAR_A + "/EXPRESSIONS/UPSET/SHAR NEUTRAL 2 A.png"
image shar_a_smile          = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR OPEN SMILE A.png"
image shar_a_close_smile    = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR CLOSE SMILE A.png"
image shar_a_side_smile     = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR SIDE SMILE A.png"
image shar_a_nervous_smile  = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR NERVOUS SMILE A.png"
image shar_a_smug           = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR SMUG A.png"
image shar_a_proud          = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR PROUD A.png"
image shar_a_creep_smile    = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR CREEP SMILE A.png"
image shar_a_creep_smile_2  = SHAR_A + "/EXPRESSIONS/HAPPY/SHAR CREEP SMILE 2 A.png"
image shar_a_surprised      = SHAR_A + "/EXPRESSIONS/OFFGUARD/SHAR SURPRISED A.png"
image shar_a_bracing        = SHAR_A + "/EXPRESSIONS/OFFGUARD/SHAR BRACING A.png"
image shar_a_disgusted      = SHAR_A + "/EXPRESSIONS/UPSET/SHAR DISGUSTED A.png"
image shar_a_frustrated     = SHAR_A + "/EXPRESSIONS/UPSET/SHAR FRUSTRATED A.png"
image shar_a_sad            = SHAR_A + "/EXPRESSIONS/UPSET/SHAR SAD A.png"
image shar_a_scared         = SHAR_A + "/EXPRESSIONS/UPSET/SHAR SCARED A.png"
image shar_a_side_look      = SHAR_A + "/EXPRESSIONS/UPSET/SHAR SIDE LOOK A.png"
image shar_a_upset          = SHAR_A + "/EXPRESSIONS/UPSET/SHAR UPSET A.png"

image shar_b_neutral = SHAR_B + "/EXPRESSIONS/SHAR NEUTRAL B.png"
image shar_b_awkward = SHAR_B + "/EXPRESSIONS/SHAR AWKWARD B.png"
image shar_b_smile   = SHAR_B + "/EXPRESSIONS/SHAR CLOSE_EYE_SMILE B.png"
image shar_b_shocked = SHAR_B + "/EXPRESSIONS/SHAR SHOCKED B.png"

image shar_blush  = SHAR_A + "/EFFECTS/SHAR BLUSH A.png"
image shar_breath = SHAR_A + "/EFFECTS/SHAR BREATH.png"
image shar_sweat  = SHAR_A + "/EFFECTS/SHAR SWEAT.png"
image shar_tear   = SHAR_A + "/EFFECTS/SHAR TEAR.png"


layeredimage sharlene:
    group outfit:
        attribute casual default "shar_a1_casual" when a1
        attribute casual "shar_a2_casual" when a2
        attribute casual "shar_b_casual" at sprite_fix when b

        attribute housewear "shar_a1_housewear" when a1
        attribute housewear "shar_a2_housewear" when a2
        attribute housewear "shar_b_housewear" at sprite_fix when b

        attribute now_uniform "shar_a1_now_uniform" when a1
        attribute now_uniform "shar_b_now_uniform" at sprite_fix when b
        attribute now_uniform "shar_a1_now_uniform" when a2
        # NEEDS UPDATE ^^^^^^^^^^^^

        attribute then_uniform "shar_a1_then_uniform" when a1
        attribute then_uniform "shar_a2_then_uniform" when a2
        attribute then_uniform "shar_b_now_uniform" at sprite_fix when b

    group pose:
        attribute a1 default:
            Null()
        attribute a2:
            Null()
        attribute b "shar_head_b" at sprite_fix
    group head:
        attribute regular default "shar_head_a" when a1 or a2
        attribute shade "shar_head_a_shadow" when a1 or a2

    group face_a:
        attribute neutral default "shar_a_neutral" when a1 or a2
        attribute neutral_2 "shar_a_neutral_2" when a1 or a2
        attribute smile "shar_a_smile" when a1 or a2
        attribute close_smile "shar_a_close_smile" when a1 or a2
        attribute side_smile "shar_a_side_smile" when a1 or a2
        attribute nervous_smile "shar_a_nervous_smile" when a1 or a2
        attribute smug "shar_a_smug" when a1 or a2
        attribute proud "shar_a_proud" when a1 or a2
        attribute creep_smile "shar_a_creep_smile" when a1 or a2
        attribute creep_smile_2 "shar_a_creep_smile_2" when a1 or a2
        attribute surprised "shar_a_surprised" when a1 or a2
        attribute bracing "shar_a_bracing" when a1 or a2
        attribute disgusted "shar_a_disgusted" when a1 or a2
        attribute frustrated "shar_a_frustrated" when a1 or a2
        attribute sad "shar_a_sad" when a1 or a2
        attribute scared "shar_a_scared" when a1 or a2
        attribute side_look "shar_a_side_look" when a1 or a2
        attribute upset "shar_a_upset" when a1 or a2

    group face_b:
        attribute b_neutral default "shar_b_neutral" at sprite_fix when b
        attribute b_awkward:
            "shar_b_awkward" at sprite_fix_new
            when b
        attribute b_smile "shar_b_smile" at sprite_fix when b
        attribute b_shocked "shar_b_shocked" at sprite_fix when b
        ## added by @n4d3k0
        attribute b_pissed:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR PISSED B.png"
            at sprite_fix
            when b 
        attribute b_clfrown:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR CLOSED EYE FROWN B.png" at sprite_fix_new
            when b 
        attribute b_frown:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR FROWN B.png" at sprite_fix
            when b 
        attribute b_complain:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR COMPLAIN B.png" at sprite_fix_new
            when b
        attribute b_fosmile:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR FORCED SMILE B.png" at sprite_fix_new
            when b
        attribute b_despair:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR DESPERATE B.png" at sprite_fix_new
            when b 
        attribute b_wismile:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR WIDESMILE B.png" at sprite_fix_new
            when b 
        attribute b_tweak:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR TWEAK SMILE B.png" at sprite_fix_new
            when b 
        attribute b_rage:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR ENRAGED B.png" at sprite_fix
            when b 
        attribute b_crazy:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR CRAZY SMILE B.png" at sprite_fix
            when b
        attribute b_surprised:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR SURPRISED B.png" at sprite_fix
            when b
        attribute b_sad:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR SAD B.png" at sprite_fix_new
            when b
        attribute b_pathetic:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR PATHETIC B.png" at sprite_fix_new
            when b
        attribute b_clsmile:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR CLOSED SMILE B.png" at sprite_fix_new
            when b
        attribute b_silook:
            "assets/sprites/SHARLENE_POSE_B/EXPRESSIONS/SHAR SIDE LOOK B.png" at sprite_fix_new
            when b

    attribute blush "shar_blush" when a1 or a2
    attribute breath "shar_breath" when a1 or a2
    attribute sweat "shar_sweat" when a1 or a2
    attribute tear "shar_tear" when a1 or a2

    always:
        "shar_a2_hands"
        when a2 and not now_uniform

######## CLASSMATES

layeredimage classA:
    always:
        "assets/sprites/CLASSMATE_A/CLASSMATE A BASE.png"
    group expression auto:
        attribute frown:
            "assets/sprites/CLASSMATE_A/CLASSMATE A FROWN.png"
        attribute shocked:
            "assets/sprites/CLASSMATE_A/CLASSMATE A SHOCKED.png"
        attribute smile:
            "assets/sprites/CLASSMATE_A/CLASSMATE A SHOCKED.png"

layeredimage classB:
    always:
        "assets/sprites/CLASSMATE_B/CLASSMATE B BASE.png"
    group expression auto:
        attribute mad:
            "assets/sprites/CLASSMATE_B/CLASSMATE B MAD.png"
        attribute shocked:
            "assets/sprites/CLASSMATE_B/CLASSMATE B SHOCKED.png"
        attribute smile:
            "assets/sprites/CLASSMATE_B/CLASSMATE B SMILE.png"

########### SOFIA

layeredimage sofia:
    group pose:
        attribute a default:
            Null()
        attribute b:
            Null()
    group outfit auto:
        attribute casual:
            "assets/sprites/SOFIA/POSE A/OUTFIT/SOFIA CASUAL A.png"
            when a
        attribute housewear:
            "assets/sprites/SOFIA/POSE A/OUTFIT/SOFIA HOUSEWEAR A.png"
            when a
        attribute nowform:
            "assets/sprites/SOFIA/POSE A/OUTFIT/SOFIA NOW UNIFORM A.png"
            when a
        attribute thenform:
            "assets/sprites/SOFIA/POSE A/OUTFIT/SOFIA THEN UNIFORM A.png"
            when a
        attribute casual:
            "assets/sprites/SOFIA/POSE B/OUTFIT/SOFIA CASUAL B.png"
            when b
        attribute housewear:
            "assets/sprites/SOFIA/POSE B/OUTFIT/SOFIA HOUSEWEAR B.png"
            when b
        attribute nowform:
            "assets/sprites/SOFIA/POSE B/OUTFIT/SOFIA NOW UNIFORM B.png"
            when b
        attribute thenform:
            "assets/sprites/SOFIA/POSE B/OUTFIT/SOFIA THEN UNIFORM B.png"
            when b
    group expression auto:
        attribute tlsmile1:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA CLOSED MOUTH SMILE 1 A.png"
            when a
        attribute tlsmile2:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA CLOSED MOUTH SMILE 2 A.png"
            when a
        attribute creepy:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA CREEPY SMILE A.png"
            when a
        attribute fake:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA FAKE A.png"
            when a
        attribute mock:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA MOCK A.png"
            when a
        attribute opsmile:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA OPEN MOUTH SMILE A.png"
            when a
        attribute sismile:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA SIDE SMILE A.png"
            when a
        attribute surp:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA SURPRISED A.png"
            when a
        attribute disgust:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA DISGUSTED A.png"
            when a
        attribute rage:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA ENRAGED A.png"
            when a
        attribute shadow:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA FACE SHADOW A.png"
            when a
        attribute mad:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA MAD A.png"
            when a
        attribute neutral1:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA NEUTRAL A.png"
            when a
        attribute neutral2:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA NEUTRAL 2 A.png"
            when a
        attribute silook:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA SIDE LOOK A.png"
            when a
        attribute clfrown:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA CLOSED EYE FROWN A.png"
            when a
        attribute upset:
            "assets/sprites/SOFIA/POSE A/EXPRESSION/SOFIA UPSET A.png"
            when a
        
            ## POSE B
        attribute tlsmile:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA CLOSED MOUTH SMILE B.png"
            when b
        attribute smile:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA SMILE B.png"
            when b
        attribute tweak:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA TWEAKING B.png"
            when b
        attribute pathetic:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA PATHETIC B.png"
            when b
        attribute scoff:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA SCOFF B.png"
            when b
        attribute opsmile:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA OPEN MOUTH SMILE B.png" at sprite_fix_s
            when b
        attribute sismile:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA SIDE SMILE B.png"
            when b
        attribute shock:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA SHOCKED B.png"
            when b
        attribute frown:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA FROWN B.png"
            when b
        attribute rage:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA ENRAGED B.png"
            when b
        attribute worried:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA WORRIED B.png"
            when b
        attribute mad:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA MAD B.png"
            when b
        attribute neutral:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA NEUTRAL B.png"
            when b
        attribute path:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA PATHETIC 2 B.png"
            when b
        attribute despair:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA DESPERATE B.png"
            when b
        attribute clfrown:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA CLOSED FROWN B.png"
            when b
        attribute pissed:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA PISSED B.png"
        attribute annoyed:
            "assets/sprites/SOFIA/POSE B/EXPRESSION/SOFIA ANNOYED B.png"
        

##### PARENTS

layeredimage mom:
    always:
        "assets/sprites/MOM/MOM BASE.png"
    group expression auto:
        attribute frown:
            "assets/sprites/MOM/MOM FROWN.png"
        attribute mad:
            "assets/sprites/MOM/MOM MAD.png"
        attribute smile:
            "assets/sprites/MOM/MOM SMILE.png"

layeredimage dad:
    always:
        "assets/sprites/DAD/DAD BASE.png"
    group expression auto:
        attribute frown:
            "assets/sprites/DAD/DAD FROWN.png"
        attribute smile:
            "assets/sprites/DAD/DAD SMILE.png"
        attribute speak:
            "assets/sprites/DAD/DAD SPEAK.png"

# POMORIMO

########### SHAR (shokoichan)

layeredimage shokoi:
    always:
        "assets/sprites/SHOKOI/MMO-SHAR_BASE-DITHERED.png"
    group expression auto:
        attribute creepy:
            "assets/sprites/SHOKOI/EXPRESSION/CREEPYSMILE.png"
        attribute despair:
            "assets/sprites/SHOKOI/EXPRESSION/DESPERATE.png"
        attribute dot:
            'assets/sprites/SHOKOI/EXPRESSION/DOT-EYED.png'
        attribute rage:
            'assets/sprites/SHOKOI/EXPRESSION/ENRAGED.png'
        attribute lol:
            'assets/sprites/SHOKOI/EXPRESSION/LAUGH.png'
        attribute mad:
            'assets/sprites/SHOKOI/EXPRESSION/MAD.png'
        attribute neutral:
            'assets/sprites/SHOKOI/EXPRESSION/NEUTRAL.png'
        attribute sad:
            'assets/sprites/SHOKOI/EXPRESSION/SAD.png'
        attribute scared:
            'assets/sprites/SHOKOI/EXPRESSION/SCARED.png'
        attribute silook:
            'assets/sprites/SHOKOI/EXPRESSION/SIDE-LOOK.png'
        attribute sismile:
            'assets/sprites/SHOKOI/EXPRESSION/SIDE-SMILE.png'
        attribute smile:
            'assets/sprites/SHOKOI/EXPRESSION/SMILE.png'
        attribute smug:
            'assets/sprites/SHOKOI/EXPRESSION/SMUG.png'
        attribute surp:
            'assets/sprites/SHOKOI/EXPRESSION/SURPRISED.png'
    group fx auto:
        attribute shade:
            'assets/sprites/SHOKOI/FX/SHADOW.png' at mmo_fix
        attribute cloud:
            'assets/sprites/SHOKOI/FX/SMUG-CLOUD.png'
        attribute sweat:
            'assets/sprites/SHOKOI/FX/SWEAT.png'

########### SOF (sofiamagandz30)

layeredimage sofmg:
    always:
        "assets/sprites/SOFMG/MMO-SOFIA_BASE-DITHERED.png"
    group expression auto:
        attribute awko:
            "assets/sprites/SOFMG/EXPRESSION/AWKWARD.png"
        attribute creepy1:
            "assets/sprites/SOFMG/EXPRESSION/CREEPYSMILE1.png"
        attribute creepy2:
            "assets/sprites/SOFMG/EXPRESSION/CREEPYSMILE2.png"
        attribute stress:
            "assets/sprites/SOFMG/EXPRESSION/DISTRESS.png"
        attribute rage:
            "assets/sprites/SOFMG/EXPRESSION/ENRAGED.png"
        attribute fluster:
            "assets/sprites/SOFMG/EXPRESSION/FLUSTERED.png"
        attribute lol:
            "assets/sprites/SOFMG/EXPRESSION/LAUGH.png"
        attribute mad:
            "assets/sprites/SOFMG/EXPRESSION/MAD.png"
        attribute neutral:
            "assets/sprites/SOFMG/EXPRESSION/NEUTRAL.png"
        attribute pout:
            "assets/sprites/SOFMG/EXPRESSION/POUT.png"
        attribute sad:
            "assets/sprites/SOFMG/EXPRESSION/SAD.png"
        attribute silook:
            "assets/sprites/SOFMG/EXPRESSION/SIDE-LOOK.png"
        attribute smile1:
            "assets/sprites/SOFMG/EXPRESSION/SMILE1.png"
        attribute smile2:
            "assets/sprites/SOFMG/EXPRESSION/SMILE2.png"
        attribute surp1:
            "assets/sprites/SOFMG/EXPRESSION/SURPRISED1.png"
        attribute surp2:
            "assets/sprites/SOFMG/EXPRESSION/SURPRISED2.png"
    group fx auto:
        attribute vein:
            "assets/sprites/SOFMG/FX/MAD.png"
        attribute dark:
            "assets/sprites/SOFMG/FX/NO-EYE-SHINE.png"
        attribute shade:
            "assets/sprites/SOFMG/FX/SHADOW.png"
        attribute sweat:
            'assets/sprites/SOFMG/FX/SWEAT.png'

#### MONSTERS

image spiderlily = "assets/sprites/MONSTERS/SPIDER-LILY.png"
        
########### TRANSFORMS

transform loc(posx=0.5, posy=1.0, zom=1):
    # crop (80, 0, 400, 768)
    # zoom (config.screen_height / 768.0)
    yoffset posy
    xpos posx
    zoom zom
    yalign 1.0

transform sprite_left:
    # crop (80, 0, 400, 768)
    # zoom (config.screen_height / 768.0)
    xalign 0.06
    yalign 1.0

transform sprite_center:
    # crop (80, 0, 400, 768)
    # zoom (config.screen_height / 768.0)
    xalign 0.5
    yalign 1.0

transform sprite_right:
    # crop (80, 0, 400, 768)
    # zoom (config.screen_height / 768.0)
    xalign 0.94
    yalign 1.0
