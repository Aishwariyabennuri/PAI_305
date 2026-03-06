import heapq

# State: (jug_a, jug_b)
class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost  # g(n) = path cost

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(state, goal):
    # Simple heuristic: min distance to goal in either jug
    a, b = state
    return min(abs(a - goal), abs(b - goal))

def get_successors(state, cap_a, cap_b):
    a, b = state
    successors = []

    # Fill Jug A
    successors.append((cap_a, b))
    # Fill Jug B
    successors.append((a, cap_b))
    # Empty Jug A
    successors.append((0, b))
    # Empty Jug B
    successors.append((a, 0))
    # Pour A -> B
    pour = min(a, cap_b - b)
    successors.append((a - pour, b + pour))
    # Pour B -> A
    pour = min(b, cap_a - a)
    successors.append((a + pour, b - pour))

    return successors

def a_star(cap_a, cap_b, goal):
    start = (0, 0)
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), Node(start)))
    explored = set()

    while frontier:
        _, current_node = heapq.heappop(frontier)
        state = current_node.state

        if state in explored:
            continue
        explored.add(state)

        # Goal check
        if state[0] == goal or state[1] == goal:
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        # Expand successors
        for succ in get_successors(state, cap_a, cap_b):
            if succ not in explored:
                cost = current_node.cost + 1
                heapq.heappush(frontier, (cost + heuristic(succ, goal), Node(succ, current_node, cost)))

    return None

# Example usage
cap_a = 4
cap_b = 3
goal = 2
solution = a_star(cap_a, cap_b, goal)
if solution:
    print("Steps to reach goal:")
    for s in solution:
        print(s)
else:
    print("No solution found")
