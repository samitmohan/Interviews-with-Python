from collections import defaultdict


# O(n*log(n))


class Solution(object):
    """
     So once we've created our dictionary, we can turn it into a list correctly sorted - i.e. by decreasing frequencies,
     and then by lexicographical order - and then return this list (sliced at index k to make sure we return only the k most frequent words)
    """

    def topKFrequent(self, words, k):
        # hm = Counter(words)

        hm = defaultdict(int)
        for w in words:
            hm[w] += 1

        # sorts first by value (descending), then by key (lexicographical)
        # val : freq, key : words (x)
        ans = sorted(hm, key=lambda x: (-hm[x], x))
        return ans[:k]

    # doesn't work for lexicographical keys if frequency same

    def topKFrequent(words, k):
        hm = defaultdict(int)
        for word in words:
            hm[word] += 1
        # min heap
        heap = []  # (freq, word)
        for key, val in hm.items():
            # pushing val and key (val : freq and key : word)
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            ans.append([heapq.heappop(heap)[1]])
        # we want reversed since it'll be appended in reverse order
        return ans[::-1]


# K most frequent elements


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
        # sorting in reverse order and getting the keys, sliced for k times.
        answer = sorted(hashmap, key=hashmap.get, reverse=True)[:k]
        return answer
