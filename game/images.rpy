init python:
    def bg_cover(path):
        w, h = renpy.image_size(path)
        zoom = max(config.screen_width / float(w), config.screen_height / float(h))
        return Transform(path, zoom=zoom, align=(0.5, 0.5))

############# BACKGROUNDS

image bg CLASSROOM = bg_cover("assets/bg/bg_CLASSROOM.png")
image bg RECOG HALL GARDEN = bg_cover("assets/bg/bg_RECOG HALL GARDEN.png")
image bg RECOG HALL = bg_cover("assets/bg/bg_RECOG HALL.png")
image bg BATHROOM = bg_cover("assets/bg/bg_BATHROOM.png")
image bg COMPLAB = bg_cover("assets/bg/bg_COMPLAB.png")
image bg HALLWAY = bg_cover("assets/bg/bg_HALLWAY.png")
image bg JP RESTAURANT = bg_cover("assets/bg/bg_JP RESTAURANT.png")
image bg JP RESTROOM = bg_cover("assets/bg/bg_JP BATHROOM.png")
image bg STORE = bg_cover("assets/bg/bg_STORE.png")
image bg BACK OF SCHOOL = bg_cover('assets/bg/bg_BACK OF SCHOOL.png')
image bg MMO VILLAGE = bg_cover("assets/bg/bg_MMO VILLAGE.png")
image bg MMORPG CRYSTAL DUNGEON = bg_cover("assets/bg/bg_MMORPG_CRYSTAL_DUNGEON.png")
image bg PATH HOME = bg_cover("assets/bg/bg_PATH HOME.png")

############# CGS

image CG1 = Movie(play="assets/cgs/CG1IMAGINATION.webm", loop=True)
image CG_sketch_1 = "assets/cgs/CG_SOFIASKETCH1.png"
image CG_sketch_2 = "assets/cgs/CG_SOFIASKETCH2.png"
image CG BATHROOM = "assets/cgs/CG_bathroom.png"
image CG BULLY = "assets/cgs/CG_BULLY 2_F.png"

########### LOADING SCREENS
image LS = DynamicImage("assets/bg/LOADING SCREENS/LOADING SCREEN [lsn].png")
############# TRANSFORMS

transform center:
    xalign 0.5
    yalign 0.5

