# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep a stack and put elements
        # operation is found -> pop the left and right element
        # and then push back the result back into the stack
        # return stack elements
        stack = []
        while len(tokens) > 0:
            tok = tokens.pop(0)
            if tok == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif tok == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tok == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif tok == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b / a)))
            else:
                stack.append(int(tok))
        return stack.pop()
