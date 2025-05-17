# https://leetcode.com/problems/range-sum-query-mutable/
# Explanation : DSAPython/Tree/segmentTree.py
import math
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        x = math.ceil(math.log2(self.n))
        max_size = 2 * pow(2, x) - 1
        self.st = [0] * max_size
        self._constructSegTree_helper(nums, 0, self.n - 1, self.st, 0)

    def _getMid(self, start, end):
        return start + (end - start) // 2

    def _constructSegTree_helper(self, arr, ss, se, st, si):
        if ss == se:
            st[si] = arr[ss]
            return arr[ss]
        mid = self._getMid(ss, se)
        st[si] = self._constructSegTree_helper(
            arr, ss, mid, st, si * 2 + 1
        ) + self._constructSegTree_helper(arr, mid + 1, se, st, si * 2 + 2)
        return st[si]

    def update(self, index: int, val: int) -> None:
        if index < 0 or index >= self.n:
            return
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update_helper(0, self.n - 1, index, diff, 0)

    def _update_helper(self, ss, se, i, diff, si):
        if i < ss or i > se:
            return
        self.st[si] += diff
        if se != ss:
            mid = self._getMid(ss, se)
            self._update_helper(ss, mid, i, diff, 2 * si + 1)
            self._update_helper(mid + 1, se, i, diff, 2 * si + 2)

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right >= self.n or left > right:
            return -1
        return self._getSum_helper(0, self.n - 1, left, right, 0)

    def _getSum_helper(self, ss, se, qs, qe, si):
        if qs <= ss and qe >= se:
            return self.st[si]
        if se < qs or ss > qe:
            return 0
        mid = self._getMid(ss, se)
        return self._getSum_helper(ss, mid, qs, qe, 2 * si + 1) + self._getSum_helper(
            mid + 1, se, qs, qe, 2 * si + 2
        )
