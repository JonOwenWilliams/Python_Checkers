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
    print("4. Jumping over the opponent will allow you to take their pieces")
    print("5. The goal is to capture all the opponent's pieces.\n")


def board_creation():
    """
    Setting up the size of the board 8x8.
    and placing the computer pieces ('X') and player pieces ('O'),
    and marking the empty places with ('*').
    """
    # Displays the board to the player filled with "*".
    board = [["*" for _ in range(8)] for _ in range(8)]
    # Places "X" for the computer's pieces.
    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'X'
    # Places "O" for the players pieces.
    for i in range(5, 8):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'O'

    return board


def display_board(board):
    """
    Displays the game board and adds numbers on board,
     to help you understand what row and columns you are choosing.
    """
    # Numbering the rows and columns.
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, " ".join(row))


def players_move():
    """
    Prompt the player to enter their move as row and column numbers.
    returns the now and column input back to the player,
     so they know what they choose to do.
    """

    while True:
        try:
            # Prompts the players to move in the specific format.
            move = input("Enter your move (old_row old_col new_row new_col): ")
            old_row, old_col, new_row, new_col = map(int, move.split())
            # Ensures the player has entered valid numbers.
            if 0 <= old_row < 8 and 0 <= old_col < 8 and\
            0 <= new_row < 8 and 0 <= new_col < 8:
                return old_row, old_col, new_row, new_col
            else:
                print("Invalid move. Enter valid column and row numbers")
        except ValueError:
            print("Invalid input. Enter four numbers separated by spaces.")


def check_move(board, old_row, old_col, new_row, new_col, player):
    """
    Checks if the number the player entered is valid.
    checks if space is free or if it lands or computer's token.
    """
    opponent = 'X' if player == 'O' else 'O'
    opponent_king = '#' if player == 'O' else '@'
    is_king = board[old_row][old_col] in ('@', '#')

    # If the piece is not a king, it should only move forward.
    if not is_king:
        if player == 'O' and new_row >= old_row:
            return False
        if player == 'X' and new_row <= old_row:
            return False
    # Checks for basic diagonal moves as well as jumping over pieces.
    if abs(new_row - old_row) == 1 and abs(new_col - old_col) == 1 and\
    board[new_row][new_col] == "*":
        return True
    elif abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        if board[new_row][new_col] == "*" and\
        board[jumped_row][jumped_col] in (opponent, opponent_king):
            return True
    return False


def move_pieces(board, old_row, old_col, new_row, new_col, player):
    """
    This function will move the players pieces and computer's pieces.
    and replace the old position with '*'
    """
    is_king = board[old_row][old_col] in ('@', '#')
    # Removed computer's or player's tokens when jumped over.
    if abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        board[jumped_row][jumped_col] = '*'
    # Removes old piece and updates new piece.
    board[old_row][old_col] = '*'
    # upgrades the pieces if they reach the opposite end of the board.
    if player == 'O' and new_row == 0:
        board[new_row][new_col] = '@'  # Upgrade player's piece to '@'.
    elif player == 'X' and new_row == 7:
        board[new_row][new_col] = '#'  # Upgrade computer's piece to '#'.
    else:
        if is_king:
            board[new_row][new_col] = '@' if player == 'O' else '#'
        else:
            board[new_row][new_col] = player


def computer_move(board):
    """
    This function will make the computer chose a random valid diagonal space.
    """
    possible_moves = []
    # Finds all possible moves for the computer.
    for i in range(8):
        for j in range(8):
            if board[i][j] in ('X', '#') and (i + j) % 2 == 1:
                if i + 1 < 8 and j + 1 < 8 and board[i + 1][j + 1] == "*":
                    possible_moves.append((i, j, i + 1, j + 1))
                if i + 1 < 8 and j - 1 >= 0 and board[i + 1][j - 1] == "*":
                    possible_moves.append((i, j, i + 1, j - 1))
                if i + 2 < 8 and j + 2 < 8 and board[i + 2][j + 2] == "*" and\
                board[i + 1][j + 1] == 'O':
                    possible_moves.append((i, j, i + 2, j + 2))
                if i + 2 < 8 and j - 2 >= 0 and board[i + 2][j - 2] == "*" and\
                board[i + 1][j - 1] == 'O':
                    possible_moves.append((i, j, i + 2, j - 2))
                # this allows the computer to move backwards after upgrading
                if board[i][j] == '#':
                    if i - 1 >= 0 and j + 1 < 8 and\
                    board[i - 1][j + 1] == "*":
                        possible_moves.append((i, j, i - 1, j + 1))
                    if i - 1 >= 0 and j - 1 >= 0 and\
                    board[i - 1][j - 1] == "*":
                        possible_moves.append((i, j, i - 1, j - 1))
                    if i - 2 >= 0 and j + 2 < 8 and\
                    board[i - 2][j + 2] == "*" and board[i - 1][j + 1] == "O":
                        possible_moves.append((i, j, i - 2, j + 2))
                    if i - 2 >= 0 and j - 2 >= 0 and\
                    board[i - 2][j + 2] == "*" and board[i - 1][j - 1] == "O":
                        possible_moves.append((i, j, i - 2, j - 2))
    # Randomly picks any valid move possible.
    if possible_moves:
        old_row, old_col, new_row, new_col = random.choice(possible_moves)
        move_pieces(board, old_row, old_col, new_row, new_col, 'X')
        print(f"Computer moves to {new_row} {new_col}.")
    else:
        # No more possible moves.
        print("Computer has no valid moves!")


def possible_moves_left(board, player):
    """
    Checks the board for any possible moves left by either computer or player.
    """
    for i in range(8):
        for j in range(8):
            if board[i][j] == player or (player == 'O' and board[i][j] == '@')\
            or (player == 'X' and board[i][j] == '#'):
                if i > 0 and j > 0 and board[i-1][j-1] == "*":
                    return True
                if i > 0 and j < 7 and board[i-1][j+1] == "*":
                    return True
                if i < 7 and j > 0 and board[i+1][j-1] == "*":
                    return True
                if i < 7 and j < 7 and board[i+1][j+1] == "*":
                    return True
    return False


def check_draw(board):
    """
    Checks to see if both the player and computer have no more moves left
    """
    if not possible_moves_left(board, 'O') and\
    not possible_moves_left(board, 'X'):
        return True
    return False


def check_winner(board):
    """
    Checks if either the player or computer,
    has any tokens left to determine who wins.
    """
    # if either one wins from no more moves left
    if not possible_moves_left(board, 'O'):
        return "Computer"
    if not possible_moves_left(board, 'X'):
        return "Player"

    # Checks for winners
    player_count = sum(row.count('O') + row.count('@') for row in board)
    computer_count = sum(row.count('X') + row.count('#') for row in board)
    # Displays who wins.
    if player_count == 0:
        return "Computer"
    elif computer_count == 0:
        return "Player"
    return None


def main():
    """
    Loop the main game to start and run "Python Checkers!" and
    handles the game alternating between the player and the computer's turns
    """
    while True:
        # Displays the rules and prompts player for their name.
        rules_section()
        player_name = input("Enter your name: ")
        print(f"Hello, {player_name}! Welcome to Python Checkers! You are 'O'")
        # Makes the board visible.
        board = board_creation()
        display_board(board)
        # Players turn.
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
            if check_draw(board):
                print("Its a draw! No more valid moves.")
                break
            # Computer's turn
            print("Now the computer's turn!")
            computer_move(board)
            display_board(board)
            # Checks for winner after computer's turn.
            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
            if check_draw(board):
                print("Its a draw! No more valid moves.")
                break
        # Asks the player if they want to play again.
        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! I hope you had fun.")
            break


main()
