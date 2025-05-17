# https://leetcode.com/problems/word-search/
# O(n * m * backtrack)
# backtrack : len(word) : 4 ^ len(word)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # cant reuse any characters : from B can't look at A
        rows, cols = len(board), len(board[0])
        path = (
            set()
        )  # add all current value in board to make sure we don't revisit same char

        def backtrack(r, c, i):
            # base case
            if i == len(word):
                return True
            # invalid cases : out of bound, char doesn't match word, same char again
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            # found : recursive calls for all positions : down, up, right, left
            path.add((r, c))
            # if any of them return true : result is true
            ans = (
                backtrack(r + 1, c, i + 1)
                or backtrack(r - 1, c, i + 1)
                or backtrack(r, c + 1, i + 1)
                or backtrack(r, c - 1, i + 1)
            )
            # backtrack
            path.remove((r, c))
            return ans

        # use this for every row, col
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
