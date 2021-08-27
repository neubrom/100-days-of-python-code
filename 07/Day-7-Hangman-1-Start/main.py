#Step 1 

word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list 
    # and assign it to a variable called chosen_word.
import random
from warnings import formatwarning
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign 
    # their answer to a variable called guess. 
    # Make guess lowercase.
guess_input = input("Your gues: ")
guess = guess_input.lower()
print(guess)
#TODO-3 - Check if the letter the user guessed (guess) 
    # is one of the letters in the chosen_word.
for n in chosen_word:
    if guess == n:
        print("Right!")
    else:
        print("Wrong!")