from random import randint


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    script_choice = str(choices[randint(0, 2)])
    user_choice = str(input(
        "Chose one of three : rock(r), paper(p), scissors(s) ")).lower()
    # Tie resolution
    if user_choice[0] == script_choice[0]:
        if user_choice[0] == 'r':
            print("It's a tie you bouth chose rock")
        elif user_choice[0] == 'p':
            print("It's a tie you bouth chose paper")
        else:
            print("It's a tie you bouth chose scissors")
    # User rock choice resolution
    elif user_choice[0] == "r" and script_choice[0] == "p":
        print("Paper beats rock you've lost")
    elif user_choice[0] == "r" and script_choice[0] == "s":
        print("Rock beats scissors you've won")
    # User scissors choice resolution
    elif user_choice[0] == "s" and script_choice[0] == "r":
        print("Rock beats scissors you've lost")
    elif user_choice[0] == "s" and script_choice[0] == "p":
        print("Scissors beats paper you've won")
    # User paper choice resolution
    elif user_choice[0] == "p" and script_choice[0] == "r":
        print("Paper beats rock you've won")
    elif user_choice[0] == "p" and script_choice[0] == "s":
        print("Scissors beat paper you've lost")
    else:
        rock_paper_scissors()
    # Replay
    replay = input("Wanna play again ( y/n ) ? ").lower()
    if replay[0] == "y":
        rock_paper_scissors()
    else:
        print("Thanks for playing")


rock_paper_scissors()
