# https://leetcode.com/problems/delete-node-in-a-linked-list/editorial/
# T : O(1) and S : O(1)
"""
Easy approach :
    1) Store next node in temp
    2) Copy data of next node to current node
    3) Change next pointer of ucrrent node to next pointer of next node
1->2->3->4->null
Delete : 2
temp = 3
copy 3 to curr node
1 -> 3 -> 3 -> 4 -> null
temp.next = None
1 -> 3 -> 4 -> null (actual 3 gone)

"""


class Solution:
    def deleteNode(self, node):
        # 1
        temp = node.next  # given input node is not last node
        # 2
        node.val = temp.val
        # 3
        node.next = temp.next
        temp.next = None
        del temp  # good practice
