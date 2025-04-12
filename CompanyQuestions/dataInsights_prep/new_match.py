def isMatch(s, p):
    dp = {}
    def dfs(i, j): # current posn of s and p
        # match : no problems till now : base case
        if i == len(s) and j == len(p): return True # reached full pattern
        # ran out of patterns
        if j == len(p): # run out of pattern characters
            return False # not match

        if (i, j) in dp: return dp[(i, j)] # memoized..

        # if curr char posn at i and j match.
        match = i < len(s) and (s[i] == p[j] or p[j] == '?')

        # mutli character
        if p[j] == '*':
            # match empty character or match one/more character from s
            dp[(i, j)] = dfs(i, j + 1) or (i < len(s) and dfs(i+1, j))
            return dp[(i, j)]
        
        if match: # do for next character also
            dp[(i, j)] = dfs(i+1, j+1) 
            return dp[(i, j)]

        dp[(i, j)] = False # if no above conditions met : not match
        return False
    return dfs(0, 0)

# worst case : exponential time complexity
# O(len(s) * len(p)) : space complexity

"""
Rules to write Recurrence.
1) Express (i,j)
2) Explore comparisions
3) Out of all comparisions if any way can : true

Matching conditions
if (s[i] = p[j]) || s[i] == '?': return f(i+1, j+1)
if (s[i] == '*') f(i-1, j) : length 0 OR f(i, j - single char matching condition1) : next character
"""