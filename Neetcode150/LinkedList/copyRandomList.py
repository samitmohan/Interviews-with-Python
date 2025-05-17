# https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

Every node ALSO has a random pointer (could be pointing anywhere (null, random node etc..))
Deep copy (clone the nodes) : new memory (create new LL)
5 nodes in inp -> 5 nodes in op
  Difficulty : random pointers
  Cloning nodes : [1,2,3]
    3rd node random ptr -> 5th node but we haven't gotten to that node yet : 2 passes/loops
    1st pass : take input node and create deep copy of all nodes (no links)
      also going to create a hashmap (original node -> new node) old node to new copy map
    2nd pass : link the nodes (next and random pointers) [leverage hashmap to get to map every old node to new node] hm : 3->5 so in our copy also copy3 -> copy5

# Time : O(n), Space : O(n)
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_copy = {None: None}  # for null edge cases

        # first pass : cloning LL nodes and adding to HM
        curr = head
        while curr:  # till end of list
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next
        # second pass : link pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]  # gives copy node of current
            # set ptrs (next and random)
            copy.next = old_to_copy[
                curr.next
            ]  # except 1 case : current.next = null (handled)
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        # return head of copy
        head_copy = old_to_copy[head]
        return head_copy
