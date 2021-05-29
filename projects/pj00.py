"""A number guessing game."""

def main() -> None:
    """Entrypoint of the program.""" 
    greet()   
    points: int = 0
    return None


def greet() -> None:
    print("Welcome to guess the number! A game where you, the user, guesses a number!")
    player: str = input("What is your name? ")


if __name__ == "__main__":
    """Calls the main function."""
    main()