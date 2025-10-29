import math

# Activation functions
def sigmoid(x): return 1 / (1 + math.exp(-x))
def relu(x): return max(0, x)

# Dot product
def dot(a, b): return sum(x*y for x, y in zip(a, b))

# XOR dataset
data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# Weights and biases (initialized manually for XOR)
# 2 input neurons -> 2 hidden neurons -> 1 output neuron

# Hidden layer (2 neurons)
w1 = [[5, 5], [-5, -5]]  # weights for each hidden neuron
b1 = [-2.5, 7.5]

# Output layer (1 neuron)
w2 = [7, 7]  # weights from hidden layer
b2 = -6

# Forward propagation
def forward(x):
    # Hidden layer
    h = []
    for i in range(2):
        z = dot(w1[i], x) + b1[i]
        h.append(relu(z))  # ReLU activation

    # Output layer
    out = sigmoid(dot(w2, h) + b2)  # Sigmoid activation
    return out

# Test on XOR dataset
for x, y in data:
    output = forward(x)
    print(f"Input: {x}, Predicted: {round(output, 3)}, Expected: {y}")