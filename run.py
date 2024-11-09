def welcome():
    print("""The shipwreck was sudden and violent. You woke up on the shore
of a deserted island, surrounded by the wreckage. As you stood, aching and
disoriented, you heard angry shouts. A group of indigenous people emerged from
the jungle, running towards you with alarming speed. You had to decide quickly:
[run] into the forest to hide or [dive] back to the ship's remains on the
beach to find a weapon. Time was running out, and your fate depended
on your next move.
[run] or [dive] ?""")
    option = input(">>>\n")
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
move. Should you go [back] to search for any survivors, or should you investigate
and [enter] the ruined structure that looms in the distance?
[back] or [enter]""")
    option = input()
    if option == 'back':
        returnback()
    elif option == 'enter':
        enterit()
    else:
        invalidoption()
        forest()


def invalidoption():
    print("You entered an invalid option, please try again.")


welcome()
