"""List utility functions for unit testing."""


def all(xs: list[int], needle: int) -> bool:
    """Return True if all elements are equal to the needle."""
    if len(xs) == 0:
        return False
    i: int = 0
    while i < len(xs):
        if xs[i] != needle:
            return False
        i += 1
    return True


def sub(a: list[int], start: int, end: list) -> list[int]:
    """Construction of a sub list based on input range."""
    if a == [] or start >= end:
        return []
    elif start < 0:
        start = 0
    elif end > len(a):
        end = len(a)
    result: list[int] = []
    for i in range(start, end):
        result.append(a[i])
    
    # i: int = start
    # while i < end:
    #     result.append(a[i])
    #     i += 1
    return result

print(sub([1, 2, 3, 4], 1, 3))

def concat(a: list[int], b: list[int]) -> list[int]:
    """Combine two lists into one."""
    result: list[int] = []
    for elt in a:
        result.append(elt)
    for elt in b:
        result.append(elt)
    return result

# def concat_2(a: list[int], b: list [int]) -> list[int]:
#     """Combine two lists into one with a while loop."""
#     result: list[int] = []
#     i: int = 0
#     while i < len(a):
#         result.append(a[i])
#         i += 1
#     j: int = 0
#     while j < len(b):
#         result.append(b[j])
#         j += 1
#     return result

def max(xs: list[int]) -> int:
    """Finds the maximum value in a list."""
    if len(xs) == 0:
        raise ValueError("max was given no args")
    curr_max: int = xs[0]
    i: int = 1
    while i < len(xs):
        if xs[i] > curr_max:
            curr_max = xs[i]
        i += 1
    return curr_max


