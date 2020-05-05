# Write your code here
water_current = 400
milk_current =  540
coffee_current = 120
money_current = 550
cups_current = 9

def take():
    global money_current
    print("I gave you ${}".format(money_current))
    money_current = 0


def buy():
    resources = False
    global water_current, milk_current, coffee_current, money_current, cups_current
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if choice == "back":
        return
    choice = int(choice)
    if choice == 1:
        if not(water_current >= 250):
            print("Sorry, not enough water!")
        elif not(coffee_current >= 16):
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            water_current -= 250
            coffee_current -= 16
            money_current += 4
            resources = True
    elif choice == 2:
        if not(water_current >= 350):
            print("Sorry, not enough water!")
        elif not(milk_current >= 75):
            print("Sorry, not enough milk!")
        elif not(coffee_current >= 20):
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            water_current -= 350
            milk_current -= 75
            coffee_current -= 20
            money_current += 7
            resources = True
    else:
        if not(water_current >= 100):
            print("Sorry, not enough water!")
        elif not(milk_current >= 75):
            print("Sorry, not enough milk!")
        elif not(coffee_current >= 12):
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            water_current -= 200
            milk_current -= 100
            coffee_current -= 12
            money_current += 6
            resources = True
    if resources:
        cups_current -= 1


def fill():
    global water_current, milk_current, coffee_current, money_current, cups_current

    water_current += int(input("Write how many ml of water do you want to add:\n"))
    milk_current += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_current += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_current += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def remaining():
    print("The coffee machine has:")
    print(str(water_current) + " of water")
    print(str(milk_current) + " of milk")
    print(str(coffee_current) + " of coffee beans")
    print(str(cups_current) + " of disposable cups")
    print(str(money_current) + " of money")


while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    else:
        break

