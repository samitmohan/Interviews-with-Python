from typing import List, Tuple


def flood_fill(
    screen: List[List[int]],
    sr: int,
    sc: int,
    row: int,
    col: int,
    source: int,
    color: int,
) -> None:
    # Condition for checking out of bounds
    if sr < 0 or sr >= row or sc < 0 or sc >= col:
        return

    if screen[sr][sc] != source:
        return

    screen[sr][sc] = color
    flood_fill(screen, sr - 1, sc, row, col, source, color)  # left
    flood_fill(screen, sr + 1, sc, row, col, source, color)  # right
    flood_fill(screen, sr, sc + 1, row, col, source, color)  # top
    flood_fill(screen, sr, sc - 1, row, col, source, color)  # bottom


if __name__ == "__main__":
    screen = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]

    # Row of the display
    m = 8

    # Column of the display
    n = 8

    # Coordinate provided by the user
    x = 4
    y = 4

    # Current color at that coordinate
    prevC = screen[x][y]

    # New color that has to be filled
    newC = 3

    flood_fill(screen, x, y, m, n, prevC, newC)

    # Printing the updated screen
    for i in range(m):
        for j in range(n):
            print(screen[i][j], end=" ")
        print()
