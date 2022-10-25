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
    if users_input < 4 or users_input > 8:
        raise ValueError("Please enter a number between 4 - 8")
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
    """
    Takes in the users guess and detrmines
    if they have won,missed already made that guess or ran out of turns
    """
    players_choice_of_row = choose_row()
    players_choice_of_col = choose_col()

    # if the user won they receieve a message and the game ends

    if players_choice_of_row == ship_row and players_choice_of_col == ship_col:
        print("YOU DESTROYED MY SHIP!")
        users_board[players_choice_of_row][players_choice_of_col] = "!"
        print_board(users_board)
        break
    else:
        # if the users choice was not in bounds receive a warning
        if players_choice_of_col < 0 or players_choice_of_col > len(users_board):
            print("your col was out of range")

        elif players_choice_of_row < 0 or players_choice_of_row > len(users_board):
            print("your row was out of range")

        # if the user enters a number to high or low they receive a warning
        elif users_board[players_choice_of_row][players_choice_of_col] == "?":
            print("you have already tried that!")

        else:
            # if they user have missed the ship it will print out a "?" on the users board
            print("you missed...")
            users_board[players_choice_of_row][players_choice_of_col] = "?"

    print(f"Turn: {turn + 1} out of {len(users_board)}")
    print_board(users_board)

if turn >= len(users_board):
    print("game over")
