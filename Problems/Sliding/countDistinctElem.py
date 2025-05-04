# https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1
'''
Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.
    

        L        L        R
nums = [1, 2, 1, 3, 4, 2, 3]
        0  1  2  3  4
        # seen = (1,2,3) = len(seen) = 3
'''
from collections import defaultdict
def countDistinct(nums, k):
    freq = defaultdict(int)
    distinct = 0
    ans = []
    for i in range(k):
        if freq[nums[i]] == 0:
            distinct += 1
        freq[nums[i]] += 1
    
    ans.append(distinct) # initial window answer

    for i in range(k, len(nums)):
        # remove outgoing elem nums[i-k]
        freq[nums[i-k]] -= 1
        if freq[nums[i-k]] == 0:
            distinct -= 1
        # add incoming elem nums[i]
        if freq[nums[i]] == 0:
            distinct += 1
        freq[nums[i]] += 1
        # append curr distinct count for this window
        ans.append(distinct)

    return ans
    
def main():
    print(countDistinct(nums = [1, 2, 1, 3, 4, 2, 3], k = 4))
main()

