import pytest
from zestaw6.points import Point
from zestaw8.rectangles import Rectangle


def test_str():
    assert Rectangle(0, 0, 1, 4).__str__() == "[(0, 0), (1, 4)]"


def test_repr():
    assert Rectangle(0, 0, 1, 4).__repr__() == "Rectangle(0, 0, 1, 4)"


def test_eq():
    assert Rectangle(0, 0, 1, 4).__eq__(Rectangle(0, 0, 1, 4)) is True


def test_ne():
    assert Rectangle(0, 0, 1, 4).__ne__(Rectangle(1, 0, 2, 4)) is True


def test_area():
    assert Rectangle(0, 0, 1, 4).area() == 4
    assert Rectangle(-1, -1, 1, 1).area() == 4


def test_move():
    assert Rectangle(0, 0, 1, 4).move(3, -1) == Rectangle(3, -1, 4, 3)


def test_coordinates():
    assert Rectangle(0, 0, 1, 4).left == 0
    assert Rectangle(0, 0, 1, 4).bottom == 0
    assert Rectangle(0, 0, 1, 4).right == 1
    assert Rectangle(0, 0, 1, 4).top == 4


def test_size():
    assert Rectangle(0, 0, 1, 4).width == 1.0
    assert Rectangle(0, 0, 1, 4).height == 4.0


def test_center():
    assert Rectangle(0, 0, 2, 1).center == Point(1.0, 0.5)


def test_points():
    assert Rectangle(0, 0, 1, 4).bottom_left == Point(0, 0)
    assert Rectangle(0, 0, 1, 4).top_left == Point(0, 4)
    assert Rectangle(0, 0, 1, 4).bottom_right == Point(1, 0)
    assert Rectangle(0, 0, 1, 4).top_right == Point(1, 4)


if __name__ == '__main__':
    pytest.main()
