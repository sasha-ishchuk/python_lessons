# TASK 10.2

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stack is full")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data

    # help function to print the Stack
    def show(self):
        for i in range(self.n):
            print(self.items[i], end=" ")
        print()


if __name__ == '__main__':
    stack = Stack()

    stack.push(2)
    stack.push(8)
    stack.show()

    print(stack.pop())
    stack.show()
