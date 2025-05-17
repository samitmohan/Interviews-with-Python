# https://leetcode.com/problems/max-points-on-a-line/

from collections import defaultdict


def find_line(x0, y0, x1, y1):
    # find slope and intercept
    if y0 == y1:  # num = 0
        return 0, y0  # slope and intercept
    if x0 == x1:  # denom = 0
        return x0, None
    else:
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        return slope, intercept


def maxPoints(points):
    if len(points) == 1:
        return 1
    # hm
    hashmap = defaultdict(lambda: set())  # unique vals
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x0, y0 = points[i]
            x1, y1 = points[j]
            # find any other point between this straight line (x0,y0 and x1,y1) -> add to our hashmap if in the same line
            line = find_line(x0, y0, x1, y1)
            hashmap[line].add(i)  # 1
            hashmap[line].add(j)  # 1 -> 1,1
    # lines -> (1,1)(2,2)(3,3)

    return max([len(hashmap[line]) for line in hashmap])


def main():
    points = [[1, 1], [2, 2], [3, 3]]
    print(maxPoints(points))  # 3


main()
