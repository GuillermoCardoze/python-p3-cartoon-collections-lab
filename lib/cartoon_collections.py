def roll_call_dwarves(name):
    for index, item in enumerate(name, start=1):
        print(f"{index}. {item}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for word in calls:
        if len(word) > 4:
            return True
    return False
    

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in snacks:
        if ingredient in cheeses:
            return ingredient
    return None
    
