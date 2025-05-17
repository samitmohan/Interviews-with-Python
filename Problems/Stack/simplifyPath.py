# https://leetcode.com/problems/simplify-path/description/

# /abc/.. -> /abc [.. -> root dire : pop abc and .. ignored] : /
# single dots are always ignored and trailing / also removed.

# /../abc//./def/
# / .. (out one direct but we're in root direc so not possible : no pop, ignore)
# //abc : multiple slash : ignore
# /abc/def
# Ignore slash, dots, no trailing slash
# if .. and in root -> ignore, else pop (.. means pop -> remove most recently added element)

# Time and Space : O(N)


def simplifyPath(path):
    stack = []
    current = ""  # stores most recent dir
    for char in path + "/":
        if char == "/":  # end reached
            # either pop or add
            if current == "..":
                if stack:
                    stack.pop()
            elif current != "" and current != ".":
                stack.append(current)
            current = ""  # empty again
        else:
            # abc or def or words -> add
            current += char

    return "/" + "/".join(stack)


def main():
    print(simplifyPath("/home/"))


main()

# https://www.youtube.com/watch?v=qYlHrAKJfyA&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=2
