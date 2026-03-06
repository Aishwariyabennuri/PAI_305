# Simple Cyber Attack-Defense Simulation
def minimax(state, depth, maximizing_player):
    # Leaf node evaluation
    if depth == 0 or state['secure'] in [True, False]:
        return state['score']

    if maximizing_player:  # Defender
        best = -float('inf')
        for move in state['defender_moves']:
            next_state = simulate(state, move, 'defender')
            val = minimax(next_state, depth-1, False)
            best = max(best, val)
        return best
    else:  # Attacker
        best = float('inf')
        for move in state['attacker_moves']:
            next_state = simulate(state, move, 'attacker')
            val = minimax(next_state, depth-1, True)
            best = min(best, val)
        return best

def simulate(state, move, player):
    # Simple simulation: modify score based on action
    next_state = state.copy()
    if player == 'defender':
        next_state['score'] += move['defense_value']
    else:
        next_state['score'] -= move['attack_value']
    # Check if system compromised or fully secured
    next_state['secure'] = next_state['score'] >= 10
    next_state['compromised'] = next_state['score'] <= -5
    return next_state

# Example game state
state = {
    'score': 0,
    'secure': False,
    'compromised': False,
    'defender_moves': [{'name':'Patch', 'defense_value':3},
                       {'name':'Firewall', 'defense_value':2}],
    'attacker_moves': [{'name':'Phish', 'attack_value':2},
                       {'name':'Exploit', 'attack_value':4}]
}

best_score = minimax(state, depth=3, maximizing_player=True)
print("Optimal defense evaluation:", best_score)
