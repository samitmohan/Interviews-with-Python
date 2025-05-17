def unsorted(nums):
    mn = float("inf")
    mx = -float("inf")
    start = end = flag = 1

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            flag = 1  # unsorted found
            mn = min(mn, nums[i])
            mx = max(mx, nums[i - 1])

    if flag == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] > mn:
            start = i
            break

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < mx:
            end = i
            break

    return end - start + 1


def main():
    print(unsorted([2, 6, 4, 8, 10, 9, 15]))


main()
