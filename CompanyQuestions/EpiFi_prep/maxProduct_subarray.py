# Given an integer array nums, find a subarray that has the largest product, and return the product.
"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


1) We first initialize our maximum and minimum products and the answer to the first element in the array.
2) We then iterate through the array starting from the second element.
3) If the current element is negative, we swap our maximum and minimum products since multiplying a negative number with a maximum product can result in a new minimum product and vice versa.
4) We then update our maximum and minimum products by comparing the current element with the product of the previous maximum and minimum products.
5) Finally, we update our answer by taking the maximum of our current answer and the maximum product.

"""


# T : O(N) and S : O(1)

# pos numbers : product increase


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    # ans = max(nums)
    # max_product, min_product = 1, 1

    max_product = min_product = ans = nums[0]  # handles 0s

    for i in range(1, len(nums)):
        if nums[i] == 0:
            max_product, min_product = 1, 1  # 0s are ignored
            continue
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        # temp = n * max_product
        # max_product = max(n * max_product, n * min_product, n)
        # min_product = max(temp, n * min_product, n)
        # ans = max(ans, max_product)

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        ans = max(ans, max_product)

    return ans
