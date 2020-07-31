# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jules", color = "#636363")
define slowdissolve = Dissolve(3.0) # in parentheses has typed time of transition
define rapiddissolve = Dissolve(.5)
define fade = Fade(0.5, 0.0, 0.5)
# define slowmove = Move() --- check function in documentation

# pre-defined transformations
transform slightright:
    xalign 0.75
    yalign 0

transform slightleft:
    xalign 0.25
    yalign 0

transform bottomright:
    xalign 1.0
    yalign .8

transform bottomleft:
    xalign 0.0
    yalign .8

# The game starts here.

label start:
################################################################################
# BEGIN

    # start play music at start of game
    # play music "snd_background_music.ogg" or play music snd bg default
    # another variant - "play music snd bg msc" if file is stored in the root

    ############################################################################
    play music "audio/music/snd bg music.ogg" fadeout 1

    "check how work play music channel" # play music replace previous(prior) soundtrack to written in command (choosen)

    play music "audio/music/snd bg music two.mp3"
    ############################################################################


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg purple

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # in real development don't positioning before pre-defining transform variable
    show jill smoking:
        xalign 0.5
        yalign 0

    j "Hi!"

    j "Welcome to the game..."

################################################################################
# note that "jill staring" also at slightright position

    scene bg grey
    show jill smoking at slightleft   # There has been used pre-defined transform "slightright"

    j "Now I'm here!"


    show jill staring
    j "I have changed skin!"

################################################################################
# Try transitions

    # transition with scene
    scene bg purple with slowdissolve
    # transiotion end

    # transition begin
    show jill staring at truecenter with slowdissolve
    # transition end

    j "Two Transitions of dissolving is completed"

    show jill staring at bottomright with move
    j "Move 1"

    show jill staring at topleft with move
    j "Move 2"

    # show jill staring at topleft with move
    show jill staring at topright with move
    show jill staring at bottomright with move
    show jill staring at bottomleft with move

    show jill staring at topleft with move
    show jill staring at topright with move
    show jill staring at bottomleft with move
    show jill staring at bottomright with move

    ############################################################################
    # Scene City transition

    scene bg city with fade
    "City of oppression and suffering"
    pause 3

    # check rapid dissolve
    scene bg purple with rapiddissolve
    show jill smoking at top with rapiddissolve
    j "I'm back"

################################################################################
# The choice syntax
    menu:
        # put the quetion here, but you can put hte quetion before the choice
        "Did you find artist for your game ?"

        "Yes, I do":
            jump choice1_yes

        "No, I don't":
            jump choice1_no

    ######################
    label choice1_yes:
        $ menu_flag = True

        j "It's good news"

        jump next_episode

    #######################
    label choice1_no:
        $ menu_flag = False

        j "It's bad news"

        jump start
    #######################
    label next_episode:

        j "Learn more"
################################################################################
    hide jill smoking


    # This ends the game.
    return
################################################################################
