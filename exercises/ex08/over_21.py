"""A program to determine names over 21."""

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your function here
    return None

# TODO 1: Define the over_21 function, and its logic, here.
def over_21(names: dict[str, int]) -> list[str]:
    """Takes a dictionary with names with their corresponding ages and returns a list with the people
    with ages over 21."""
    results: list[str] = []
    for age in names:
        if names[age] > 21:
            results.append(age)
    return results

if __name__ == "__main__":
    main()