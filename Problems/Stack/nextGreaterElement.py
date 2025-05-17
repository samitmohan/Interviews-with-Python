# https://leetcode.com/problems/next-greater-element-i/
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hmp = {}
        for i in nums2:
            while (
                stack and stack[-1] < i
            ):  # greater element found : map stack's top element to greater element
                hmp[stack[-1]] = i
                stack.pop()
            # otherwise
            stack.append(i)
        # hmp
        # 1 -> 3
        # 3 -> 4
        # 4 -> -1
        # 2 -> -1
        return [
            hmp.get(x, -1) for x in nums1
        ]  # return answer if no greater element : return -1
