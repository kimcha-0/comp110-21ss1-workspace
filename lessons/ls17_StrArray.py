"""Examples of vectorized operations."""

from __future__ import annotations
from typing import Union

class StrArray:
    """Utility class for common string operations."""
    values: list[str]
    def __init__(self, v: list[str]):
        """Initializing a StrArray object."""
        self.values = v
    
    def __repr__(self) -> str:
        """String representation of a StrArray object."""
        return f"StrArray({self.values})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        if isinstance(rhs, str):
            new_values: list[str] = []
            for i in self.values:
                new_values.append(i + rhs)
            return StrArray(new_values)
        else:
            assert len(self.values) == len(rhs.values)
            new_values: list[str] = []
            for i in range(len(self.values)):
                new_values.append(self.values[i] + rhs.values[i])
            return StrArray(new_values)
  
s: StrArray = StrArray(["a", "b", "c"])
t: StrArray = StrArray(["d", "e", "f"])
print(s)

print(s + "!")
print(s + t)
