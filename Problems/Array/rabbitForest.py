# https://leetcode.com/problems/rabbits-in-forest/?envType=daily-question&envId=2025-04-20
"""

[10,10,10] is a group of 3 and 11 in each
ceil(3/11) = 1 group. answer = 11

[1,1,2] both first and second rabbit say there is one more rabbit of my color = group of 2.
2 -: group of 3 (2 rabits that have diff colors and itself)

total = 3 + 2 = 5

Group 1 → Rabbits who said 1:
    Count: 2
    Each group can have 1 + 1 = 2 rabbits
    We have exactly 2 rabbits → fits into 1 group
    So we count 2 rabbits

Group 2 → Rabbit who said 2:
    Count: 1
    Group size: 2 + 1 = 3
    But we only have 1 rabbit → still have to assume a full group of 3 exists
    So we count 3 rabbits

Ideas
Keep hashmap for count of rabits : [1,1,2] has hashmap = {1 : 2, 2 : 1} lets say freq = 2,1
rabbits (group_size) = answer[i] + 1 (itself) # 2, 2, 3
groups : ceil(rabbits / count) # 2/2, 3/1 = 1, 3
total rabbits = rabbits * groups (1 group * 2 = 2, 1 group * 3 rabbits = 3 :: sum = 5)

For each unique answer x, group size is x + 1.
Let count be how many times x occurs.
Compute groups = ceil(count / (x + 1))
Total rabbits for this answer = groups * (x + 1)
Sum across all answers.

# count = freq[x]
# group_size = x + 1  # actual rabbits
# groups_needed = ceil(count / group_size)
"""

from collections import Counter
from math import ceil


class Solution:
    def numRabbits(self, answers):
        freq = Counter(answers)  # key = rabit, value = frequency
        total_rabbits = 0
        for answer, count in freq.items():
            group_size = answer + 1  # actual rabbits
            num_groups = ceil(count / group_size)
            total_rabbits += group_size * num_groups
        return total_rabbits
