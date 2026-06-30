from collections import deque

#BFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(graph, 'A')
print()

#DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for i in graph[node]:
            dfs(graph, i, visited)

visited = set()
dfs(graph, 'A', visited)
print()

#UCS
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

def ucs(graph, start):
    visited = set()
    queue = [(0, start)]

    while queue:
        cost, node = heapq.heappop(queue)

        if node not in visited:
            print(node, cost)
            visited.add(node)

            for i, c in graph[node]:
                heapq.heappush(queue, (cost + c, i))

ucs(graph, 'A')
print()

#IDFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(graph, node, visited, limit):
    if limit < 0:
        return

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for i in graph[node]:
            dls(graph, i, visited, limit - 1)

def idfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth", depth)
        visited = set()
        dls(graph, start, visited, depth)

idfs(graph, 'A', 2)

