import math

from zestaw6.points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        # x1 < x2, y1 < y2
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Must be: x1 < x2 and y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return "[({x1}, {y1}), ({x2}, {y2})]".format(x1=self.pt1.x, y1=self.pt1.y,
                                                     x2=self.pt2.x, y2=self.pt2.y)

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return "{cl}({x1}, {y1}, {x2}, {y2})".format(cl=self.__class__.__name__, x1=self.pt1.x, y1=self.pt1.y,
                                                     x2=self.pt2.x, y2=self.pt2.y)

    # rect1 = rect2
    def __eq__(self, other):
        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y \
               and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y

    # rect1 != rect2
    def __ne__(self, other):
        return not self.pt1.x == other.pt1.x or not self.pt1.y == other.pt1.y \
               or not self.pt2.x == other.pt2.x or not self.pt2.y == other.pt2.y

    # zwraca środek prostokąta
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    # pole powierzchni
    def area(self):
        a = math.sqrt(math.pow(self.pt2.x - self.pt1.x, 2) + math.pow(self.pt1.y - self.pt1.y, 2))
        b = math.sqrt(math.pow(self.pt2.x - self.pt2.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2))
        return a * b

    # przesunięcie o (x, y)
    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    # część wspólna prostokątów
    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        x2 = min(self.pt2.x, other.pt2.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    # prostąkąt nakrywający oba
    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = min(self.pt1.y, other.pt1.y)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    # zwraca krotkę czterech mniejszych
    def make4(self):
        rectangle_1 = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)
        rectangle_2 = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        rectangle_3 = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        rectangle_4 = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        return rectangle_1, rectangle_2, rectangle_3, rectangle_4


if __name__ == '__main__':
    try:
        rect = Rectangle(2, 5, 1, 6)
        rect.__str__()
    except ValueError:
        print("Must be: x1 < x2 and y1 < y2")
