from random import randint


def dice_roller():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print("You'r roll was " + str(dice1) + " and " + str(dice2))
    retry_question = input("Do you wish to try again? ( y/n ) ").lower()
    if retry_question[0] == "y":
        dice_roller()

    else:
        print("Thanks for using my small script it means a lot to me ^^")


dice_roller()
