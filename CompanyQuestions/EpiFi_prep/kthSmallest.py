# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/
# Time : O(M * N * logK) Space : O(K)
class Solution:
    def kthSmallest(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])
        heap = []  # maxHeap
        for r in range(rows):
            for c in range(cols):
                heappush(heap, -matrix[r][c])  # min heap
                if len(heap) > k:
                    heappop(heap)  # pop all

        return -heappop(heap)
