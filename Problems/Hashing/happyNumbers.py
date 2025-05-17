# https://leetcode.com/problems/happy-number
# easy set solution, keep adding to set until 1 reached and return n == 1


def happyNumber(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1


def main():
    print(happyNumber(19))


main()
