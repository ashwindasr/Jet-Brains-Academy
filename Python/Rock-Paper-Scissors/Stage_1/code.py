# Write your code here
def unfair_version(player_move_):
    disadvantage = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    print(f"Sorry, but computer chose {disadvantage[player_move_]}")


if __name__ == '__main__':
    player_move = input()
    unfair_version(player_move)
