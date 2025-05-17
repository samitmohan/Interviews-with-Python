# https://leetcode.com/problems/baseball-game/description/


def baseball(operations):
    stack = []
    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))  # append number
    return sum(stack)


def main():
    operations = ["5", "2", "C", "D", "+"]
    print(baseball(operations))


main()
