"""
https://leetcode.com/problems/flood-fill/
Given matrix, matrix[i][j] = pixel value of the image
start at matrix[start_row][start_col] and flood fill -:
"""


# dfs
def floodFill(image, sr, sc, color):
    original_color = image[sr][sc]
    # base case *no need for this, put this in the dfs call itself*
    # if original_color == color:
    #     return image

    def dfs(sr, sc):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != original_color:
            return
        if original_color == color:
            return  # already filled
        # check adjacent
        image[sr][sc] = color
        dfs(sr + 1, sc)
        dfs(sr - 1, sc)
        dfs(sr, sc + 1)
        dfs(sr, sc - 1)

    dfs(sr, sc)
    return image


# bfs ~ no recursion
from collections import deque


def floodFill(image, sr, sc, color):
    original_color = image[sr][sc]

    queue = deque()
    queue.append((sr, sc))

    while queue:
        r, c = queue.popleft()
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            continue
        if image[r][c] != original_color:
            continue
        if original_color == color:
            continue

        image[r][c] = color
        queue.append((r + 1, c))
        queue.append((r - 1, c))
        queue.append((r, c + 1))
        queue.append((r, c - 1))

    return image


def main():
    floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)


main()
