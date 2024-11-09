def welcome():
    print("""The shipwreck was sudden and violent. You woke up on the shore
of a deserted island, surrounded by the wreckage. As you stood, aching and
disoriented, you heard angry shouts. A group of indigenous people emerged from
the jungle, running towards you with alarming speed. You had to decide quickly:
[run] into the forest to hide or [dive] back to the ship's remains on the
beach to find a weapon. Time was running out, and your fate depended
on your next move.""")
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
The indigenous people quickly caught up to you, and you were captured and consumed.
This is where your story ends.""")
    option = input("Would you like to play again? [yes]/[no]\n")
    if option == 'yes':
        welcome()
    else:
        print("Thanks for playing!")


def invalidoption():
    print("You entered an invalid option, please try again.")


welcome()
