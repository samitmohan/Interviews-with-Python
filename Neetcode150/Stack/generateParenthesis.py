# https://leetcode.com/problems/generate-parentheses/description/
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# 2 counters : open brackets and close brackets
# only add open parenthesis in stack if open < n
# only add closing parentheses in stack if closed < open
# valid if open == closed == n (base case)
# backtrack every time : single variable stack : pop()


def generateParenthesis(n):
    stack = []
    ans = []

    def backtrack(open_count, closed_count):
        if open_count == closed_count == n:
            ans.append("".join(stack))
            return

        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()  # backtrack : single var stack

        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0, 0)
    return ans


def main():
    print(generateParenthesis(3))


main()
