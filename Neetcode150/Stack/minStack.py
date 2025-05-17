# https://leetcode.com/problems/min-stack/description/

# 2 stacks : normal and a current minimum on another stack (minStack)
# one stack tells us values and order of items [stack]
# other stack tells min value added at each position of stack [minStack]
# top value of other stack : getMin() in O(1)


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  # normal stack
        # appending in minstack : if already number exists : check between that and curr val : whichever's min : append/update
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
