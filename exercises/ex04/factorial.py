"""An exercise in computing the factorial of an int."""

__author__ = "730407570"


# Begin your solution here...
number: int = int(input("Choose a number: "))

integer: int = 1

while number > 0:
    integer *= number
    number -= 1

print(integer)