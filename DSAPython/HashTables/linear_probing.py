#!/usr/bin/env python3
# fast searching
# implement dictionary

# hashing : hash function : hf(key) = key % size
# problem with this function : doesn't work on strings (list : [cat, dog, rain]) can't do cat % 3 : need to find ascii('c') + ascii('a') + ascii('t') % 3
# python inbuilt : hash() : hash(123) = 123 works and hash(cat) : 1329667300978243676
# problem : sometimes hashes are negative : use abs
# Linear Probing : if same hash : rehash : (old_hash_value + 1) % size : looks for next open slot until empty slot found

# handling collisions -> probing (open addressing) and chaining (closed addressing (in place)
# probing : changing the position of they key to next empty slot available
# chaining : forming linked list / tree for chaining of collisions

# 2 arrays needed : slots (keys) and data (values)
# {python : 37} : python's hash value : 2 so in 2th index of slots array : put python and in 2nd index of data array : put 37
# slots : [_,_,python,_,_,_] # key
# data : [_,_,37,_,_,_] # value


class Dictioanry:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if (
            self.slots[hash_value] == None
        ):  # if empty : put key in slot and value in data
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            # 2 options : same key already present : update value || different key present : rehash
            if self.slots[hash_value] == key:
                self.data[hash_value] = (
                    value  # update with new value (no need to change key)
                )
            else:
                new_hash_value = self.rehash(hash_value)
                # keep iterating ahead until empty space found -> to put the value && same key already present : [c++, java, php, python, _] and key = python -> then it'll place it in _ (it shouldn't)
                while (
                    self.slots[new_hash_value] != None
                    and self.slots[new_hash_value] != key
                ):
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value] == None:
                    # put key and value
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:  # update existing key
                    self.data[new_hash_value] = value

    def get(self, key):
        # keep iterating until you get the item.
        # how to know if item not present : if start_pos = end_pos (checked everything) || empty slot found
        start_pos = self.hash_function(key)
        current_pos = start_pos
        while (
            self.slots[current_pos] != None
        ):  # keep looking until empty slot found -> empty slot represnts value not present
            if self.slots[current_pos] == key:
                return self.data[current_pos]
            current_pos = self.rehash(current_pos)  # increment by 1 every time
            if current_pos == start_pos:
                return "Not found"

        return "Not found -> empty slot"

    # printing key value pair like an actual {} : magic method __str__ used
    def __str__(self) -> str:
        for i in range(len(self.slots)):
            if self.slots[i] != None:  # if not empty : print
                print(self.slots[i], ":", self.data[i], end=", ")
        return ""

    # magic methods for put and get : instead of d1.get(k) or d1.push(k, v) we can do put = d["k"] = v and get = d["k"] {like a dictionary}
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def hash_function(self, key):
        return abs(hash(key)) % self.size


d1 = Dictioanry(3)
print(d1.slots)  # None None None
print(d1.data)  # None None None

d1["python"] = 56
d1["c++"] = 100
d1["java"] = 230
print(d1.get("java"))  # 230
print(d1)  # c++ : 100, java : 230, python : 56,
