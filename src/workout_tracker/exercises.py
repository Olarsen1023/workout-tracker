
from __future__ import annotations

from datetime import datetime
from typing import Optional


class Exercise:
    """Base class for all exercise types.

    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """

    def __init__(self, name: str, date: Optional[str] = None):
        """Initialize an Exercise.

        Args:
            name: The name of the exercise
            date: The date performed in 'YYYY-MM-DD' format (defaults to today if not provided)
        """
        self.name = name
        # If date is None, use today; otherwise validate format
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            # Basic validation to ensure correct format; raises ValueError if invalid
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError(
                    f"Invalid date '{date}'. Expected format 'YYYY-MM-DD'."
                ) from exc
            self.date = date

    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.

        Subclasses must override this method.

        Returns:
            float: Estimated calories burned
        """
        # Base implementation returns 0; subclasses provide specifics
        return 0.0

    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.

        Subclasses must override this method.

        Returns:
            float: Duration in minutes
        """
        # Base implementation returns 0; subclasses provide specifics
        return 0.0

    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        # Example: "Push-ups: 100 calories"
        calories = self.calculate_calories()
        # Format to remove trailing .0 for whole numbers
        cals_text = f"{calories:.0f}" if calories.is_integer() else f"{calories:.2f}"
        return f"{self.name}: {cals_text} calories"


class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.

    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """

    def __init__(self, name: str, distance: float, duration: float, date: Optional[str] = None):
        """Initialize a CardioExercise.

        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles (non-negative)
            duration: Time spent in minutes (non-negative)
            date: Date performed in 'YYYY-MM-DD' format (optional)
        """
        super().__init__(name, date)

        if distance < 0:
            raise ValueError("distance must be non-negative")
        if duration < 0:
            raise ValueError("duration must be non-negative")
        try:
            d = float(distance)
            t = float(duration)
        except (TypeError, ValueError) as exc:
            raise TypeError("Distance and Duration has to numeric") from exc
        
        if d < 0:
            raise ValueError("distance has to be greater than 0")
        if t < 0:
            raise ValueError("duration has to be greater than 0")
        

        self.distance = float(distance)
        self.duration = float(duration)

    def calculate_calories(self) -> float:
        """Calculate calories burned based on distance.

        Formula: distance * 100

        Returns:
            float: Estimated calories burned
        """
        return self.distance * 100.0

    def get_duration(self) -> float:
        """Get the duration of the cardio exercise.

        Returns:
            float: Duration in minutes
        """
        return self.duration

    def __str__(self) -> str:
        """Return detailed string representation."""
        calories = self.calculate_calories()
        cals_text = f"{calories:.0f}" if calories.is_integer() else f"{calories:.2f}"
        dist_text = f"{self.distance:g}"  # trims trailing zeros
        dur_text = f"{self.duration:g}"   # trims trailing zeros
        return f"{self.name} ({dist_text} miles, {dur_text} min): {cals_text} calories"


class StrengthExercise(Exercise):

    def __init__(
        self,
        name: str,
        weight: float,
        reps: int,
        sets: int,
        date: str | None = None,
    ):

        super().__init__(name, date)

        # Validate and coerce inputs
        try:
            w = float(weight)
        except (TypeError, ValueError) as exc:
            raise TypeError("weight must be numeric") from exc

        try:
            r = int(reps)
            s = int(sets)
        except (TypeError, ValueError) as exc:
            raise TypeError("reps and sets must be integers") from exc

        if w < 0:
            raise ValueError("weight must be non-negative")
        if r < 1:
            raise ValueError("reps must be at least 1")
        if s < 1:
            raise ValueError("sets must be at least 1")

        # store vals
        self.weight = w
        self.reps = r
        self.sets = s

    def calculate_calories(self) -> float:

        return self.weight * self.reps * self.sets * 0.05

    def get_duration(self) -> float:

        return float(self.sets * 3)

    def __str__(self) -> str:
  
        # str to format the output!
        calories_int = round(self.calculate_calories())
        weight_text = f"{self.weight:g}"
        return (
            f"{self.name} ({weight_text} lbs x {self.reps} reps x {self.sets} sets): "
            f"{calories_int} calories"
        )


class FlexibilityExercise(Exercise):
    INTENSITY_MULTIPLIER = {
        'low': 1.0,
        'medium': 1.5,
        'high': 2.0,
    }

    def __init__(
        self,
        name: str,
        duration: float,
        intensity: str = 'medium',
        date: str | None = None,
    ):
        super().__init__(name, date)

       # made some execptions across all of the classes
        try:
            dur = float(duration)
        except (TypeError, ValueError) as exc:
            raise TypeError("duration must be numeric") from exc
        if dur < 0:
            raise ValueError("duration must be non-negative")

        inten = (intensity or 'medium').lower()
        if inten not in self.INTENSITY_MULTIPLIER:
            valid = "', '".join(self.INTENSITY_MULTIPLIER.keys())
            raise ValueError(f"intensity must be one of '{valid}'")

        self.duration = dur
        self.intensity = inten

    def calculate_calories(self) -> float:
        multiplier = self.INTENSITY_MULTIPLIER[self.intensity]
        return self.duration * 2.5 * multiplier

    def get_duration(self) -> float:
        return self.duration

    def __str__(self) -> str:

        # same format but little smaller because less varibles to worry about
        calories_int = round(self.calculate_calories())
        dur_text = f"{self.duration:g}"
        return f"{self.name} ({dur_text} min, {self.intensity} intensity): {calories_int} calories"

