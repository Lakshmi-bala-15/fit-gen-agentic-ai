def generate_meal_plan(user):
    diet = user["diet"]

    if diet == "vegetarian":
        return """
Breakfast: Oats + Fruits  
Lunch: Veg Thali + Dal  
Dinner: Paneer Salad  
Snacks: Nuts + Smoothie  
"""

    if diet == "vegan":
        return """
Breakfast: Smoothie Bowl  
Lunch: Veg Burrito  
Dinner: Tofu Stir-fry  
Snacks: Fruits + Seeds  
"""

    return """
Breakfast: Eggs + Toast  
Lunch: Rice + Chicken + Veggies  
Dinner: Chapati + Sabzi  
Snacks: Fruit + Yogurt  
"""
