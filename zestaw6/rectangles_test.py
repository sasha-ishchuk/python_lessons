import unittest
from zestaw6.rectangles import Rectangle
from zestaw6.points import Point


class MyTestCase(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(Rectangle(2, 0, 1, 4).__str__(), "[(2, 0), (1, 4)]")

    def test_repr(self):
        self.assertEqual(Rectangle(2, 0, 1, 4).__repr__(), "Rectangle(2, 0, 1, 4)")

    def test_eq(self):
        self.assertTrue(Rectangle(2, 0, 1, 4).__eq__(Rectangle(2, 0, 1, 4)))

    def test_ne(self):
        self.assertTrue(Rectangle(2, 0, 1, 4).__ne__(Rectangle(1, 0, 1, 4)))

    def test_center(self):
        self.assertEqual(Rectangle(2, 0, 1, 4).center(), Point(1.5, 2))

    def test_area(self):
        self.assertEqual(Rectangle(2, 0, 1, 4).area(), 4)
        self.assertEqual(Rectangle(2, 0, 2, 4).area(), 0)
        self.assertEqual(Rectangle(-1, -1, 1, 1).area(), 4)

    def test_move(self):
        self.assertEqual(Rectangle(2, 0, 1, 4).move(3, -1), Rectangle(5, -1, 4, 3))


if __name__ == '__main__':
    unittest.main()
