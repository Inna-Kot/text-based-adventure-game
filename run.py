def welcome():
    print("""The shipwreck was sudden and violent. You woke up on the shore
of a deserted island, surrounded by the wreckage. As you stood, aching and
disoriented, you heard angry shouts. A group of indigenous people emerged from
the jungle, running towards you with alarming speed. You had to decide quickly:
[run] into the forest to hide or [dive] back to the ship's remains on the
beach to find a weapon. Time was running out, and your fate depended
on your next move.
[run] or [dive] ?""")
    option = input("\n")
    if option == 'dive':
        remains()
    elif option == 'run':
        forest()
    else:
        invalidoption()
        welcome()


def remains():
    print("""In the wreckage of the ship, there were no weapons, only debris.
The indigenous people quickly caught up to you, and you were captured and
consumed. This is where your story ends.""")
    option = input("Would you like to play again? [yes]/[no]\n")
    if option == 'yes':
        welcome()
    else:
        print("Thanks for playing!")


def forest():
    print("""You run as the indigenous people chase after you, hurling spears.
Branches scratch your face, and your heart pounds wildly in your chest.
You dive into a ravine, hiding among the bushes. Fortune smiles upon you -
the indigenous people rush past, not noticing your hiding spot. You take
a moment to catch your breath, looking around and contemplating your next
move. Should you go [back] to search for any survivors, or should you
investigate and [enter] the ruined structure that looms in the distance?
[back] or [enter]""")
    option = input()
    if option == 'back':
        returnback()
    elif option == 'enter':
        enterit()
    else:
        invalidoption()
        forest()


def returnback():
    print("""You returned to the beach in search of survivors,
but you failed to notice the lion stalking you. In the end,
you were caught and eaten.""")
    option = input("Would you like to play again? [yes]/[no]\n")
    if option == 'yes':
        welcome()
    elif:
        print("Thanks for playing!")
    else:
        invalidoption()
        returnback()

def enterit():
    print("""You stumble upon a native islander, and you are faced with
a choice: rush in and engage in a [fight] or [throw] a rock at him from
a distance. What is your choise? [fight] or [throw]""")
    option = input()
    if option == 'throw':
        throwstone()
    elif option == 'fight':
        fight()
    else:
        invalidoption()
        enterit()

def fight():
    print("""You charged into the fight, but without the necessary skills,
you were easily defeated and killed. Your story ended here.""")
    option = input("Would you like to play again? [yes]/[no]\n")
    if option == 'yes':
        welcome()
    else:
        print("Thanks for playing!")


def invalidoption():
    print("You entered an invalid option, please try again.")


welcome()
