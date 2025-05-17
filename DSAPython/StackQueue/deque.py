class Deque:
    def __init__(self):
        self._deque = []

    def push_front(self, item):
        self._deque.insert(0, item)

    def push_back(self, item):
        self._deque.append(item)

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty deque")
        return self._deque.pop(0)

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty deque")
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


# From scratch


class DequeNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DequeScratch:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, value):
        new_node = DequeNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = DequeNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value


d = Deque()
d.push_front("a")
d.push_back("b")
d.push_front("c")
d.push_back("d")
while not d.is_empty():
    print(d.pop_front(), d.pop_back())
