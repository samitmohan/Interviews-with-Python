# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
def robotWithString(s):
    stack = []
    n = len(s)
    # precomputed arr
    precomp_arr = [""] * n

    for i in range(n):  # 3
        precomp_arr[i] = min(s[i:])
    # precom_arr looks like [a,a,c]
    p = ""
    for i in range(n):
        stack.append(s[i])  # b is pushed to stack
        next_min = precomp_arr[i + 1] if i + 1 < len(s) else "z"

        # can we pop b? : is b <= next_min_char(a)
        while stack and stack[-1] <= next_min:
            p += stack.pop()

    # remaining characters
    while stack:
        p += stack.pop()

    return p


def main():
    print(robotWithString(s="bac"))
    print(robotWithString(s="zza"))
    print(robotWithString(s="bdda"))


main()

# this gives TLE since we precomp_arr takes O(N^2) time as i'm calling min() on a substring every time.

# Build precomputed arr efficiently.
precomp_arr[n - 1] = s[n - 1]  # last char (c)
for i in range(n - 2, -1, -1):
    precomp_arr[i] = min(s[i], precomp_arr[i + 1])
