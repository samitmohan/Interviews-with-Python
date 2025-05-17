# https://leetcode.com/problems/swap-nodes-in-pairs/
# 1->2->3->4
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        temp = ListNode(0)  # dumnmy node
        temp = head.next  # points to 2
        head.next = self.swapPairs(head.next.next)  # 1 -> 3 (recursively)
        temp.next = head  # 2 -> 1
        return temp
