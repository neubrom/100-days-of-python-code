import random

#ASCI
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

variant=[rock, paper, scissors]
choise = int(input("Please your choise - rock(0), paper(1), scissors(2): "))
if choise >= 0 and choise <=2:
    print("You: " + variant[int(choise)])

    computer_choise = int(random.randint(0, 2))
    print("Computer: " + variant[computer_choise])

    game = str(choise) + str(computer_choise)
    print(game)

    if game == "02" or game == "10" or game == "21":
        print("You win!")
    elif computer_choise == choise:
        print("It is draw - try one more time!")
    else:
        print("You lose!")
else:
    print("Invalid choise, you lose!")