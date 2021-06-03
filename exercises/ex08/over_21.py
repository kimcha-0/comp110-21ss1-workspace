"""A program to determine names over 21."""

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your function here
    s: dict[str, int] = {"David": 20, "Sahil": 21}
    print(over_21(s))
    return None


# TODO 1: Define the over_21 function, and its logic, here.
def over_21(x: dict[str, int]) -> list[str]:
    over_21_names: list[str] = []
    for i in x:
        if x[i] >= 21:
            over_21_names.append(i)
    return over_21_names
        

if __name__ == "__main__":
    main()