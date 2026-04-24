import numpy as np

# -------------------------------
# GridWorld MDP Class
# -------------------------------
class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.state_space = [(i, j) for i in range(size) for j in range(size)]
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def get_next_state(self, state, action):
        i, j = state

        if action == 'UP':
            i -= 1
        elif action == 'DOWN':
            i += 1
        elif action == 'LEFT':
            j -= 1
        elif action == 'RIGHT':
            j += 1

        # Stay inside grid
        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))

        return (i, j)

    def get_reward(self, state):
        if state == self.goal:
            return 0
        elif state == self.trap:
            return -10
        else:
            return -1


# -------------------------------
# Value Iteration
# -------------------------------
def value_iteration(mdp, gamma=0.9, epsilon=0.01):
    V = {s: 0 for s in mdp.state_space}

    while True:
        delta = 0
        for s in mdp.state_space:

            if s == mdp.goal or s == mdp.trap:
                continue

            v = V[s]
            values = []

            for a in mdp.action_space:
                s_next = mdp.get_next_state(s, a)
                r = mdp.get_reward(s_next)
                values.append(r + gamma * V[s_next])

            V[s] = max(values)
            delta = max(delta, abs(v - V[s]))

        if delta < epsilon:
            break

    return V


# -------------------------------
# Policy Iteration
# -------------------------------
def policy_iteration(mdp, gamma=0.9):
    policy = {
        s: np.random.choice(mdp.action_space)
        for s in mdp.state_space
        if s != mdp.goal and s != mdp.trap
    }

    V = {s: 0 for s in mdp.state_space}

    while True:

        # Policy Evaluation
        while True:
            delta = 0
            for s in mdp.state_space:

                if s == mdp.goal or s == mdp.trap:
                    continue

                v = V[s]
                a = policy[s]
                s_next = mdp.get_next_state(s, a)
                r = mdp.get_reward(s_next)

                V[s] = r + gamma * V[s_next]
                delta = max(delta, abs(v - V[s]))

            if delta < 0.01:
                break

        # Policy Improvement
        stable = True
        for s in mdp.state_space:

            if s == mdp.goal or s == mdp.trap:
                continue

            old_action = policy[s]

            best_action = None
            best_value = float('-inf')

            for a in mdp.action_space:
                s_next = mdp.get_next_state(s, a)
                r = mdp.get_reward(s_next)
                value = r + gamma * V[s_next]

                if value > best_value:
                    best_value = value
                    best_action = a

            policy[s] = best_action

            if old_action != best_action:
                stable = False

        if stable:
            break

    return policy, V


# -------------------------------
# MAIN PROGRAM (IMPORTANT)
# -------------------------------

# Create MDP (THIS FIXES YOUR ERROR)
mdp = GridWorldMDP(3, (2, 2), (1, 1))

# Value Iteration
V = value_iteration(mdp)

print("Value Iteration Results:")
for state in V:
    print(state, ":", round(V[state], 2))

# Policy Iteration
policy, V = policy_iteration(mdp)

print("\nPolicy Iteration Results:")
for state in policy:
    print(state, "->", policy[state], "| Value:", round(V[state], 2))
