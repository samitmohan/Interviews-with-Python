# https://leetcode.com/problems/find-median-from-data-stream/description/
# https://www.youtube.com/watch?v=itmhHWaHupI (helps a lot)
"""
Getting the middle from a sorted list : easy
Add elements in order : getMedian : O(1) but array : O(n) = to improve use heap
    2 subsets : [1,2,3,4] : [1,2] and [3,4] all elements in left <= all elements in right
Small heap and large heap : all elements in small heap <= all elements in large heap (size of them approx same)
Small heap : maxheap
Large heap : minheap
[1,2] [3,4]
To check maxheap from small heap : 2 and minheap from large heap gives 3 and 2 <=3 (max(small) <= max(large))
+ another reason : median : [1,2,3,4] = (maxvalue of minheap + minvalue of maxheap)/2 : 2 + 3 / 2 = 2.5
if len of one heap is greater than other by 1 : approx equal
len(A) > len(B) : odd number
    max from A [1,2,3] : 3 -> median :: [1,2,3] [3,4] = 3

By default the elements can go in any heap : small heap (if ppt failing -> remove max from small heap and add to
large heap) Similarly if len(B) >> len(A) : move min element from large heap and move to small heap MAKE SURE
DIFFERENCE BETWEEN BOTH HEAPS IS LESS OR EQUAL TO 1"""

import heapq


class MedianFinder:
    def __init__(self):
        # two heaps : large = minheap and small : maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)  # max heap in python = -1 *
        # make sure every num in small = every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            # some value in small heap > value in large heap : wrong -> pop and shift to large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size? difference is 2 or more
        if (
            len(self.small) > len(self.large) + 1
        ):  # small is too big -> pop from small and push in large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if (
            len(self.large) > len(self.small) + 1
        ):  # large is too big -> pop from large and push in small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(
            self.large
        ):  # odd elements (small has one more extra element)
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # both equal : median
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
