# Hidden states (user engagement levels)
states = ['Interested', 'Neutral', 'Disengaged']

# Observations (user behavior logs)
observations = ['click_high', 'time_long', 'click_low']

# Initial probabilities
start_prob = {
    'Interested': 0.7,
    'Neutral': 0.2,
    'Disengaged': 0.1
}

# Transition probabilities (state → state)
transition_prob = {
    'Interested': {'Interested': 0.6, 'Neutral': 0.3, 'Disengaged': 0.1},
    'Neutral': {'Interested': 0.3, 'Neutral': 0.5, 'Disengaged': 0.2},
    'Disengaged': {'Interested': 0.1, 'Neutral': 0.3, 'Disengaged': 0.6}
}

# Emission probabilities (state → observations)
emission_prob = {
    'Interested': {'click_high': 0.5, 'time_long': 0.4, 'click_low': 0.1},
    'Neutral': {'click_high': 0.3, 'time_long': 0.4, 'click_low': 0.3},
    'Disengaged': {'click_high': 0.1, 'time_long': 0.3, 'click_low': 0.6}
}

# Observation sequence from user
obs_sequence = ['click_high', 'time_long', 'click_low']
def forward_algorithm(states, observations, start_prob, transition_prob, emission_prob):

    forward = []

    # Step 1: Initialization
    f0 = {}
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][observations[0]]
    forward.append(f0)

    # Step 2: Recursion
    for t in range(1, len(observations)):
        ft = {}
        for current_state in states:
            prob = 0
            for previous_state in states:
                prob += forward[t-1][previous_state] * transition_prob[previous_state][current_state]

            ft[current_state] = prob * emission_prob[current_state][observations[t]]

        forward.append(ft)

    # Step 3: Termination
    total_probability = sum(forward[-1][state] for state in states)

    return forward, total_probability


# Run model
forward_table, result = forward_algorithm(
    states, obs_sequence, start_prob, transition_prob, emission_prob
)

print("Forward Table:")
for t, step in enumerate(forward_table):
    print(f"t={t}:", step)

print("\nProbability of observation sequence:", result)
