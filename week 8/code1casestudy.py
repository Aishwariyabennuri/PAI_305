import numpy as np

# States and Actions
states = ['LOW', 'MEDIUM', 'HIGH']
actions = ['SHORT', 'MEDIUM', 'LONG']

# Rewards (based on traffic improvement)
rewards = {
    'LOW': 5,
    'MEDIUM': 2,
    'HIGH': -5
}

# Transition Model (simplified probabilities)
transitions = {
    'LOW': {
        'SHORT': [('LOW', 0.7), ('MEDIUM', 0.3)],
        'MEDIUM': [('LOW', 0.8), ('MEDIUM', 0.2)],
        'LONG': [('LOW', 0.9), ('MEDIUM', 0.1)]
    },
    'MEDIUM': {
        'SHORT': [('MEDIUM', 0.6), ('HIGH', 0.4)],
        'MEDIUM': [('LOW', 0.3), ('MEDIUM', 0.5), ('HIGH', 0.2)],
        'LONG': [('LOW', 0.5), ('MEDIUM', 0.4), ('HIGH', 0.1)]
    },
    'HIGH': {
        'SHORT': [('HIGH', 0.8), ('MEDIUM', 0.2)],
        'MEDIUM': [('HIGH', 0.6), ('MEDIUM', 0.4)],
        'LONG': [('MEDIUM', 0.6), ('LOW', 0.4)]
    }
}

# Value Iteration
def value_iteration(gamma=0.9, epsilon=0.01):
    V = {s: 0 for s in states}

    while True:
        delta = 0
        new_V = V.copy()

        for s in states:
            action_values = []

            for a in actions:
                value = 0
                for next_state, prob in transitions[s][a]:
                    value += prob * (rewards[next_state] + gamma * V[next_state])
                action_values.append(value)

            new_V[s] = max(action_values)
            delta = max(delta, abs(new_V[s] - V[s]))

        V = new_V

        if delta < epsilon:
            break

    return V


# Run Value Iteration
V = value_iteration()

print("Optimal State Values:")
for state in V:
    print(state, ":", round(V[state], 2))
