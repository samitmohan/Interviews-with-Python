# https://leetcode.com/problems/word-search-ii/description/
# Use Trie + DFS
# REVIST : Can't do.


class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = None  # word


class Tries:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = Node()
                cur = cur.children[c]
        cur.end_of_word = word

    # O(M(4(3**L-1)))


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # tries build tries
        # backtracking in each node
        # if word in node.child
        rows, cols = len(board), len(board[0])

        tries = Tries()
        visited = set()
        RR = set(range(rows))
        CC = set(range(cols))

        for word in words:
            tries.insert(word)

        words = set(words)
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = set()

        def backtracking(r, c, node):
            if node.end:
                res.add(node.end)

            if not node.child:
                return

            for dr, dc in direction:
                row, col = r + dr, c + dc
                if (
                    row in RR
                    and col in CC
                    and (row, col) not in visited
                    and board[row][col] in node.child
                ):
                    visited.add((row, col))
                    backtracking(row, col, node.child[board[row][col]])
                    visited.remove((row, col))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in tries.root.children:
                    visited.add((i, j))
                    backtracking(i, j, tries.root.children[board[i][j]])
                    visited.remove((i, j))
        return res
