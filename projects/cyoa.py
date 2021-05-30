"""A number guessing game."""
from random import randint

points: int = 0
NAMED_CONSTANT: STR = "\U00000000"

def main() -> None:
    """Entrypoint of the program and starts the game.""" 
    greet()
    print("Now, you have three options: Exit (type 0), Play version 1 (type 1), Play version 2 (type 2)")
    option: int = int(input("Type in your choice (0, 1, 2): "))
    if option == 0:
        print(f"Thanks for checking us out. We hope to see you again. Points: {points}")
    elif option == 1:
        print(f"Let's begin. Points: {points}")
        game()
    else:
        print(f"Let's begin. Points: {points}")
        other_game()
    return None

def greet() -> None:
    print("Welcome to guess the number! A game where you, the user, guesses a number!")
    player: str = input("What is your name? ")
    ver_1: str = "In version one, you guess a number between 1-10."
    ver_2: str = "In version two, you guess a number between 1-100!"
    print(f"{player}, there are two versions for you to play. {ver_1} {ver_2}")
    return None


def game() -> int:
    """Generates a random integer 1-10. If player is correct, add 10 points."""
    answer: int = randint(1,10)
    attempt: int = int(input("Take a guess: "))


def other_game(x: int) -> int:
    return x
    

if __name__ == "__main__":
    """Calls the main function."""
    main()