from random import randint


def dice_roller():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print("You'r roll was " + str(dice1) + " and " + str(dice2))
    retry_question = input("Do you wish to try again? ( yes/no ) ").lower()
    if retry_question == "yes":
        dice_roller()
    elif retry_question == 'no':
        print("Thanks for using my small script it means a lot to me ^^")


dice_roller()
