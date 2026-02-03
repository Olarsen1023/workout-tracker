"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        self.name = name
        self.date = datetime.now().strftime("%Y - %m - %d")
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        # TODO: Set self.name
        # TODO: Set self.date (use datetime.now().strftime("%Y-%m-%d") if date is None)
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        print(f"{self.name}: {self.calculate_calories()})
        """Return a string representation of the exercise."""
        # TODO: Return a string like "ExerciseName: 100 calories"
        # Use self.calculate_calories() to get the calories
        