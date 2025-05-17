# https://leetcode.com/problems/ipo/
class Solution:
    """
      2 arrays give : capital and profit. w = 0 at first, need to maximise w
      profits = [1,2,3] : can take atmost k elements out of profits : 2,3 : 0 + 2 + 3 : 5
        Only catch here : the profit we're adding, correpsonding capital <= w (which in this case wasn't since 1 <=! 0) :: so we can only take 0 as first : 0 <= 0 : add 1 (corresponding profit) : 0 + 1 = 1 (now we can take 3 : 1 + 3 = 4) answer w = 4
      capital = [0,1,1]

      Use max heap for profits so we can get the max element : 3,2,1 (not a good idea since 3 can't be popped at beginning since w = 0 and capital[3] = 1 (1 !<= 0))
      Initialise heap with values that can be added to w => (1,0) : (profit, capital)
        Pop element 1, check if w <= 0 (it is) add to w.
        Now max heap is empty. As our capital changes we have access to more profit elements

      Use a min heap for remaining elements (2,3) based on capital (1,1) :: pop min value : 1, check if w <= capital : it is. Push it to max heap and add answer to w

    Pattern : 2 Heaps : max heap on profits (to figure out most profit )and min heap on capacity (to figure out least capacity so it can be compared to w and be added to max heap and then w can be incremented)

    Time : O(k * log(n)), Space : O(n)
    """

    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # 2 Heaps
        max_profit = []  # only projects we can afford
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)  # in python default : minheap
        for i in range(k):
            while (
                min_capital and min_capital[0][0] <= w
            ):  # condition : if true : pop from MH and push to MX
                c, p = heapq.heappop(min_capital)  # get c, p. only care about profit
                heapq.heappush(max_profit, -1 * p)  # max heap : mulitple -1

            if not max_profit:
                break  # max heap is empty -> none of profits available can't increase w

            w += -1 * heapq.heappop(max_profit)  # to make it positive
        return w
