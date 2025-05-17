# https://leetcode.com/problems/online-stock-span/description/
# Use stack : pair : (price, span)
# O(N) :: make use of previous span
class StockSpanner:
    def __init__(self):
        self.stack = []  # pair : (price, span)

    def next(self, price: int) -> int:
        span = 1  # default
        # if price at top of stack <= current price : increment span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # add span
            self.stack.pop()  # pop after all span added

        self.stack.append((price, span))  # update
        return span


# price : [100,80,60,70,60,75,85]
# span : [1,1,1,2,1,4,6]
#   for 100 : default : 1
#   for 80, 80 <= 100 : default 1
#   for 60, 60 <= 100 : default 1
#   for 70, 70 > stack[-1] (60) : 1 + 1 and then check for stack[-2] : 70 !> 80 so ignore
#   for 60, 60 <= 70 : default 1 [consecuctive days needed]
#   for 75, 75 > 60 : 1 + 1 and 75 > 70 : 1 + 1 + 2 (saved result for 70) then check with 80, 75 !> 80 : ignore
#   for 85, 85 > 70 : 4 + 1 and then check directly with 85 : 85 >= 85 so + 1 and 85 !> 100 : ignore :: 6
