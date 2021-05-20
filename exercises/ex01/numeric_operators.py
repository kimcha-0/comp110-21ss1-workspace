"""Exercise 1, numberic operators."""

__author__ = "730407570"

# Your solution starts here...
left: str = input("Left hand side: ")
right: str = input("Right hand side: ")

print(left + " ** " + right + " is " + str(int(left) ** int(right)))
print(left + " / " + right + " is " + str(int(left) / int(right)))
print(left + " // " + right + " is " + str(int(left) // int(right)))
print(left + " % " + right + " is " + str(int(left) % int(right)))
