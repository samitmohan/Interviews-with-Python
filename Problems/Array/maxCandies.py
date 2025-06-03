# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(box for box in initialBoxes if status[box])
        locked = set(box for box in initialBoxes if not status[box])
        keys_set, visited, ans = set(), set(), 0
        
        while queue:
            box = queue.popleft()
            if box in visited: continue
            visited.add(box)
            ans += candies[box]
            
            for key in keys[box]:
                keys_set.add(key)
                if key in locked:
                    locked.remove(key)
                    queue.append(key)
            
            for new_box in containedBoxes[box]:
                if new_box not in visited:
                    if status[new_box] or new_box in keys_set:
                        queue.append(new_box)
                    else:
                        locked.add(new_box)
        
        return ans
