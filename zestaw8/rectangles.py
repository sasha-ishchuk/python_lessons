import math
from zestaw6.points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Must be: x1 < x2 and y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({x1}, {y1}), ({x2}, {y2})]".format(x1=self.pt1.x, y1=self.pt1.y,
                                                     x2=self.pt2.x, y2=self.pt2.y)

    def __repr__(self):
        return "{cl}({x1}, {y1}, {x2}, {y2})".format(cl=self.__class__.__name__, x1=self.pt1.x, y1=self.pt1.y,
                                                     x2=self.pt2.x, y2=self.pt2.y)

    def __eq__(self, other):
        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y \
               and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y

    def __ne__(self, other):
        return not self.pt1.x == other.pt1.x or not self.pt1.y == other.pt1.y \
               or not self.pt2.x == other.pt2.x or not self.pt2.y == other.pt2.y

    def area(self):
        return self.width * self.height

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    @classmethod
    def from_points(cls, points):
        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)

    # LEFT

    @property
    def left(self):
        return self.pt1.x

    @left.setter
    def left(self, value):
        self.pt1.x = value

    @left.deleter
    def left(self):
        self.pt1.x = None

    # BOTTOM

    @property
    def bottom(self):
        return self.pt1.y

    @bottom.setter
    def bottom(self, value):
        self.pt1.y = value

    @bottom.deleter
    def bottom(self):
        self.pt1.y = None

    # RIGHT

    @property
    def right(self):
        return self.pt2.x

    @right.setter
    def right(self, value):
        self.pt2.x = value

    @right.deleter
    def right(self):
        self.pt2.x = None

    # TOP

    @property
    def top(self):
        return self.pt2.y

    @top.setter
    def top(self, value):
        self.pt2.y = value

    @top.deleter
    def top(self):
        self.pt2.y = None

    # WIDTH

    @property
    def width(self):
        return math.sqrt(math.pow(self.pt2.x - self.pt1.x, 2) + math.pow(self.pt1.y - self.pt1.y, 2))

    # HEIGHT

    @property
    def height(self):
        return math.sqrt(math.pow(self.pt2.x - self.pt2.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2))

    # CENTER

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    # BOTTOM LEFT POINT

    @property
    def bottom_left(self):
        return Point(self.pt1.x, self.pt1.y)

    @bottom_left.setter
    def bottom_left(self, point):
        self.pt1.x = point.x
        self.pt1.y = point.y

    @bottom_left.deleter
    def bottom_left(self):
        self.pt1.x = None
        self.pt1.y = None

    # TOP LEFT POINT

    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)

    @top_left.setter
    def top_left(self, point):
        self.pt1.x = point.x
        self.pt2.y = point.y

    @top_left.deleter
    def top_left(self):
        self.pt1.x = None
        self.pt2.y = None

    # BOTTOM RIGHT POINT

    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    @bottom_right.setter
    def bottom_right(self, point):
        self.pt2.x = point.x
        self.pt1.y = point.y

    @bottom_right.deleter
    def bottom_right(self):
        self.pt2.x = None
        self.pt1.y = None

    # TOP RIGHT POINT

    @property
    def top_right(self):
        return Point(self.pt2.x, self.pt2.y)

    @top_right.setter
    def top_right(self, point):
        self.pt2.x = point.x
        self.pt2.y = point.y

    @top_right.deleter
    def top_right(self):
        self.pt2.x = None
        self.pt2.y = None


if __name__ == '__main__':
    my_points = [Point(0, 0), Point(2, 1)]
    rect = Rectangle.from_points(my_points)
    print(rect.__str__())

    print(rect.center)



