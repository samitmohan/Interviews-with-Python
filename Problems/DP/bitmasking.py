# since i am not confident about bitmasking

"""
# n
# mask = 1 << (k-1) for kth bit
# now bitwise AND = n & mask  to see if kth bit is set to 1 or 0 (if n & mask == 1 -> kth bit is set to 1, else 0)

Subsets with recursion-:
Subsets without recursion-:

How to find subset of mask

Range of mask values = 0 to 2^n - 1 (7 is 2^3 - 1) for 3 bits.

2^n = 1 << n
2^0 = 1 << 0, 2^1 = 1 << 1, 2^2 = 1 << 2 so on..
for i in range(0, 2^n):


How to print the subsets??
1) Given mask -> parse from LSB to MSB (one bit at a time)
2) if jth posn bit is set in mask -> then include element else curr element
A    B      C
1    0      1
<---       j=0
0    0      1 mask
BITWISE = 0 0 1 = include 1 = C = {C}
    j=1
0    1      0 mask
BITWISE = 0 0 0 = include nothing
j=1
BITWISE = 1 0 0 = include A = {AC}


{AC}

so basically
if (1 << j) & mask = 1, include jth element else skip jth element
"""


# Creating all subsets of given set of N elements
def subsets(N):
    all_subsets = []
    # runs 0 to 2^N times
    for mask in range(1 << N):
        cur_set = []
        # runs N times
        for j in range(N):
            if mask & (1 << j):
                cur_set.append(j)
        all_subsets.append(cur_set)
    return all_subsets


def subsets_recursion(N, idx=0, curr_set=None, all_subsets=None):
    if curr_set is None:
        curr_set = []
    if all_subsets is None:
        all_subsets = []
    # base case
    if idx == N:
        all_subsets.append(curr_set[:])
        return all_subsets
    # include element
    curr_set.append(idx)
    subsets_recursion(N, idx + 1, curr_set, all_subsets)
    # exclude elem
    curr_set.pop()
    subsets_recursion(N, idx + 1, curr_set, all_subsets)

    return all_subsets


def main():
    # (Ω(N × 2ᴺ))
    print(subsets(3))
    print(subsets_recursion(3))  # space: call stack -> O(n)


main()
