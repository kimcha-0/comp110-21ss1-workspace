"""Perfect squares and lists."""

def perfect_square(n: int) -> bool:
    i: int = 1
    while i < n:
        if i * i == n:
            return True
        i += 1
    return False