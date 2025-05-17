class MyHashMap:
    def __init__(self):
        self.number_of_buckets = 1000
        self.buckets = [-1] * self.number_of_buckets

    def put(self, key: int, value: int) -> None:
        # index = key mod 1000
        index = key % self.number_of_buckets
        # if bucket exists then look for key otherwise create key
        if self.buckets[index] == -1:
            self.buckets[index] = [[key, value]]
            return
        for idx, kv in enumerate(self.buckets[index]):
            if kv[0] == key:  # if key present
                self.buckets[index][idx][1] = value
                return
        self.buckets[index].append([key, value])
        return

    def get(self, key: int) -> int:
        index = key % self.number_of_buckets
        if self.buckets[index] == -1:
            return -1
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.number_of_buckets
        index_to_remove = -1
        if self.buckets[index] == -1:
            return
        for i, kvPair in enumerate(self.buckets[index]):
            if kvPair[0] == key:
                index_to_remove = i
                break
        if index_to_remove == -1:
            return
        else:
            del self.buckets[index][index_to_remove]
