# Write your code here
import random
import sqlite3
from sqlite3 import Error
 
 
def luhn_algorithm(number: str) -> int:
    number = list(map(int, list(number)))[:15]
    for position, digit in enumerate(number):
        if position % 2 == 0:
            temp = digit * 2
            if temp > 9:
                temp -= 9
            number[position] = temp
    return sum(number)
 
 
def generate_card_number():
    # return '400000' + ''.join([f"{random.randint(0, 9)}" for num in range(0, 10)])
 
    number = '400000' + ''.join([f"{random.randint(0, 9)}" for num in range(0, 9)])
 
    sum_ = luhn_algorithm(number)
 
    if sum_ % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - sum_ % 10
 
    number += str(checksum)
 
    return number
 
 
def generate_pin():
    return ''.join([f"{random.randint(0, 9)}" for num in range(0, 4)])
 
 
def connect_database(database_name):
    conn = None
 
    try:
        conn = sqlite3.connect(f'{database_name}.s3db')
    except Error as e:
        print(e)
 
    return conn
 
 
def initialize_table(conn):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM card;")
    except sqlite3.OperationalError:
        cur.execute(f"""CREATE TABLE card(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);""")
 
 
def add_to_database(cur, conn, card_number, pin):
    try:
        cur.execute(f"""INSERT INTO card (number, pin) VALUES ('{card_number}', '{pin}');""")
        conn.commit()
        print("Added data to database")
 
    except Error:
        print("Query Error")
 
 
def credentials_correct(cur, card_number, pin) -> bool:
    cur.execute(f"SELECT number, pin from card WHERE number = '{card_number}' AND pin = '{pin}'")
    if len(cur.fetchall()) != 0:
        return True
    else:
        return False
 
 
def get_balance(cur, conn, card_number):
    cur.execute(f"SELECT balance from card WHERE number = '{card_number}'")
    return cur.fetchall()[0][0]
 
 
def close_account(cur, conn, card_number):
    try:
        cur.execute(f"DELETE FROM card WHERE number = '{card_number}';")
        conn.commit()
        print("The account has been closed!")
 
    except Error as e:
        print(e)
 
 
def add_income(cur, conn, card_number):
    amount = int(input("Enter income: "))
    cur.execute(f"UPDATE card SET balance = balance + {amount} WHERE number = '{card_number}';")
    conn.commit()
    print("Income was added!")
 
 
def transfer(cur, conn, card_number):
    destination_card = input("Transfer\nEnter card number: ")
 
    cur.execute(f"SELECT number from card WHERE number = '{destination_card}';")
    sum_ = luhn_algorithm(destination_card)
    if (sum_ + int(destination_card[-1])) % 10 != 0:
        print("Probably you made mistake in the card number. Please try again!")
    elif len(cur.fetchall()) == 0:
        print("Such a card does not exist.")
    elif destination_card == card_number:
        print("You can't transfer money to the same account!")
    else:
        amount = int(input("Enter how much money you want to transfer: "))
 
        cur.execute(f"SELECT balance FROM card WHERE number = '{card_number}';")
        current_amount = cur.fetchall()[0][0]
 
        if amount > current_amount:
            print("Not enough money!")
        else:
            cur.execute(f"UPDATE card SET balance = balance - {amount} WHERE number = '{card_number}'")
            conn.commit()
            cur.execute(f"UPDATE card SET balance = {amount} WHERE number = '{destination_card}'")
            conn.commit()
            print("Success!")
 
 
def main():
    conn = connect_database("card")
    initialize_table(conn)
    cur = conn.cursor()
 
    while True:
        cur.execute("select * from card;")
        print(cur.fetchall())
 
        choice = input("""1. Create an account
2. Log into account
0. Exit
""")
 
        if choice == '1':
            # generating credentials
            card_number = generate_card_number()
            pin = generate_pin()
 
            # adding data to database
            add_to_database(cur, conn, card_number, pin)
 
            print(f"""Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin}""")
 
        elif choice == '2':
            card_number = input("Enter your card number:\n")
            pin = input("Enter your pin:\n")
 
            if credentials_correct(cur, card_number, pin):
                print("You have successfully logged in!")
                while True:
                    choice = input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
""")
                    if choice == '1':
                        print("Balance:", get_balance(cur, conn, card_number))
                    elif choice == '2':
                        add_income(cur, conn, card_number)
                    elif choice == '3':
                        transfer(cur, conn, card_number)
                    elif choice == '4':
                        close_account(cur, conn, card_number)
                    elif choice == '5':
                        print("You have successfully logged out!")
                        break
                    elif choice == '0':
                        print("Bye!")
                        return  # to break out of two while loops
            else:
                print("Wrong card number or PIN!")
 
        else:
            print("Bye!")
            break
    conn.close()
 
 
if __name__ == '__main__':
    main()
