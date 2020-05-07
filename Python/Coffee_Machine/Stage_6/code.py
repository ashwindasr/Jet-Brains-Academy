# Write your code here
class CoffeeMachine:

    def __init__(self, water_current, milk_current, coffee_current, money_current, cups_current):
        self.water_current = int(water_current)
        self.milk_current = milk_current
        self.coffee_current = coffee_current
        self.money_current = money_current
        self.cups_current = cups_current
        self.state = None
        self.fill_state = "water"
        
        print("Write action (buy, fill, take, remaining, exit):\n")

    def console(self, input_):
        if self.state is None:
            self.state = "choosing a state"
            if input_ == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
                self.state = "choosing a coffee"
            elif input_ == "fill":
                print("Write how many ml of {CoffeeMachine.fill_state} do you want to add:\n")
                self.state = "fill"
            elif input_ == "take":
                self.take()
                self.state = None
                print("Write action (buy, fill, take, remaining, exit):\n")
            elif input_ == "remaining":
                self.remaining()
                self.state = None
                print("Write action (buy, fill, take, remaining, exit):\n")
            else:
                return True

        elif self.state == "choosing a coffee":
            self.buy(input_)
            self.state = None
            print("Write action (buy, fill, take, remaining, exit):\n")
        elif self.state == "fill":
            if self.fill_state == "water":
                self.fill("water", input_)
                self.fill_state = "milk"
                print("Write how many ml of {CoffeeMachine.fill_state} do you want to add:\n")
            elif self.fill_state == "milk":
                self.fill("milk", input_)
                self.fill_state = "coffee beans"
                print("Write how many grams of {CoffeeMachine.fill_state} do you want to add:\n")
            elif self.fill_state == "coffee beans":
                self.fill("coffee beans", input_)
                self.fill_state = "cups"
                print("Write how many disposable cups of coffee do you want to add:\n")
            else:
                self.fill("cups", input_)
                self.fill_state = "water"
                self.state = None

    def take(self):
        print("I gave you ${}".format(self.money_current))
        self.money_current = 0

    def buy(self, choice):
        resources = False
        if choice == "back":
            return
        choice = int(choice)
        if choice == 1:
            if not (self.water_current >= 250):
                print("Sorry, not enough water!")
            elif not (self.coffee_current >= 16):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_current -= 250
                self.coffee_current -= 16
                self.money_current += 4
                resources = True
        elif choice == 2:
            if not (self.water_current >= 350):
                print("Sorry, not enough water!")
            elif not (self.milk_current >= 75):
                print("Sorry, not enough milk!")
            elif not (self.coffee_current >= 20):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_current -= 350
                self.milk_current -= 75
                self.coffee_current -= 20
                self.money_current += 7
                resources = True
        else:
            if not (self.water_current >= 100):
                print("Sorry, not enough water!")
            elif not (self.milk_current >= 75):
                print("Sorry, not enough milk!")
            elif not (self.coffee_current >= 12):
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water_current -= 200
                self.milk_current -= 100
                self.coffee_current -= 12
                self.money_current += 6
                resources = True
        if resources:
            self.cups_current -= 1

    def fill(self, type_, input_):
        input_ = int(input_)

        if type_ == "water":
            self.water_current += input_
        elif type_ == "milk":
            self.milk_current += input_
        elif type_ == "coffee beans":
            self.coffee_current += input_
        else:
            self.cups_current += input_

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water_current) + " of water")
        print(str(self.milk_current) + " of milk")
        print(str(self.coffee_current) + " of coffee beans")
        print(str(self.cups_current) + " of disposable cups")
        print("$" + str(self.money_current) + " of money")


machine = CoffeeMachine(400, 540, 120, 550, 9)
while True:
    input_ = input()
    if machine.console(input_):
        break
