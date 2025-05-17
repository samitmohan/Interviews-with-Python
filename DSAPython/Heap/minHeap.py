"""
_sift_up() and _sift_down() methods are used to maintain the heap property after adding or removing an element.
siftDown swaps a node that is too small with its largest child (thereby moving it down) until it is at least as large as both nodes below it.
siftUp swaps a node that is too large with its parent (thereby moving it up) until it is no larger than the node above it.
"""


class MinHeap:
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

    def extract_min(self):
        if self.size == 0:
            return None
        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.heap.pop()
            self._sift_down(0)
            return min_val

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
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        r = self.right_child(i)
        if l < self.size and self.heap[l] < self.heap[min_index]:
            min_index = l
        if r < self.size and self.heap[r] < self.heap[min_index]:
            min_index = r
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)
