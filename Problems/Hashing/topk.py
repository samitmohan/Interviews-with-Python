def topKFrequent(nums, k):
    # hashmap
    hashmap = {}
    # add all elements into that hashmap
    for x in nums:
        if x not in hashmap:
            hashmap[x] = 1
        else:
            hashmap[x] += 1
    # return the answer
    return sorted(hashmap, key=hashmap.get, reverse=True)[:k]


def main():
    nums = [1]
    k = 1
    print(topKFrequent(nums, k))


main()
