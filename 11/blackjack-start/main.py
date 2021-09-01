############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import os
from art import logo
from sum import sum_total

new_game = True
computer = []
you = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
rest_cards =[]

def get_cards(player, amount_card, rest):
    """Get(pop) random card from rest and retourn new rest and player card"""
    while amount_card != 0:
        card_random_position = random.randint(0, (len(rest)-1))
        player.append(rest[card_random_position])
        rest.pop(card_random_position)
        amount_card -= 1
    return player, rest

def get_another_card(player_an, amount_card_an, rest_an):
        another_card = input("Type 'y' to get another card, type 'n' to pass: y: ")
        if another_card == "y":
            get_cards(player=player_an, amount_card=amount_card_an, rest=rest_an)
            print(f"Your cards: {you}, current score: {sum_total(you)}")
            if sum_total(you) > 21:
                print("You went over. You lose")
                return
            get_another_card(player_an, amount_card_an, rest_an)
        return player_an, rest_an


def get_total(player):
    """calculate total score for player and test if > 21"""
    sum = sum_total(player)
    if sum > 21:
        print(f"{sum}! {player} lose")  
    return sum

#start_game
rest_cards = cards
begin = str(input("Start new game y/n?"))
if begin == "y":
    print(logo)
get_cards(player=you, amount_card=2, rest=rest_cards)
get_cards(player=computer, amount_card=1, rest=rest_cards)
print(f"Your cards: {you}, current score: {sum_total(player=you)}")
print(f"Computer's first card: {computer}")
get_another_card(player_an=you, amount_card_an=1, rest_an=rest_cards)
while sum_total(computer)<=21:
    get_cards(player=computer, amount_card=1, rest=rest_cards)
print(f"Computer's cards: {computer}, score: {sum_total(player=computer)}")
if sum_total(you) > sum_total(computer) and sum_total(you) <= 21:
    print(f"You win!")
elif sum_total(you) > sum_total(computer) and sum_total(computer) > 21:
    print(f"You win!")
elif sum_total(you) < sum_total(computer) and sum_total(computer) <= 21:
    print(f"You lose!")
elif sum_total(you) < sum_total(computer) and sum_total(you) > 21:
    print(f"You lose!")
elif sum_total(you) < sum_total(computer) and sum_total(computer) > 21:
    print(f"You win!")
elif sum_total(you) < sum_total(computer) and sum_total(you) > 21:
    print(f"You lose!")   
elif sum_total(you) == sum_total(computer)  and sum_total(compile) <= 21:
    print(f"Draw!")
#else:
 #   print(f"You win!")