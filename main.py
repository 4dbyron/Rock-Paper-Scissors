#!/usr/bin/env python3

# Task 55: Rock-Paper-Scissors
# Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands,
# representing a rock, a piece of paper, or a pair of scissors.
# By Byron Taaka, For Zuri Training.

import random


def play_rps():
    # 2. Create a list to store all possible options.
    rps_options = ["R", "P", "S"]

    while True:  # handles ties
        # 3. Ask the user to pick an option between "R", "P" or "S"
        user_option = input('What Is Your Move? ("R", "P" or "S"): ').upper()

        # 4. on invalid input, print an error, and ask for input again
        while user_option.upper() not in rps_options:
            print(f"\nError! Got '{user_option}', Yet 'R' or 'P' or 'S' Expected.\n")
            user_option = input('What Is Your Move? ("R", "P" or "S"): ').upper()

        # 5. make a choice for CPU player(computer) Using the `choice` function from the `random` module.
        computer_option = random.choice(rps_options)

        # 6. using a dictionary to avoid "Player: CPU:" print repetition in if-elif-else statements.
        rps_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        print(f"Player ({rps_dict[user_option]}) : CPU ({rps_dict[computer_option]})")

        # concat player choices into a two-characters string easy checking
        moves = f"{user_option}{computer_option}"

        # 7 Check Player Moves
        if moves in ["RR", "PP", "SS"]:  # play again (loop) if a tie
            print("You Tied!\n")
        elif moves in ["RS", "PR", "SP"]:  # Player Wins With Any of these 3 options
            print("You Win!")
            break
        else:   # the CPU wins Otherwise. No Need for elif here. (since player didn't win & it is not a tie)
            print("CPU Wins!")
            break


# Execution Entry Point
if __name__ == '__main__':
    print("******* Rock Paper Scissors (RPS) Game *******")
    play_rps()
