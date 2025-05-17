# https://leetcode.com/problems/valid-parentheses/description/
# Input: s = "()", "(]"
# Output: true, false
# characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# valid : open brackets must be closed, in correct order and of same type

# idea : if close parenthesis, look for open ones in stack : if exist :: pop else false
#  if open parenthesis, no issues -> append to stack
# in the end : return True if stack empty else False
# Time & Space : O(N)


def isValid(s):
    stack = []
    close_matching = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in close_matching:  # keys
            # check it's corresponding value in stack (opening) stack[-1] = top element
            if stack and stack[-1] == close_matching[char]:
                stack.pop()
            else:
                return False
        else:  # opening parenthesis -> just append
            stack.append(char)
    return True if not stack else False


def main():
    print(isValid("()"))


main()
