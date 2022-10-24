"""
Welcome to my battleships game.
"""
from random import randint


def create_board(users_input):
    """
    creates a board depending on the users input
    """
    board = []
    for i in range(users_input):
        board.append(["~"]*users_input)
    return board


def print_board(board):
    """"prints the board with spaces between"""
    for i in users_board:
        print(" ".join(i))


def random_row(board):
    """
    generates random row for the computers ship
    """
    return randint(0, len(users_board) - 1)

def random_col(board):
    """
    generates random col for the computers ship
    """
    return randint(0, len(users_board[0]) - 1)


print("WELCOME TO BATTLE SHIPS")
print("please enter the size of your battle field")
users_board = create_board(int(input("battlefield must be between 4-8: ")))
print_board(users_board)
ship_row = random_row(users_board)
ship_col = random_col(users_board)
