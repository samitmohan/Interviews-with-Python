# https://leetcode.com/problems/push-dominoes/description/
"""
Input: dominoes = ".L.R...LR..L.."
if dominoes[i] == '.':
    if dominoes[i+1] == "L":
        if dominoes[i-1] != "R":
            dominoes[i] == "L":
    if dominoes[i-1] == "R":
        if dominoes[i+1] != "L":
            dominoes[i] == "R":

 Pass 1: Left-to-Right (Simulating "R" forces)
    Whenever we see an 'R', we set force = N (maximum force).
    Then we reduce the force by 1 each step moving right (like a domino’s push weakening over distance).
    If we see an 'L', it cancels any rightward force (force = 0).
    We add this force to the forces[i] array.

 Pass 2: Right-to-Left (Simulating "L" forces)
    Same logic, but now looking for 'L' and simulating leftward force (also from max strength N, counting down).
    If we see 'R', it resets the leftward force to 0.
    We subtract this force from forces[i].

This adds in leftward influence (as a negative number).

At each domino position:
    If forces[i] == 0: equal pull → '.'
    If forces[i] > 0: stronger right pull → 'R'
    If forces[i] < 0: stronger left pull → 'L'
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        forces = [0] * len(dominoes)
        N = len(dominoes)
        # left to right pass
        force = 0
        for i in range(N):
            if dominoes[i] == "R":
                force = N
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        # right to left pass
        force = 0
        for i in reversed(range(len(dominoes))):
            if dominoes[i] == "L":
                force = N
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for f in forces:
            if f == 0:
                result.append(".")
            elif f > 0:
                result.append("R")
            else:
                result.append("L")
        return "".join(result)


s = Solution()
print(s.pushDominoes(".L.R...LR..L.."))
