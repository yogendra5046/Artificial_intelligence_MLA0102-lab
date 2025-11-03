# Map Coloring Problem using Backtracking

def is_safe(graph, colors, node, color):
    """Check if it's safe to assign the color to the node."""
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
    return True


def graph_coloring(graph, colors, node, available_colors):
    """Recursive function to color the graph."""
    # If all nodes are colored, return True
    if node == len(graph):
        return True

    current_node = list(graph.keys())[node]

    for color in available_colors:
        if is_safe(graph, colors, current_node, color):
            colors[current_node] = color
            if graph_coloring(graph, colors, node + 1, available_colors):
                return True
            colors[current_node] = None  # backtrack

    return False


def solve_map_coloring(graph, available_colors):
    """Main function to solve and display the map coloring."""
    colors = {node: None for node in graph}

    if graph_coloring(graph, colors, 0, available_colors):
        print("✅ Coloring solution found:\n")
        for region, color in colors.items():
            print(f"{region} --> {color}")
    else:
        print("❌ No valid coloring possible with given colors.")


# --- Example usage ---
if __name__ == "__main__":
    # Example graph (map) — each key is a region, values are adjacent regions
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['A', 'C', 'E'],
        'E': ['B', 'C', 'D']
    }

    # Available colors
    available_colors = ['Red', 'Green', 'Blue']

    solve_map_coloring(graph, available_colors)
