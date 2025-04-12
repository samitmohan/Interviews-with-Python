class Solution:
    def isValid(self, s: str) -> bool:
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
