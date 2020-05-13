# write your code here
def print_grid(symbols):
    print("-" * 9)
    print(
        f"""| {symbols[0]} {symbols[1]} {symbols[2]} |\n| {symbols[3]} {symbols[4]} {symbols[5]} |\n| {symbols[6]} {symbols[7]} {symbols[8]} |""")
    print("-" * 9)


def create_grid(string):
    counter = 0
    game = []
    for outer_loop in range(3):
        temp = []
        for inner_loop in range(3):
            temp.append(string[counter])
            counter += 1
        game.append(temp)
    return game


def win(check_grid, symbol):
    # Checking leading diagonal
    flag = True
    for i in range(3):
        if check_grid[i][i] != symbol:
            flag = False
    if flag:
        return True

    # Checking non-leading diagonal
    flag = True
    for i in range(3):
        if check_grid[i][2 - i] != symbol:
            flag = False
    if flag:
        return True

    # Checking rows
    flag = False
    for i in range(3):
        inner_flag = True
        for j in range(3):
            if check_grid[i][j] != symbol:
                inner_flag = False
        if inner_flag:
            return True

    # Checking columns
    flag = False
    for i in range(3):
        inner_flag = True
        for j in range(3):
            if check_grid[j][i] != symbol:
                inner_flag = False
        if inner_flag:
            return True


def not_finished(check_grid):
    for i in check_grid:
        for j in i:
            if j == '_':
                return True
    return False

def count(check_grid, symbol):
    counter = 0
    for i in check_grid:
        for j in i:
            if j == symbol:
                counter += 1
    return counter


if __name__ == "__main__":
    input_ = input()
    grid = create_grid(input_)
    print_grid(input_)

    if (win(grid, 'X') and win(grid, 'O')) or (abs(count(grid, 'X') - count(grid, 'O')) >= 2):
        print("Impossible")
    elif win(grid, 'X'):
        print("X wins")
    elif win(grid, 'O'):
        print("O wins")
    elif not_finished(grid):
        print("Game not finished")
    elif not(win(grid, 'X') or win(grid, 'O')):
        print("Draw")

