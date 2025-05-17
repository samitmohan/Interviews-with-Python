# Implement PQ using heap

import heapq


class PQ:
    def __init__(self) -> None:
        self._queue = []  # _ : private
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(
            self._queue, (-priority, self._index, item)
        )  # min heap : - max heap
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0


q = PQ()
q.push("task 1", 3)
q.push("task 2", 1)
q.push("task 3", 2)

while not q.is_empty():
    print(q.pop())


# Without using heap (using array : O(N))


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, item, priority):
        self.queue.append((item, priority))

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty queue")
        highest_priority_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] > self.queue[highest_priority_index][1]:
                highest_priority_index = i  # update

        return self.queue.pop(highest_priority_index)[0]
