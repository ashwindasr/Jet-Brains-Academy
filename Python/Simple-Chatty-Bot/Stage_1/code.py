# write your code here
class SimpleChattyBot:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def greeting(self):
        print(f"""Hello! My name is {self.name}.
I was created in {self.birth_year}.""")


bot = SimpleChattyBot("Jarvis", 2020)
bot.greeting()
