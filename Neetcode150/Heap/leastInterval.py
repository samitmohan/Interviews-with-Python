# https://leetcode.com/problems/task-scheduler/
"""
AAABBCC
Hashmap : {A : 3, B : 2, C : 2}
n (waiting time) = 1

Best to pick most frequent character first so we're never idle even in waiting time
If we pick C first
  CBCBA_A_A_A = NAHHHH : 9
Pick A first
  ABCABCA : minimises the IDLE time : 7

MaxHeap : Configure which task if frequent : O(log(26))
Count occurence of each task and pop and add to maxHeap : O(n)

Time : n + time to process (1 second per task)
Queue to add task and time
"""

import heapq
from collections import Counter

# Time : O(n(log(n))) Space : O(n) (Counter takes nlogn)
# Round Robin technique (queue needed for tasks which are waiting for cool down period)
# Iterate till all the tasks are processed.
# Pick the task from heap having the maximum frequency.
# Since only one task can be processed in a unit time. So process the task. frequency -= 1
# Now if this task is left then it will have to wait for the cooldown period.
# So, add queue the task till its cooldown period is expired. (cooldown period : time taken by task + n)
# At end : process the tasks whose cooling period is expired.
from collections import deque


class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)  # no waiting time
        hashmap = Counter(tasks)
        heap = [-val for val in hashmap.values()]
        heapq.heapify(heap)
        queue = deque()  # [frequency, time_at_which_it_can_start_executing] # hold tasks which are waiting for cool down period

        time_taken = 0
        while heap or queue:  # iterate till all tasks processed (round robin)
            time_taken += 1
            # pick task with max freq
            if heap:
                frequency = -heapq.heappop(heap)
                # since only one task can be processed in unit time : process this task and update freq
                frequency -= 1
                # if task still left : put it in waiting queue and continue round robin
                if frequency:
                    queue.append(
                        [frequency, time_taken + n]
                    )  # enque task till it's cooldown period

            # process tasks whose cooling period is expired (waiting queue tasks)
            while queue and queue[0][1] == time_taken:
                heapq.heappush(
                    heap, -queue.popleft()[0]
                )  # only pop the frequncy (3 or 2 or 1 of letters)
        return time_taken
