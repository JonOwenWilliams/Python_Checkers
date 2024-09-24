import random

def rules_section():
    """
    Displays the rules at the top of the screen.
    """

    print("Welcome to Python Checkers!")
    print("Rules:")
    print("1. Players alternate turns. You are 'O' and the computer is 'X'.")
    print("2. To move, input row and column (e.g., '2 3').")
    print("3. You can move diagonally forward. Jumping over the opponent is allowed.")
    print("4. The goal is to capture all the opponent's pieces or block them from moving.\n")

def board_creation():
    """
    setting up the size of the board 8x8.
    and placeing the computer peices ('X') and player peices ('O'),
    and in the empty places marking ('*').
    """
    board = [["*" for _ in range(8)] for _ in range (8)]

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


board = board_creation()
rules_section()
display_board(board)
