#!/usr/bin/env python3
import math


def canPlaceBirds(b, n, nests, sep):
    birds = 1
    last_location = nests[0]
    for i in range(1, n - 1):
        currLoc = nests[i]
        if currLoc - last_location >= sep:
            birds += 1
            last_location = currLoc
            if birds == b:
                return True
    return False


def main():
    nests = [1, 2, 4, 8, 9]
    b = 3
    nests.sort()
    n = len(nests)

    # binary search
    low = 0
    high = nests[n - 1] - nests[0]
    ans = -1
    while low <= high:
        mid = (low + high) / 2
        canPlace = canPlaceBirds(b, n, nests, mid)
        if canPlace == True:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(math.ceil(ans))


main()
