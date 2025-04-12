class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for i, r in enumerate(ranges):
            # Ignore taps that don't water anything
            if r == 0:
                continue
            # Calculate the start and end positions of the tap
            start = max(0, i - r)
            end = min(n, i + r)
            taps.append((start, end))

        # Sort taps by their start position
        taps.sort()

        # Current position and maximum reachable position
        curr_pos = 0
        max_reach = 0

        # Number of taps used so far
        taps_used = 0

        # Iterate over taps and find the farthest tap that can be reached
        i = 0
        while i < len(taps) and curr_pos < n:
            # Check if the current tap can be reached
            while i < len(taps) and taps[i][0] <= curr_pos:
                max_reach = max(max_reach, taps[i][1])
                i += 1

            # If no tap can be reached from the current position, return -1
            if max_reach <= curr_pos:
                return -1

            # Use the farthest tap that can be reached and update the position
            taps_used += 1
            curr_pos = max_reach

        # If the entire garden has been watered, return the number of taps used
        if curr_pos >= n:
            return taps_used

        # Otherwise, there are still parts of the garden that have not been watered
        return -1
