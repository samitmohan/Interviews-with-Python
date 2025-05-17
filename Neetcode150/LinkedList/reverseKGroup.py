# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""
Use a dummy head, and

l, r : define reversing range

pre, cur : used in reversing, standard reverse linked linked list method

jump : used to connect last node in previous k-group to first node in following k-group
"""


class Solution:
    def reverseKGroup(self, head, k):
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:
                count += 1
                right = right.next
            if count == k:  # if size k satisfied, reverse the inner linked list
                prev, curr = right, left
                for _ in range(k):  # standard reverseing
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                # connect two k-groups
                jump.next = prev
                jump = left
                left = right
            else:
                return dummy.next
