import unittest

from zestaw6.points import Point
from zestaw7.rectangles import Rectangle


class MyTestCase(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).__str__(), "[(-2, 0), (2, 4)]")

    def test_repr(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).__repr__(), "Rectangle(-2, 0, 2, 4)")

    def test_eq(self):
        self.assertTrue(Rectangle(-2, 0, 2, 4).__eq__(Rectangle(-2, 0, 2, 4)))

    def test_ne(self):
        self.assertTrue(Rectangle(-2, 0, 2, 4).__ne__(Rectangle(1, 0, 5, 4)))

    def test_center(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).center(), Point(0, 2))

    def test_area(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).area(), 16)

    def test_move(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).move(3, -1), Rectangle(1, -1, 5, 3))

    def test_intersection(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).intersection(Rectangle(-1, 1, 3, 4)), Rectangle(-1, 1, 2, 4))

    def test_cover(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).cover(Rectangle(-1, 1, 3, 4)), Rectangle(-2, 0, 3, 4))

    def test_make4(self):
        self.assertEqual(Rectangle(-2, 0, 2, 4).make4(), (Rectangle(-2, 0, 0, 2), Rectangle(0, 2, 2, 4),
                         Rectangle(-2, 2, 0, 4), Rectangle(0, 0, 2, 2)))


if __name__ == '__main__':
    unittest.main()
