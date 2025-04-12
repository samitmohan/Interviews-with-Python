# O(N)

def merge_intervals(intervals):
    # Sort the intervals by their start time
    intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize the merged intervals list with the first interval
    merged = [intervals[0]]

    # Iterate through the remaining intervals
    for interval in intervals[1:]:
        # If the current interval overlaps with the last merged interval, merge them
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        # Otherwise, add the current interval to the merged list
        else:
            merged.append(interval)

    return merged
