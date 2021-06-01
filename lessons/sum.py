"""Sums the elements of a list."""

def sum(xs: list[int]) -> int:
    """Summation of input list is returned."""
    total: int = 0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total