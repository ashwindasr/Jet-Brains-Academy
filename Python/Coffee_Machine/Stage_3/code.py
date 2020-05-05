# Write your code here
water_capacity = int(input("Write how many ml of water the coffee machine has: "))
milk_capacity = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans_capacity = int(input("Write how many grams of coffee beans the coffee machine has: "))

cups_of_coffee = int(input("Write how many cups of coffee you will need: "))
water = 200 * cups_of_coffee
milk = 50 * cups_of_coffee
coffee_beans = 15 * cups_of_coffee

if water <= water_capacity and milk <= milk_capacity and coffee_beans <= coffee_beans_capacity:
    extra_coffee = min((water_capacity - water) // 200, (milk_capacity - milk) // 50, (coffee_beans_capacity - coffee_beans) // 15)
    if extra_coffee == 0:
        print("Yes, I can make that amount of coffee")
    else:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(extra_coffee))
else:
    minimum_coffee = min(water_capacity // 200, milk_capacity // 50, coffee_beans_capacity // 15)
    print("No, I can make only {} cups of coffee".format(minimum_coffee))