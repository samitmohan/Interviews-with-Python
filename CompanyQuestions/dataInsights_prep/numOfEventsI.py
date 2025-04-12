# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

# time : O(nlogn) : O(logn) for heap operations.
# space : O(n)
 
import heapq
# min heap
def maxEvents(self, events):
    heap = []
    i = 0 # event index
    ans = 0
    events.sort(key = lambda x : x[0]) # sort by start time
    while heap or i < len(events): 
        # if no events : move current time to start time of next day
        if not heap:
            curr_time = events[i][0]
        # add to heap (all events starting at same time) : avail to attend
        while i < len(events) and events[i][0] == curr_time:
            heapq.heappush(heap, events[i][1]) # add end time bcs all these events are avail to attend
            i += 1
        # greedy approach to pick min time avail events
        heapq.heappop(heap)
        ans += 1
        curr_time += 1
        # pop events that can't be attended bcs end time < current time
        while heap and heap[0] < curr_time: 
            heapq.heappop(heap)
    return ans
