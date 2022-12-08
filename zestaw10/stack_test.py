import unittest

from zestaw10.stack import Stack


class MyTestCase(unittest.TestCase):
    def setUp(self): pass

    def test_empty(self):
        self.assertTrue(Stack().is_empty())

    def test_full(self):
        stack = Stack()
        stack.push(2)
        stack.push(4)
        stack.push(6)
        stack.push(2)
        stack.push(0)
        stack.push(6)
        stack.push(-3)
        stack.push(1)
        stack.push(67)
        stack.push(5)
        self.assertTrue(stack.is_full())

    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.n, 0)
        stack.push(2)
        self.assertEqual(stack.n, 1)
        stack.push(5)
        stack.push(3)
        self.assertEqual(stack.n, 3)

    def test_pop(self):
        stack = Stack()
        stack.push(2)
        stack.push(4)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 4)


if __name__ == '__main__':
    unittest.main()
