spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names
def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy in spicy_foods:
        hot_emoji = '🌶' * spicy['heat_level']
        print(f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {hot_emoji}")
    return None
    


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy in spicy_foods:
        if spicy['cuisine'] == cuisine:
            return spicy
    return None

def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        if spicy['heat_level'] > 5:
            hot_emoji = '🌶' * spicy['heat_level']
            print(f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {hot_emoji}")
    return None

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
