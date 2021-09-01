#Number Guessing Game Objectives:

# Include an ASCII art logo.
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")


number = random.randint(1, 100)
print(f"Psst! Number: {number}")
#guesses = 0
guess = 10
finish = False

def your_guess(guesses_c, number_c):
    guess_c = int(input("Your gess: "))
    finish_c = False
    while finish_c != True:
        if number_c > guess_c:
            print("Too low. Guess again.")
            finish_c = False
        elif number_c < guess_c:
            print("Too high. Guess again.")
            finish_c = False
        elif number_c == guess_c:
            print(f"You got it! The answer was {number_c}.")        
            finish_c = True            
        guesses_c -= 1
        if guess_c == 0:
            return print("you lose!")
        else:
            your_guess(guesses_c, number_c)


level = input("Choise difficulty level - ""easy"" or ""hard"": ")
if level == "easy":
    guesses = 10
    print(f"You have {guesses} attempts remaining to guess the number.")               
elif level == "hard":
    guesses = 5
    print(f"You have {guesses} attempts remaining to guess the number.")             
  
your_guess(guesses_c=guesses, number_c=number)