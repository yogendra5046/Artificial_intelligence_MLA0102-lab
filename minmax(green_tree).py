def minimax(depth, node_index, is_maximizing, scores, height):
    """Recursive Minimax function."""
    # Base case: if we reach a leaf node
    if depth == height:
        return scores[node_index]
    
    # If it's the maximizer's move
    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    # If it's the minimizer's move
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )


# --- Example usage ---
if __name__ == "__main__":
    # Final scores at leaves (L1, L2, L3, L4)
    scores = [3, 5, 2, 9]

    # Height of tree = log2(4) = 2
    height = 2

    print("Leaf Node Scores:", scores)
    optimal_value = minimax(0, 0, True, scores, height)
    print("Optimal value for Maximizing Player:", optimal_value)
