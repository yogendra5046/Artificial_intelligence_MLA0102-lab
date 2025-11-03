from collections import deque
import heapq

# --- Graph Representation (Weighted Graph) ---
graph = {
    'A': {'B': 1, 'C': 4, 'D': 7},
    'B': {'E': 2, 'F': 5},
    'C': {'G': 3},
    'D': {'H': 2},
    'E': {'I': 3},
    'F': {'J': 1},
    'G': {'K': 2},
    'H': {'L': 3},
    'I': {},
    'J': {},
    'K': {},
    'L': {}
}

# --- Heuristic Function (straight-line estimates to goal) ---
heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 6,
    'E': 4, 'F': 3, 'G': 4, 'H': 5,
    'I': 0, 'J': 1, 'K': 2, 'L': 3
}

# --- Beam Search Implementation ---
def beam_search(graph, start, goal, beam_width):
    level = [(heuristic[start], [start], 0)]  # (heuristic, path, cost)
    visited = set()
    print(f"\n=== Beam Search (Beam Width = {beam_width}) ===")

    while level:
        new_level = []
        for _, path, cost in level:
            node = path[-1]
            if node == goal:
                print(f"Goal found! Path: {path}, Total Cost: {cost}")
                return path, cost

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_path = path + [neighbor]
                    score = heuristic[neighbor]
                    new_level.append((score, new_path, new_cost))
                    visited.add(neighbor)

        # Keep only k best nodes based on heuristic
        level = heapq.nsmallest(beam_width, new_level, key=lambda x: x[0])

        print(f"Current Beam: {[p[-1] for _, p, _ in level]} (Top {beam_width} nodes)")

    print("No path found — beam too narrow to reach goal.")
    return None, None


# --- BFS Implementation for Comparison ---
def bfs(graph, start, goal):
    print("\n=== Breadth-First Search (BFS) ===")
    queue = deque([(start, [start], 0)])
    visited = set([start])

    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            print(f"Goal found! Path: {path}, Total Cost: {cost}")
            return path, cost

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], cost + weight))

    print("Goal not reachable.")
    return None, None


# --- Run Both Searches ---
start_node = 'A'
goal_node = 'I'
beam_width = 2  # Change this to see trade-off (1 = greedy, larger = more complete)

b_path, b_cost = beam_search(graph, start_node, goal_node, beam_width)
f_path, f_cost = bfs(graph, start_node, goal_node)

# --- Comparison Summary ---
print("\n=== Comparison Summary ===")
if b_path:
    print(f"Beam Search Path: {b_path}, Cost: {b_cost}")
else:
    print("Beam Search failed to find the goal (narrow beam).")

if f_path:
    print(f"BFS Path: {f_path}, Cost: {f_cost}")

print("\nTrade-off:")
print("- Beam Search is FASTER but may MISS the optimal or any path if beam is too narrow.")
print("- BFS is COMPLETE (always finds a path if one exists) but explores more nodes.")
