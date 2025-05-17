# https://leetcode.com/problems/course-schedule/description/
# Topological Sort
# 1. Adjacency matrix -> ingoing and outgoing edges
# 2. if ingoing edge of any node = 0, add to answer, course_take.pop(), course_taken += 1
# 3. Re-evaluate by removing outgoing edges of course_take from ingoing edges
# 4. if courses_taken = numCourses : return True else False
# Time complexity : O(E + V)

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ingoing = defaultdict(set)
        outgoing = defaultdict(set)
        # adj list (j -> i) means j is a prequesite for i
        for i, j in prerequisites:
            ingoing[i].add(j)
            outgoing[j].add(i)

        canTake = [i for i in range(numCourses) if len(ingoing[i]) == 0]
        taken = 0
        while (
            len(canTake) > 0
        ):  # pop -> remove ingoing edges and their relationships with outgoing edges
            take = canTake.pop()
            taken += 1
            for next_course in outgoing[
                take
            ]:  # take -> next_course :: from outgoing edges of take : remove
                ingoing[next_course].remove(take)
                if len(ingoing[next_course]) == 0:
                    canTake.append(next_course)  # check for next
        return taken == numCourses
