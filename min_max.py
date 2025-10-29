import math
import copy

# Simple constants
EMPTY = '.'
PLAYER = 'x'     # Human
AI = 'o'         # Computer
SIZE = 6         # Smaller 6x6 board for simplicity

# Create initial board
def create_board():
    board = [[EMPTY]*SIZE for _ in range(SIZE)]
    for r in range(2):
        for c in range((r+1)%2, SIZE, 2):
            board[r][c] = AI
    for r in range(SIZE-2, SIZE):
        for c in range((r+1)%2, SIZE, 2):
            board[r][c] = PLAYER
    return board

def print_board(board):
    print("\n  " + " ".join(map(str, range(SIZE))))
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()

# Generate simple legal moves (forward only)
def get_moves(board, player):
    moves = []
    direction = -1 if player == PLAYER else 1
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == player:
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and board[nr][nc] == EMPTY:
                        moves.append(((r, c), (nr, nc)))
    return moves

# Apply move
def make_move(board, move):
    (r1, c1), (r2, c2) = move
    new_board = copy.deepcopy(board)
    new_board[r2][c2] = new_board[r1][c1]
    new_board[r1][c1] = EMPTY
    return new_board

# Simple evaluation: difference in piece count
def evaluate(board):
    p1 = sum(row.count(PLAYER) for row in board)
    p2 = sum(row.count(AI) for row in board)
    return p2 - p1

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate(board), board
    player = AI if maximizing else PLAYER
    moves = get_moves(board, player)
    if not moves:
        return evaluate(board), board

    if maximizing:
        max_eval = -math.inf
        best_board = None
        for m in moves:
            eval_score, _ = minimax(make_move(board, m), depth-1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval, best_board = eval_score, make_move(board, m)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_board
    else:
        min_eval = math.inf
        best_board = None
        for m in moves:
            eval_score, _ = minimax(make_move(board, m), depth-1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval, best_board = eval_score, make_move(board, m)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_board

# Main game
def play():
    board = create_board()
    print_board(board)
    turn = PLAYER
    while True:
        if not get_moves(board, turn):
            print("No moves left!")
            break

        if turn == PLAYER:
            moves = get_moves(board, PLAYER)
            for i, m in enumerate(moves):
                print(i, m)
            choice = int(input("Your move (index): "))
            board = make_move(board, moves[choice])
        else:
            print("AI is thinking...")
            _, board = minimax(board, 2, -math.inf, math.inf, True)

        print_board(board)
        turn = AI if turn == PLAYER else PLAYER

    # Result
    if evaluate(board) > 0:
        print("AI wins!")
    elif evaluate(board) < 0:
        print("You win!")
    else:
        print("Draw!")

# Run
if __name__ == "__main__":
    play()
