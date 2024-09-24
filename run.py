import random


def rules_section():
    """
    Displays the rules at the top of the screen.
    To help players understand how to play.
    """

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
    board = [["*" for _ in range(8)] for _ in range(8)]

    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 1:
                board[i][j] = 'X'

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
            move = input("Enter your move (old_row old_col new_row new_col): ")
            old_row, old_col, new_row, new_col = map(int, move.split())
            if 0 <= old_row < 8 and 0 <= old_col < 8 and
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

    if abs(new_row - old_row) == 1 and abs(new_col - old_col) == 1 and
    board[new_row][new_col] == "*":
        return True
    elif abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        if board[new_row][new_col] == "*" and
        board[jumped_row][jumped_col] == opponent:
            return True
    return False


def move_pieces(board, old_row, old_col, new_row, new_col, player):
    """
    this function will move the players pieces and computers pieces.
    and replace the old position with '*'
    """
    if abs(new_row - old_row) == 2 and abs(new_col - old_col) == 2:
        jumped_row = (old_row + new_row) // 2
        jumped_col = (old_col + new_col) // 2
        board[jumped_row][jumped_col] = '*'

    board[old_row][old_col] = '*'

    board[new_row][new_col] = player


def computer_move(board):
    """
    This function will make the computer chose a random valid diagonal space.
    """
    possible_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'X' and (i + j) % 2 == 1:
                if i + 1 < 8 and j + 1 < 8 and board[i + 1][j + 1] == "*":
                    possible_moves.append((i, j, i + 1, j + 1))
                if i + 1 < 8 and j - 1 >= 0 and board[i + 1][j - 1] == "*":
                    possible_moves.append((i, j, i + 1, j - 1))
                if i + 2 < 8 and j + 2 < 8 and board[i + 2][j + 2] == "*" and
                board[i + 1][j + 1] == 'O':
                    possible_moves.append((i, j, i + 2, j + 2))
                if i + 2 < 8 and j - 2 >= 0 and board[i + 2][j - 2] == "*" and
                board[i + 1][j - 1] == 'O':
                    possible_moves.append((i, j, i + 2, j - 2))

    if possible_moves:
        old_row, old_col, new_row, new_col = random.choice(possible_moves)
        move_pieces(board, old_row, old_col, new_row, new_col, 'X')
        print(f"Computer moves to {new_row} {new_col}.")
    else:
        print("Computer have no valid moves!")


def check_winner(board):
    """
    Checks if either the layer or computer.
    has any tokens left to determin who wins.
    """
    player_count = sum(row.count('O') for row in board)
    computer_count = sum(row.count('X') for row in board)
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
        rules_section()
        player_name = input("Enter your name: ")
        print(f"Hello, {player_name}! Welcome to Python Checkers! You are 'O'")

        board = board_creation()
        display_board(board)

        while True:
            print(f"{player_name}'s turn!")
            old_row, old_col, new_row, new_col = players_move()
            if check_move(board, old_row, old_col, new_row, new_col, 'O'):
                move_pieces(board, old_row, old_col, new_row, new_col, 'O')
            else:
                print("invalid move, try something else.")
                continue

            display_board(board)

            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break

            print("Now the computers turn!")
            computer_move(board)
            display_board(board)

            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break

        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! I hope you had fun.")
            break


main()
