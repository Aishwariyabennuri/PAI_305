import numpy as np

# States: (Load, Battery)
states = [
    ('EMPTY', 'HIGH'),
    ('EMPTY', 'LOW'),
    ('LOADED', 'HIGH'),
    ('LOADED', 'LOW')
]

actions = ['PICK', 'MOVE', 'CHARGE']

# Reward Function
def get_reward(state, action):
    load, battery = state

    if action == 'PICK' and load == 'EMPTY':
        return 10
    elif action == 'MOVE':
        return 2
    elif action == 'CHARGE':
        return 1
    elif battery == 'LOW':
        return -5
    else:
        return 0


# Transition Function (deterministic for simplicity)
def get_next_state(state, action):
    load, battery = state

    if action == 'PICK' and load == 'EMPTY':
        load = 'LOADED'
        battery = 'LOW'
    elif action == 'MOVE':
        battery = 'LOW'
    elif action == 'CHARGE':
        battery = 'HIGH'

    return (load, battery)


# Policy Iteration
def policy_iteration(gamma=0.9):
    policy = {s: np.random.choice(actions) for s in states}
    V = {s: 0 for s in states}

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for s in states:
                v = V[s]
                a = policy[s]
                s_next = get_next_state(s, a)
                r = get_reward(s, a)

                V[s] = r + gamma * V[s_next]
                delta = max(delta, abs(v - V[s]))

            if delta < 0.01:
                break

        # Policy Improvement
        stable = True
        for s in states:
            old_action = policy[s]

            best_action = None
            best_value = float('-inf')

            for a in actions:
                s_next = get_next_state(s, a)
                r = get_reward(s, a)
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


# Run Program
policy, V = policy_iteration()

print("Optimal Policy:")
for state in policy:
    print(state, "->", policy[state], "| Value:", round(V[state], 2))
