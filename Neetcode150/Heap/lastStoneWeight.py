# https://leetcode.com/problems/last-stone-weight/description/
# Easy rules given -> implement. [max_heap]
# Python only provides min heap. To get max heap : Negate your values when you store them in the heap
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * s for s in stones]
        heapq.heapify(heap)  # O(n)
        while len(heap) > 1:  # while only 1 element is left
            # remove two stones
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, first - second)
        # edge case : if stones empty
        if len(heap) == 0:
            return 0
        return -1 * heap[0]  # first element (converting - val to pos by * -1)
