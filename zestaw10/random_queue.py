# TASK 10.8
from random import randint


class RandomQueue:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    # O(1)
    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full")
        self.items[self.n] = item
        self.n += 1

    # O(1), returns random element
    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        rand = randint(0, self.n - 1)
        data = self.items[rand]

        self.items[rand] = self.items[self.n - 1]
        del self.items[self.n - 1]
        self.n -= 1

        return data

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.n == self.size

    def clear(self):
        for i in range(self.n):
            self.n -= 1
            self.items[i] = None

    # help function to print the Stack
    def show(self):
        for i in range(self.n):
            print(self.items[i], end=" ")
        print()


if __name__ == '__main__':
    queue = RandomQueue()
    queue.insert(5)
    queue.insert(2)
    queue.insert(4)
    queue.show()

    print("\n" + str(queue.remove()))
    queue.show()

    queue.clear()
    print(queue.is_empty())
