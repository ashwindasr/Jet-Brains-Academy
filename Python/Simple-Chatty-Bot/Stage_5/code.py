# write your code here
class SimpleChattyBot:
    user_name = None
    user_age = None

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def greeting(self):
        print(f"""Hello! My name is {self.name}.
I was created in {self.birth_year}.""")

    def get_user_name(self):
        self.user_name = input("Please, remind me your name.\n")
        print(f"What a great name you have, {self.user_name}!")

    def guess_age(self):
        print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
        self.user_age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105
        print(f"Your age is {self.user_age}; that's a good time to start programming!")

    @staticmethod
    def count_number():
        number_range = int(input("Now I will prove to you that I can count to any number you want.\n"))
        for number in range(number_range + 1):
            print(" ".join([str(number), "!"]))
        print("Completed, have a nice day!")

    @staticmethod
    def test():
        print("Let's test your programming knowledge.")
        print("""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
        while True:
            answer = int(input())
            if answer == 2:
                print("Congratulations, have a nice day!")
                break
            print("Please, try again.")


bot = SimpleChattyBot("Jarvis", 2020)
bot.greeting()
bot.get_user_name()
bot.guess_age()
bot.count_number()
bot.test()
