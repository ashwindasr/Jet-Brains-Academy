# write your code here


def print_grid(grid_parameter):
    print("-" * 9)
    for row in grid_parameter:
        print(" ".join(["|"] + row + ["|"]))
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


def finished(check_grid):
    for i in check_grid:
        for j in i:
            if j == ' ':
                return False
    return True


def count(check_grid, symbol):
    counter = 0
    for i in check_grid:
        for j in i:
            if j == symbol:
                counter += 1
    return counter


def check_coordinates():
    check = False
    while not check:
        coordinates_parameter = input("Enter the coordinates: ").split()

        try:
            coordinates_parameter = list(map(int, coordinates_parameter))
        except ValueError:
            print("You should enter numbers!")
            continue
        if not ((1 <= coordinates_parameter[0] <= 3) and (1 <= coordinates_parameter[1] <= 3)):
            print("Coordinates should be from 1 to 3!")
            continue
        check = True

    if check:
        return coordinates_parameter


def not_occupied(coordinates_parameter, grid_parameter):
    column = coordinates_parameter[0]
    row = coordinates_parameter[1]

    if grid_parameter[3 - row][column - 1] != " ":
        return False
    return True


def place(coordinates_parameter, grid_parameter, symbol):
    column = coordinates_parameter[0]
    row = coordinates_parameter[1]

    grid_parameter[3 - row][column - 1] = symbol
    return grid_parameter


if __name__ == "__main__":
    grid = create_grid("         ")
    print_grid(grid)
    current_symbol = 'X'

    while True:
        coordinates = check_coordinates()
        while not not_occupied(coordinates, grid):
            print("This cell is occupied! Choose another one!")
            coordinates = check_coordinates()

        grid = place(coordinates, grid, current_symbol)
        current_symbol = 'X' if current_symbol == 'O' else 'O'
        print_grid(grid)

        if win(grid, 'X'):
            print("X wins")
            break
        if win(grid, 'O'):
            print("O wins")
            break
        if finished(grid) and not(win(grid, 'X') or win(grid, 'O')):
            print("Draw")
            break
