# write your code here
def print_grid(symbols):
    print("-" * 9)
    print(f"""| {symbols[0]} {symbols[1]} {symbols[2]} |
    | {symbols[3]} {symbols[4]} {symbols[5]} |
    | {symbols[6]} {symbols[7]} {symbols[8]} |""")
    print("-" * 9)
if __name__ == "__main__":
    print_grid(input("Enter cells: "))
