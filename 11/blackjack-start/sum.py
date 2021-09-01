
def sum_total(player):
    """calculate total score for player"""
    sum_temp = 0
    ass = False
    if (11 not in player): 
        sum_temp = sum(player)           
    else:
        total = 0           
        if sum(player) > 21:              
            for i in player:
                if i != 11:                
                    total += i         
            sum_temp = total+1            
        else:
            sum_temp = sum(player)        
    #print(f"current score: {sum_temp}")
    return sum_temp

