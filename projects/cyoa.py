"""A number guessing game."""
from random import randint  
"""Above and beyond: Instead of simply adding a flat amount of points when the player guesses the 
number correctly,I introduced a condition that bases the amount of points rewarded on the number 
of attempts it takes the player to guess the number correctly. The less attempts it takes them, 
the more points they get. Further, I included two versions of this game with one having a wider 
range of numbers to guess from, thereby increasing the possible points that the player can receive."""


__author__ = "730407570"


points: int = 0
happy_face = "\U0001F600"
player: str = ""


def main() -> None:
    """Entrypoint of the program and starts the game.""" 
    str_1: str = "years old and you answered"
    str_2: str = "Thanks for checking us out. We hope to see you again."
    global points
    points = 0
    greet()
    # custom procedure
    print("Now, let's get to know you a little better. For each response, you will receive 10 points.")
    age: str = input("How old are you? ")
    if age != "":
        points += 10
    print(f"Total points: {points}")
    guessing: str = input("Are you good at guessing? ")
    if guessing != "":
        points += 10
    print(f"Total points: {points}")
    print(f"So, {player}, you're {age} {str_1} {guessing} to whether or not you are good at guessing.")
    print("Even if you aren't at least you got some points here before you start!")
    is_playing: bool = True
    while is_playing:
        print("Now, you have three options: Exit (type 0), Play version 1 (type 1), Play version 2 (type 2)")
        option: int = int(input("Type in your choice (0, 1, 2): "))
        
        if option == 0:
            print(f"{str_2} {player,} you accrued a total of {points} points. Great job!")
        
        elif option == 1:
            print(f"Let's begin. Total points: {points}")
            points += game(points)
                
            print(f"Total points: {points}")
        else:
            print(f"Let's begin. Points: {points}")
            points += other_game(points)
            print(f"Total points: {points}")
        play_again: str = input("Play again? yes/no ")
        if play_again == "no":
            is_playing = False
    print(f"{str_2} {player}, you accrued a total of {points} points. Great job!")
    return None


def greet() -> None:
    """Greets the player and prompts them for their name. Gives instructions to the game."""
    global player
    print(f"Welcome to guess the number! A game where you, the user, guesses a number {happy_face}!")
    player = input("What is your name? ")
    ver_1: str = "In version one, you guess a number between 1-10."
    ver_2: str = "In version two, you guess a number between 1-20!"
    point_rules: str = "The less attempts it takes you to guess the number, the more points you get!"
    print(f"{player}, there are two versions for you to play.")
    print(f"{ver_1} {ver_2}")
    print(f"{point_rules}")
    return None


# custom function 1
def game(a: int) -> int:
    """Generates a random integer 1-10 and returns the final point value to the function."""
    attempts: int = 1
    a = 0
    i = 100
    answer: int = randint(1, 10)
    
    while attempts < i: 
        user_guess: int = int(input(f"Take a guess {player}: "))
        if user_guess != answer:
            print(f"Incorrect, {player}. Try again.")
            attempts += 1
        else: 
            print(f"Correct, {player} you guessed the correct number in {attempts} attempts.")
            break
    if attempts <= 5:
        a += 20
    elif attempts > 5:
        a += 10
    print(f"{player}, you have received {a} points.")
    return a


# custom function 2
def other_game(a: int) -> int:
    """Guess the number between 1-20, outputs the updated points value."""
    attempts: int = 1
    i = 100
    answer: int = randint(1, 20)
    a = 0
    while attempts < i: 
        user_guess: int = int(input("Take a guess: "))
        if user_guess != answer: 
            print(f"Incorrect, {player}. Try again.")
            attempts += 1
        else:
            print(f"Correct, {player} you guessed the correct number in {attempts} attempts.")
            break
    if attempts <= 5: 
        a += 40
    elif attempts > 5 and attempts <= 10:
        a += 30
    elif attempts > 10 and attempts <= 15:
        a += 20
    else:
        a += 10
    print(f"{player}, you have received {a} points.")
    return a


if __name__ == "__main__":
    main()