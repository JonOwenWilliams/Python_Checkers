import random


def rules_section():
    """
    Displays the rules at the top of the screen.
    To help players understand how to play.
    """

    # Displays rules to player to read

    print("Welcome to Python Checkers!")
    print("Rules:")
    print("1. Players alternate turns. You are 'O' and the computer is 'X'.")
    print("2. To move, input row and column (e.g., '2 3').")
    print("3. You can move diagonally forward.")
    print("4. Jumping over opponent will allow you to take they pieces")
    print("4. The goal is to capture all the opponent's pieces.\n")


def board_creation():
    """
    setting up the size of the board 8x8.
    and placeing the computer peices ('X') and player peices ('O'),
    and in the empty places marking ('*').
    """
    # Displays the board to the player filled with "*".
    board = [["*" for _ in range(8)] for _ in range(8)]
    # Places "X" for the computers pieces.
    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'X'
    # Places "O" for the playes pieces.
    for i in range(5, 8):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'O'

    return board


def display_board(board):
    """
    Displays the game board and adds numbers on board,
     to help you understand what row and collumns you are choosing.
    """
    # Numbering the rows and columns.
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, " ".join(row))


def players_move():
    """
    prompt the player to enter their move as row and column numbers.
    returns the now and column input back to the player,
     so they know what they choose to do.
    """

    while True:
        try:
            # Prompts the playes to move in the specific format.
            move = input("Enter your move (old_row old_col new_row new_col): ")
            old_row, old_col, new_row, new_col = map(int, move.split())
            # Ensures the player has entered valid numbers.
            if 0 <= old_row < 8 and 0 <= old_col < 8 and \
            0 <= new_row < 8 and 0 <= new_col < 8:
                return old_row, old_col, new_row, new_col
            else:
                print("Invalid move. Enter valid column and row numbers")
        except ValueError:
            print("Invalid input. Enter four numbers separated by spaces.")


def check_move(board, old_row, old_col, new_row, new_col, player):
    """
    Checks if the number the player entered is valid.
    checks if stace is free or if it lands or computers token.
    """
    opponent = 'X' if player == 'O' else 'O'
    # Ensures players are moving in the correct direction.
    if player == 'O' and new_row >= old_row:
        return False
    elif player == 'X' and new_row <= old_row:
        return False
    # Checks for basic diagonal moves aswel as jumping over pieces.
    if abs(new_row - old_row) == 1 and abs(new_col - old_col) == 1 and \
    board[new_row][new_col] == "*":
        return True
    elif abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        if board[new_row][new_col] == "*" and \
        board[jumped_row][jumped_col] == opponent:
            return True
    return False


def move_pieces(board, old_row, old_col, new_row, new_col, player):
    """
    this function will move the players pieces and computers pieces.
    and replace the old position with '*'
    """
    # Removed computer or playes tokens when jumped over.
    if abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        board[jumped_row][jumped_col] = '*'
    # Removes old peice and updates new piece.
    board[old_row][old_col] = '*'

    board[new_row][new_col] = player


def computer_move(board):
    """
    This function will make the computer chose a random valid diagonal space.
    """
    possible_moves = []
    # Finds all possible moves for the computer.
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'X' and (i + j) % 2 == 1:
                if i + 1 < 8 and j + 1 < 8 and board[i + 1][j + 1] == "*":
                    possible_moves.append((i, j, i + 1, j + 1))
                if i + 1 < 8 and j - 1 >= 0 and board[i + 1][j - 1] == "*":
                    possible_moves.append((i, j, i + 1, j - 1))
                if i + 2 < 8 and j + 2 < 8 and board[i + 2][j + 2] == "*" and \
                board[i + 1][j + 1] == 'O':
                    possible_moves.append((i, j, i + 2, j + 2))
                if i + 2 < 8 and j - 2 >= 0 and board[i + 2][j - 2] == "*" and \
                board[i + 1][j - 1] == 'O':
                    possible_moves.append((i, j, i + 2, j - 2))
    # Randomly picks any valid move possible.
    if possible_moves:
        old_row, old_col, new_row, new_col = random.choice(possible_moves)
        move_pieces(board, old_row, old_col, new_row, new_col, 'X')
        print(f"Computer moves to {new_row} {new_col}.")
    else:
        # No more possible moves.
        print("Computer have no valid moves!")


def check_winner(board):
    """
    Checks if either the layer or computer.
    has any tokens left to determin who wins.
    """
    # Checks for winners
    player_count = sum(row.count('O') for row in board)
    computer_count = sum(row.count('X') for row in board)
    # Displays who wins.
    if player_count == 0:
        return "Computer"
    elif computer_count == 0:
        return "Player"
    return None


def main():
    """
    loop the main gme to start and run "Python Checkers!"
    and handles the gae alternating between the player and the computers turns
    """
    while True:
        # Displays the rules and prompts player for their name.
        rules_section()
        player_name = input("Enter your name: ")
        print(f"Hello, {player_name}! Welcome to Python Checkers! You are 'O'")
        # Makes the board visible.
        board = board_creation()
        display_board(board)
        # Playes turn.
        while True:
            print(f"{player_name}'s turn!")
            old_row, old_col, new_row, new_col = players_move()
            if check_move(board, old_row, old_col, new_row, new_col, 'O'):
                move_pieces(board, old_row, old_col, new_row, new_col, 'O')
            else:
                print("invalid move, try something else.")
                continue
            # Updates Board
            display_board(board)
            # Checks for winner
            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
            # Computer's turn
            print("Now the computers turn!")
            computer_move(board)
            display_board(board)
            # Checks for winner after computer's turn.
            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
        # Asks the player if they want to play again.
        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! I hope you had fun.")
            break


main()
