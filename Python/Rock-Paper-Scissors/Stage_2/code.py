# Write your code here
import random


def check(player_move_):
    disadvantage = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    moves = ["rock", "paper", "scissors"]

    computer_move = random.choice(moves)
    if disadvantage[player_move_] == computer_move:
        print(f"Sorry, but computer chose {computer_move}")
    elif player_move_ == computer_move:
        print(f"There is a draw ({computer_move})")
    else:
        print(f"Well done. Computer chose {computer_move} and failed")


if __name__ == '__main__':
    player_move = input()
    check(player_move)
