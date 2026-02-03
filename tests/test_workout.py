"""Unit tests for Workout class."""

import pytest
from workout_tracker import (
    Workout,
    CardioExercise,
    StrengthExercise,
    FlexibilityExercise
)


class TestWorkout:
    """Tests for Workout class."""
    
    def test_workout_creation(self):
        """Test creating an empty workout."""
        workout = Workout()
        assert workout.exercise_count() == 0
        assert len(workout) == 0
    
    def test_add_single_exercise(self):
        """Test adding a single exercise to workout."""
        workout = Workout()
        exercise = CardioExercise("Running", distance=3, duration=25)
        workout.add_exercise(exercise)
        
        assert workout.exercise_count() == 1
        assert len(workout) == 1
    
    def test_add_multiple_exercises(self):
        """Test adding multiple exercises to workout."""
        workout = Workout()
        
        cardio = CardioExercise("Running", distance=5, duration=40)
        strength = StrengthExercise("Bench Press", weight=135, reps=10, sets=3)
        flexibility = FlexibilityExercise("Yoga", duration=30, intensity="medium")
        
        workout.add_exercise(cardio)
        workout.add_exercise(strength)
        workout.add_exercise(flexibility)
        
        assert workout.exercise_count() == 3
    
    def test_add_invalid_type(self):
        """Test that adding non-Exercise object raises error."""
        workout = Workout()
        with pytest.raises(TypeError):
            workout.add_exercise("not an exercise")
    
    def test_total_calories_empty(self):
        """Test total calories for empty workout."""
        workout = Workout()
        assert workout.total_calories() == 0
    
    def test_total_calories_single_exercise(self):
        """Test total calories with one exercise."""
        workout = Workout()
        exercise = CardioExercise("Running", distance=5, duration=30)
        workout.add_exercise(exercise)
        
        # 5 miles * 100 = 500 calories
        assert workout.total_calories() == 500
    
    def test_total_calories_multiple_exercises(self):
        """Test total calories with multiple exercises."""
        workout = Workout()
        
        # Cardio: 3 * 100 = 300 calories
        cardio = CardioExercise("Cycling", distance=3, duration=20)
        # Strength: 100 * 8 * 3 * 0.05 = 120 calories
        strength = StrengthExercise("Squats", weight=100, reps=8, sets=3)
        # Flexibility: 20 * 2.5 * 1.5 = 75 calories
        flexibility = FlexibilityExercise("Stretching", duration=20, intensity="medium")
        
        workout.add_exercise(cardio)
        workout.add_exercise(strength)
        workout.add_exercise(flexibility)
        
        # Total: 300 + 120 + 75 = 495
        assert workout.total_calories() == 495
    
    def test_total_duration_empty(self):
        """Test total duration for empty workout."""
        workout = Workout()
        assert workout.total_duration() == 0
    
    def test_total_duration_multiple_exercises(self):
        """Test total duration with multiple exercises."""
        workout = Workout()
        
        cardio = CardioExercise("Running", distance=5, duration=35)  # 35 min
        strength = StrengthExercise("Deadlift", weight=200, reps=5, sets=4)  # 4 * 3 = 12 min
        flexibility = FlexibilityExercise("Yoga", duration=25, intensity="low")  # 25 min
        
        workout.add_exercise(cardio)
        workout.add_exercise(strength)
        workout.add_exercise(flexibility)
        
        # Total: 35 + 12 + 25 = 72 minutes
        assert workout.total_duration() == 72
    
    def test_get_exercises(self):
        """Test getting list of exercises."""
        workout = Workout()
        
        ex1 = CardioExercise("Running", distance=3, duration=20)
        ex2 = StrengthExercise("Push-ups", weight=0, reps=20, sets=3)
        
        workout.add_exercise(ex1)
        workout.add_exercise(ex2)
        
        exercises = workout.get_exercises()
        assert len(exercises) == 2
        assert ex1 in exercises
        assert ex2 in exercises
    
    def test_get_exercises_returns_copy(self):
        """Test that get_exercises returns a copy, not the original list."""
        workout = Workout()
        exercise = CardioExercise("Running", distance=5, duration=30)
        workout.add_exercise(exercise)
        
        exercises1 = workout.get_exercises()
        exercises2 = workout.get_exercises()
        
        # Should be equal but not the same object
        assert exercises1 == exercises2
        assert exercises1 is not exercises2
    
    def test_workout_str(self):
        """Test string representation of workout."""
        workout = Workout()
        cardio = CardioExercise("Running", distance=5, duration=30)
        workout.add_exercise(cardio)
        
        result = str(workout)
        assert "1 exercise" in result or "1 exercises" in result
        assert "500" in result  # calories
    
    def test_get_summary_empty(self):
        """Test summary for empty workout."""
        workout = Workout()
        summary = workout.get_summary()
        assert "Empty workout" in summary
    
    def test_get_summary_with_exercises(self):
        """Test summary with exercises."""
        workout = Workout()
        
        cardio = CardioExercise("Running", distance=5, duration=40)
        strength = StrengthExercise("Squats", weight=150, reps=10, sets=3)
        
        workout.add_exercise(cardio)
        workout.add_exercise(strength)
        
        summary = workout.get_summary()
        assert "Workout Summary" in summary
        assert "Running" in summary
        assert "Squats" in summary
        assert "Total:" in summary


class TestWorkoutIntegration:
    """Integration tests for complete workout scenarios."""
    
    def test_complete_workout_scenario(self):
        """Test a complete workout with all exercise types."""
        workout = Workout()
        
        # Add variety of exercises
        workout.add_exercise(CardioExercise("Running", distance=3.5, duration=30))
        workout.add_exercise(StrengthExercise("Bench Press", weight=135, reps=10, sets=3))
        workout.add_exercise(StrengthExercise("Pull-ups", weight=0, reps=12, sets=3))
        workout.add_exercise(FlexibilityExercise("Yoga", duration=20, intensity="medium"))
        
        # Verify counts
        assert workout.exercise_count() == 4
        
        # Verify total calories
        # Cardio: 3.5 * 100 = 350
        # Bench: 135 * 10 * 3 * 0.05 = 202.5
        # Pullups: 0 * 12 * 3 * 0.05 = 0
        # Yoga: 20 * 2.5 * 1.5 = 75
        # Total: 627.5
        assert workout.total_calories() == 627.5
        
        # Verify total duration
        # Running: 30, Bench: 9, Pullups: 9, Yoga: 20 = 68 minutes
        assert workout.total_duration() == 68
    
    def test_workout_with_only_cardio(self):
        """Test workout with only cardio exercises."""
        workout = Workout()
        
        workout.add_exercise(CardioExercise("Running", distance=5, duration=35))
        workout.add_exercise(CardioExercise("Cycling", distance=10, duration=45))
        
        assert workout.exercise_count() == 2
        assert workout.total_calories() == 1500  # 500 + 1000
        assert workout.total_duration() == 80  # 35 + 45
