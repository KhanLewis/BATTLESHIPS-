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


def print_board(users_board):
    for i in users_board:
        print(" ".join(i))


users_board = create_board(int(input("battlefield must be between 4-8: ")))

print_board(users_board)
