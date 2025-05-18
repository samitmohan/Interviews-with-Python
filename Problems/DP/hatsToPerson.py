from collections import defaultdict
from functools import cache
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/description/

"""
Everyone should wear different hats -> matching problem -> dp + bitmask
dp(i, mask) -> i represents person, mask represents current state (does i wear hat or not) -> 2^40 -> TLE
1 <= n <= 10

Observation: instead of people (10) to hats (40) options -> we can have hats (40) to people (10) -> 10 options only -> much better
key = hats
val = people liking hat

h1           h2          h3

[0,,,10]    [0,,,10]     [0,,,10] 

use bitmasking for selection -> keeps track of which people use which hat

if no overlap -> we can use hat
lets say bitmask is 1000
                    0100 
                & = 0000 -> no overlap -> h1 can be assigned to prsn1 and h2 can be assigned to prsn2
how to keep track of people who have selected hats = OR -> 1000 | 0100 -> 1100 0> h1 and h2 are assigned already.
0/1 use or don't use -> kind of like knapsack
h1      h3        h5
[0]     [0,1]     [0,1]

Instead of tracking which hats are free, let's instead track which people don't have a hat yet. 
Instead of iterating over the people to select a hat, we will iterate over the hats and select people.


Iterate over hats, select a person that prefers the current hat and isn't already wearing one
Keep track of which people don't have a hat yet

hats = [[3,4], [4,5], [5]]
hats_to_people  dict
key = 3 -> value = [0]
key = 4 -> value = [0,1]
key = 5 -> value = [1,2]
dp(hat, mask) -> hat is the curr hat we are trying to place, mask denotes which people are already wearing a hat
returns how many ways to place hats in range [1,40] such that everyone wears a distinct hat -> ans in dp(1, 0) -> start with 1st hat, no one wearing a hat yet.

iterate over hatsToPeople[hat], which holds a list of all the people that prefer this hat
For each person, we check if the bit at position person is set in mask. If it's not set, it means person both prefers hat and is also not currently wearing a hat - therefore we could place hat on person. 
    To do this, we need to set the bit in mask, which we can do with mask | (1 << person)
The answer to a state (hat, mask) is the sum of all these possibilities.


-so just go thru all the people in hats
            -then go thru all the preferred hats for that person
                -if the hat has already been chosen, then just continue
                -else, i will mask that hat
                
        [[3,4],[4,5],[5]]
        10000
        
        
        shoot, so now i need to do it backwards instead actually
        -i need to assign HATS to people, instead of PEOPLE to hats
        
        so my map looks like this:
        -key = hat number:
        -value = peopleIds that like that hat
"""


class Solution:
    def numberWays(self, hats) -> int:
        @cache
        def dp(hat, mask):
            if mask == done:
                return 1  # everyone can wear a hat
            if hat > 40:
                return 0  # base
            ans = dp(hat + 1, mask)
            for person in hats_to_people[hat]:
                if mask & (1 << person) == 0:
                    ans = (ans + dp(hat + 1, mask | (1 << person))) % MOD
            return ans

        hats_to_people = defaultdict(list)
        for i in range(len(hats)):
            for hat in hats[i]:
                hats_to_people[hat].append(i)
        n = len(hats)
        MOD = 10**9 + 7
        done = 2**n - 1  # combinations
        return dp(1, 0)


# Given n as the number of people and k as the number of hats: O(k⋅n⋅2n)
s = Solution()
print(s.numberWays([[3, 4], [4, 5], [4, 5]]))
