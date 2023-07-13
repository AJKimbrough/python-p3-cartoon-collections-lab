def roll_call_dwarves(dwarves):
   return [print(f"{dwarves.index(name) + 1}. {name}") for name in dwarves]

def summon_captain_planet(planeteer_calls):
    new_list = []
    [new_list.append(f"{item.capitalize()}!") for item in planeteer_calls]
    return new_list

def long_planeteer_calls(calls):
    new_list = []
    [new_list.append(len(call)) for call in calls if len(call) > 4]
    print(new_list)
    if new_list != []:
        return True
    else:
        return False
    
def find_the_cheese(food):
    if "gouda" in food:
        return "gouda"
    elif "cheddar" in food:
        return "cheddar"
    elif "camembert" in food:
        return "camembert"
    else:
        return None
    

print(find_the_cheese(['banana', 'cheddar', 'sock']))