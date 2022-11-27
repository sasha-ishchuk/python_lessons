import unittest

from zestaw9.singlelist import SingleList
from zestaw9.singlelist import Node


class MyTestCase(unittest.TestCase):

    single_list = None

    def setUp(self):
        self.single_list = SingleList()
        self.single_list.insert_head(Node(2))
        self.single_list.insert_head(Node(5))
        self.single_list.insert_head(Node(3))

    # here we test make_str() function, because all next results
    # will be testing by representing the list as a string
    def test_make_str(self):
        self.assertEqual(self.single_list.make_str(), "3 5 2 ")

    def test_is_empty(self):
        self.assertTrue(SingleList().is_empty())
        self.assertEqual(self.single_list.is_empty(), False)

    def test_count(self):
        self.assertEqual(self.single_list.count(), 3)

    def test_insert_head(self):
        self.single_list.insert_head(Node(1))
        self.assertEqual(self.single_list.make_str(), "1 3 5 2 ")

    def test_insert_tail(self):
        self.single_list.insert_tail(Node(7))
        self.assertEqual(self.single_list.make_str(), "3 5 2 7 ")

    def test_remove_head(self):
        self.single_list.remove_head()
        self.assertEqual(self.single_list.make_str(), "5 2 ")

    # TESTS FOR FUNCTIONS FROM TASK 9.1

    def test_remove_tail(self):
        self.single_list.remove_tail()
        self.assertEqual(self.single_list.make_str(), "3 5 ")

    def test_join(self):
        lst = SingleList()
        lst.insert_head(Node(1))
        lst.insert_head(Node(-9))
        self.single_list.join(lst)
        self.assertEqual(self.single_list.make_str(), "3 5 2 -9 1 ")

    def test_clear(self):
        self.single_list.clear()
        self.assertEqual(self.single_list.is_empty(), True)

    # TESTS FOR FUNCTIONS FROM TASK 9.2

    def test_search(self):
        node = self.single_list.search(5)
        self.assertEqual(node.data, 5)
        self.assertEqual(self.single_list.search(33), None)

    def test_find_min(self):
        node = self.single_list.find_min()
        self.assertEqual(node.data, 2)

    def test_find_max(self):
        node = self.single_list.find_max()
        self.assertEqual(node.data, 5)

    def test_reverse(self):
        self.single_list.reverse()
        self.assertEqual(self.single_list.make_str(), "2 5 3 ")


if __name__ == '__main__':
    unittest.main()
