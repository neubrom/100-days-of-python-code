#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only 
# stop once the user has guessed all the letters in the chosen_word and 'display' 
# has no more blanks ("_"). Then you can tell the user they've won.
display = []
lengh = len(chosen_word)
for leters in range(lengh):
    display.append("_")

print(display)

lengh2 = lengh

while lengh2 != 0:
    guess = input("Guess a letter: ").lower()
    for position in range(lengh):
        if chosen_word[position]== guess:
            display[position] = guess
            lengh2 -= 1
    if lengh2 == 0:
        print("you win!")





#Check guessed letter
"""for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter"""

print(display)