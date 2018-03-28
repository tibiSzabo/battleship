import os
import random
from battleship_artwork import *
from battleship_boards import *


def main():
    os.system('clear')
    artwork()
    asd = ""
    while asd.lower() != "c":
        asd = input("\n\n\n\n\nEnter 'c' to continue: ")


def print_board(board):
    os.system('clear')
    n = 0
    print("\n")
    for i in board:
        print(board[n])
        n += 1


def set_ship_1(board, random=False):
    whos_turn(board)
    if random is False:
        value = input("Set your first ship: ")
    if random is True:
        value = generate_random_coords()
    if len(value) == 3 and value[1] == "-":
        try:
            board[int(value[0])-1][int(value[2])-1] = "-H-"
        except (IndexError, ValueError):
            print_board(board)
            whos_turn(board)
            set_ship_1(board)
    else:
        print_board(board)
        whos_turn(board)
        set_ship_1(board)
    if random is False:
        print_board(board)


def set_ship_2(board, random=False):
    if random is False:
        orientation = input("\nSet the orientation of your second ship, (h)orizontal or (v)ertical: ")
    if random is True:
        orientation = generate_random_orientation()
    if orientation == "h":
        if random is False:
            value = input("\nSet the starter position of your second ship: ")
        if random is True:
            value = generate_random_coords()
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])-1][int(value[2])] != "-H-":
                    board[int(value[0])-1][int(value[2])] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                else:
                    if random is False:
                        print_board(board)
                        set_ship_2(board)
                    if random is True:
                        set_ship_2(board, True)
            except (IndexError, ValueError):
                if random is False:
                        print_board(board)
                        set_ship_2(board)
                if random is True:
                    set_ship_2(board, True)
        else:
            print_board(board)
            set_ship_2(board)
    elif orientation == "v":
        if random is False:
            value = input("\nSet the starter position of your second ship: ")
        if random is True:
            value = generate_random_coords()
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])][int(value[2])-1] != "-H-":
                    board[int(value[0])][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                else:
                    if random is False:
                        print_board(board)
                        set_ship_2(board)
                    if random is True:
                        set_ship_2(board, True)
            except (IndexError, ValueError):
                if random is False:
                        print_board(board)
                        set_ship_2(board)
                if random is True:
                    set_ship_2(board, True)
        else:
            print_board(board)
            set_ship_2(board)
    else:
        print_board(board)
        set_ship_2(board)
    if random is False:
        print_board(board)


def set_ship_3(board, random=False):
    if random is False:
        orientation = input("\nSet the orientation of your third ship, (h)orizontal or (v)ertical: ")
    if random is True:
        orientation = generate_random_orientation()
    if orientation == "h":
        if random is False:
            value = input("\nSet the starter position of your third ship: ")
        if random is True:
            value = generate_random_coords()
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])-1][int(value[2])] != "-H-" and board[int(value[0])-1][int(value[2])+1] != "-H-":
                    board[int(value[0])-1][int(value[2])+1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])] = "-H-"
                else:
                    if random is False:
                        print_board(board)
                        set_ship_3(board)
                    if random is True:
                        set_ship_3(board, True)
            except (IndexError, ValueError):
                if random is False:
                        print_board(board)
                        set_ship_3(board)
                if random is True:
                    set_ship_3(board, True)
        else:
            print_board(board)
            set_ship_3(board)
    elif orientation == "v":
        if random is False:
            value = input("\nSet the starter position of your third ship: ")
        if random is True:
            value = generate_random_coords()
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])][int(value[2])-1] != "-H-" and board[int(value[0])+1][int(value[2])-1] != "-H-":
                    board[int(value[0])+1][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                    board[int(value[0])][int(value[2])-1] = "-H-"
                else:
                    if random is False:
                        print_board(board)
                        set_ship_3(board)
                    if random is True:
                        set_ship_3(board, True)
            except (IndexError, ValueError):
                if random is False:
                        print_board(board)
                        set_ship_3(board)
                if random is True:
                    set_ship_3(board, True)
        else:
            print_board(board)
            set_ship_3(board)
    else:
        print_board(board)
        set_ship_3(board)
    if random is False:
        print_board(board)


def whos_turn(board, computer=False):
    if computer is False:
        if board == board1:
            print("Player 1")
        elif board == board2:
            print("Player 2")
    else:
        print("Computer")


def shoot(board, board_2, board_3, win, random=False):
    if random is False:
        whos_turn(board_3)
        value = input("\nWhere do you want to shoot? ")
    if random is True:
        whos_turn(board_3, True)
        value = generate_random_coords()
    try:
        if board[int(value[0])-1][int(value[2])-1] == "-H-":
            board[int(value[0])-1][int(value[2])-1] = "-X-"
            board_2[int(value[0])-1][int(value[2])-1] = "-X-"
            return 1
        elif board[int(value[0])-1][int(value[2])-1] == "-X-":
            return 0
        else:
            board[int(value[0])-1][int(value[2])-1] = "-O-"
            board_2[int(value[0])-1][int(value[2])-1] = "-O-"
            return 0
    except (IndexError, ValueError):
        print("\n   Oops You can't shoot there")
        return shoot(board, board_2, board_3, win)


def print_enemy(board):
    n = 0
    print("\n")
    for i in board:
        print(board[n])
        n += 1
    print("Your Board ")


def generate_random_coords():
    a1 = random.randrange(1, 5)
    a2 = "-"
    a3 = random.randrange(1, 5)
    result = str(a1) + a2 + str(a3)
    return result


def generate_random_orientation():
    random_int = random.randrange(1, 2)
    if random_int == 1:
        orientation = "v"
    else:
        orientation = "v"
    return orientation


def create_player_table(board):
    set_ship_1(board)
    set_ship_2(board)
    set_ship_3(board)


def generate_computer_table(board):
    set_ship_1(board, True)
    set_ship_2(board, True)
    set_ship_3(board, True)
