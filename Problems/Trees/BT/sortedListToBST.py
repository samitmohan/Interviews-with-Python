# dividing the Linked List into 2 parts first half = left Node, middle = root and right = second half.
# To find middle element use 2 pointer approach: slow and fast

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        mid = self.getMid(head)
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        mid.next = None
        root.left = self.sortedListToBST(head)
        return root

    def getMid(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow  # save
            slow = slow.next
        if prev:
            prev.next = None
        return slow  # mid element
