def get_next(state, cap):
    a, b, c = state
    A, B, C = cap
    nxt = []

    # Fill
    nxt += [(A, b, c), (a, B, c), (a, b, C)]

    # Empty
    nxt += [(0, b, c), (a, 0, c), (a, b, 0)]

    # Pour function
    def pour(x, y, limit):
        t = min(x, limit - y)
        return x - t, y + t

    # Pour operations
    nxt += [(pour(a, b, B)[0], pour(a, b, B)[1], c)]
    nxt += [(pour(a, c, C)[0], b, pour(a, c, C)[1])]
    nxt += [(pour(b, a, A)[1], pour(b, a, A)[0], c)]
    nxt += [(a, pour(b, c, C)[0], pour(b, c, C)[1])]
    nxt += [(pour(c, a, A)[1], b, pour(c, a, A)[0])]
    nxt += [(a, pour(c, b, B)[1], pour(c, b, B)[0])]

    return nxt


def bfs(cap, goal):
    start = (0, 0, 0)
    queue = [(start, [start])]
    visited = set([start])

    while queue:
        state, path = queue.pop(0)
        if goal in state:
            return path

        for nxt in get_next(state, cap):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))


def dfs(cap, goal):
    start = (0, 0, 0)
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if goal in state:
            return path

        if state in visited:
            continue

        visited.add(state)

        for nxt in get_next(state, cap):
            if nxt not in visited:
                stack.append((nxt, path + [nxt]))


cap = (8, 5, 3)
goal = 4

print("BFS Path:", bfs(cap, goal))
print("DFS Path:", dfs(cap, goal))
