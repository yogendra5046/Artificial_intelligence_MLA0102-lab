# --- Sudoku Solver using Backtracking and Constraint Checking ---

# Check if placing num at (row, col) is valid
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


# Find the next empty cell (returns row, col) or None if full
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


# Solve Sudoku using backtracking search with constraint checking
def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Try
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Undo (backtrack)

    return False  # Trigger backtracking


# Display the Sudoku grid neatly
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()


# --- Example Sudoku Puzzle (0 = empty cell) ---
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("=== Sudoku Puzzle ===")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("✅ Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("❌ No solution exists.")
