import os
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


def set_ship_1(board):
    whos_turn(board)
    value = input("Set your first ship: ")
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
    print_board(board)


def set_ship_2(board):
    orientation = input("\nSet the orientation of your second ship, (h)orizontal or (v)ertical: ")
    if orientation == "h":
        value = input("\nSet the starter position of your second ship: ")
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])-1][int(value[2])] != "-H-":
                    board[int(value[0])-1][int(value[2])] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                else:
                    print_board(board)
                    set_ship_2(board)
            except (IndexError, ValueError):
                print_board(board)
                set_ship_2(board)
        else:
            print_board(board)
            set_ship_2(board)
    elif orientation == "v":
        value = input("\nSet the starter position of your second ship: ")
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])][int(value[2])-1] != "-H-":
                    board[int(value[0])][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                else:
                    print_board(board)
                    set_ship_2(board)
            except (IndexError, ValueError):
                print_board(board)
                set_ship_2(board)
        else:
            print_board(board)
            set_ship_2(board)
    else:
        print_board(board)
        set_ship_2(board)
    print_board(board)


def set_ship_3(board):
    orientation = input("\nSet the orientation of your third ship, (h)orizontal or (v)ertical: ")
    if orientation == "h":
        value = input("\nSet the starter position of your third ship: ")
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])-1][int(value[2])] != "-H-" and board[int(value[0])-1][int(value[2])+1] != "-H-":
                    board[int(value[0])-1][int(value[2])+1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])] = "-H-"
                else:
                    print_board(board)
                    set_ship_3(board)
            except (IndexError, ValueError):
                print_board(board)
                set_ship_3(board)
        else:
            print_board(board)
            set_ship_3(board)
    elif orientation == "v":
        value = input("\nSet the starter position of your third ship: ")
        if len(value) == 3:
            try:
                if board[int(value[0])-1][int(value[2])-1] != "-H-" and board[int(value[0])][int(value[2])-1] != "-H-" and board[int(value[0])+1][int(value[2])-1] != "-H-":
                    board[int(value[0])+1][int(value[2])-1] = "-H-"
                    board[int(value[0])-1][int(value[2])-1] = "-H-"
                    board[int(value[0])][int(value[2])-1] = "-H-"
                else:
                    print_board(board)
                    set_ship_3(board)
            except (IndexError, ValueError):
                print_board(board)
                set_ship_3(board)
        else:
            print_board(board)
            set_ship_3(board)
    else:
        print_board(board)
        set_ship_3(board)
    print_board(board)


def whos_turn(board):
    if board == board1:
        print("Player 1")
    elif board == board2:
        print("Player 2")


def shoot(board, board_2, board_3, win):
    whos_turn(board_3)
    value = input("\nWhere do you want to shoot? ")
    try:
        if board[int(value[0])-1][int(value[2])-1] == "-H-":
            board[int(value[0])-1][int(value[2])-1] = "-X-"
            board_2[int(value[0])-1][int(value[2])-1] = "-X-"
            return 1
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
