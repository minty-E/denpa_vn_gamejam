default textbox_style = "irl"

define n = Character(None, kind=nvl)
define so = Character("Sofia")
define sh = Character("Sharlene")
define shoko = Character("shokoichan")
define sofiam = Character("sofiamagandz30")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    shoko "You've created a new Ren'Py game."

    $ textbox_style = "mmo"

    shoko "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
