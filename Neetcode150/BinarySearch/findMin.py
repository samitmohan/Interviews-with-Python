# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Observation : Rotated array : there will always be a left sorted subarray and and right sorted sub array no matter how you rotate it
  [1,2,3,4,5] = [3,4,5,1,2] : [3,4,5] and [1,2]
  # search for middle value ; if middle value lies in left half then look at right
                              if middle value lies in right half then look at left
                              keep updating min as we keep seeing mid
"""


def findMin(nums):
    ans = nums[0]  # for now
    low, high = 0, len(nums) - 1
    while low <= high:
        # if array sorted : ans = min(ans, nums[left]) : left here means the first element (Smallest)
        if nums[low] < nums[high]:
            ans = min(ans, nums[low])
            break

        mid = (low + high) // 2
        ans = min(ans, nums[mid])

        # figure out if mid is in left subarray or right subarray: if left subarray : look at right
        if (
            nums[mid] >= nums[low]
        ):  # 5 > 3 that means its in left subarray : look at right
            low = mid + 1
        else:
            high = mid - 1
    return ans


def main():
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))


main()
