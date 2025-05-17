def addToArrayForm(nums, k):
    s = 0
    # convert to string
    for i in nums:
        s = s * 10 + i
    s += k  # add number 34 : 3421
    # convert to list
    lst = []
    while s != 0:
        lst.append(s % 10)
        s //= 10
    return lst[::-1]  # in reverse


def main():
    nums = [1, 2, 0, 0]
    k = 34
    print(addToArrayForm(nums, k))  # [1,2,3,4]


main()
