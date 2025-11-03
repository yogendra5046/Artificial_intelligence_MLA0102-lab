import heapq

# --- Graph Representation (Adjacency List with Weights) ---
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1, 'E': 3},
    'D': {'E': 2, 'F': 1},
    'E': {'F': 2},
    'F': {}
}

# --- Uniform-Cost Search Implementation ---
def uniform_cost_search(graph, start, goal):
    """Perform UCS from start to goal on a weighted graph."""
    priority_queue = []  # (cost, path)
    heapq.heappush(priority_queue, (0, [start]))
    visited = {}

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        # Skip if we already found a cheaper path to this node
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost

        # Goal reached
        if node == goal:
            return path, cost

        # Explore neighbors
        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            heapq.heappush(priority_queue, (new_cost, new_path))

    return None, float('inf')

# --- Dijkstra’s Algorithm for Validation ---
def dijkstra(graph, start, goal):
    """Find shortest path using Dijkstra’s algorithm."""
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        if node == goal:
            break
        for neighbor, weight in graph[node].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = prev[n]
    path.reverse()
    return path, dist[goal]

# --- Main Program ---
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'

    print("Uniform-Cost Search (UCS):")
    ucs_path, ucs_cost = uniform_cost_search(graph, start_node, goal_node)
    print("Path:", " → ".join(ucs_path))
    print("Total Cost:", ucs_cost)

    print("\nDijkstra’s Algorithm (for validation):")
    dij_path, dij_cost = dijkstra(graph, start_node, goal_node)
    print("Path:", " → ".join(dij_path))
    print("Total Cost:", dij_cost)

    print("\n✅ Validation:",
          "UCS is optimal!" if ucs_cost == dij_cost else "❌ UCS is not optimal!")
