# With and without using inbuilt methods.


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)


class StackScratch:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, data):
        self.stack.insert(self.top + 1, data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.stack[self.top]
        self.stack.pop(
            self.top
        )  # can do self.stack = self.stack[:self.top + 1] (without using pop)
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def size(self):
        return self.top + 1


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())
