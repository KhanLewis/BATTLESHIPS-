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
    """"prints the board with spaces between"""
    for i in users_board:
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
    takes users input for their row choice
    """
    players_choice_of_row = int(input(f"Choose a row between 1 - {len(users_board)}: ")) - 1
    return players_choice_of_row


def choose_col():
    """
    takes users input for their column choice
    """
    players_choice_of_col = int(input(f"Choose a col between 1 - {len(users_board)}: ")) - 1
    return players_choice_of_col

for turn in range(len(users_board)):
    players_choice_of_row = choose_row()
    players_choice_of_col = choose_col()

    if players_choice_of_row == ship_row and players_choice_of_col == ship_col:
        print("you destoryed my ship.. you won")
        break
    elif players_choice_of_col < 0 or players_choice_of_col > len(users_board):
        print("your col was out of range")

    elif players_choice_of_row < 0 or players_choice_of_row > len(users_board):
        print("your row was out of range")

    else:
        if players_choice_of_row != ship_row and players_choice_of_col != ship_col:
            print("you missed...")
            users_board[players_choice_of_row][players_choice_of_col] = "?"

        elif users_board[players_choice_of_row][players_choice_of_col] == "?":
            print("you have already tried that!")
            
    print(f"{turn + 1} out of {len(users_board)}")
    print_board(users_board)
