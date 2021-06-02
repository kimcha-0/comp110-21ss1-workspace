"""An exercise with functions and lists."""

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Test your functions here
    print(list_primes(1, 10))
    return None


# TODO 1: Define the is_prime function, and its logic, here.
def is_prime(n: int) -> bool:
    """Tests if the integer input n is prime."""
    i: int = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    if n <= 1:
        return False
    return True


# TODO 2: Define the list_primes function, and its logic, here.
def list_primes(start: int, stop: int) -> list[int]:
    """Takes a range of integers and returns the prime numbers in a list."""
    i: int = start
    result: list[int] = []
    while i < stop:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


if __name__ == "__main__":
    main()