import math

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    """Checks if there is a winner or if the game is a draw."""
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a draw
    for row in board:
        if " " in row:
            return None  # Game is still ongoing
    return "Draw"

def minimax(board, is_maximizing):
    """Minimax algorithm for optimal AI decision-making."""
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    """Finds the best move for the AI using the minimax algorithm."""
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print_board(board)

    while True:
        # Player's move
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")

        print_board(board)

        # Check for a winner after the player's move
        result = check_winner(board)
        if result:
            print(f"Game Over! {result} wins!" if result != "Draw" else "It's a draw!")
            break

        # AI's move
        print("AI is making its move...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        print_board(board)

        # Check for a winner after the AI's move
        result = check_winner(board)
        if result:
            print(f"Game Over! {result} wins!" if result != "Draw" else "It's a draw!")
            break

# Run the game
play_game()
