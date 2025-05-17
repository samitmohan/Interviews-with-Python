# https://leetcode.com/problems/implement-stack-using-queues/description/
# use 1 queue
# only trick : pop function
# stack = [1, 2, 3, 4, 5]
# queue = [1, 2, 3, 4, 5]
# pop : should return 5 (stack) but queue returns 1
# so go through all the numbers unntil the last one (len(queue) - 1)
# and add all of them in the queue (to the right side) : [5, 1, 2, 3, 4]
# return q.popleft()

from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

    # Your MyStack object will be instantiated and called as such:


# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
