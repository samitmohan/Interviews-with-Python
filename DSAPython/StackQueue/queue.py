# With and without using inbuilt methods.


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)


class QueueScratch:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.rear < self.front

    def enqueue(self, data):
        self.rear += 1
        self.queue.insert(self.rear, data)  # where and what

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.queue[self.front]
        self.front += 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def size(self):
        return self.rear - self.front + 1


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())  # Output: 2
print(q.is_empty())  # Output: False
print(q.size())  # Output: 2
