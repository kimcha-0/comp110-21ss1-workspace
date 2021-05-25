"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407570"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = randint(1, 4)

if fortune == 1:
    print("You will have a long and prosperous life.")
else:
    if fortune == 2:
        print("Great trouble is ahead, but you will persevere.")
    if fortune == 3: 
        print("You will meet a lifelong friend.")
    if fortune == 4: 
        print("You will a fun and productive summer.")

print("Now, you will go spread positive vibes!")