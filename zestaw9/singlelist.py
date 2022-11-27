# zadania 9.1 oraz 9.2

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:

    # nie trzeba obliczać za każdym razem
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    # return self.length == 0
    def is_empty(self):
        return self.head is None

    # tworzymy interfejs do odczytu
    def count(self):
        return self.length

    # add to end
    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        # pusta lista
        else:
            self.head = self.tail = node
        self.length += 1

    # O(1)
    def insert_tail(self, node):
        # dajemy na koniec listy
        if self.head:
            self.tail.next = node
            self.tail = node
        # pusta lista
        else:
            self.head = self.tail = node
        self.length += 1

    # O(1)
    def remove_head(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        # self.length == 1
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        # czyszczenie łącza
        node.next = None
        self.length -= 1
        # zwracamy usuwany node
        return node

    # FUNCTIONS FROM TASK 9.1

    # O(n)
    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")

        if self.head == self.tail:
            self.head = self.tail = None
            return None

        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None
        self.length -= 1
        return curr

    def join(self, other):
        if self.is_empty():
            self.head = other.head
            return self.head

        if other.is_empty():
            return self.head

        curr = self.head
        while curr.next:
            curr = curr.next

        temp = curr.next
        curr.next = other.head
        while other.head.next is not None:
            other.head = other.head.next

        other.head.next = temp
        return self.head

    def clear(self):
        if self.is_empty():
            raise ValueError("pusta lista")

        while self.head:
            self.remove_head()

    # FUNCTIONS FROM TASK 9.2

    # O(n)
    def search(self, data):
        if self.is_empty():
            return None

        if self.head.data == data:
            return self.head

        curr = self.head
        while curr.next is not None:
            if curr.next.data == data:
                break
            curr = curr.next
        return curr.next

    # O(n)
    def find_min(self):
        if self.is_empty():
            return None

        curr = self.head
        min_node = curr
        while curr.next is not None:
            if curr.next.data < min_node.data:
                min_node = curr.next
            curr = curr.next
        return min_node

    # O(n)
    def find_max(self):
        if self.is_empty():
            return None

        curr = self.head
        max_node = curr
        while curr.next is not None:
            if curr.next.data > max_node.data:
                max_node = curr.next
            curr = curr.next
        return max_node

    # O(n)
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # help function to display list
    # it displays FROM HEAD (from end to start)
    def show(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    # help function needed for testing other functions
    # from SingleList class (in 'singlelist_test.py' file)
    def make_str(self):
        string_list = ""
        curr = self.head
        while curr:
            string_list += str(curr.data) + " "
            curr = curr.next
        return string_list


if __name__ == '__main__':
    s_list1 = SingleList()
    s_list1.insert_head(Node(2))
    s_list1.insert_head(Node(5))
    s_list1.insert_head(Node(3))
    s_list1.insert_head(Node(-3))
    s_list1.insert_head(Node(8))

    s_list1.show()  # [8, -3, 3, 5, 2]

    print(s_list1.find_min())  # -3
    print(s_list1.find_max())  # 8

    s_list1.remove_tail()
    s_list1.remove_tail()
    s_list1.show()  # [8, -3, 3]

    s_list1.reverse()
    s_list1.show()  # [3, -3, 8]

    node = s_list1.search(6)
    print(node)  # None
    node = s_list1.search(3)
    print(node)  # 3

    s_list2 = SingleList()
    s_list2.insert_head(Node(7))
    s_list2.insert_head(Node(1))

    # s_list1 = [3, -3, 8]
    # s_list2 = [1, 7]
    s_list1.join(s_list2)
    s_list1.show()  # [3, -3, 8, 1, 7]

    s_list1.clear()
    print(s_list1.is_empty())  # True

    s_list1.join(s_list2)
    s_list1.show()  # [7]
