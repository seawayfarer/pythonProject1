import json

class JSONContextManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            return data

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with JSONContextManager('path/to/json/file.json') as data:
    print(data)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
print(p1)

p2 = Point(-1, 4)
print(p2)


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def contains_point(self, point):
        return (self.top_left.x <= point.x <= self.bottom_right.x and
                self.bottom_right.y <= point.y <= self.top_left.y)

    def __contains__(self, point):
        return self.contains_point(point)


# Creating a rectangle
        top_left = Point(0, 5)
        bottom_right = Point(10, 0)
        rectangle = Rectangle(top_left, bottom_right)

# Checking if the rectangle contains a point
        point = Point(5, 3)
        print(rectangle.contains_point(point))

# Using the 'in' operator to check if a point is inside a rectangle
        point = Point(7, 6)
        print(point in rectangle)
