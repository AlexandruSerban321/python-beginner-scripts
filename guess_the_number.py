from random import randint


def guess_the_number():
    try:
        user_range = int(input(
            "What is the range from which a random number will be chosen ? "))
        number_chosen = randint(1, int(user_range))
        user_guess = input("Guess the number? ")
        while not number_chosen == int(user_guess):
            user_guess = int(input("Wrong answer try again "))
            if user_guess == number_chosen:
                print("Well done you've guessed the number!!")
        replay = input("Do you wish to play again? ( y/n ) ").lower()
        if replay[0] == "y":
            guess_the_number()
        else:
            print("Thanks for using my script it means a lot to me ^^")
    except ValueError:
        print("Please enter a number not a letter or punctuation try again. ")
        guess_the_number()

guess_the_number()
