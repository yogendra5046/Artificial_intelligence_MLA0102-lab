import random

# Function to print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # columns
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):  # diagonals
        return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function for AI move (random available cell)
def ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

# Main game function
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    ai = 'O'
    current_player = human

    print("Welcome to Tic Tac Toe!")
    print("You are 'X' and the AI is 'O'.")
    print_board(board)

    while True:
        if current_player == human:
            print("Your turn! Enter row and column (0, 1, or 2):")
            try:
                row = int(input("Row: "))
                col = int(input("Col: "))
                if board[row][col] != ' ':
                    print("Cell already taken! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue
        else:
            print("AI's turn...")
            row, col = ai_move(board)

        # Place the move
        board[row][col] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            if current_player == human:
                print("🎉 You win!")
            else:
                print("🤖 AI wins!")
            break

        # Check for draw
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch turns
        current_player = ai if current_player == human else human

# Run the game
if __name__ == "__main__":
    play_game()
