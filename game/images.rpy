init python:
    def bg_cover(path):
        w, h = renpy.image_size(path)
        zoom = max(config.screen_width / float(w), config.screen_height / float(h))
        return Transform(path, zoom=zoom, align=(0.5, 0.5))

image bg CLASSROOM = bg_cover("assets/bg/bg_CLASSROOM.png")
image bg BATHROOM = bg_cover("assets/bg/bg_BATHROOM.png")
image bg COMPLAB = bg_cover("assets/bg/bg_COMPLAB.png")
image bg HALLWAY = bg_cover("assets/bg/bg_HALLWAY.png")
image bg JP RESTAURANT = bg_cover("assets/bg/bg_JP RESTAURANT.png")
image bg MMORPG_CRYSTAL_DUNGEON = bg_cover("assets/bg/bg_MMORPG_CRYSTAL_DUNGEON.png")
image bg PATH HOME = bg_cover("assets/bg/bg_PATH HOME.png")
