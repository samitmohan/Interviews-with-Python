# https://leetcode.com/problems/keys-and-rooms/description/
# The main idea you need to understand to solve this problem that it is a graph problem. We have list of rooms - nodes and for each room you have list of keys, this is edges which go from this node. Problem is asking if you can traverse all graph, starting from node 0. As usual, there are different ways to do it

# rooms -> nodes
# keys -> edges


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room not in visited:
                visited.add(room)  # add node
                for key in rooms[room]:
                    dfs(key)

        dfs(0)  # start from 0
        return len(visited) == len(rooms)
