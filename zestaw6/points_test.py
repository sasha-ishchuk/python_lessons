import math
import unittest
from zestaw6.points import Point


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(Point(2, 4).__str__(), "(2, 4)")

    def test_repr(self):
        self.assertEqual(Point(2, 4).__repr__(), "Point(2, 4)")

    def test_eq(self):
        self.assertTrue(Point(2, 4).__eq__(Point(2, 4)))

    def test_ne(self):
        self.assertTrue(Point(2, 4).__ne__(Point(2, 9)))

    def test_add(self):
        self.assertEqual(Point(2, 4).__add__(Point(1, 3)), Point(3, 7))

    def test_sub(self):
        self.assertEqual(Point(2, 4).__sub__(Point(1, 3)), Point(1, 1))

    def test_mul(self):
        self.assertEqual(Point(2, 4).__mul__(Point(1, 3)), 14)

    def test_cross(self):
        self.assertEqual(Point(2, 4).cross(Point(1, 3)), 2)

    def test_length(self):
        self.assertEqual(Point(2, 4).length(), math.sqrt(20))


if __name__ == '__main__':
    unittest.main()
