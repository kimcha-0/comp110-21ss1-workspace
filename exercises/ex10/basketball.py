"""A class to model a basketball game."""

__author__ = "730407570"


# TODO 1: Define the BBallGame class, and its logic, here.
class BBallGame:
    """Represents a sim of a basketball game."""
    biscuits: bool 
    points: int
    winning_team: str
    losing_team: str

    def __init__(self, points: int, winning_team: str, losing_team: str):
        """Construct values for the attributes."""
        self.biscuits = False
        self.points = points 
        self.winning_team = winning_team
        self.losing_team = losing_team
    
    def check_points(self) -> None:
        """Checks if points scored are greater than 100."""
        if self.points >= 100: 
            self.biscuits = True

    def winner(self) -> str:
        """Returns different strings based on who the winning team is."""
        beat_duke: str = "GTHD!!"
        win: str = "woohoo"
        loss: str = "daggum"
        if self.winning_team == "UNC" and self.losing_team == "Dook":
            return beat_duke
        elif self.winning_team == "UNC" and self.losing_team != "Dook":
            return win
        else:
            return loss

    def reset_points(self) -> int:
        """Resets point total to 0."""
        result = self.points
        self.points = 0
        return result