# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# find a pattern, do it in O(1) complexity
# 3 and 7 : numbers between them : 7-3 + 1 : 5 and odd numbers between them : 3 (3,5,7) so since 3 is inclusive and it is odd : we add one.
# odd numbers between it : 5 // 3 = 2 and and + 1 for 3 to be inclusive and odd : total : 3
# if range even then just return count


def countOdds(low, high):
    length = high - low + 1
    answer = length // 2
    if length % 2 or low % 2 == 1:
        answer += 1
    return answer


def main():
    low, high = 3, 7
    print(countOdds(low, high))


main()
