import heapq

graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def best_first(graph, heuristic, start):
    visited = set()
    queue = [(heuristic[start], start)]

    while queue:
        h, node = heapq.heappop(queue)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for i, cost in graph[node]:
                heapq.heappush(queue, (heuristic[i], i))

best_first(graph, heuristic, 'A')

print()

import heapq

graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star(graph, heuristic, start):
    visited = set()
    queue = [(heuristic[start], 0, start)]

    while queue:
        f, g, node = heapq.heappop(queue)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for i, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + heuristic[i]
                heapq.heappush(queue, (new_f, new_g, i))

a_star(graph, heuristic, 'A')