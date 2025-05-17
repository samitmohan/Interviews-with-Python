# can you even do this
# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointers [1->2->3->4] : store the link for 1->2
        prev, curr = None, head  # [_ 1->2->3->4]
        while curr:
            temp = curr.next  # store link (temp = 2)
            curr.next = (
                prev  # _ <- 1 and now shift prev and curr for entire LL (while curr)
            )
            prev = curr
            curr = temp
        return prev  # end of list
