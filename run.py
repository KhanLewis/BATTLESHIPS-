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
        i = ["~"]
        board.append(i*users_input)
    if users_input < 4 or users_input > 8:
        raise ValueError("Please enter a")
    return board


def print_board(board):
    """"prints the board with spaces between"""
    for i in board:
        print(" ".join(i))


print("WELCOME TO BATTLE SHIPS")
print("please enter the size of your battle field")
users_board = create_board(int(input("battlefield must be between 4-8: ")))
print_board(users_board)


def random_row(users_board_input):
    """
    generates random row for the computers ship
    """
    return randint(0, len(users_board_input) - 1)


def random_col(users_board_input):
    """
    generates random col for the computers ship
    """
    return randint(0, len(users_board_input[0]) - 1)


ship_row = random_row(users_board)
ship_col = random_col(users_board)


def choose_row():
    """
    Takes users input for their row choice
    """
    choose_a_row = int(input(f"choose between 1- {len(users_board)}: ")) - 1
    return choose_a_row


def choose_col():
    """
    Takes users input for their column choice
    """
    choose_a_col = int(input(f"Choose between 1- {len(users_board)}: ")) - 1
    return choose_a_col


for turn in range(len(users_board)):

    players_choice_row = choose_row()
    players_choice_col = choose_col()

    # if the user won they receieve a message and the game ends

    if players_choice_row == ship_row and players_choice_col == ship_col:
        print("YOU DESTROYED MY SHIP!")
        users_board[players_choice_row][players_choice_col] = "!"
        print_board(users_board)
        break
    else:
        # if the users choice was not in bounds receive a warning
        if players_choice_col < 0 or players_choice_col > len(users_board):
            print("your col was out of range")

        elif players_choice_row < 0 or players_choice_row > len(users_board):
            print("your row was out of range")

        # if the user enters a number to high or low they receive a warning
        elif users_board[players_choice_row][players_choice_col] == "?":
            print("you have already tried that!")

        else:
            # if they user have missed the ship it will print out a "?"
            print("you missed...")
            users_board[players_choice_row][players_choice_col] = "?"

        print(f"Turn: {turn + 1} out of {len(users_board)}")
        print_board(users_board)
