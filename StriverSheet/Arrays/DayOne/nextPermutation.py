# https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
"""
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Example 1 :

Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.

Example 2:

Input format: Arr[] = {3,2,1}
Output: Arr[] = {1,2,3}
Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.

Generate all permutations
    Base case:
    If your list has only one element, there's only one way to arrange it: itself!
    Example: [3] → [[3]]

    Recursive case:
    For a list with more than one element, pick each element in turn, and:
        Remove it from the list.
        Find all permutations of the remaining elements (recursively).
        Add the removed element to the front of each of those smaller permutations.

Sort them lexicographically
Find the index of arr in the sorted list
Return the next permutation if it exists
"""


def nextPermutation(arr):
    # Horrible Time and Space complexity : O(n! * n), O(n!)
    def generate_permutations(arr):
        # base case
        if len(arr) == 1:
            return [[arr[0]]]  # only element -> permutation

        # recursive case
        permutations = []
        for i in range(len(arr)):
            # pick one, permute rest
            rest = arr[:i] + arr[i + 1 :]
            for perm in generate_permutations(rest):
                permutations.append([arr[i]] + perm)
        return permutations

    all_perms = generate_permutations(arr)
    all_perms.sort()
    idx = all_perms.index(arr)
    return all_perms[(idx + 1) % len(all_perms)]  # return next or first if its the last


# The replacement must be in place and use only constant extra memory.
def nextPermutationBetter(arr):
    """
    Honestly, I think this is just a matter of whether you know it or not, so don't worry too much if you can't do it.
    Modifies the input array to the next lexicographical permutation.

    Steps:
    1. Find the largest index i such that arr[i] < arr[i + 1] (pivot)
    2. Find the largest index j > i such that arr[j] > arr[i]
    3. Swap arr[i] and arr[j]
    4. Reverse from arr[i + 1] to the end

    Time: O(n), Space: O(1)
    """
    breakPt = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            breakPt = i
            break

    if breakPt == -1:
        # [1,2,3,4,5] -> next permutation will be [5,4,3,2,1] (this is last permutation)
        arr.reverse()
        return

    for i in range(len(arr) - 1, breakPt, -1):
        if arr[i] > arr[breakPt]:
            arr[i], arr[breakPt] = arr[breakPt], arr[i]  # swap
            break

    # Reverses the suffix to make it the smallest permutation after the break point (try to place remaining in sorted order)
    arr[breakPt + 1 :] = reversed(arr[breakPt + 1 :])
    return arr


def main():
    print(nextPermutation([1, 3, 2]))  # Output: [2, 1, 3]
    print(nextPermutationBetter([1, 3, 2]))  # Output: [2, 1, 3]


main()
