"""
Note that the only difference between this implementation and the MinHeap implementation I provided earlier is in the _sift_up() and _sift_down() methods.
In the MaxHeap implementation, _sift_up() swaps an element with its parent if the parent is smaller than the element
while _sift_down() swaps an element with its larger child (if there is one).
"""


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self._sift_up(self.size - 1)

    def extract_max(self):
        if self.size == 0:
            return None
        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.heap.pop()
            self._sift_down(0)
            return max_val

    def delete(self, x):
        for i in range(self.size):
            if self.heap[i] == x:
                self.heap[i] = self.heap[self.size - 1]
                self.size -= 1
                self.heap.pop()
                self._sift_down(i)
                self._sift_up(i)
                return True
        return False

    def _sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _sift_down(self, i):
        max_index = i
        l = self.left_child(i)
        r = self.right_child(i)
        if l < self.size and self.heap[l] > self.heap[max_index]:
            max_index = l
        if r < self.size and self.heap[r] > self.heap[max_index]:
            max_index = r
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)
