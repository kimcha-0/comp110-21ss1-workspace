"""Simple example of union types."""

from typing import Union

def add_or_concat(x: Union[str, int]) -> Union[str, int]:
    """Add or concatenate 10 depending on type."""
    if isinstance(x, int):
        return x + 10
    else:
        return x + str(10)

print(add_or_concat(5))