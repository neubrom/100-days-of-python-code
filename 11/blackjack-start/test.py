import random
from warnings import resetwarnings

player = [23, 7, 2]
amount_card = 2
rest = [23, 22, 2, 223]

sum_total = 0
if 1 not in player:
    print("test 1 if")
    for i in player:
        sum_total += i
else:
    print("test 1 else")
    if sum(player) > 11:
        print(sum(player))
        for i in player:
            if i != 1:
                total = 0
                total += i
        sum_total = total+1
    else:
        sum_total = (sum(player) + 10)
print(f"current score: {sum_total}")
# if sum > 21:
#    print(f"{sum}! {player} lose")