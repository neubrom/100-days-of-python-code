#answer Guessing Game Objectives:

# Include an ASCII art logo.
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# Allow the player to submit a guess for a answer between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the answer of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

guess = 10

HARD_GUESS = 5
EASY_GUESS =10

print(logo)
print("""Welcome to the answer Guessing Game!
I'm thinking of a answer between 1 and 100.""")

def input_level():
    level = input("Choise difficulty level - ""easy"" or ""hard"": ")
    if level == "easy":
        return EASY_GUESS              
    elif level == "hard":
        return HARD_GUESS  


def game():
    answer = random.randint(1, 100)
    print(f"Psst! answer: {answer}")
    guess_c = 0
    turn = int(input_level())
    while guess_c != answer:
        print(f"You have {turn} attempts remaining to guess the answer.")
        if turn != 0:
            guess_c = int(input("Your gess: ")) 
            if answer > guess_c:
                print("Too low. Guess again.")
                turn -= 1
            elif answer < guess_c:
                print("Too high. Guess again.")
                turn -= 1
            elif answer == guess_c:
                print(f"You got it! The answer was {answer}.")
        else:
            return print("You've run out of guesses, you lose.")




game()