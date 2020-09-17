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
            elif user_guess < number_chosen:
                print("Aim a bit higher")
            else:
                print("Aim a bit lower")
        replay = input("Do you wish to play again? ( y/n ) ").lower()
        if replay[0] == "y":
            guess_the_number()
        else:
            print("Thanks for using my script it means a lot to me ^^")
    except ValueError:
        print("Please enter a valid number")
        guess_the_number()
    except KeyboardInterrupt:
        print("\n Thanks for playing")

guess_the_number()
