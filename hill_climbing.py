import random

# --- Helper Functions ---

def random_state(n):
    """Generate a random state: one queen per column."""
    return [random.randint(0, n - 1) for _ in range(n)]

def compute_cost(state):
    """Compute number of attacking pairs of queens."""
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def get_neighbors(state):
    """Generate all possible neighbors by moving one queen in its column."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(n, max_restarts=5):
    """Hill Climbing with optional random restarts."""
    best_state = None
    best_cost = float('inf')
    
    for restart in range(max_restarts):
        current = random_state(n)
        current_cost = compute_cost(current)
        
        while True:
            neighbors = get_neighbors(current)
            neighbor_costs = [compute_cost(neighbor) for neighbor in neighbors]
            min_cost = min(neighbor_costs)
            best_neighbor = neighbors[neighbor_costs.index(min_cost)]
            
            # If no improvement, stop (local optimum)
            if min_cost >= current_cost:
                break
            
            current, current_cost = best_neighbor, min_cost
        
        # Keep track of the best solution found so far
        if current_cost < best_cost:
            best_state, best_cost = current, current_cost
        
        # Stop early if we find a perfect solution
        if best_cost == 0:
            break
    
    return best_state, best_cost

def print_board(state):
    """Display the board."""
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

# --- Main Program ---
if __name__ == "__main__":
    N = int(input("Enter the number of queens (N): "))
    final_state, final_cost = hill_climbing(N, max_restarts=10)

    print("\nFinal Board:")
    print_board(final_state)
    print("Final Cost:", final_cost)
    if final_cost == 0:
        print("✅ Valid solution found!")
    else:
        print("❌ Local optimum reached (no perfect solution).")
