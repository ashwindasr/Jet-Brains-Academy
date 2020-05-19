# Write your code here
import random


def check_custom_win(player_move_, moves):
    computer_move = random.choice(moves)
    if computer_move == player_move:
        print(f"There is a draw ({computer_move})")
        return 50
    else:
        player_move_index = moves.index(player_move)
        custom_move_list = moves[player_move_index + 1:] + moves[:player_move_index]
        computer_move_index = custom_move_list.index(computer_move)
        if computer_move_index + 1 <= len(custom_move_list) // 2:
            print(f"Sorry, but computer chose {computer_move}")
            return 0
        else:
            print(f"Well done. Computer chose {computer_move} and failed")
            return 100


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


def check_valid_move(player_move_, moves=("rock", "paper", "scissors")):
    if player_move_ not in moves:
        print("Invalid input")
        return False
    return True


if __name__ == '__main__':
    name = input("Enter your name: ")
    rating = 0
    print(f"Hello, {name}")

    all_moves = input().split(",")
    print("Okay, let's start")

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

            if all_moves == ['']:
                if check_valid_move(player_move):
                    rating += check_win(player_move)
            else:
                if check_valid_move(player_move, all_moves):
                    rating += check_custom_win(player_move, all_moves)

