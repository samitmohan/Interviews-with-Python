# https://leetcode.com/problems/race-car/description/
# https://www.youtube.com/watch?v=DBJPWJr5zZ4 (Great Explanation)
# Most asked Google Question 2023
# BFS, consider points like a graph
import collections


class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque([(0, 0, 1)])  # curr num of moves, pos and speed
        visited = set()

        while q:
            moves, pos, speed = q.popleft()
            if pos == target:
                return moves

            if (pos, speed) in visited:
                continue
            else:  # new pos : explore
                visited.add((pos, speed))
                # move forward
                q.append((moves + 1, pos + speed, speed * 2))

                # we will hit a point where we overshoot a target, and we need to reverse
                # cases:
                # 1) overshot our target,
                # 2) speed negative (target = 6, and we're at 4 then we need to go reverse IF speed is neg)
                if (pos + speed > target and speed > 0) or (
                    pos + speed < target and speed < 0
                ):
                    speed = -1 if speed > 0 else 1
                    q.append((moves + 1, pos, speed))
