# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Brianna", colour = "#c8ffc8")
define t = Character("Mr Freeman", colour ="#cbc8ff")
define l = Character("Lina", colour= "#ffc8d4")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bri

    # These display lines of dialogue.
    "You wake up and the only thing you remember is your name, Evie"
    b "Umm, hello?"

    b "You kinda spaced out there... Are you feeling ok?"
    menu:
        "Yes. Why?":
            jump questionOnBoard
        "No, I don't remember what happened":
            jump explain

label explain:
    show bri concern
    b "Look at me. I am your bestfriend. And you are Evie."
    b "Its almost like the dream you told me about. Do you remember which dream I am talking about."
    menu:
        "Obviously yes! It was my dream in the end":
            jump questionOnBoard
        "Noo... could you explain?":
            jump lost

label questionOnBoard:
    b "Oh good! Lesson is about to start"
    hide bri 
    "You look ahead, and find unsolvable maths questions staring back"
    show teach
    "You look at the teacher and  see his lanyard saying Mr Freeman"
    t "Good to see the chatter has died down... Now lets focus on the starter on the board"
    t "Oh Evie! Smart as ever! Please tell us the answer"
    menu:
        "Is it 4?":
            jump answered
        "I haven't worked it out":
            jump workOut
        "Ummm, I don't know the answer sir":
            show teach scary
            jump lost

label workOut:
    t "I see, you should work it out next time"
    hide teach
    b "Thats a close one"
    b "Hurry up before he gets angry"
    menu:
        "Is it 4?":
            jump answered
        "I can't be asked":
            jump lost

label answered:
    hide teach
    show teach at left
    hide Bri
    show Bri at right
    t "Ah I am proud of you, just like I expected"
    show Bri proud
    t "I will leave you guys to it"
    hide teach
    "You let out a sigh after that drilling maths question."
    b "Knew you wouldn't embaress me"
    hide Bri
    "You feel a poke on your shoulder"
    l "Shhhh, don't turn around. I have a question"
    l "So you really don't remember your dream?"
    menu:
        "What dream?":
            l "Keep you card close to your chest"
            jump fake
        "Which one?":
            l "Appear less fake"
            jump fake
        "Nah I remember":
            l "Really now."
            jump fake
        "I dream a lot, which dream?":
            l "The real Evie won't say that."
            jump lost

label fake:
    l "Don't slip up like this again."
    l "Next time someone asks you about your dream, say you got a bad headache trying to remember it"
    l "At least pretend to act like Evie, if you slip up, then something bad will happen"
    "You decide to investigate who is giving advice. You turn around suddenly trying to catch them from shock"
    show bg wall
    "You see no one was behind you."
    show bg room with dissolve
    show Bri
    b "Who were you talking to?"
    menu:
        "Lina":
            l "rat me out?"
            jump lost
        "Oh myself":
            b "Oh yeah, I forgot how often you do that!"
            jump endMaths
        "No one. Must have been the wind":
            b "The wind hahaha, you are in a fun mood after solving that maths question"
            jump endMaths

label endMaths:
    t"SHHHH, QUIET DOWN GUYS"
    hide Bri
    show teach
    t "Remember the thing that is happening at lunch"
    "You consider asking Brianna about what will happen at lunch but decide against it, following Lina's tips"
    t "CLASS DISMISSED"
    
label lost:
    scene bg lost
    "You lost"

    # This ends the game.