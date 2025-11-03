import numpy as np
import random

# Grid dimensions
ROWS, COLS = 5, 5

# Rewards
GOAL = (4, 4)
OBSTACLES = [(1, 1), (2, 3)]
STEP_PENALTY = -1
GOAL_REWARD = 10
OBSTACLE_PENALTY = -5

# Actions: up, down, left, right
ACTIONS = ['U', 'D', 'L', 'R']
ACTION_MAP = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# Q-learning parameters
alpha = 0.1       # Learning rate
gamma = 0.9       # Discount factor
epsilon = 0.2     # Exploration rate
episodes = 500    # Number of episodes

# Initialize Q-table
Q = {}
for r in range(ROWS):
    for c in range(COLS):
        Q[(r, c)] = {a: 0 for a in ACTIONS}

# Environment: returns next_state and reward
def step(state, action):
    if state == GOAL:
        return state, GOAL_REWARD
    
    dr, dc = ACTION_MAP[action]
    nr, nc = state[0] + dr, state[1] + dc

    # Check boundaries
    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
        return state, OBSTACLE_PENALTY  # hitting wall penalty
    
    new_state = (nr, nc)

    if new_state in OBSTACLES:
        return new_state, OBSTACLE_PENALTY
    elif new_state == GOAL:
        return new_state, GOAL_REWARD
    else:
        return new_state, STEP_PENALTY

# Epsilon-greedy action selection
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(ACTIONS)
    else:
        return max(Q[state], key=Q[state].get)

# Q-learning algorithm
for ep in range(episodes):
    state = (0, 0)  # Start position
    while state != GOAL:
        action = choose_action(state)
        next_state, reward = step(state, action)
        best_next_action = max(Q[next_state], key=Q[next_state].get)
        Q[state][action] = Q[state][action] + alpha * (reward + gamma * Q[next_state][best_next_action] - Q[state][action])
        state = next_state

# Display learned Q-table
print("\n--- Learned Q-Table ---")
for r in range(ROWS):
    for c in range(COLS):
        print(f"{(r, c)}: {Q[(r, c)]}")

# Extract optimal path from start to goal
def get_optimal_path(start):
    path = [start]
    state = start
    while state != GOAL:
        action = max(Q[state], key=Q[state].get)
        dr, dc = ACTION_MAP[action]
        state = (state[0] + dr, state[1] + dc)
        if state in path:  # avoid loops
            break
        path.append(state)
    return path

optimal_path = get_optimal_path((0, 0))
print("\nOptimal Path from Start to Goal:")
print(" -> ".join(map(str, optimal_path)))
