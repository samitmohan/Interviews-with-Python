# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1  # why 1> arrow has to be shot to start the process
        current_end = points[0][1]  # first elem of 0th sub array
        for start, end in points:  # compare start of every sub array and current_end
            if (
                start > current_end
            ):  # 1 > 6 no 2 > 6 no 7 > 6 (yes) current end = 12 (6,12) res++
                current_end = end
                arrows += 1
        return arrows


# sort balloons in ascending order and think of shooting end point of first balloon in order to maximise bursting of all balloons with min arrows
