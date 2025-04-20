import bisect

# https://leetcode.com/problems/count-the-number-of-fair-pairs/
"""
2 for loops : Not efficient, constraint are too high
fair_pair = 0
for i in range(0, n-1):
    for j in range(i+1, n-1):
        if lower <= nums[i] + nums[j] <= upper:
            fair_pair += 1
    return fair_pairs

Doing it in O(nlogn) (single pass)
Sort the nums now i < j
[0,1,7,4,4,5], lower = 3, upper = 6
After sorting : [0,1,4,4,5,7]
3 <= nums[i] + nums[j] <= 6
3 <= 1 <= 6
3 <= 4 <= 6 : fair pair
3 <= 5 <= 6 : fair pair etc..
Keep two pointers -> increment until left pointer = lower, right pointer = upper
    Whatever elements in the middle of left and right pointer check the condition nums[i] + nums[j] and if true, add to fair_pairs.

You fix nums[i].

You want to find how many elements nums[j] (with j > i) satisfy:
lower - nums[i] <= nums[j] <= upper - nums[i]

        # 1) sort array
        nums.sort()

        # 2) fix each index i and count valid js using binary search/two pointer
        n = len(nums)
        for i in range(n - 1):

            low, high = lower - nums[i], upper - nums[i]
            left = i + 1
            while left < n and nums[left] < low:
                left += 1
            
            right = left
            while right < n and nums[right] <= high:
                right += 1

            fair_pairs += (right - left)
        return fair_pair

Since the array is sorted, you can binary search for valid j's.
            # find j using BS such that this condition is true in range nums[i+1:]
            #lower - nums[i] <= nums[j] <= upper - nums[i]
            # left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            # right = bisect.bisect_right(nums, upper - nums[i], i + 1)

Same without using Bisect (manual binary search)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        fair_pairs = 0

        def lower_bound(arr, target, start):
            left, right = start, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound(arr, target, start):
            left, right = start, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for i in range(n - 1):
            low = lower_bound(nums, lower - nums[i], i + 1)
            high = upper_bound(nums, upper - nums[i], i + 1)
            fair_pairs += (high - low)

        return fair_pairs

"""


class Solution:
    def countFairPairs(self, nums, lower, upper):
        fair_pairs = 0
        # 1) sort array
        nums.sort()

        # 2) fix each index i and count valid js using binary search/two pointer
        n = len(nums)
        for i in range(n - 1):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1)
            fair_pairs += right - left
        return fair_pairs
