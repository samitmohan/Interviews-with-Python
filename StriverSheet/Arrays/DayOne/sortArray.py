# https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/

"""
Given an array consisting of only 0s, 1s, and 2s.
Write a program to in-place sort the array without using inbuilt sort functions.
Expected: Single pass-O(N) and constant space

Take freq of 0,1,2 :: count_one = x, count_zero = y, count_two = z
replace first x indices of arr with 0, next y indices of arr with 1, next z indices of arr with 2 and return arr
"""


def sortColors(arr):
    count_zero, count_one, count_two = 0, 0, 0
    for i in arr:
        if i == 0:
            count_zero += 1
        elif i == 1:
            count_one += 1
        else:
            count_two += 1
    # for first x indices -> arr[i] = 0
    for idx in range(count_zero):
        arr[idx] = 0
    for idx in range(count_zero, count_zero + count_one):
        arr[idx] = 1
    for idx in range(count_zero + count_one, len(arr)):
        arr[idx] = 2

    return arr


def main():
    print(sortColors(arr=[2, 0, 2, 1, 1, 0]))  # [0,0,1,1,2,2]
    print(sortColors(arr=[2, 0, 1]))
    print(sortColors([0]))


main()
