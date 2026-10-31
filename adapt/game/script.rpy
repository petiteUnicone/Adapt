# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Brianna", colour = "#c8ffc8")
define t = Character("Mr Freeman", colour ="#cbc8ff")
define l = Character("Lina", colour= "#ffc8d4")
define p = Character("Miss Patel", colour="#ffdbbb")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg maths with dissolve

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
    hide bri
    show bri at right
    t "Ah I am proud of you, just like I expected"
    show Bri proud
    t "I will leave you guys to it"
    hide teach
    "You let out a sigh after that drilling maths question."
    b "Knew you wouldn't embaress me"
    hide bri
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
    scene bg wall
    "You see no one was behind you."
    scene bg room with dissolve
    show bri
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
    hide bri
    show teach
    t "Remember the thing that is happening at lunch"
    "You consider asking Brianna about what will happen at lunch but decide against it, following Lina's tips"
    t "CLASS DISMISSED"
    b "Lets go"
    "You sit still, still thinking about lunch"
    b "Lets go?"
    "You stand up and enter the hallway"
    scene bg hallway with dissolve
    people around you "HEY EVIE!"
    "You turn to ask Brianna why they all know you, but Lina's warning echoes in your mind"
    b "Hurry up slow coach, only one more lesson till lunch!"
    l "You have Economics"
    "You turn around frantically trying to put a face to Lina but faces blur past as Brianna tugs you along to your seat"
    b "Hey by the way do you remember your dream?"
    menu:
        "Yea!":
            jump econLesson
        "Yea, faintly":
            b "hmmmm"
            jump econLesson
        "Not really":
            jump lost
        "Nope":
            jump lost

label econLesson:
    scene bg econ with dissolve
    show pat at right
    p "So everyone get out your econ  textbooks and turn to page 28"
    b "You do have your book right?"
    "You check your bag and find: a lunch box, pencil case, notebook, textbook, laptop, what do you choose?"
    menu:
        "Lunch Box":
            "Ok big back"
            jump lost
        "Pencil case":
            "Useful"
            jump Textbook
        "Notebook":
            jump Textbook
        "Textbook":
            jump gotTextbook
        "Laptop":
            "Why though?"
            jump lost

label Textbook:
    show bri concern
    b "Are you not going to take out your textbook?"
    menu:
        "Yea, let me take out my Textbook":
            jump gotTextbook
        "I think I forgot it at home":
            b "The real Evie won't do that"
            jump lost
        "What are you going to do about it?":
            b "What would I not do is a better question."
            jump lost
        "Nahh I am fine":
            b "We can share mine"
            jump shareTextbook

label gotTextbook:
    "You flip to page 28 and see that your page is different to the people around you"
    "You consider asking why your page is different, but you remember the warning. Do you make an excuse and share with the Brianna or use your own book?"
    menu:
        "Hey Brianna, my book seems outdated, could i share with you?":
            jump shareTextbook
        "You use your book and try to peek at Brianna's book":
            b "You we can share..."
            menu:
                "Could we share?":
                    jump shareTextbook
                "Nah I am fine":
                    p "You can't be in my lesson if you can't see the textbook"
                    jump loser
        "You don't mind not having a book and proceed":
            p "You can't be in my lesson if you can't see the textbook"
            jump loser

label shareTextbook:
    hide bri
    hide pat
    scene textBook with dissolve
    "You notice doodles around the page and random highlights."
    "Random words are highlighted, you try to read them in order."
    "L.I.N.A. You. Won't. be. able. to. see. her. She. Is. everywhere."
    l "Don't lose your attention in lessons."
    "You turn your attention towards the teacher, but realise she has left the classroom."
    "You consider asking Brianna about Lina, do you?"
    menu:
        "Do you know a Lina?":
            jump infoLina
        "You decide against it, remembering Lina's warning":
            jump readTextbook

label infoLina:
    b "Funny you mention her, yes I do"
    b "Do you want to know about her?"
    menu:
        "Yeah, I don't know much about her":
            b "She was your sister, you liar"
            jump lost
        "Its fine, i was just testing you!":
            b "You silly goose"
            jump readTextbook
        "Yea it feels like she is everywhere":
            show bri caring
            b "She was only your twin, its ok to feel that way"
            jump readTextbook

label readTextbook:
    hide bri 
    "You hear a loud crash and look up"
    scene bg econ with dissolve
    show pat scared at left
    "You see Mr Freeman enter the classroom"
    show teach angry at right
    t "HOW. DARE. YOU."
    p "i am so sorry, i didn't mean it, i am so sorry."
    l "Yeah. She better be."
    t "I will see you at lunch"
    "You see Mr Freeman pick up a chair"
    show teach chair
    b "TURN AROUND EVIE, PUT YOUR HEAD DOWN"
    hide teach
    hide pat
    scene bg head
    b "Stay that way until I tell you."
    "You hear a loud thud, curiosity gets you"
    menu:
        "Look up":
            b "NOOO PUT YOUR HEAD DOWN!"
            jump lost
        "Keep your head down":
            jump endEcon
label endEcon:
    "You hear the door open and slam shut."
    p "class, dismissed."
    b "You can open your eyes now!"
    scene bg econ with dissolve
    b "Lets go to lunch"
    "You remember Lina's warning"
    l "GO, move yourself"
    scene bg hall with dissolve
    "Brianna holds your hand and guides you to a hall and the both of you sit down."
    jump lunch

label lunch:
    show teach at left
    show pat hurt at right
    t "Most of you already know what this assembly is about."
    p "It's about Lina"
    l "I told them not to"
    "You turn around to try find her"
    l "Look in a mirror"
    scene bg mirror with dissolve
    l "This is what I looked like"



label lost:
    scene bg lost
    "You lost"

    # This ends the game.