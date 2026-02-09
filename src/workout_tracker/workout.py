from typing import List
from workout_tracker.exercises import Exercise


class Workout:
    def __init__(self) -> None:
        self._exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise) -> None:

        # same thing ive kinda been doing with typeerror just so I can check where its going
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout")
        self._exercises.append(exercise)

    def get_exercises(self) -> List[Exercise]:

        return self._exercises.copy()

    def total_calories(self) -> float:
        return sum(ex.calculate_calories() for ex in self._exercises)

    def total_duration(self) -> float:
        return sum(ex.get_duration() for ex in self._exercises)

    def exercise_count(self) -> int:
        return len(self._exercises)

    def get_summary(self) -> str:
        # base case basicly 
        if not self._exercises:
            return "Empty workout - no exercises added"

        lines: List[str] = ["=== Workout Summary ==="]
        for idx, ex in enumerate(self._exercises, start=1):
            lines.append(f"{idx}. {str(ex)}")

        lines.append("-" * 40)
        total_cals = self.total_calories()
        total_mins = self.total_duration()
        lines.append(f"Total: {total_cals:.0f} calories, {total_mins:.0f} minutes")

        return "\n".join(lines)

    # this is giving them a update every time they add something. jsut a lil teaser
    def __str__(self) -> str:

        return f"Workout with {self.exercise_count()} exercise(s), {self.total_calories():.0f} calories"

    def __len__(self) -> int:

        return self.exercise_count()