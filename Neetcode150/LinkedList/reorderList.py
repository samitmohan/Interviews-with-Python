# https://leetcode.com/problems/reorder-list/description/
# [1->2->3->4] :: split into middle :: [1->2] and [3->4] :: reverse second half
# [1->2] and [4->3] now point 1 to 4 and 2 to 3 :: [1->4->2->3]

# 3 parts:
# fast and slow pointer to find middle of list
# reverse linked list
# merge


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at middle : reverse linked list [3->4 to 4->3]
        # second = 3 : curr
        second = slow.next  # first element of second half of the list
        prev = slow.next = (
            None  # slow.next = None because we don't want 2->3 :: break link between two sublists [1->2] and [3->4]
        )
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs (first.next -> second and second.next -> first) : first : first element of first half and second : first element of second half
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            # shift pointers
            first, second = temp1, temp2
