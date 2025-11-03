import itertools

def travelling_salesman(distance_matrix, start=0):
    """Find the shortest possible route that visits each city exactly once and returns to the start."""
    n = len(distance_matrix)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    # Generate all possible permutations of cities (except the start)
    for perm in itertools.permutations(cities[1:]):
        path = [start] + list(perm) + [start]  # complete cycle
        cost = 0

        # Calculate total cost of this route
        for i in range(len(path) - 1):
            cost += distance_matrix[path[i]][path[i + 1]]

        # Update if we find a better (shorter) path
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost


# --- Example Usage ---
if __name__ == "__main__":
    # Distance matrix representing distances between 4 cities (A, B, C, D)
    # distance[i][j] = distance from city i to city j
    distance_matrix = [
        [0, 10, 15, 20],   # A to others
        [10, 0, 35, 25],   # B to others
        [15, 35, 0, 30],   # C to others
        [20, 25, 30, 0]    # D to others
    ]

    cities = ['A', 'B', 'C', 'D']
    best_path, best_cost = travelling_salesman(distance_matrix, start=0)

    # Print results
    print("Cities:", cities)
    print("\nShortest Path (indices):", best_path)
    print("Shortest Path (cities):", " → ".join(cities[i] for i in best_path))
    print("Total Minimum Cost:", best_cost)
