'''
Identical to Koko Eating Bananas
weights = [1,2,3,4,5]
days : 2
capacity ranges from [5,15]

mid = 5+15/2 : 10 -> capacity
[1,2,3,4] can be consumed in 1 day
[5] can be consumed in 2nd day 
WORKS : but 10 is a lot, can we minimise this : binary search
ans_so_far = 10
  look in the left half : high = mid - 1
ans_so_far = min(ans_so_far, mid)
'''


class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(mid):
            # go through input array and consume weights until mid (capacity) reached (10 in this case)
            ships = 1  # need atleast one
            current_capacity = mid
            for w in weights:
                if current_capacity - w < 0:  # can't hold weight : need more ships
                    ships += 1
                    current_capacity = mid  # fresh ship has new capacity
                current_capacity -= w

            return ships <= days

        # range of binary search explained in video :: 5 = min capacity and capacity can't exceed sum(weights) : 15
        low, high = max(weights), sum(weights)
        ans = high  # for now
        while low <= high:
            mid = (low + high) // 2
            if canShip(mid):
                # new min res
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
