# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# BST : Sorted in L M R order : so is a sorted list. Use Binary Search T and S : O(log(n)) and O(n) In a balanced
# binary search Tree height difference b/w left and right node cannot be more than 1 or in other words they contain
# almost equal number of nodes.
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root
