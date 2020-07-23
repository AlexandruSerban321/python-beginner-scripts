from string import ascii_letters, punctuation, digits
from random import choice


def password_generatore():
    characters = ascii_letters + punctuation + digits
    try:
        password_range = int(
            input("How long do you wish you password to be ( 8-16 recomandet )? "))
        password = "".join(choice(characters) for x in range(password_range))+'\n'
        save_password = open('passwords.txt', 'a+')
        save_password.write(password)
        save_password.close()
        print(password)
        replay = input("Do you wish to try again? y/n ").lower()
        if replay[0] == "y":
            password_generatore()
        else:
            print("Thanks for using my small script it means a lot to me ^^")
    except ValueError:
        print("Please enter a number not a letter or punctuation try again. ")
        password_generatore()


password_generatore()
