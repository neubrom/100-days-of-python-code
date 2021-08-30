import os
import art
print(art.logo)

bidder = {}

def add_person():
    name = input("Your name: ")
    bid = input ("Your bid :$")
    bidder[name] = bid

add_person()
add_q = input("Add new person? yes / no: ")
while add_q == "yes":
    os.system("clear")
    add_person()
    add_q = input("Add new person? yes / no: ")
winner = max(bidder, key=bidder.get)
print(f"Winner: {winner}")