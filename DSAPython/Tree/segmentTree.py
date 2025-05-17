# segment tree / range sum query problem
import math

"""
Given an integer array nums, handle multiple queries of the following types:

    Update the value of an element in nums.
    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
 
 0 1 2 3 4
[1,2,3,4,5]


Brute force : Range Sum : O(NQ), Update : O(1)
Segment Tree : Range Sum : O(Q), Update : O(N)
Instead of calculating sum for N numbers Q number of times it'll take O(N * Q) : not efficient -> keep precomputed sum
[1,3,6,10,15] now for sum(1,3) we can find sum(left-1) - sum(right) = sum(0) - sum(3) = abs(1 - 20) = 19 -> O(Q)
When we are updating lets say arr[1] = 4 we need to update array and precomuted sum array : new arr = [1,4,3,4,5], precomp = [1,5,8,12,17] Each update takes O(N) time

Segment Tree using array (Using FBT) -:
    if curr_node = i: left_child = 2*i + 1, right_child = 2*i + 2, parent = floor((i-1)/2) # same as FBT
    Once you reach leaf node -> return sum, for internal node -> sum = left + right

    [1,2,5,6,7,9]
     /        \
    [1,2,5]    [6,7,9]

    Root node will store sum of all
    Sum of [6,7,9] will be stored in 2*0 + 2 = 2nd index
    Sum of [1,2,5] will be stored in 2*0 + 1 = 1st index
    Similarily, sum of [1,2] will be stored in 2*1 + 1 = 3rd index

Final array looks like this-:
 0   1  2   3 
[30, 8, 22, 3...]

Number of leaf nodes in FBT : n, number of internal nodes : n-1, ht(h) = ceil(log(n+1)), size of segment tree array : n = 2^h - 1 

Range Sum Query after making Segment Tree of array :: 3 cases -:
Total overlap, no overlap, partial overlap (of ranges)
When no overlap, return 0 value
Complete overlap, return the value
Partial overlap, make call to left and right side and return left+right

Update : update original array (O(1)) and update segment tree (same cases) if out of range : return; takes log(N) time

Segment Trees are useful only when updates are frequent. 

"""


# utility function to get middle index
def getMid(start, end):
    return start + (end - start) // 2


# recursive function to get sum of values in given range of array
"""
st = pointer to segment tree
si = index of current node in segment tree (0 is passed as it's the root)
ss and se = start and end index of segment represented by current node
qs and qe = start and end index of query range
"""


def getSum_helper(st, ss, se, qs, qe, si):
    if qs <= ss and qe >= se:
        return st[si]  # segment of node is part of given range
    if se < qs or ss > qe:
        return 0  # segment of node is outside given range
    # if part of segment overlaps with given range -> split again
    mid = getMid(ss, se)
    return getSum_helper(st, ss, mid, qs, qe, 2 * si + 1) + getSum_helper(
        st, mid + 1, se, qs, qe, 2 * si + 2
    )


# update
"""
i = index of element to be updated (in input array)
diff = value to be added to all nodes in seg tree which have i in range 
"""


def update_helper(st, ss, se, i, diff, si):
    if i < ss or i > se:
        return  # input index lies outside of range of this segment
    # in range
    st[si] = st[si] + diff
    # if not leaf node, update all internal nodes by splitting
    if se != ss:
        mid = getMid(ss, se)
        update_helper(st, ss, mid, i, diff, 2 * si + 1)
        update_helper(st, mid + 1, se, i, diff, 2 * si + 2)


# now update in array
def update(arr, st, n, i, new_val):
    if i < 0 or i > n - 1:
        return
    diff = new_val - arr[i]  # difference between new val and old val
    arr[i] = new_val
    update_helper(st, 0, n - 1, i, diff, 0)  # index to be updated is 0 (ROOT)


def getSum(st, n, qs, qe):
    if qs < 0 or qe > n - 1 or qs > qe:
        return -1
    return getSum_helper(st, 0, n - 1, qs, qe, 0)


def constructSegTree_helper(
    arr, ss, se, st, si
):  # si = index of current node in segment tree st
    # if only 1 element in array : store in current node of seg tree and return
    if ss == se:
        st[si] = arr[ss]
        return arr[ss]
    # if more -> split
    mid = getMid(ss, se)
    st[si] = constructSegTree_helper(
        arr, ss, mid, st, si * 2 + 1
    ) + constructSegTree_helper(arr, mid + 1, se, st, si * 2 + 2)
    return st[si]


def constructSegTree(arr, n):
    # ht
    x = math.ceil(math.log2(n))
    max_size = 2 * pow(2, x) - 1
    st = [0] * max_size
    constructSegTree_helper(arr, 0, n - 1, st, 0)
    return st


def main():
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
    st = constructSegTree(arr, n)
    print("Sum of values in given range = ", getSum(st, n, 1, 3))  # 15
    update(arr, st, n, 1, 10)  # 3 updated to 10
    print("Updated sum of values in range range = ", getSum(st, n, 1, 3))  # 22


main()
