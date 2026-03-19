import random

def predict_food(img_path):
    foods = ["pizza", "steak"]
    
    food = random.choice(foods)
    
    calorie_dict = {
        "pizza": 285,
        "steak": 271
    }
    
    calories = calorie_dict[food]
    
    return food, calories