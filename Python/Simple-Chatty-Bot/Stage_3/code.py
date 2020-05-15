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
        
        
bot = SimpleChattyBot("Jarvis", 2020)
bot.greeting()
bot.get_user_name()
bot.guess_age()
