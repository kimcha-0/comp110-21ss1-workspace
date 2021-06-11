"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730407570"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, v: list[float]):
        """Constructor method."""
        self.values = v
    
    def __repr__(self) -> str:
        """Prints self.values."""
        return f"Simpy({self.values})"

    def fill(self, a:float, b: int) -> None:
        """Fills Simpy with the value a, b times."""
        result: list[float] = []
        i: int = 0
        while i < b:
            result.append(a)
            i += 1
        return None

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds or concatenates the elements of self and rhs depending on if rhs is float or Simpy."""
        if isinstance(rhs, float):
            new_values = []
            for i in self.values:
                new_values.append(i + rhs)
            return Simpy(new_values)
        else:
            assert len(self.values) == len(rhs.values)
            new_values = []
            for i in range(len(self.values)):
                new_values.append(self.values[i] + rhs.values[i])
            return Simpy(new_values)

    def __getitem__(self, rhs: float) -> float:
        """Returns the value at the self[rhs] index."""
        return self.values[rhs]


