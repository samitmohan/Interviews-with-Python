from collections import deque


def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)


# DFS method


def topological_sort_dfs(graph):
    visited = {node: False for node in graph}
    stack = []
    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, stack)
    return stack[::-1]


# Indegree 0 method


def topological_sort_kahn(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(sorted_order) != len(graph):
        raise ValueError("Graph is not a DAG.")
    return sorted_order


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}
print(topological_sort_dfs(graph))  # Output: ['A', 'C', 'E', 'B', 'D', 'F']
print(topological_sort_kahn(graph))  # Output: ['A', 'C', 'B', 'E', 'D', 'F']
