# in place unstable sorting algorithm.
"""
Given range 1-N : Use Cyclic Sort (should be in continuous order in range 1-N)
0 1 2 3 4 # index
3 5 2 1 4
After sorting
0 1 2 3 4
1 2 3 4 5

Observation : index = value - 1
Sort it with just one pass.

0 1 2 3 4
3 5 2 1 4

is 3 placed at correct index? (value - 1 : 3 - 1 : 2), no 3 is not at 2nd index. Swap with correct index.
0 1 2 3 4
2 5 3 1 4

is 2 placed at correct index? (value - 1 : 2 - 1 : 1), no 2 is not at 1st index. Swap with correct index.
0 1 2 3 4
5 2 3 1 4

is 5 placed at correct index (5 - 1 : 4), no 5 is not at 4th index. Swap.

0 1 2 3 4
4 2 3 1 5

is 4 placed at correct index (4 - 1 : 3), no 4 is not at 3rd index. Swap.

0 1 2 3 4
1 2 3 4 5

Sorted.
"""


# if range = [0, N] : every element will be at index = value
# if range = [1, N] : every element will be at index = value - 1


def cyclicSort(arr):
    # start looking from i, swap with correct index, only move i pointer when i is at correct index.
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1

    return arr


if __name__ == "__main__":
    arr = [3, 5, 2, 1, 4]
    print(cyclicSort(arr))
