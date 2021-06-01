"""A number guessing game."""
__author__ = "730407570"

from random import randint

points: int = 0
player: str = ""
happy_face = "\U0001F600"

def main() -> None:
    """Entrypoint of the program and starts the game.""" 
    points: int = 0
    greet()
    print("Now, you have three options: Exit (type 0), Play version 1 (type 1), Play version 2 (type 2)")
    option: int = int(input("Type in your choice (0, 1, 2): "))
    is_playing: bool = True
    if option == 0:
        print(f"Thanks for checking us out. We hope to see you again. You accrued a total of {points} points. Great job!")
    
    elif option == 1:
        print(f"Let's begin. Points: {points}")
        while is_playing: 
            game(points)
            play_again: str = input("Play again? yes/no ")
            points += 10
            if play_again == "no":
                is_playing = False
            
        print(f"Thanks for checking us out. We hope to see you again. You accured a total of {points} points. Great job!")
    else:
        print(f"Let's begin. Points: {points}")
        while is_playing:
            other_game(points)
            play_again: str = input("Play again? yes/no ")
            points += 10
            if play_again == "no":
                is_playing = False
        print(f"Thanks for checking us out. We hope to see you again. Points: {points}")
    return None

def greet() -> None:
    print(f"Welcome to guess the number! A game where you, the user, guesses a number {happy_face}!")
    player: str = input("What is your name? ")
    ver_1: str = "In version one, you guess a number between 1-10."
    ver_2: str = "In version two, you guess a number between 1-20!"
    print(f"{player}, there are two versions for you to play.")
    print(f"{ver_1} {ver_2}")
    return None


def game(a: int) -> int:
    """Generates a random integer 1-10. If player is correct, add 10 points. 
    Returns the final point value to the function."""
    attempts: int = 1
    i = 100
    answer: int = randint(1,10)
    
    while attempts < i:
        user_guess: int = int(input("Take a guess: "))
        if user_guess != answer:
            print("Incorrect. Try again.")
            attempts += 1
        else: 
            print(f"Correct you guessed the correct number in {attempts} attempts and you receive 10 points.")
            break
    a += 10
    return a


def other_game(a: int) -> None:
    attempts: int = 1
    i = 100
    answer: int = randint(1,20)

    while attempts < i:
        user_guess: int = int(input("Take a guess: "))
        if user_guess != answer: 
            print("Incorrect. Try again.")
            attempts += 1
        else:
            print(f"Correct you guessed the correct number in {attempts} attempts and you receive 10 points.")
            break
    a += 10
    return a

if __name__ == "__main__":
    main()