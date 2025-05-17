# https://leetcode.com/problems/add-two-numbers/description/
"""
Reverse order : add numbers from one's place : convinient.
Have a carry integer
Edge Case : if 564 + 3422 : assume in the it's a 0 (5640)
Edge Case : if carry exists and no numbers to carry that carry : just add carry to result : 7 and 8 = 5 -> 1 (add carry to result)

Dummy LL : new linkedlist where answers are saved

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy  # points to first element in new list
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # new digit
            val = val1 + val2 + carry
            # get carry serperate (15 : only want 1) 15 // 10
            carry = val // 10
            # get just val : (15 : only want 5) val % 10
            val = val % 10
            current.next = ListNode(val)

            # update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
