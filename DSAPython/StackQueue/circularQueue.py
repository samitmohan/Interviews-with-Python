"""
(index + 1) % size = newIndex
[1,2,3,4,5]
4 + 1 % 5 = 0 : put new element in the beginning
"""


class MyCircularQueue:
    def __init__(self, k: int):  # k is the size
        if k == 0:
            raise Exception
        self.q = [0] * k
        self.rear = 0
        self.front = 0
        self.size = 0
        self.max_size = k

    # put element
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # put element in rear
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1
        return True

    # remove element
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # increment front pointer by one and decrement size
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

        # get first element

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
