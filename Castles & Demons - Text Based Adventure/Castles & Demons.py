print(r'''
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
''')

print("Welcome to Castles & Demons")
print("Your mission is to find and defeat the Wizard that resides in the castle")

room = "outside"
lives = 1
coin = 0
correct_answer = 0

# Variables to track if descriptions have already been shown
outside_visited = False
castle_entrance_visited = False
main_hall_visited = False
dungeon_visited =  False
study_visited = False
secret_room_visited = False
wizards_room_visited = False

# Creature & Item Variables
dragon_dead = False
keyhole_found = False

while True:
    if room == "outside":
        if not outside_visited:
            print("You stand outside a large intimidating castle. There is a gate with the drawbridge lowered and the doors to the castle are open wide.")
            outside_visited = True
        choice = input("What would you like to do? ")

        if choice == "equipment":
            print("You carry a sword and a heavy shield. You wear metal armor embellished with a symbol of your house. You carry nothing else.")
        elif choice == "walk to castle":
            room = "castle entrance"
        elif choice == "walk around castle":
            print("You observe the castle from all angles and find a secret entrance into the dungeon.")
            room = "dungeon"
        else:
            print("Invalid choice. Please try again.")

    elif room == "castle entrance":
        if not castle_entrance_visited:
            print("As you approach, you see two guards standing to attention. They seem to have noticed you.")
            castle_entrance_visited = True
        choice = input("What would you like to do? ")

        if choice == "attack guards":
            print("You attack the guards but are quickly overpowered. You die.")
            break
        elif choice == "sneak past guards":
            print("They cut you down as you attempt to sneak past. What were you thinking?")
            break
        elif choice == "charm guards":
            print("The guards are wooed by your charm and grace, allowing you to pass.")
            room = "main hall"
        elif choice == "intimidate guards":
            print("You pull your sword and threaten to slice the guards' throats where they stand. They run for the hills, tails between their legs.")
            room = "main hall"
        else:
            print("Invalid choice. Please try again.")

    elif room == "main hall":
        if not main_hall_visited:
            print("Stepping through, you enter a large main hall. Food sits at a banquet table before you. A winding staircase to your left will let you go up or down.")
            main_hall_visited = True
        choice = input("What would you like to do? ")

        if choice == "go upstairs":
            print("You head up the winding staircase. Floor after floor passes you until you reach the top.")
            print("You enter into what looks like a study.")
            room = "study"
        elif choice == "go downstairs":
            print("You head down the winding staircase. It isn't long before you reach a dark room. It is damp and cold.")
            room = "dungeon"
        elif choice == "eat food":
            print("You begin to stuff your face full of food. You feel full and ready for a fight.")
            print("You gain +1 life!")
            lives += 1
        else:
            print("Invalid choice. Please try again.")

    elif room == "dungeon":
        if not dungeon_visited:
            print("It is cold and wet in this dark dungeon room, you hear the sound of heavy breathing as you grasp around in the darkness")
            dungeon_visited = True
        choice = input("What would you like to do? ")

        if choice == "go upstairs":
            print("You rush out of the dungeon, into the main hall once again")
            room = "main hall"
        elif choice == "light torch":
            print("You light a torch as light illuminates the area. You see curled up in the centre of the room. A large scaled beast, with a black and slimy exterior.")
            print("This thing was once a dragon but no longer, corrupted by the demonic powers of this castle")
        elif choice == "throw torch at dragon":
            print("You watch as the oiled skin bursts into flames as you throw your torch upon the creature, with a horrific scream it falls dead.")
            dragon_dead = True
        elif choice == "attack dragon":
            if lives >= 2:
                print("The dragon claws you badly as you slash at it wildly in the bursts of light that come from the torch.")
                print("You feel blood dripping from you, but you push forward, piercing the dragons hide as it falls dead")
                dragon_dead = True
                lives -= 1
            else:
                print("You fight the dragon bravely but as dashes forward it bites you, tearing you arm from its socket. You fall to floor your own blood pooling around you")
                print("You are dead")
                exit()
        elif choice == "search dragon":
            if dragon_dead:
                print("You find a large red crystal embedded in its chest, a worthy prize")
                coin += 100
            else:
                print("The dragon tears you to pieces. You are dead.")
                exit()
        elif choice == "search dungeon":
            if dragon_dead:
                print("You search the remainder of the dungeon, finding a horde of gold!")
                coin += 100
            else:
                print("You begin to search around the dungeon, as you do something from the darkness jumps out and tears you limb from limb")
                print("You are dead")
                exit()
        else:
            print("Invalid choice. Please try again.")

    elif room == "study":
        if not study_visited:
            print("You enter a large study, bookcases full of books line the walls, as well as a desk near the centre of the room, and a chest against a large stained glass window")
            study_visited = True
        choice = input("What would you like to do? ")

        if choice == "look at stained glass window":
            print("You study the stained glass, which seems to depict a robed figure commanding a horde of undead")
        elif choice == "search desk":
            print("The desk is locked")
        elif choice == "lockpick desk":
            print("You attempt to lockpick the desk but it is far beyond your skill level")
        elif choice == "smash lock":
            print("You smash the desk lock and open it up. Inside is a golden key. You pick it up.")
        elif choice == "search bookcases":
            print("You find a number of curious books, but as you search inside one of the bookcases is a golden keyhole")
            keyhole_found = True
        elif choice == "put key in keyhole":
            if keyhole_found:
                print("You turn the golden key in the keyhole and hear a satisfying click, as the bookcase swings open")
                room = "secret room"
            else:
                print("What keyhole?")
        elif choice == "search chest":
            print("You throw open the chest and find a collection of valuables!")
            coin += 50
        elif choice == "go downstairs":
            print("You head back downstairs to the main hall")
            room = "main hall"
        else:
            print("Invalid choice. Please try again.")


    elif room == "secret room":
        if not secret_room_visited:
            print("You enter through the secret door in the bookcase, head down a corridor lit with rows of torches.")
            print("At the end of the corridor is a wooden door.")
            print("The door speaks to you.")
            print("Three Riddles, Three Riddles, I speak to thee. Answer two correctly and you shall pass.")
            print("Answer incorrectly and this will be your last.")
            print("Riddle One: What is light as a feather, but becomes harder to keep the longer you hold it?")
            secret_room_visited = True

# Question 1
            answer = input("")
            if answer == "breath":
                correct_answer += 1
                print("Well done well done.")
            else:
                print("Better luck next time.")

# Question 2
        print("Now for the next riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?")
        answer = input("")
        if answer == "candle":
            correct_answer += 1
            if correct_answer == 2:
                print("Correct again, well done. Do you wish for one more riddle?")
                answer_continue = input("")
                if answer_continue == "yes":
                    print("What can you catch but never throw?")
                    answer = input("")
                    if answer == "a cold":
                        print("Well done well done! Now enter forthwith.")
                        room = "wizards_room"
                else:
                    print("Very well, continue on.")
                    room = "wizards_room"

# Question 3
        else:
            print("Better luck next time.")
            print("Now for the final riddle: What can you catch but never throw?")
            answer = input("")
            if answer == "a cold":
                print("Well done well done! Now enter forthwith.")
                room = "wizards_room"
            else:
                print("A shame you had such potential.")
                print("You are dead")
                exit()


    elif room == "wizards_room":
        if not wizards_room_visited:
            print("You enter a large circular room, in the centre of the room a robed man stands")
            print("The robed man speaks: So your finally here I see")
            print("To strike me down")
            print("A FOOL YOU ARE")
            print("The robed wizards begins to hurl a spell in your direction")
            wizards_room_visited = True


        choice = input("What would you like to do? ")
        if choice == "dodge out of the way":
            print("You dodge out of the way of the Wizards fireball as it barely scorches your back.")
            choice = input("What now? ")
            if choice == "attack the wizard":
                print("You rush forward at the wizard, slicing through him with ease.")
                print("The wizard falls to the ground. Dead. An evil has been defeated you should be proud")
                room = "victory"
        elif choice == "dodge the spell":
            print("You dodge out of the way of the Wizards fireball as it barely scorches your back.")
            choice = input("What now? ")
            if choice == "attack the wizard":
                print("You rush forward at the wizard, slicing through him with ease.")
                print("The wizard falls to the ground. Dead. An evil has been defeated you should be proud")
                room = "victory"
        elif lives >= 2:
            print("You barely escape the fireball! You lose a life as you're badly hurt.")
            choice = input("What now? ")
            if choice == "attack the wizard":
                print("You rush forward at the wizard, slicing through him with ease.")
                print("The wizard falls to the ground. Dead. An evil has been defeated you should be proud")
                room = "victory"
            elif choice == "attack wizard":
                print("You rush forward at the wizard, slicing through him with ease.")
                print("The wizard falls to the ground. Dead. An evil has been defeated you should be proud")
                room = "victory"
        else:
            print("Your attempts fail, as the wizard hurls another fireball in your direction.")
            print("You are turned to ash. You are dead.")
            exit()

    elif room == "victory":
        print("CONGRATULATION YOU'VE WON")
        print("You defeated the wizard and earned an extra 100 gold as a reward.")
        coin += 100
        print(f"Your total gold is {coin} gold")
        print("Thank you for playing!")
        exit()