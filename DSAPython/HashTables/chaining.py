#!/usr/bin/env python3

# handling collisions -> probing (open addressing) and chaining (closed addressing (in place)
# probing : changing the position of they key to next empty slot available
# chaining : forming linked list / tree for chaining of collisions
# if chain too long -> O(N) complexity : to fix : rehash -> typically double the size of the array and rehash it.
# chaining is done via linkedlist O(N) or tree O(logN)
# be on the same index and go down and attach to the linked list

# We're making an array of linked lists (buckets) : each item in array is of type linked list.

# creating linked list class


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # initially


class LL:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = Node(key, value)
        if self.head == None:  # add to beginning of LL
            self.head = new_node
        else:  # add to end of LL
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    # deleting head
    def delete_head(self):
        if self.head == None:
            return "Empty"
        else:
            self.head = self.head.next

    # removing is based on key only
    def remove(self, key):
        if self.head.key == key:
            self.delete_head()
            return

        if self.head == "None":
            return "Empty"
        else:  # find the key to be deleted
            temp = self.head
            while temp.next != None:
                if temp.next.data == key:
                    break
                temp = temp.next
            if temp.next == None:
                return "Not found"
            else:
                temp.next = temp.next.next  # delete node and point it to next.next : temp = 1 :: 1 -> 2 -> 3 [2 delete] : 1 -> 3

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.key, "-->", temp.value, " ", end=" ")
            temp = temp.next

    # size of linkedlist : used in lf rehash
    def size(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return counter

    def search(self, key):  # returns index of the key
        temp = self.head
        pos = 0
        while temp != None:
            if temp.key == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    # for put : get_node_at_index :: if {2 -> 3,  4 -> 5, 6 -> 8} and get_node_at_index(1).key : 4 and get_node_at_index(0).value = 3
    # helps in updating the node if already present in put case in chaining
    def get_node_at_index(self, index):
        temp = self.head
        counter = 0
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter += 1


# Hashing via chaining
# rehashing is based on laod factor : size / capacity
# size = nnumber of linked list chaining at that position
# capacity = number of elements in array
# load factor <= 2 (asusume) : if more than 2 -> array size double (capacity * 2)
# old bucket -> rehash and add it to new bucket of new capacity
# capacity changed so hash_function also changed -> balances things out


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity  # number of items in array
        self.size = 0  # how many k-v pairs in my dictionary
        # array of linked list
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(
                LL()
            )  # inside L there will exists n number of linked list class (n = capacity)
        return L

    def get(self, key):
        bucket_index = self.hash_function(key)
        res = self.buckets[bucket_index].search(key)
        if res == -1:
            return "Not Present"
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.value

    def put(self, key, value):
        # index position will be finalised (unlike linear probing in which index posn + 1 if already filled) -> forms chain if already filled.
        # this index is called bucket index (each LL is called bucket)
        bucket_index = self.hash_function(key)
        # 2 possibilities : if empty : add to it, if filled : add to tail
        # edge case check : if key already present -> just update the value no need to enter it again else if new key : just add to tail
        # 2 functions : insert and update
        # update : get node index
        node_index = self.get_node_index(bucket_index, key)

        if node_index == -1:  # new fresh node
            # insert
            self.buckets[bucket_index].add(
                key, value
            )  # in the array of linked list : goto that index/element_made_of_LL where insert and add key value pair
            self.size += 1

            load_factor = self.size / self.capacity
            if load_factor >= 2:  # more than lf
                self.rehash()
        else:
            # update
            node = self.buckets[bucket_index].get_node_at_index(
                node_index
            )  # get the updated node (K, V)
            node.value = value  # update

    def rehash(self):
        # double array size when load_Factor / threshold reached [re-initialise everything]
        self.capacity *= 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        # every item in old bucket needs to be re-hashed and put into the new bucket
        for i in old_buckets:  # LL [1,2,3,4]
            for j in range(i.size()):  # inside chaining LL traverse [1[1,2,3]]
                node = i.get_node_at_index(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item, value_item)

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index

    # magic methods
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)

    def __str__(self):
        for i in self.buckets:
            i.traverse()
        return ""

    def __len__(self):
        return self.size


d1 = Dictionary(4)
d1.put("python", 1)
d1["java"]  # not present
d1.put("java", 2)
d1.put("c++", 34)
d1["matlab"] = 334
print(d1)
print(len(d1))
