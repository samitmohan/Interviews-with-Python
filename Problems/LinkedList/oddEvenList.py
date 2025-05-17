# https://leetcode.com/problems/odd-even-linked-list
# Good explanation : https://leetcode.com/problems/odd-even-linked-list/solutions/1606963/c-simplest-solution-w-explanation-one-pass/?orderBy=most_votes


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check for null value
        if not head:
            return head

        odd = head
        even = head.next
        even_start = even  # store for eonnecting in the future
        while (
            even and even.next
        ):  # what if only 1 val (odd) -> need multiple values hence check if even != nullptr
            # link
            odd.next = odd.next.next
            even.next = even.next.next
            # keep traversing also (actual placement of the pointers)
            odd = odd.next
            even = even.next

        # at the end connect the last odd LL val to even_start (1-2-3-4-5 = 1-3-5->2-4) [-> even_start]
        odd.next = even_start
        return head
