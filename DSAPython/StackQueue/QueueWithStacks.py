# queue -> fifo -> push -> adds to starting of list
# peek -> returns list[0]
# pop -> removes first element
# empty -> bool -> checks if list[0] present or not


class QueueWithStacks:
    # use 2 lists -> in and out and move elements -> O(N)
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)  # append in stack 1

    def pop(self) -> int:
        self.move()  # move elements from in -> out (reverse order)
        return self.out_stack.pop()  # remove last element.

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return (not self.in_stack) and (not self.out_stack)

    # helper function
    def move(self):
        # if out stack empty and in stack not empty -> place in stack elements in out stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(
                    self.in_stack.pop()
                )  # place in out stack and pop elemnts from in stack


q = QueueWithStacks()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())  # Output: 1
print(q.pop())  # Output: 2
q.push(4)
print(q.pop())  # Output: 3
print(q.pop())  # Output: 4
