# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/?envType=daily-question&envId=2025-05-16
# Beautiful question

from functools import cache

"""
already handled the first condition via greedy. Now, conditions (2) and (3) bring new constraints that make it more combinatorial — hence, DP or graph search comes into play.

Now we also care about word content and their differences -> so can't pick the next valid word.


dp[j] is the length of a valid sequence ending at j
Adding words[i] extends that sequence, so we consider dp[j] + 1
We compare it with dp[i] to potentially update the best chain ending at i


"""


class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)

        def valid(j, i):
            if groups[i] == groups[j]:
                return False
            if len(words[i]) != len(words[j]):
                return False
            diff = sum(a != b for a, b in zip(words[i], words[j]))
            return diff == 1

        # build dp table
        dp = [1] * n
        prev = [-1] * n
        for i in range(n):
            for j in range(i):
                if valid(j, i):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # now need to reconstruct actual sequence from prev
        max_len = max(dp)
        end_idx = dp.index(max_len)
        path = []
        while end_idx != -1:
            path.append(words[end_idx])
            end_idx = prev[end_idx]

        path.reverse()  # since we built it backwards
        return path

    # another direction -> think of dag -> longest chain is the answer
    def getWordsinLongestSubsequenceDAG(self, words, groups):
        n = len(words)

        def valid(i, j):
            return (
                groups[i] != groups[j]
                and len(words[i]) == len(words[j])
                and sum(a != b for a, b in zip(words[i], words[j])) == 1
            )

        # build graph
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if valid(i, j):
                    graph[i].append(j)

        @cache
        def dfs(u):
            best = [words[u]]  # init
            for vrtx in graph[u]:
                path = dfs(vrtx)
                if 1 + len(path) > len(best):
                    best = [words[u]] + path
            return best

        # run dfs from all nodes
        ans = []
        for i in range(n):
            path = dfs(i)
            if len(path) > len(ans):
                ans = path
        return ans


s = Solution()
print(
    s.getWordsInLongestSubsequence(words=["bab", "dab", "cab"], groups=[1, 2, 2])
)  # ["bab","cab"]
print(
    s.getWordsInLongestSubsequence(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4])
)  # ["a","b","c","d"]
print(
    s.getWordsinLongestSubsequenceDAG(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4])
)  # ["a","b","c","d"]
print(
    s.getWordsinLongestSubsequenceDAG(words=["bab", "dab", "cab"], groups=[1, 2, 2])
)  # ["bab","cab"]
