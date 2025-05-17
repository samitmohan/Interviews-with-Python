# https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
Keep a hashmap of number and freq
  Number with freq 1 = answer
"""


def singleNonDuplicate(nums):
    hm = {}
    for x in nums:
        if x in hm:
            hm[x] += 1
        else:
            hm[x] = 1
    for key in hm:
        if hm[key] == 1:
            return key


def main():
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums2 = [3, 3, 7, 7, 10, 11, 11]
    print(singleNonDuplicate(nums2))


main()
