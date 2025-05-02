import heapq
from types import List


class Solution:
    """
    1) Sort tasks and workers so that it's easy to find which worker to give the pill to
    2) Put these tasks and worker items in a stack in reverse order such that the minimum element is on top for both of these.
    Something like this for the given example-:
    task_stack               worker_stack
    .                                             .
    1                                            0
    2                                            3
    3                                            3
    .                                              .

    4) Iterate until either one of these stacks get finished -> check if workerStack.top() >= taskStack.top() -> if yes pop both and increment answer by 1. Also final_ans = max(ans, final_ans) so that it returns correct answer.
    5) If the top elements of both stacks are not equal -> the magic pill part. workerStack.top() += strength but for atmost 1 pill per worker.
    6) Return final_ans

    """


# original solution
class Solution:
    def maxTaskAssign( self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks_sorted = sorted(tasks, reverse=True)
        workers_sorted = sorted(workers, reverse=True)
        tStack = tasks_sorted[:]
        wStack = workers_sorted[:]
        curr_ans, final_ans = 0, 0

        while tStack and wStack:
            # Direct assignment
            if wStack[-1] >= tStack[-1]:
                wStack.pop()
                tStack.pop()
                curr_ans += 1
                final_ans = max(final_ans, curr_ans)
            # Try with pill
            elif pills > 0 and wStack[-1] + strength >= tStack[-1]:
                pills -= 1
                wStack.pop()
                tStack.pop()
                curr_ans += 1
                final_ans = max(final_ans, curr_ans)
            else:
                # Can't do this task even with pill
                # tStack.pop()
                break

        return final_ans  # doesn't work, use BS


# This works great for greedy matching, but doesn't handle tricky edge cases where task assignment order matters.
# If the strongest workers get matched with easier tasks, the harder tasks may become impossible later.
# That’s why the heap-based version gives more flexibility by always assigning the hardest task possible per worker.

"""
One good trick to use here is binary search
     # Binary search over number of assignable tasks
        left, right = 0, min(len(tasks), len(workers))
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid): # answer found!, look for right part for more answers 
                answer = mid
                left = mid + 1
            else: # u need fewer task for the worker -> look left
                right = mid - 1
Also we’re assigning tasks greedily, matching:
    The hardest task with the strongest worker
    If no direct match, then using a pill on the weakest viable worker
    If neither works, we skip that worker
"""

# Better approach


class Solution:
    def maxTaskAssign( self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k):
            # Use the hardest k tasks and strongest k workers
            task_stack = tasks[:k][::-1]
            worker_stack = workers[-k:][::-1]
            pills_left = pills

            while task_stack and worker_stack:
                task = task_stack[-1]
                worker = worker_stack[-1]

                if worker >= task:
                    task_stack.pop()
                    worker_stack.pop()
                elif worker + strength >= task and pills_left > 0:
                    task_stack.pop()
                    worker_stack.pop()
                    pills_left -= 1
                else:
                    # this worker can't do this task, try a stronger worker
                    worker_stack.pop()

            return not task_stack  # all tasks assigned or not

        # Binary search over number of assignable tasks
        left, right = 0, min(len(tasks), len(workers))
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


# Issue with this? The hardest k task pairing with strongest k workers doesn't always work.
"""
The stack approach processes tasks and workers in a fixed order, typically matching the hardest tasks with the strongest workers. 
However, this rigid matching doesn't account for scenarios where a more flexible pairing could yield better results. 
In this test case, the optimal assignment requires a non-greedy pairing that the stack approach doesn't consider.

A better approach for flexibility is to use a heap.
Cant use dp -> O(m*n) is still huge {looking at the constraints}
"""


from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()  # Easiest to hardest
        workers.sort(reverse=True)  # Strongest to weakest

        def can_assign(num_tasks):
            current_tasks = tasks[:num_tasks]           # Easiest tasks
            current_workers = workers[:num_tasks]       # Strongest workers
            available_workers = SortedList(current_workers)
            pills_left = pills

            for task in reversed(current_tasks):  # From hardest of the `num_tasks` tasks
                # If we can assign without a pill
                if available_workers and available_workers[-1] >= task:
                    available_workers.pop()
                else:
                    # Need a pill
                    if pills_left == 0:
                        return False
                    idx = available_workers.bisect_left(task - strength)
                    if idx == len(available_workers):
                        return False
                    available_workers.pop(idx)
                    pills_left -= 1
            return True

        # Binary search on the maximum number of tasks we can assign
        left, right = 0, min(len(tasks), len(workers))
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
``