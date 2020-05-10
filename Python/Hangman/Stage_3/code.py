# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)

print("""H A N G M A N
Guess the word: > """)
print("You survived!" if input() == word else print("You are hanged!"))
