"""Examples of object-oriented programming concepts."""

# class name
class Point: 
    """Represents a 2D Point."""

    # Define attributes (related variables)
    x: float = 0.0
    y: float = 0.0
    # Define our own constructor
    def __init__(self, x: float, y: float): 
        """Construct a point by giving a specific x and y."""
        # update our attributes to be assigned the value of the parameters
        self.x = y
        self.y = y
    # define methods to give each object of your class certain capabilities
    def translate_x(self, dx: float) -> None:
        """Translate the point in the x direction."""
        # Mutate the object it is called on
        self.x += dx
        return None
    
    def reset_y(self) -> float:
        """Return the current value of y and then reset it."""
        result: float = self.y
        self.y = 0
        return result


# declared a new Point object
# to give it an initial value, we need to call the Constructor
a: Point = Point(2.0, 3.0)
b: Point = Point(2.0, -1.0)
# Method call! We provide the specific object being used and the method
# name with arguments.
a.translate_x(-6.0)
a.translate_x(1.0)
b.translate_x(1.0)

a.reset_y()
# access attributes using the dot operator.
print(f"The y value is {a.y}")
# you can also directly update attributes using the dot operator
# <location> = <new_value>
a.x = 20

b: Point(2.0, -1.0)
# b.x = 2.0
# b.y = -1.0