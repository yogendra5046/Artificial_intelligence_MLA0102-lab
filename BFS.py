from collections import deque

def bfs(graph, start):
    visited = set()           # To keep track of visited nodes
    queue = deque([start])    # Queue for BFS

    print("BFS Traversal Order:")

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting BFS from node 'A'
bfs(graph, 'A')
