# https://leetcode.com/problems/product-of-array-except-self/

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

"""
Documentation
TC -> O(N), SC -> O(N) [Can be improved to O(1))
Logic -> [1,2,3,4] -> except arr[i] multiply left_part_of_arr * right_part_of_arr and do this for all elements
Case -> first and last number (of left and right resp) should always be 1 so to avoid multiplication by 0.
"""


class Solution:
    """
    Hint: Think about creating two passes:
        One to calculate product of everything to the left of index i
        One to multiply that by product of everything to the right of index i
    """

    def productExceptSelf(nums):
        n = len(nums)

        left_product = [0] * n
        right_product = [0] * n
        ans = [0] * n
        left_product[0], right_product[n - 1] = 1, 1
        # left / prefix generation
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # merge
        for i in range(n):
            ans[i] = left_product[i] * right_product[i]
        return ans


# alt solution -> O(1) Space
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    first_pass = 1
    for i in range(len(nums)):
        res[i] = first_pass
        first_pass *= nums[i]

    second_pass = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= second_pass
        second_pass *= nums[j]

    return res
