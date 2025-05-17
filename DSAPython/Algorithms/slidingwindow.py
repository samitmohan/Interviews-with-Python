# Sliding winodw : overlapping subproblems in O(N) time

# Find sum of sub-arrays
# k = 3
# [1,2,3,4,5,6]

# [1+2+3], [2+3+4], [3+4+5] -> we're computing 2+3 again : O(N * k)
# first subarray : include one do not include 4
# second subarray : dont include one but include 4
# only thing that changes : first and last value

# [2+3+4] = 9
# [1+2+3] = 6
# exlude one and include 4 : 6 - 1 + 4
# k = 5
# [1,2,3,4,5] [2,3,4,5,6] : large overlap between these subarrays
# subtract first val and add last val to sum
# 15 - 1 + 6 : 20

# slide window by 1 every time by subtracting first index and adding last index

# FIXED SIZE SLIDING WINDOW : always size k


def fixed_sw(arr, k):
    # sum up first subarray and add it to result
    current_subarray = sum(arr[:k])
    result = [current_subarray]

    # add next value in list and remove first value
    for i in range(1, len(arr) - k + 1):
        current_subarray -= arr[i - 1]
        current_subarray += arr[i + k - 1]
        result.append(current_subarray)
    return result


# DYNAMIC SIZE SLIDING WINDOW : to find largest/smallest subarray give a condition
# x = 7
# [1,2,3,4,5,6] find shortest subarray with sum >= 7
# 1,2,3,4 minlength = 4, found now contract from first half : [2,3,4] -> [3,4] *FOUND*
# sum = 10 -1 = 9, minlength = 3, contract again, 9 -2 = 7, minlength = 2, contract again 7-3 = 4 < 7 NO.
# expand again, 4,5 : sum = 9, minLength = 2

# similarily : 4,5 and 5,6 of length 2
# allows us to start small (size = 1) and expand until we match our condition
# once subarray found with sum, contract the first half to find minimal size subarray


def dynamic_sw(arr, x):
    minlength = float("inf")
    start, end, curr_sum = 0, 0, 0  # current range and sum of our sliding window
    # extend sliding window until criteria is met
    while end < len(arr):
        curr_sum += arr[end]
        end -= 1
        # contract sliding window until it no longer meets our condition
        while start < end and curr_sum >= x:
            curr_sum -= arr[start]
            start += 1

            minlength = min(minlength, end - start + 1)
    return minlength


# Problems -> Problems section
# Most likely : use hashmaps with sliding window problems
# Window size : r + l - 1
# Always right += 1 and left += 1 when window size reached
