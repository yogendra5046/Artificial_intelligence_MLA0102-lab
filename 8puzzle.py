
puzzle = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
def print_puzzle():
    for row in puzzle:
        for val in row:
            print(val if val != 0 else ' ', end=' ')
        print()
    print()

# Find the position of 0 (empty tile)
def find_empty():
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def move(direction):
    i, j = find_empty()
    if direction == 'up' and i < 2:
        puzzle[i][j], puzzle[i + 1][j] = puzzle[i + 1][j], puzzle[i][j]
    elif direction == 'down' and i > 0:
        puzzle[i][j], puzzle[i - 1][j] = puzzle[i - 1][j], puzzle[i][j]
    elif direction == 'left' and j < 2:
        puzzle[i][j], puzzle[i][j + 1] = puzzle[i][j + 1], puzzle[i][j]
    elif direction == 'right' and j > 0:
        puzzle[i][j], puzzle[i][j - 1] = puzzle[i][j - 1], puzzle[i][j]
    else:
        print("Can't move in that direction!")

# Check if solved
def is_solved():
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    return puzzle == goal

# Main loop
print("Welcome to 8-Puzzle! Move the empty space using: up / down / left / right")
print_puzzle()

while True:
    move_input = input("Move (up/down/left/right or quit): ").lower()
    if move_input == "quit":
        print("Game ended.")
        break
    move(move_input)
    print_puzzle()

    if is_solved():
        print("🎉 Congratulations! You solved the puzzle!")
        break
