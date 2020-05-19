# Write your code here
import random


def check_win(player_move_):
    disadvantage = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    moves = ["rock", "paper", "scissors"]

    computer_move = random.choice(moves)
    if disadvantage[player_move_] == computer_move:
        print(f"Sorry, but computer chose {computer_move}")
    elif player_move_ == computer_move:
        print(f"There is a draw ({computer_move})")
    else:
        print(f"Well done. Computer chose {computer_move} and failed")


def check_valid_move(player_move_):
    moves = ["rock", "paper", "scissors"]
    if player_move_ not in moves:
        print("Invalid input")
        return False
    return True


if __name__ == '__main__':
    while True:
        input_ = input()
        if input_ == "!exit":
            break
        player_move = input_
        if check_valid_move(player_move):
            check_win(player_move)
