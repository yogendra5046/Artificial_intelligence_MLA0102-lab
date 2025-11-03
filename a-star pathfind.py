import heapq

# --- Define the Graph ---
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'F': 1, 'E': 1},
    'E': {'F': 2},
    'F': {}
}

# --- Heuristic Function (Estimated cost to reach Goal) ---
# For simplicity, we define heuristic values manually
# (in a real problem, this could be Manhattan or Euclidean distance)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 0
}

def a_star_search(graph, start, goal, heuristic):
    """Perform A* search and print the optimal path and total cost."""
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()
    expansion_order = []

    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node in visited:
            continue

        visited.add(node)
        expansion_order.append(node)

        # Goal check
        if node == goal:
            print("Order of Node Expansion:", " → ".join(expansion_order))
            print("Optimal Path:", " → ".join(path))
            print("Total Cost:", g)
            return

        # Explore neighbors
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    print("No path found!")

# --- Run the A* Algorithm ---
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'
    print("A* Search from", start_node, "to", goal_node)
    print("-" * 40)
    a_star_search(graph, start_node, goal_node, heuristic)
