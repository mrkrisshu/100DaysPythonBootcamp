import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

guess = input("Guess a Letter: ").lower()


display = ""

for letter in chosen_word:
    if letter == guess:
        display += guess
    else :
        display += "_"

print(display)