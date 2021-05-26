"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730407570"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None


# TODO 1: Define your fortune_cookie function here.


def fortune_cookie() -> str:
    fortune: int = randint(1, 4)
    if fortune == 1:
        return "You will have a long and prosperous life."
    else: 
        if fortune == 2:
            return "Great trouble is ahead, but you will persevere"
        else: 
            if fortune == 3:
                return "You will meet a lifelong friend."
            else:
                return "You will have a fun and productive summer."
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 

if __name__ == "__main__":
    main()

