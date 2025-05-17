# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


"""
10
range = [1,10]
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

lol this dont work we need to create partitions
    ans = []
    for i in range(1, n+1):
        prod = i * i # 81
        summ = 0
        for digits in str(prod):
            summ += digits
            if summ == i: # 8 + 1 = 9 : yes
                ans.append(prod) # 81
    return sum(ans)
"""

# bro this a bitchass problem istg

"""
main crux is how do i get all partitions -> recursion 
1234
tree -> 1, 12, 123, 1234
            1 -> 2 -> 23 -> 234 -> ..
            12 -> 3 -> 34 -> ...
            123 -> 4
            1234
base case : currsum = target sum or we reached terminal node

not that hard once you solve enough recursion questions i guess
"""


class Solution:
    def partition(self, i, currsum, target, digit):
        # base case
        if i == len(digit) and currsum == target:
            return True
        # recursive
        for j in range(i, len(digit)):
            if self.partition(j + 1, currsum + int(digit[i : j + 1]), target, digit):
                return True
        return False  # otherwise

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.partition(
                0, 0, i, str(i * i)
            ):  # index, curr_sum, target, string to partition
                ans += i * i
        return ans


s = Solution()
print(s.punishmentNumber(10))
