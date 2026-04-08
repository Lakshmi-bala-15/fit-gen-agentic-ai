def generate_workout_plan(user):
    goal = user["goal"]

    if goal == "fat_loss":
        return """
DAY 1: Full-body HIIT
DAY 2: Cardio + Core
DAY 3: Strength Training
DAY 4: Yoga + Abs
DAY 5: HIIT + Stretching
"""
    if goal == "muscle_gain":
        return """
DAY 1: Push Day
DAY 2: Pull Day
DAY 3: Leg Day
DAY 4: Upper Body
DAY 5: Full Body Strength
"""
    return "General fitness routine for maintenance."
