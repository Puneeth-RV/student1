from collections import deque

def bfs():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) not in visited:
            print((x, y))
            visited.add((x, y))

            if x == 2:
                break

            next_states = [
                (4, y),                 # Fill Jug1
                (x, 3),                 # Fill Jug2
                (0, y),                 # Empty Jug1
                (x, 0),                 # Empty Jug2
                (max(0, x-(3-y)), min(3, x+y)),   # Jug1 -> Jug2
                (min(4, x+y), max(0, y-(4-x)))    # Jug2 -> Jug1
            ]

            for state in next_states:
                queue.append(state)

bfs()

def dfs(x, y, visited):
    if (x, y) in visited:
        return

    print((x, y))
    visited.add((x, y))

    if x == 2:
        return

    next_states = [
        (4, y),
        (x, 3),
        (0, y),
        (x, 0),
        (max(0, x-(3-y)), min(3, x+y)),
        (min(4, x+y), max(0, y-(4-x)))
    ]

    for state in next_states:
        dfs(state[0], state[1], visited)

visited = set()
dfs(0, 0, visited)