# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/?envType=daily-question&envId=2025-05-15
'''
What we know-:
    len(words) = len(groups)
    pick longest ALTERNATING subsequence from words
    A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ.


Elements in words are distinct

What I think of this-:
    Either LCS comes to mindL DP solution
    Greedy Soln should also work seeing the constraints -:
        go from 1 to n-1 and if groups[i] != groups[i-1]: 
            add to answer

dry run-:
words = ["e","a","b"], groups = [0,0,1])
    n = 3
    1->2
    if groups[0] != groups[1] -> continue
    if groups[


words = ["a","b","c","d"], groups = [1,0,1,1])
    n = 4
    1->3
    groups[1] != groups[0] -> true -> add a, b
    ans = "a", "b"

    groups[2] != groups[1] -> true -> add b, c 
    ans = "a", "b", "b", "c"
    set(ans) = "a", "b", "c"
    list(set(ans)) = ["a", "b", "c"]

    groups[3] != groups[2] -> false -> continue

'''
# pretty neat soln
class Solution:
    def getLongestSubsequence(self, words, groups):
        n = len(words)
        ans = [words[0]]
        last_grp = groups[0]
        for i in range(1, n):
            if groups[i] != last_grp:
                ans.append(words[i])
                last_grp = groups[i]
        return ans

s = Solution()
print(s.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1])) # eb
print(s.getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1])) # abc
print(s.getLongestSubsequence(words = ["d"], groups = [1])) #d 

# one liner
# return [x for i,x in enumerate(words) if not i or groups[i] != groups[i-1]
