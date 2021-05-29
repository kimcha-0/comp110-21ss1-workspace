"""A number guessing game."""
from random import randint

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
    return 


def other_game(x: int) -> int:
    return x

def main() -> None:
    """Entrypoint of the program and starts the game.""" 
    greet()
    points: int = 0
    print("Now, you have three options: Exit, Play, Play a different game")
    choice: str = input("What do you choose? ")
    if choice == "Exit" or "exit":
        print(f"Thanks for checking us out, we hope you come back again. Points: {points}")
    elif choice == "Play" or "play":
        print(f"Let's begin. Points: {points}")
        game()
    else:
        print(f"Let's play! Points: {points}")
        other_game()

    return None


if __name__ == "__main__":
    """Calls the main function."""
    main()