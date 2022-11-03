from zestaw5 import polys as p
import unittest


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]  # W(x) = x
        self.p2 = [0, 0, 1]  # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(p.add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(p.sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(p.mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        self.assertEqual(p.is_zero(self.p1), False)

    def test_eq_poly(self):
        self.assertEqual(p.eq_poly(self.p1, self.p2), False)

    def test_eval_poly(self):
        self.assertEqual(p.eval_poly(self.p2, 5), 25)

    def test_combine_poly(self):
        self.assertEqual(p.combine_poly(self.p1, self.p2), [0, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(p.pow_poly(self.p2, 2), [0, 0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(p.diff_poly(self.p2), [0, 2])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
