from collections import deque

def water_jug_problem():
    # Jug capacities
    max_x = 4  # 4-gallon jug
    max_y = 3  # 3-gallon jug
    
    # Set to keep track of visited states
    visited = set()

    # Queue for BFS: each element is (x, y, path)
    queue = deque()
    queue.append((0, 0, []))  # Start from (0, 0) with empty path

    while queue:
        x, y, path = queue.popleft()

        # Skip already visited states
        if (x, y) in visited:
            continue

        # Mark state as visited
        visited.add((x, y))

        # Add current state to path
        current_path = path + [(x, y)]

        # Check goal condition
        if x == 2:
            print("Solution found:")
            for step in current_path:
                print(f"4-gallon: {step[0]}, 3-gallon: {step[1]}")
            return

        # Generate all possible next states

        next_states = [
            (max_x, y),              # Fill 4-gallon jug
            (x, max_y),              # Fill 3-gallon jug
            (0, y),                  # Empty 4-gallon jug
            (x, 0),                  # Empty 3-gallon jug

            # Pour from 4-gallon to 3-gallon
            (x - min(x, max_y - y), y + min(x, max_y - y)),

            # Pour from 3-gallon to 4-gallon
            (x + min(y, max_x - x), y - min(y, max_x - x))
        ]

        # Add new states to queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))

    print("No solution found.")

# Run the function
water_jug_problem()