"""TODO: Describe your scene program."""

__author__ = "730407570"

import turtle
import math

# def main() -> None:
#     """The entrypoint of my scene."""
#     # TODO: Declare your Turtle variable(s) here.
#     Bob: Turtle = Turtle()
#     # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
#     draw_square(Bob, 0, 0, 2)
#     done()


# # TODO: Define the procedures for other components in your scene here. 
# # example procedure
# def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
#     """Draw a square of the given width whose top left corner is located at x, y."""
#     a_turtle.penup()
#     a_turtle.goto(x, y)
#     a_turtle.setheading(0.0)
#     a_turtle.pendown()
#     i: int = 0
#     while i < 4:
#         a_turtle.forward(width)
#         a_turtle.right(90)
#         i += 1

def fibo(n):
    a: int = 0
    b: int = 1
    square_a = a
    square_b = b

    # Setting the color of the pen
    x.pencolor("blue")
    
    # Drawing the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.backward(square_a * factor)
        x.right(90)  
        x.backward(square_a * factor)
        x.right(90)  
        x.backward(square_a * factor)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
    # Bringing thepen to starting point
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Setting the color of the plotting pen to red  
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1
 
# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))
 
# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fibo(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")
# TODO: Use the __name is "__main__" idiom

# if __name__ == "__main__":
#     main()