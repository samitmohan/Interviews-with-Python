# O(n)
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


# O(1) : rolling
# "what is the sum of elements in a range [i, j]?"


def prefix_sum_optimized(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    def range_sum(i, j):
        if i == 0:
            return prefix[j]
        else:
            return prefix[j] - prefix[i - 1]

    return range_sum
