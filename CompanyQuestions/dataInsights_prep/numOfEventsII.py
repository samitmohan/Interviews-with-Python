"""
Hermoine of Hogwarts gets hands on the schedule of all events going on during winter breaks. She would like to attend a maximum of these events and get points to her house Griffindor.
She can only attend one event at a time, if she chooses to attend an event, she must attend the entire event. Note that the end day is inclusive, that is you cannot attend two events where one of them starts and other ends on the same day. 

Given an array of events where events[i] - [startDay[i], endDay[i], points[i]]. The ith event starts at startDay[i] and ends at endDay[i], and if you attend this event you will recieve point of points[i]. You are also given an integer k which represents the maximum number of events Hermoine can attend.

Return maximum of total points that you can recieve by attending these events.

Test cases -:

Input : events = [[1,2,4], [3,4,3], [2,3,1]], k = 2
Output : 7
Explanation : Total points : 4+3=7

Input : events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output : 10

Input : events = [[1,1,1], [2,2,2], [3,3,3], [4,4,4]], k = 3
Output: 9

Sample input explanation : First line is k, next line is the number of events. Next 3n lines are the start, end and points of each event.

Sample Input (Example 1)
2
3
1
2
4
3
4
3
2
3
10

Sample Output (Example 1)
10
"""
# Time : O(nk*logn)
# Space : O(nk)
# k = max events she can attend
def maxEvents(events):
    e = sorted(events)
    @functools.lru_cache(None)

    def dp(i, k):
        if k == 0 or i == len(e): return 0
        # find the index j of the first event whose start time is greater than the end time of the current event e[i][1]
        # finds first event that can be attended after current event.

        j = bisect.bisect(e, [e[i][1], math.inf, math.inf], i + 1) # e[i][1] : end time of curr, i+1 : starts search imediately after current event e[i]
        # max val calc by either attending or not attending event e[i]
            # dp(i+1, k) : not attended, skip to next.
            # e[i][2] + dp(j, k - 1) : attending curr event, adding its value (e[i][2]) and calling same function on other events (k-1 now)
        return max(dp(i + 1, k), e[i][2] + dp(j, k - 1))

    return dp(0, k) # start with index 0
