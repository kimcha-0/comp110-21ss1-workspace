"""A function to abbreviate strings."""

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    word: str = input("Write some text with some uppercase letters: ")
    print("The abbreviation is " + abbreviate(word))
    return None

# TODO 1: Define the abbreviate function, and its logic, here.
def abbreviate(x: str) -> str:
    return str(x)


if __name__ == "__main__":
    main()