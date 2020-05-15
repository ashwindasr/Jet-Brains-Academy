# write your code here
class SimpleChattyBot:
    user_name = None

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def greeting(self):
        print(f"""Hello! My name is {self.name}.
I was created in {self.birth_year}.""")

    def get_user_name(self):
        self.user_name = input("Please, remind me your name.\n")
        print(f"What a great name you have, {self.user_name}!")


bot = SimpleChattyBot("Jarvis", 2020)
bot.greeting()
bot.get_user_name()
