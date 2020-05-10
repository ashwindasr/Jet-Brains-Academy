# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
hidden_format = "-" * len(word)
tries = 8
all_letters = set(word)
successful_letters = set()
won = False

print("H A N G M A N\n")
while tries > 0:
    print()
    print(hidden_format)
    letter = input("Input a letter: ")
    if letter in all_letters:
        all_letters.discard(letter)
        successful_letters.add(letter)

        temp = ""
        for i in word:
            if i in all_letters:
                temp += "-"
            else:
                temp += i

        hidden_format = temp
    elif all_letters is None:
        won = True
        continue
    elif letter in successful_letters:
        print("No improvements")
        tries -= 1
    else:
        print("No such letter in the word")
        tries -= 1

print("You survived!" if won else "You are hanged!")
