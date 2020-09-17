from random import shuffle


def enigma():
    try:
        digits = list(range(10))
        shuffle(digits)
        digit_list = digits[:3]
        while not len(digit_list) == 0:
            user_guess = int(
                input("Chose a number and see if it's in the list: "))
            if user_guess == digit_list[0]:
                digit_list.remove(user_guess)
                print("Well done you guest a number in the list go ahed and see if you can find " +
                      str(len(digit_list)) + " unknowns left")
            elif user_guess > digit_list[0]:
                print("Try aiming a bit lower")
            elif user_guess < digit_list[0]:
                print("Try aiming a bit higher")
        print("Well done you got\' em all")
        replay = input("Wanna play again ( yes/no ) ?: ").lower()
        if replay == "yes":
            enigma()
        elif replay == 'no':
            print("Thanks for playing")
            exit()
        while not replay == 'yes' or replay == 'no':
            replay = input("Please answer with 'yes' or 'no': ")
            if replay == "yes":
                enigma()
            elif replay == 'no':
                print("Thanks for playing")
                exit()
    except ValueError:
        print("Please enter only numbers otherwise you will restart the game")
        enigma()
    except KeyboardInterrupt:
        print("\n Thanks for playing")


enigma()
