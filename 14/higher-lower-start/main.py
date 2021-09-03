from art import vs
from art import logo
import random
from game_data import data

## Game
def random_data_a_b():
    """return value for A and B as dictionary"""
    data_c = data
    item_number_a = random.randint(0, len(data)-1)
    item_a = data_c.pop(item_number_a)
    item_number_b = random.randint(0, len(data)-1)
    item_b = data_c.pop(item_number_b)
    return item_a, item_b



def compare(a_ch, b_ch, your_choise, your_score):
    if a_ch > b_ch and your_choise == "A":         
        return False
    elif a_ch < b_ch and your_choise == "B":         
        return False
    else:
        print(f"Sorry, that's wrong. Final score: {your_score}")
        return True

def game():
    score = 0
    guess_fals = False
    game_end = False
    
    while not guess_fals:
        print(logo)
        if game_end:
            return
        else:
            # choise to compare "A"
            random_a_b = random_data_a_b()
            a_dict = random_a_b[0]
            a = a_dict.get('follower_count')                
            print(f"Compare A: {a_dict.get('name')}, a {a_dict.get('description')}, from {a_dict.get('country')}")
            # print "VS"
            print(vs)
            # choise to compare "B"
            b_dict = random_a_b[1]
            b = b_dict.get('follower_count')
            print(f"Compare B: {b_dict.get('name')}, a {b_dict.get('description')}, from {b_dict.get('country')}")       
            guess = input(print("Who has more followers? Type A or B: ")).lower()
            guess_fals = compare(a_ch=a,b_ch=b, your_choise=guess, your_score=score)
            if not guess_fals:
                score += 1
                print (f"You're right! Current score: {score}")
            else:
                game_end = True

game()