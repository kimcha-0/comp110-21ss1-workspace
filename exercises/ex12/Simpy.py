"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730407570"


class Simpy:
    """Simpy class!"""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, v: list[float]):
        """Constructor method."""
        self.values = v
    
    def __repr__(self) -> str:
        """Prints self.values."""
        return f"Simpy({self.values})"

    def fill(self, a: float, b: int) -> None:
        """Fills Simpy with the value a, b times."""
        self.values = []
        i: int = 0
        while i < b:
            self.values.append(a)
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

    def __getitem__(self, rhs: int) -> float:
        """Returns the value at the self[rhs] index."""
        return self.values[rhs]
    
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Range but with floats."""
        self.values = []
        assert step != 0.0
        i = start
        while i < stop:
            self.values.append(i)
            i += step    
    
    def sum(self) -> float:
        """Sums all items in the values attribute of Simpy."""
        result: float = sum(self.values)
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic exponent method."""
        if isinstance(rhs, float):
            new_values = []
            for i in self.values:
                new_values.append(i ** rhs)
            return Simpy(new_values)
        else:
            assert len(self.values) == len(rhs.values)
            new_values = []
            for i in range(len(self.values)):
                new_values.append(self.values[i] ** rhs.values[i])
            return Simpy(new_values)
    
    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic modular arithmetic method."""
        if isinstance(rhs, float):
            new_values = []
            for i in self.values:
                new_values.append(i % rhs)
            return Simpy(new_values)
        else:
            assert len(self.values) == len(rhs.values)
            new_values = []
            for i in range(len(self.values)):
                new_values.append(self.values[i] % rhs.values[i])
            return Simpy(new_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        