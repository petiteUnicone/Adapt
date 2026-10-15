# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Brianna", colour = "#c8ffc8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    b "Umm, hello?"

    b "You kinda spaced out there... Are you feeling ok?"
    menu:
        "Yes. Why?":
            jump larp
        "No, I don't remember what happened":
            jump explain

label explain:
    b "Look at me. I am your bestfriend. And you are Evie."
    b "Its almost like the dream you told me about. Do you remember which dream I am talking about."
    menu:
        "Obviously yes! It was my dream in the end":
            jump larp
        "Noo... could you explain?":
            jump lost
label larp:
    return

label lost:
    scene bg lost
    "You lost"

    # This ends the game.
