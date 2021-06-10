from __future__ import annotations
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def __add__(self, other: Point) -> Point:
        print("In special method!!!")
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def __mul__(self, other: Point) -> Point:
        print("In special multiplication method!!")
        x: float = self.x * other.x
        y: float = self.y * other.y
        return Point(x, y)
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    def __gt__(self, other: Point) -> bool:
        return self.x > self.x
a: Point = Point(1.0, 2.0)
b: Point = Point(3.0, 4.0)

f: bool = a > b
print(f)
print(a[1])
# c: Point = a.add(b)
# print(f"Point C: {c.x}, {c.y}")
# d: Point = a + b
# print(f"Point D: {d.x}, {d.y}")
# e: Point = a * b
# print(f"Point E: {e.x}, {e.y}")