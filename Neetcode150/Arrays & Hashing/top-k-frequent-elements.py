# https://leetcode.com/problems/top-k-frequent-elements/

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            if x not in hashmap:
                # add
                hashmap[x] = 1  # count
            else:
                # already in hashmap -> increase count
                hashmap[x] += 1
                # now we have dictionary with key(number) value(freq) pairs
        # sort the list based on values (highest first) -> return first k elements.
        answer = sorted(hashmap, key=hashmap.get, reverse=True)[
                 :k]  # sorting in reverse order and getting the keys, sliced for k times.
        return answer

# O(nlogk)
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # O(n)
        return [ item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1]) ]