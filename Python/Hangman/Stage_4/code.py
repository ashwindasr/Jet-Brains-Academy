# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
hidden_format = word[:3] + "-" * (len(word) - 3)

print(f"H A N G M A N\nGuess the word {hidden_format}:")
print("You survived!" if input() == word else print("You are hanged!"))
