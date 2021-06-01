"""Perfect squares and lists."""

def perfect_square(n: int) -> bool:
    i: int = 1
    while i < n:
        if i * i == n:
            return True
        i += 1
    return False

def squares(start: int, stop: int) -> list[int]:
    """Prints all perfect squares in a range."""
    i: int = start
    result: list[int] = []
    while i < stop:
        if perfect_square(i):
            result.append(i)
        i += 1
    return result