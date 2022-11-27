import gc


class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node     # stary head
            self.head = node          # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node     # stary tail
            self.tail = node          # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node

    # FUNCTIONS FROM TASK 9.3

    def find_max(self):
        if self.is_empty():
            return None

        temp = max_node = self.head

        while temp is not None:
            if temp.data > max_node.data:
                max_node = temp
            temp = temp.next

        return max_node

    def find_min(self):
        if self.is_empty():
            return None

        temp = min_node = self.head

        while temp is not None:
            if temp.data < min_node.data:
                min_node = temp
            temp = temp.next

        return min_node

    def remove(self, node):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.data == node.data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == node.data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == node.data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.length -= 1

    def clear(self):
        if self.is_empty():
            raise ValueError("pusta lista")

        while self.head:
            self.remove_head()

    def show(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def make_str(self):
        string_list = ""
        curr = self.head
        while curr:
            string_list += str(curr.data) + " "
            curr = curr.next
        return string_list


if __name__ == '__main__':
    s_list1 = DoubleList()
    s_list1.insert_head(Node(2))
    s_list1.insert_head(Node(5))
    s_list1.insert_head(Node(3))
    s_list1.insert_head(Node(-3))
    s_list1.insert_head(Node(8))

    s_list1.show()  # [8, -3, 3, 5, 2]

    s_list1.insert_tail(Node(15))
    s_list1.show()  # [8, -3, 3, 5, 2, 15]

    node = s_list1.find_min()
    print(node)     # -3
    node = s_list1.find_max()
    print(node)     # 15

    s_list1.remove_tail()
    s_list1.remove_tail()
    s_list1.show()  # [8, -3, 3, 5]

    s_list1.remove_head()
    s_list1.show()  # [-3, 3, 5]

    s_list1.remove(Node(3))
    s_list1.show()  # [-3, 5]

    s_list1.clear()
    print(s_list1.is_empty())     # True

