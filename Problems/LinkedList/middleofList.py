# https://leetcode.com/problems/middle-of-the-linked-list/o


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast slow pointer solution
        # two pointers both at head
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
