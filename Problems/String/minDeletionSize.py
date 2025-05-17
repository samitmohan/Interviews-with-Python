#!/usr/local/bin/python3

# abc
# bce
# cae

# a,b,c -> sorted
# b,c,e -> sorted
# c,a,e -> not sorted
# ans = 1


def minDelete(s):
    a = list(zip(*s))
    count = 0
    for char in a:
        # if sorted = actual
        if list(char) != sorted(char):
            count += 1
    return count


def main():
    print(minDelete(["zyx", "wvu", "tsr"]))


main()
