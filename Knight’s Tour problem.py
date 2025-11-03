# Knight's Tour Problem using Backtracking

N = 8  # Board size (you can change this to 5, 6, etc.)

# All possible moves for a knight
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

def is_safe(x, y, board):
    """Check if (x, y) is a valid move for the knight."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_solution(board):
    """Print the chessboard solution path."""
    for row in board:
        for val in row:
            print(f"{val:2}", end=" ")
        print()
    print()

def solve_knight_tour():
    """Main solver function for the Knight's Tour."""
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Starting position
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0  # First move

    if not solve_kt_util(start_x, start_y, 1, board):
        print("❌ No solution exists for this board size.")
    else:
        print("✅ Knight’s Tour Path Found:\n")
        print_solution(board)

def solve_kt_util(x, y, movei, board):
    """Recursive utility function to solve the Knight’s Tour."""
    if movei == N * N:
        return True  # all squares visited

    # Try all possible knight moves
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solve_kt_util(next_x, next_y, movei + 1, board):
                return True
            # Backtrack
            board[next_x][next_y] = -1

    return False


# --- Run the Knight's Tour ---
if __name__ == "__main__":
    solve_knight_tour()
