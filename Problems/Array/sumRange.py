# https://leetcode.com/problems/range-sum-query-immutable/submissions/901393506/

# prefix sum question : just return the right pointer of prefix sum, for more general range : value of prefix sum - values not needed
#         L      R
# [-2, 0, 3, -5, 2, -1]
# [-2, -2, 1, -4, -2, -3]
# R : till now sum : -2 but we don't need the first 2 values (-2, 0) : sum of that : -2 (L - 1th index) in prefix arr : subtract :: -2 - -2 : 0 same as 3 + -5 + 2 = 0

# if L out of bounds : just return R pointer
#  L      R
# [-2, 0, 3, -5, 2, -1]
# prefix_sum : [-2, -2, 1, -4, -2, -3] :: 1 - 0(L-1th index : out of bounds) = 1


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        i = 0
        for n in nums:
            i += n
            self.prefix_sum.append(i)

    def sumRange(self, left: int, right: int) -> int:
        L = self.prefix_sum[left - 1] if left > 0 else 0
        R = self.prefix_sum[right]
        return R - L
