import heapq

def manhattan(state, goal):
    distance = 0
    goal_pos = {}
    for i in range(3):
        for j in range(3):
            goal_pos[goal[i][j]] = (i, j)
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gx, gy = goal_pos[val]
                distance += abs(i - gx) + abs(j - gy)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), 0, start))
    visited = set()
    parent = {start: None}
    g_cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + manhattan(neighbor, goal)
                heapq.heappush(pq, (f_cost, new_g, neighbor))
                parent[neighbor] = current

    return None

def take_input(name):
    print(f"Enter {name} state (use 0 for blank):")
    state = []
    for _ in range(3):
        row = tuple(map(int, input().split()))
        state.append(row)
    return tuple(state)

if __name__ == "__main__":
    start = take_input("START")
    goal = take_input("GOAL")
    solution = a_star(start, goal)

    if solution:
        print("Solution found in", len(solution)-1, "moves:")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")
