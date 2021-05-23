"""Fortune cookie boolean program."""

__author__ = "730407570"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
#
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100
from random import randint

# Begin your solution here...

fortune: int = randint(1,4)
print("Your fortune cookie says...")
if fortune == 1:
    print("You will find just what you were looking for.")
if fortune == 2:
    print("Soon, a sense of normalcy will be present in your life.")
if fortune == 3: 
    print("You will have a fulfilling and happy life.int")
if fortune == 4:
    print("Great difficulty is ahead, but you will persevere.")
    
print("Now, go spread positive vibes!")

