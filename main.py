"""Simple command-line interface for the workout tracker.

This is an optional example showing how to use the workout tracker classes.
Students are not required to implement this CLI.
"""

from workout_tracker import (
    CardioExercise,
    StrengthExercise,
    FlexibilityExercise,
    Workout
)


def create_cardio_exercise():
    """Prompt user for cardio exercise details."""
    name = input("Exercise name (e.g., Running, Cycling): ").strip()
    distance = float(input("Distance (miles): "))
    duration = float(input("Duration (minutes): "))
    return CardioExercise(name, distance, duration)


def create_strength_exercise():
    """Prompt user for strength exercise details."""
    name = input("Exercise name (e.g., Bench Press, Squats): ").strip()
    weight = float(input("Weight (lbs): "))
    reps = int(input("Reps per set: "))
    sets = int(input("Number of sets: "))
    return StrengthExercise(name, weight, reps, sets)


def create_flexibility_exercise():
    """Prompt user for flexibility exercise details."""
    name = input("Exercise name (e.g., Yoga, Stretching): ").strip()
    duration = float(input("Duration (minutes): "))
    intensity = input("Intensity (low/medium/high): ").strip().lower()
    return FlexibilityExercise(name, duration, intensity)


def main():
    """Main CLI loop."""
    print("=== Workout Tracker ===\n")
    
    workout = Workout()
    
    while True:
        print("\nExercise type?")
        print("1. Cardio")
        print("2. Strength")
        print("3. Flexibility")
        print("4. Finish workout")
        
        choice = input("\nChoice (1-4): ").strip()
        
        try:
            if choice == "1":
                exercise = create_cardio_exercise()
                workout.add_exercise(exercise)
                print(f"\n✓ Added: {exercise}")
            elif choice == "2":
                exercise = create_strength_exercise()
                workout.add_exercise(exercise)
                print(f"\n✓ Added: {exercise}")
            elif choice == "3":
                exercise = create_flexibility_exercise()
                workout.add_exercise(exercise)
                print(f"\n✓ Added: {exercise}")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + workout.get_summary())
    print("\nWorkout complete! 💪")


if __name__ == "__main__":
    main()
