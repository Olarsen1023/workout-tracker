

"""Workout Tracker - A simple OOP-based workout tracking system."""

from workout_tracker.exercises import (
    Exercise,
    CardioExercise,
    StrengthExercise,
    FlexibilityExercise
)
from workout_tracker.workout import Workout

__version__ = "0.1.0"

__all__ = [
    "Exercise",
    "CardioExercise",
    "StrengthExercise",
    "FlexibilityExercise",
    "Workout"
]

