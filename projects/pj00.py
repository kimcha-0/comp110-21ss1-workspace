"""A number guessing game."""

def greet() -> None:
    print("Welcome to guess the number! A game where you, the user, guesses a number!")
    player: str = input("What is your name? ")
    return None


def main() -> None:
    """Entrypoint of the program.""" 
    greet()
    points: int = 0
    print("Now, you have three options: Exit,"
    choice: str =  input("What do you choose? ")
    if choice == "Exit" or "exit":
        print(f"Thanks for checking us out, we hope you come back again. Points: {points}.")
    return None


if __name__ == "__main__":
    """Calls the main function."""
    main()