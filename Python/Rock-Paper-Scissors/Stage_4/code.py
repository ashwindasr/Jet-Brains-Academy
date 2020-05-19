# Write your code here
# Write your code here
import random


def check_win(player_move_):
    disadvantage = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    moves = ["rock", "paper", "scissors"]

    computer_move = random.choice(moves)
    if disadvantage[player_move_] == computer_move:
        print(f"Sorry, but computer chose {computer_move}")
        return 0
    elif player_move_ == computer_move:
        print(f"There is a draw ({computer_move})")
        return 50
    else:
        print(f"Well done. Computer chose {computer_move} and failed")
        return 100


def check_valid_move(player_move_):
    moves = ["rock", "paper", "scissors"]
    if player_move_ not in moves:
        print("Invalid input")
        return False
    return True


if __name__ == '__main__':
    name = input("Enter your name: ")
    rating = 0
    print(f"Hello, {name}")

    rating_file = open("rating.txt", "r")
    for line in rating_file:
        line_list = line.split()
        if line_list[0] == name:
            rating = int(line_list[1])
    rating_file.close()

    while True:
        input_ = input()
        if input_ == "!exit":
            break
        elif input_ == "!rating":
            print(f"Your rating: {rating}")
        else:
            player_move = input_
            if check_valid_move(player_move):
                rating += check_win(player_move)
