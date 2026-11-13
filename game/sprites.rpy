init -1 python:
    SHAR_A = "assets/sprites/SHARLENE_POSE_A1_A2"
    SHAR_B = "assets/sprites/SHARLENE_POSE_B"


image shar_a1_casual       = SHAR_A + "/SHAR_A1/OUTFITS/SHAR CASUAL A1.png"
image shar_a1_housewear    = SHAR_A + "/SHAR_A1/OUTFITS/SHAR HOUSEWEAR A1.png"
image shar_a1_now_uniform  = SHAR_A + "/SHAR_A1/OUTFITS/SHAR NOW UNIFORM A1.png"
image shar_a1_then_uniform = SHAR_A + "/SHAR_A1/OUTFITS/SHAR THEN UNIFORM A1.png"

image shar_a2_casual       = SHAR_A + "/SHAR_A2/OUTFITS/SHAR CASUAL A2.png"
image shar_a2_housewear    = SHAR_A + "/SHAR_A2/OUTFITS/SHAR HOUSEWEAR A2.png"
image shar_a2_then_uniform = SHAR_A + "/SHAR_A2/OUTFITS/SHAR THEN UNIFORM A2.png"

image shar_a2_hands = SHAR_A + "/SHAR_A2/SHAR HANDS OVER FACE A2.png"
image shar_head_a  = SHAR_A + "/SHAR HEAD WITH SHADOW A.png"

image shar_b_casual      = SHAR_B + "/OUTFITS/SHAR CASUAL B.png"
image shar_b_housewear   = SHAR_B + "/OUTFITS/SHAR HOUSEWEAR B.png"
image shar_b_now_uniform = SHAR_B + "/OUTFITS/SHAR NOW UNIFORM B.png"
image shar_head_b        = SHAR_B + "/SHAR HEAD B/SHAR HEAD B.png"

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
        attribute casual "shar_b_casual" when b

        attribute housewear "shar_a1_housewear" when a1
        attribute housewear "shar_a2_housewear" when a2
        attribute housewear "shar_b_housewear" when b

        attribute now_uniform "shar_a1_now_uniform" when a1
        attribute now_uniform "shar_b_now_uniform" when b
        attribute now_uniform "shar_a1_now_uniform" when a2

        attribute then_uniform "shar_a1_then_uniform" when a1
        attribute then_uniform "shar_a2_then_uniform" when a2
        attribute then_uniform "shar_b_now_uniform" when b

    group pose:
        attribute a1 default "shar_head_a"
        attribute a2 "shar_head_a"
        attribute b "shar_head_b"

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
        attribute b_neutral default "shar_b_neutral" when b
        attribute b_awkward "shar_b_awkward" when b
        attribute b_smile "shar_b_smile" when b
        attribute b_shocked "shar_b_shocked" when b

    attribute blush "shar_blush" when a1 or a2
    attribute breath "shar_breath" when a1 or a2
    attribute sweat "shar_sweat" when a1 or a2
    attribute tear "shar_tear" when a1 or a2

    always:
        "shar_a2_hands"
        when a2 and not now_uniform


transform sprite_at(pos=0.5):
    crop (80, 0, 400, 768)
    zoom (config.screen_height / 768.0)
    xalign pos
    yalign 1.0

transform sprite_left:
    crop (80, 0, 400, 768)
    zoom (config.screen_height / 768.0)
    xalign 0.06
    yalign 1.0

transform sprite_center:
    crop (80, 0, 400, 768)
    zoom (config.screen_height / 768.0)
    xalign 0.5
    yalign 1.0

transform sprite_right:
    crop (80, 0, 400, 768)
    zoom (config.screen_height / 768.0)
    xalign 0.94
    yalign 1.0
