# https://leetcode.com/problems/detect-squares/
"""
An axis-aligned square is a square whose edges are all the same length and
are either parallel or perpendicular to the x-axis and y-axis.

Trick for detecting squares/rectangle in a grid
Count of occurrences matter : more count/duplicates : more squares. (hashmap)
Trick:
    Find diagonal point. How to verify if points are square by diagonal?
        height difference = width difference :: Diagonal : Form a square
    qx,qy and x,y :: if x, qy and qx, y are in hashmap : square can be formed and if multiple counts : multiple count by squares
"""

# defaultdict : if key not present : 0 (Default Value)
# list can't be a key for hashmap in python : convert to tuple.
# use list not hashmap to store points (we need duplicates)
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.ptsCounter = defaultdict(int)
        self.pts = []

    def add(self, point):
        self.ptsCounter[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        # if diagonals same : we can form square
        # area should be positive : 2 points can't be stacked on top of each other : no square
        ans = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue  # can't form square
            ans += self.ptsCounter[(x, py)] * self.ptsCounter[(px, y)]
        return ans


if __name__ == "__main__":
    obj = DetectSquares()
    obj.add([3, 10])
    obj.add([11, 2])
    obj.add([3, 2])
    obj.count([11, 10])  # 1
    obj.count([14, 8])  # 0
    obj.add([11, 2])
    obj.count([11, 10])  # 2
