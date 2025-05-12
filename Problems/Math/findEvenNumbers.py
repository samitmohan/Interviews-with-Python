# https://leetcode.com/problems/finding-3-digit-even-numbers/?envType=daily-question&envId=2025-05-12
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits):
        ans = []
        for a in digits:
            for b in digits:
                for c in digits:
                    if a == 0: continue # skip leading zeroes
                    if c % 2 != 0: continue # skip odd
                    number = 100 * a + 10 * b + c # form
                    temp = [a, b, c]
                    if Counter(temp) <= Counter(digits):
                        ans.append(number)
        return sorted(set(ans))


# s = Solution()
# print(s.findEvenNumbers(digits=[2,1,3,0]))
        


def findEvenNumbers(digits):
    '''
    Count freq of each dig from digits
    Loop thru 100 to 998 (last even 3 dig)
    for each num-:
            split it into its digit
            check if it can be built using given digits (compare freq)
    
    '''
    ans = []
    frequency = Counter(digits)
    for i in range(100, 1000, 2):
        split = [i // 100, (i // 10) % 10, i % 10]
        count = Counter(split)
        if all(frequency[d] >= count[d] for d in count):
                ans.append(i)
    return ans

def main():
    print(findEvenNumbers(digits=[2,1,3,0]))
main()
