from agents.intake_agent import get_user_profile
from agents.workout_agent import generate_workout_plan
from agents.nutrition_agent import generate_meal_plan

def main():
    print("AI Fitness & Nutrition Agent")
    user = get_user_profile()
    workout = generate_workout_plan(user)
    meals = generate_meal_plan(user)

    print("\nWORKOUT PLAN:")
    print(workout)
    print("\nMEAL PLAN:")
    print(meals)

if __name__ == "__main__":
    main()
