print "Hello, unknown traveler."
print "Enter your name:"
name = raw_input("-->")
print """
You find yourself in a challenging situation.
You have to choose between 1, 2 or 3.
Choose wisely.
You will never know what happens. Or if you'll come out alive.
"""

decision = raw_input("-->")

if decision == "1":
    print "You have chosen well! You find yourself in a nice looking forest!"
    print "Now you face another big decision, which can end, or start you life."
    print "You see light between the trees and surely that direction leads out of the forest. It says on there: '%s go this way.'" %name
    print "In the other direction is a sign, which points directly in the darker part of the forest."
    print "Press Enter for following the light out of the forest and probably going back home."
    print "Or write: I am fearless, if you are ready for the adventure of your lifetime."
    forest = raw_input("-->")

    if forest == "I am fearless":
        print "You follow the sign and come to the abandoned ruins of a long lost castle."
        print """
        Of course you are curious and can't go around looking into the castle.
        When you are standing in the large forecourt, a cold draft of air goes around you.
        You shiver a little bit and begin to feel like you are not alone.
        Have you always wanted to go on a ghost hunt? Then write 'Yes'.
        If not and you would like to leave the castle, write 'No'. """

        ghost_hunt = raw_input("-->")
        if ghost_hunt == "Yes":
            print "You are one brave fellow. For your misfortune, the ghost you are searching for, is black-hearted."
            print "It is eating you with hair and bone."
            print "You poor creature. Maybe you want to start over?"
            print "On your tomb stone will stand:'Here lies %s, the hero of a whole generation.'" %name
            exit()

        if ghost_hunt == "No":
            print "That is much better young fellow! You just got away from the black-hearted spirit of the former king."
            print "Anyways. You live and can continue your life in happiness."
            print "You go home to your loved ones without a scratch."
            exit()

        else:
            print "You are not ready for this adventure. Go to Mama."
            exit()

if decision == "2":
    print "There is a huge city. You have never seen something so futuristic."
    print "It is night and you have to choose again."
    print "You can either follow the empty, long street that lays before you and is lit with gloomy lights."
    print "Or you can enter the next buiding, which seems to be in the style of former times."
    print "For the streets enter: 1 and for the hotel enter 2 ."

    City = raw_input("-->")
    if City == "1":
        print "You wander along the streets. When you stop, to watch the moon, somebody is approaching you."
        print "The man is looking very old and poor. You have a bad feeling about him."
        print "In the next moment he has his gun out and you are dead. You poor fellow. He gets all your things and leaves you like that."
        exit()

    if City == "2":
        print "The hotel you enter is full of people and you directly feel warmer."
        print "After you stood in the hall for some minutes, an old lady approaches you."
        print "She ask you to follow her. She says she is a fortune teller: '%s , I know your future and your end. You have to listen to me.'" %name
        print "How does she know your name?"
        print "Enter 'Yes', to follow her and 'No', to leave for the bar."

        fortune_teller = raw_input("-->")
        if fortune_teller == "Yes":
            print "She leads you in a small, dark room full of crystal balls."
            print "With another look to you, she says to you: 'You will die tonight.'"
            print "You directly want her to tell you when and why. She reaches for your hand to read in it."
            print "As soon as she touches it, it gets black. The blackness spreads in your whole body and you die. "
            print "You should have known she is a soul eater. You will never see your home again."
            exit()
        if fortune_teller == "No":
            print "You go to the bar and take a Martini. Shaken, not stirred. It is the best one in you life."
            print "After you pay the bartender, you go home. You will tell everyone, that you met James Bond."
            print "He is today a bartender and works in a strange hotel and mixes nothing else than Martinis. Shaken, not stirred."
            exit()
    else:
        print "You are not ready for this adventure. Go home to Mama."
        exit()

if decision == "3":
    print """
    With a small explosion, you enter a library. It has books up until the ceiling.
    They are all looking so unique and old and interesting, like no other book you have seen before.
    In between the shelves, you also see a black, dark, small door. It has a sign on it:
    Do not open. You will pay with your life.
    Decide: Take out one random book or enter the door.
    Enter: Book or Door.
    """
    Library = raw_input("-->")

    if Library == "Book":
        print "The book opens itself when you open it. You get a small glance at the text, but then a whirl grabs you and drags you into the book."
        print "Poor %s. You never knew what was coming. That  books can kill."%name
        print "Start over or don't. Your choice."
        exit()

    if Library == "Door":
        print "Like the door said. You better should have not entered."
        print "In the small room, you can't see anything but a flame in the back."
        print "When you turn you smartphone flashlight on, you see the big, frightening dragon in the back."
        print "It breathes fire out of its nostrils. When it sees you, it gets up and the last thing you see, is a huge fireball coming right at you."
        print "Then you lie at the floor. Dead."
        print "The dragon whispers: 'Poor %s. We all knew, he wasn't ready for this adventure yet.'" %name
        exit()

else:
    print "You are not brave enough. You are going home."
    print "Or start over again."
    exit()
