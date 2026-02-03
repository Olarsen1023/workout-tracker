from workout_tracker import CardioExercise

# Create a cardio exercise
run = CardioExercise("Morning Run", distance=3.5, duration=30)

print(f"Exercise: {run}")
print(f"Calories: {run.calculate_calories()}")
print(f"Duration: {run.get_duration()} minutes")