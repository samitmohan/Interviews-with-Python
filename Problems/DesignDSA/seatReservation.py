# https://leetcode.com/problems/seat-reservation-manager/
# reserve : smallest numbered seat
# min value : min heap.

import heapq


# the reserve and unreserve calls will always be valid
# only need 1 minheap = track of unreserved seats
# reserve = pop from unreserve = reserved : logN
# unreserve = take seat and add to unreserve minheap : logN

# heapify : take array and convert to heap
# but no need to heapify arr since values are from 1 - n
# 1,2,3...n =
#    1
#   / \
#  2   3
# already a min heap : no need to heapify


class SeatManager:
    def __init__(self, n: int):
        self.unres = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.unres)  # pop min val

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres, seatNumber)  # in unres heap and at seatNumber
