# DSU
# n = houses
# wells = list of cost of building a well in each house
# pipes : list of lists representing cost of laying pipes between houses.

"""
Thakur is the head constructor of a town. He wants to supply Electricity to n public places by building power houses and laying wires. For each public place 'i', he can either build a power house inside it directly with cost power[i], or lay wires from another place. 

The cost to lay wires between different public places are given by the array wires, where each wires[i] = [place1, place2, cost] represents the cost to connect place1 and place2 together using a wire. 

Connections are bidirectional.

Devise a strategy to supply electricity to all public places having minimum cost.

Example 1:
Input :
n = 3, power = [1,2,2], wires = [[1,2,1], [2,3,1]]
Output : 3
Explanation : The best strategy to build a powerhouse in the first public palce with cost 1 and connect the other public places to it with cost 2 so the total cost is 3.

Sample Input Explanation: 
First line is value n, the next set of lines contains value for power[n]. Next line is the number of wires w, the next set of lines contains values for wires[w]

Sample Input (Example 1) -:
3
1
2
2
1
2
1
2
3
1

Sample Output (Example 1) -:
3
"""


# Time : O(n*logn)
# Space : O(n)

def minCost(n, wells, pipes):
    # each well at i, append new pipe to pipe list
    # pipe connects house 0 -> house i + 1 : cost = w
    for i, w in enumerate(wells):
        pipes.append([0, i + 1, w])
    
    # sort pipes on 3rd element (cost of laying the pipe) : asc order of cost
    pipes.sort(key = lambda x : x[2])
    p = list(range(n + 1))

    # Union Find : keep track of connected house
    # Recursively finds parent of set to which x belongs.
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    
    # u, v houses connected by pipe and w is cost of pipe
    ans = 0
    for u, v, w in pipes:
        # if houses u, v are in same set if yes : connecting with pipe -> creates cycle, loop continues to next pipe
        if find(u) == find(v): continue
        # house not in same set (not connected) then connect them
        p[find(u)] = find(v)
        ans += w # each valid pipe added to house, cost is added to ans
        n -= 1 # num of houses decrement due to connection above
        if n == 0: break
    return ans
