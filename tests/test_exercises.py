"""Unit tests for exercise classes."""

import pytest
from workout_tracker.exercises import (
    Exercise,
    CardioExercise,
    StrengthExercise,
    FlexibilityExercise
)


class TestCardioExercise:
    """Tests for CardioExercise class."""
    
    def test_cardio_creation(self):
        """Test creating a cardio exercise."""
        exercise = CardioExercise("Running", distance=3.5, duration=30)
        assert exercise.name == "Running"
        assert exercise.distance == 3.5
        assert exercise.duration == 30
    
    def test_cardio_calories(self):
        """Test calorie calculation for cardio."""
        exercise = CardioExercise("Cycling", distance=10.0, duration=45)
        # Formula: distance * 100
        assert exercise.calculate_calories() == 1000.0
    
    def test_cardio_duration(self):
        """Test getting duration for cardio."""
        exercise = CardioExercise("Swimming", distance=1.0, duration=25)
        assert exercise.get_duration() == 25
    
    def test_cardio_str(self):
        """Test string representation of cardio exercise."""
        exercise = CardioExercise("Running", distance=5.0, duration=40)
        result = str(exercise)
        assert "Running" in result
        assert "5.0 miles" in result
        assert "500" in result  # calories


class TestStrengthExercise:
    """Tests for StrengthExercise class."""
    
    def test_strength_creation(self):
        """Test creating a strength exercise."""
        exercise = StrengthExercise("Bench Press", weight=135, reps=10, sets=3)
        assert exercise.name == "Bench Press"
        assert exercise.weight == 135
        assert exercise.reps == 10
        assert exercise.sets == 3
    
    def test_strength_calories(self):
        """Test calorie calculation for strength training."""
        exercise = StrengthExercise("Squats", weight=200, reps=8, sets=4)
        # Formula: weight * reps * sets * 0.05
        # 200 * 8 * 4 * 0.05 = 320
        assert exercise.calculate_calories() == 320.0
    
    def test_strength_duration(self):
        """Test duration estimate for strength training."""
        exercise = StrengthExercise("Deadlift", weight=225, reps=5, sets=5)
        # 3 minutes per set * 5 sets = 15 minutes
        assert exercise.get_duration() == 15
    
    def test_strength_str(self):
        """Test string representation of strength exercise."""
        exercise = StrengthExercise("Pull-ups", weight=0, reps=12, sets=3)
        result = str(exercise)
        assert "Pull-ups" in result
        assert "12 reps" in result
        assert "3 sets" in result


class TestFlexibilityExercise:
    """Tests for FlexibilityExercise class."""
    
    def test_flexibility_creation(self):
        """Test creating a flexibility exercise."""
        exercise = FlexibilityExercise("Yoga", duration=30, intensity="medium")
        assert exercise.name == "Yoga"
        assert exercise.duration == 30
        assert exercise.intensity == "medium"
    
    def test_flexibility_calories_medium(self):
        """Test calorie calculation for medium intensity."""
        exercise = FlexibilityExercise("Stretching", duration=20, intensity="medium")
        # Formula: duration * 2.5 * multiplier
        # 20 * 2.5 * 1.5 = 75
        assert exercise.calculate_calories() == 75.0
    
    def test_flexibility_calories_low(self):
        """Test calorie calculation for low intensity."""
        exercise = FlexibilityExercise("Gentle Yoga", duration=30, intensity="low")
        # 30 * 2.5 * 1.0 = 75
        assert exercise.calculate_calories() == 75.0
    
    def test_flexibility_calories_high(self):
        """Test calorie calculation for high intensity."""
        exercise = FlexibilityExercise("Power Yoga", duration=40, intensity="high")
        # 40 * 2.5 * 2.0 = 200
        assert exercise.calculate_calories() == 200.0
    
    def test_flexibility_invalid_intensity(self):
        """Test that invalid intensity raises error."""
        with pytest.raises(ValueError):
            FlexibilityExercise("Yoga", duration=30, intensity="extreme")
    
    def test_flexibility_duration(self):
        """Test getting duration for flexibility exercise."""
        exercise = FlexibilityExercise("Pilates", duration=45, intensity="medium")
        assert exercise.get_duration() == 45
    
    def test_flexibility_case_insensitive(self):
        """Test that intensity is case-insensitive."""
        exercise1 = FlexibilityExercise("Yoga", duration=30, intensity="HIGH")
        exercise2 = FlexibilityExercise("Yoga", duration=30, intensity="high")
        assert exercise1.intensity == exercise2.intensity
        assert exercise1.calculate_calories() == exercise2.calculate_calories()


class TestExerciseInheritance:
    """Tests to verify inheritance works correctly."""
    
    def test_all_exercises_are_exercises(self):
        """Test that all exercise types inherit from Exercise."""
        cardio = CardioExercise("Running", distance=5, duration=30)
        strength = StrengthExercise("Squats", weight=100, reps=10, sets=3)
        flexibility = FlexibilityExercise("Yoga", duration=30, intensity="medium")
        
        assert isinstance(cardio, Exercise)
        assert isinstance(strength, Exercise)
        assert isinstance(flexibility, Exercise)
    
    def test_exercises_have_date(self):
        """Test that all exercises have a date attribute."""
        cardio = CardioExercise("Running", distance=5, duration=30)
        assert hasattr(cardio, 'date')
        assert cardio.date is not None
    
    def test_exercise_custom_date(self):
        """Test creating exercise with custom date."""
        exercise = CardioExercise("Running", distance=5, duration=30, date="2024-01-15")
        assert exercise.date == "2024-01-15"
