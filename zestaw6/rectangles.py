import math
from zestaw6.points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
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

    # obsługa rect1 != rect2
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
