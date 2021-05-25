"""An exercise in remainders and boolean logic."""

__author__ = "730407570"


# Begin your solution here...
integer_str: str = input("Enter an int: ")

integer = int(integer_str)

if integer % 2 == 0 and integer % 7 != 0:
    print("TAR")
if integer % 7 == 0 and integer % 2 != 0:
    print("HEELS")
elif integer % 7 == 0 and integer % 2 == 0:
    print("TAR HEELS")
else:
    print("CAROLINA")