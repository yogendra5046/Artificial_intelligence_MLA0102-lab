import random

# Define constants for node types
MAX, MIN, CHANCE = "MAX", "MIN", "CHANCE"

# --- Define Game Tree Structure ---
class Node:
    def __init__(self, node_type, children=None, value=None, probabilities=None, name=""):
        self.node_type = node_type
        self.children = children if children else []
        self.value = value
        self.probabilities = probabilities  # Only for chance nodes
        self.name = name  # For display purposes


# --- Expectiminimax Algorithm ---
def expectiminimax(node):
    # Base case: leaf node
    if node.value is not None:
        return node.value

    if node.node_type == MAX:
        # Maximizing player's turn
        best = float("-inf")
        for child in node.children:
            val = expectiminimax(child)
            best = max(best, val)
        return best

    elif node.node_type == MIN:
        # Minimizing player's turn
        best = float("inf")
        for child in node.children:
            val = expectiminimax(child)
            best = min(best, val)
        return best

    elif node.node_type == CHANCE:
        # Chance node: expected value weighted by probabilities
        expected_value = 0
        for child, prob in zip(node.children, node.probabilities):
            val = expectiminimax(child)
            expected_value += prob * val
        return expected_value


# --- Build Example Game Tree ---

# Leaf utilities (end of game)
leaf_A1 = Node(None, value=3, name="A1")
leaf_A2 = Node(None, value=12, name="A2")
leaf_B1 = Node(None, value=8, name="B1")
leaf_B2 = Node(None, value=2, name="B2")
leaf_C1 = Node(None, value=4, name="C1")
leaf_C2 = Node(None, value=6, name="C2")

# Chance nodes (random events)
chance_A = Node(CHANCE, children=[leaf_A1, leaf_A2], probabilities=[0.4, 0.6], name="Chance_A")
chance_B = Node(CHANCE, children=[leaf_B1, leaf_B2], probabilities=[0.7, 0.3], name="Chance_B")
chance_C = Node(CHANCE, children=[leaf_C1, leaf_C2], probabilities=[0.5, 0.5], name="Chance_C")

# Min node (opponent)
min_node = Node(MIN, children=[chance_A, chance_B], name="Min_Node")

# Root Max node (AI's decision)
root = Node(MAX, children=[min_node, chance_C], name="Root_MAX")

# --- Run Expectiminimax ---
best_value = expectiminimax(root)

print("=== Expectiminimax Algorithm ===")
print(f"Expected utility at root (best for AI): {best_value:.2f}")

# --- Explain Decision ---
val_move1 = expectiminimax(min_node)
val_move2 = expectiminimax(chance_C)

print("\nPossible Moves for AI (Root Node):")
print(f"1️⃣  Move to Min_Node → Expected Utility = {val_move1:.2f}")
print(f"2️⃣  Move to Chance_C → Expected Utility = {val_move2:.2f}")

if val_move1 > val_move2:
    print("\n✅ Optimal Move: Choose Min_Node (Expected Utility higher)")
else:
    print("\n✅ Optimal Move: Choose Chance_C (Expected Utility higher)")

print("\n🎲 Note: Randomness in Chance Nodes affects the overall expected value!")
