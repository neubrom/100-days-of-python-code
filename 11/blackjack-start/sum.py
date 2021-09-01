
def sum_total(player):
    """calculate total score for player"""
    sum_temp = 0
    ass = False
    if (11 not in player): 
        sum_temp = sum(player)
    elif sum(player) == 21 and len(player) ==2:
        return 0
    else:
        total = 0           
        if sum(player) > 21:              
            for i in player:
                if i != 11:                
                    total += i         
            sum_temp = total+1            
        else:
            sum_temp = sum(player)        
    if sum_temp > 21:
        return
    return sum_temp

