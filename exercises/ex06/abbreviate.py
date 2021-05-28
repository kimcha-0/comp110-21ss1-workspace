"""A function to abbreviate strings."""

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    word: str = input("Write some text with some uppercase letters: ")
    print("The abbreviation is " + abbreviate(word))
    return None

# TODO 1: Define the abbreviate function, and its logic, here. 
def abbreviate(x: str) -> str: 
    i = 0
    abbreviation: str = ""
    while i < len(x):
        if x[i].isupper():
            abbreviation += x[i]
        i += 1
    return abbreviation


if __name__ == "__main__":
    main()