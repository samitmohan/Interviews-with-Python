# https://leetcode.com/problems/design-browser-history/description/
# Doubly Linked List
# init
# current pointer = current homepage (google.com)
# visit (leetcode.com)
# 1. make new node : leetcode.com
# 2. current pointer points to leetcode.com and leetcode.com points to current pointer : google -> <- leetcode
# 3. update current pointer : leetcode.com and not google.com
# back & forward
# make sure that steps never go out of bounds (example : 3 nodes and back steps : 4 : should return the last step it can go to)
# check if current.prev != None instead of current != None : go back upto that pointu


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)  # google

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(
            url, self.curr
        )  # google -> leetcode and leetcode -> google
        self.curr = self.curr.next  # update current (lc not google)

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev  # go back steps number of times and return val
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
