# https://leetcode.com/problems/merge-k-sorted-lists/
# Use D&C : merge sort
class Solution:
    def mergeKLists(self, lists):
        # edge cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        # edge cases
        if not left or not right:
            return left or right

        if left.val < right.val:
            # left comes first [left -> right] recursively
            left.next = self.merge(left.next, right)
            return left
        right.next = self.merge(left, right.next)
        return right
