import jovian.pythondsa

# https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
In this code, we use a modified version of the binary search algorithm to find the target element in array

Initialize the left pointer l to the first index (0) and the right pointer r to the last index (n - 1) of the array.
Enter the while loop, which continues until the left pointer becomes greater than the right pointer.
Calculate the middle index mid using the formula (l + r) // 2.
Check if the element at the mid index nums[mid] is equal to the target. If it is, return mid as the index of the target.

Check if the left half of the array is sorted by comparing nums[l] with nums[mid].
    If it is, perform a normal binary search in the left half.

If nums[l] <= target < nums[mid], the target lies in the left half. Update the right pointer r to mid - 1.
Otherwise, the target does not lie in the left half. Update the left pointer l to mid + 1.

    If the left half is not sorted, then the right half must be sorted. Perform a binary search in the right half.
If nums[mid] < target <= nums[r], the target lies in the right half. Update the left pointer l to mid + 1.
Otherwise, the target does not lie in the right half. Update the right pointer r to mid - 1.

If the target is not found after the loop, return -1 to indicate that it is not in the array.
This algorithm has a time complexity of O(log n) because it halves the search space in each iteration of the while loop.
"""


def search(nums, target):
    l, h = 0, len(nums) - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] == target:  # answer found
            return m
        elif nums[l] <= nums[m]:  # left half is sorted, perform bs in left half.
            if nums[l] <= target < nums[m]:  # answer in left half
                h = m - 1
            else:
                l = m + 1
        else:  # right half is sorted, perform bs in right half.
            if nums[m] < target <= nums[h]:  # answer in right half
                l = m + 1
            else:
                h = m - 1
    return -1  # if not found


tests = []

test = {"input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, "output": 4}
tests.append(test)

tests.append({"input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3}, "output": -1})

tests.append({"input": {"nums": [3, 1], "target": 1}, "output": 1})

print(jovian.pythondsa.evaluate_test_cases(search, tests))
