#!/usr/bin/env python3

# Task 55: Rock-Paper-Scissors
import random


def play_rps():
    # Create a list to store all possible options
    rps_options = ["R", "P", "S"]

    # Ask the user to pick an option between "R", "P" or "S"
    user_option = input("What Is Your Move? (R,P,S): ").upper()

    # make a choice for CPU player(computer) Using the `choice` function from the inbuilt `random` module.
    computer_option = random.choice(rps_options)

    if user_option in rps_options:
        # using a dict to avoid "Player: CPU:" print repetition (no if-elif-else needed)
        rps_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        print(f"Player ({rps_dict[user_option]}) : CPU ({rps_dict[user_option]})")

        # concat player choices into a two-characters string easy checking
        moves = f"{user_option}{computer_option}"

        if moves in ["RR", "PP", "SS"]:  # play again if a tie
            print("You Tied!")
            play_rps()
        elif moves in ["RS", "PR", "SP"]:
            print("You Win Wins!")
        else:
            print("CPU Wins!")
    else:
        print(f"\nError! Got '{user_option}', Yet 'R' or 'P' or 'S' Expected.\n")
        play_rps()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("******* Rock Paper Scissors (RPS) Game *******")
    play_rps()
