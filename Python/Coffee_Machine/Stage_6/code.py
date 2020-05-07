# Write your code here
class CoffeeMachine:
    water_current = 400
    milk_current = 540
    coffee_current = 120
    money_current = 550
    cups_current = 9
    state = None
    fill_state = "water"

    def __init__(self):
        print("Write action (buy, fill, take, remaining, exit):\n")

    def console(self, input_):
        if CoffeeMachine.state is None:
            CoffeeMachine.state = "choosing a state"
            if input_ == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
                CoffeeMachine.state = "choosing a coffee"
            elif input_ == "fill":
                print("Write how many ml of {CoffeeMachine.fill_state} do you want to add:\n")
                CoffeeMachine.state = "fill"
            elif input_ == "take":
                self.take()
                CoffeeMachine.state = None
                print("Write action (buy, fill, take, remaining, exit):\n")
            elif input_ == "remaining":
                self.remaining()
                CoffeeMachine.state = None
                print("Write action (buy, fill, take, remaining, exit):\n")
            else:
                return True

        elif CoffeeMachine.state == "choosing a coffee":
            self.buy(input_)
            CoffeeMachine.state = None
            print("Write action (buy, fill, take, remaining, exit):\n")
        elif CoffeeMachine.state == "fill":
            if CoffeeMachine.fill_state == "water":
                self.fill("water", input_)
                CoffeeMachine.fill_state = "milk"
                print("Write how many ml of {CoffeeMachine.fill_state} do you want to add:\n")
            elif CoffeeMachine.fill_state == "milk":
                self.fill("milk", input_)
                CoffeeMachine.fill_state = "coffee beans"
                print("Write how many grams of {CoffeeMachine.fill_state} do you want to add:\n")
            elif CoffeeMachine.fill_state == "coffee beans":
                self.fill("coffee beans", input_)
                CoffeeMachine.fill_state = "cups"
                print("Write how many disposable cups of coffee do you want to add:\n")
            else:
                self.fill("cups", input_)
                CoffeeMachine.fill_state = "water"
                CoffeeMachine.state = None

    def take(self):
        print("I gave you ${}".format(self.money_current))
        CoffeeMachine.money_current = 0

    def buy(self, choice):
        resources = False
        if choice == "back":
            return
        choice = int(choice)
        if choice == 1:
            if not (CoffeeMachine.water_current >= 250):
                print("Sorry, not enough water!")
            elif not (CoffeeMachine.coffee_current >= 16):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water_current -= 250
                CoffeeMachine.coffee_current -= 16
                CoffeeMachine.money_current += 4
                resources = True
        elif choice == 2:
            if not (CoffeeMachine.water_current >= 350):
                print("Sorry, not enough water!")
            elif not (CoffeeMachine.milk_current >= 75):
                print("Sorry, not enough milk!")
            elif not (CoffeeMachine.coffee_current >= 20):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water_current -= 350
                CoffeeMachine.milk_current -= 75
                CoffeeMachine.coffee_current -= 20
                CoffeeMachine.money_current += 7
                resources = True
        else:
            if not (CoffeeMachine.water_current >= 100):
                print("Sorry, not enough water!")
            elif not (CoffeeMachine.milk_current >= 75):
                print("Sorry, not enough milk!")
            elif not (CoffeeMachine.coffee_current >= 12):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                CoffeeMachine.water_current -= 200
                CoffeeMachine.milk_current -= 100
                CoffeeMachine.coffee_current -= 12
                CoffeeMachine.money_current += 6
                resources = True
        if resources:
            CoffeeMachine.cups_current -= 1

    def fill(self, type_, input_):
        input_ = int(input_)

        if type_ == "water":
            CoffeeMachine.water_current += input_
        elif type_ == "milk":
            CoffeeMachine.milk_current += input_
        elif type_ == "coffee beans":
            CoffeeMachine.coffee_current += input_
        else:
            CoffeeMachine.cups_current += input_

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water_current) + " of water")
        print(str(self.milk_current) + " of milk")
        print(str(self.coffee_current) + " of coffee beans")
        print(str(self.cups_current) + " of disposable cups")
        print("$" + str(self.money_current) + " of money")


machine = CoffeeMachine()
while True:
    input_ = input()
    if machine.console(input_):
        break
