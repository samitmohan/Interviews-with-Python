# https://leetcode.com/problems/remove-k-digits/description/
# Use monotonic stack : if current number < stack[top] : pop and decrement k, else stack.append(char)
# Trick case : if all numbers already in monotonic way : 12345 : so even after loop k > 0, just remove k elements from end : stack[:len(stack) - k] = 12 if k = 3
# return string(integer(stack)) to remove leading zeroes and as "" and not as stack


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while stack and k > 0 and stack[-1] > char:
                k -= 1
                stack.pop()
            stack.append(char)  # otherwise
        # 12345 -> worst case : remove last k digits
        if k:  # not fully spent
            stack = stack[0:-k]

        ans = "".join(stack)  # return as string not result
        return str(int(ans)) if ans else "0"
