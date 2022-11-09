import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # return string "(x, y)"
    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    # return string "Point(x, y)"
    def __repr__(self):
        return "{cl}({x}, {y})".format(cl=self.__class__.__name__, x=self.x, y=self.y)

    # return point1 == point2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # return point1 != point2
    def __ne__(self, other):
        return not self.x == other.x or not self.y == other.y

    # v1 + v2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # v1 - v2
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # długość wektora
    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    # bazujemy na tuple, immutable points
    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == '__main__':
    point = Point(2, 4)
    point1 = Point(1, 1)
    point2 = Point(2, 4)

    print(point.__str__())
    print(point.__repr__())

    print(point.__eq__(point1))  # False
    print(point.__eq__(point2))  # True

    print(point.__ne__(point1))  # True
    print(point.__ne__(point2))  # False

    a = point.__add__(point1)
    print(a.__str__())  # (3, 5)

    b = point.__sub__(point1)
    print(b.__str__())  # (1, 3)

    print(point.__mul__(point2))    # 20
    print(point.cross(point1))      # -2

    print(point.length())           # sqrt(20) = ~4,47

    print(point.__hash__())
