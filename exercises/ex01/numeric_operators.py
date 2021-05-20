"""Exercise 1, numberic operators."""

__author__: str = "730407570"

# Your solution starts here...
left_num: str = input("Left hand side: ")
right_num: str = input("Right hand side: ")

print(left_num + " ** " + right_num + " is " + str(int(left_num) ** int(right_num)))
print(left_num + " / " + right_num + " is " + str(int(left_num) / int(right_num)))
print(left_num + " // " + right_num + " is " + str(int(left_num) // int(right_num)))
print(left_num + " % " + right_num + " is " + str(int(left_num) % int(right_num)))
