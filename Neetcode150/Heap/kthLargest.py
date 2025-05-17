# https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
4,5,8,2 : k = 3
while len(nums) > k: pop
4,5,8 : min value : kth largest : 3rd largest value : 8,5,4 = 4

add() : just push to heap and pop the latest element only if size overflow (4 elements but k = 3, need to pop)

1) convert to min heap
    2) keep popping until heap.size() == 3 (then the top element of heap is our answer)
3) insert new values into heap
    4) do the same (keep popping until new heap.size() = k (size))
5) Top element of pq = answer for that val.
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # heap nums with k elements

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:  # if overflow
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # min element = 0th element in min heap.


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
