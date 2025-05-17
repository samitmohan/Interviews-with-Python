# https://www.youtube.com/watch?v=7ABFKPK2hD4
# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None  # DLL


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to nodes
        self.left, self.right = Node(0, 0), Node(0, 0)  # LRU AND MRU
        # put val in middle (left and right are connected)
        self.left.next = self.right
        self.right.prev = self.left

    # helper pointer functions -> applied to linked list
    # simple LL pointer manipulation

    def remove(self, node):  # remove from list
        # prev and next
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):  # insert at right most posn
        # prev.next -> node and nxt.prev -> node and node.nxt -> right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node  # in the middle
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # return self.cache[key] = node -> for val -> .val
            # todo : update most recent
            # take node -> self.cache[key] and remove from list and re insert it at Right most posn (MRU)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # node already exists in hashmap
            self.remove(self.cache[key])
        # create new node with k,v pair
        self.cache[key] = Node(key, value)
        # DLL -> take node and insert it to right most
        self.insert(self.cache[key])
        # capacity check
        if len(self.cache) > self.cap:
            # if yes -> del LRU (remove from LL and from cache/hm)
            # finding LRU -> using DLL pointers (left and right)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
