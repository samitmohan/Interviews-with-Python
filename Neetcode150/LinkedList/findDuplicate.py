# https://leetcode.com/problems/find-the-duplicate-number/description/
# https://www.youtube.com/watch?v=wjYnzkAhcNk
# https://leetcode.com/problems/find-the-duplicate-number/solutions/2013321/python-o-n-time-and-o-1-space-optimal-easy-to-understand-solution/?languageTags=python3
"""
Without modifying it : Linked List : O(N) Time and O(1) Space
# Memorize Solution
  Form a LL with nums given -> notice that numbers are from range [1,n] and will always point to their indices
   0 1 2 3 4
  [1,3,4,2,2]
1->0
3->1
4->2
3->2
2->4

From this we can tell the cycle is at 4->2 and 3->2 because they both point to same. Using Floyd we can figure this
out. (First iteration of fast and slow will give us the point 3) To get the duplicate number : run floyd again with
slow2 pointer at same speed as slow (the next cycle will give answer/duplicate point) [memorize]

Floyd Algorithm and LL Cycle
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break  # cycle detected

        # Locate the start node of cycle (i.e., the duplicate number)
        slow2 = 0  # at same speed
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow  # duplicate found


# Cyclic Sort Solution : [1, N] :: index = value - 1

"""
0 1 2 3 4 
1 3 4 2 2 

After cyclic sort
0 1 2 3 4
1 2 3 4 2

for i in len(arr): 
    if arr[i] != i + 1: (2 != 4)
        return arr[i] # 2
"""


def findDuplicate(arr):
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1
    # find incorrect index
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return arr[i]
