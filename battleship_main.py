import os


board1 = [["1-1", "1-2", "1-3", "1-4", "1-5"],  # player 1 board
          ["2-1", "2-2", "2-3", "2-4", "2-5"],
          ["3-1", "3-2", "3-3", "3-4", "3-5"],
          ["4-1", "4-2", "4-3", "4-4", "4-5"],
          ["5-1", "5-2", "5-3", "5-4", "5-5"]]

board2 = [["1-1", "1-2", "1-3", "1-4", "1-5"],  # player 2 board
          ["2-1", "2-2", "2-3", "2-4", "2-5"],
          ["3-1", "3-2", "3-3", "3-4", "3-5"],
          ["4-1", "4-2", "4-3", "4-4", "4-5"],
          ["5-1", "5-2", "5-3", "5-4", "5-5"]]

board1a = [["1-1", "1-2", "1-3", "1-4", "1-5"],  # the shots of player 1 on player 2's board
           ["2-1", "2-2", "2-3", "2-4", "2-5"],
           ["3-1", "3-2", "3-3", "3-4", "3-5"],
           ["4-1", "4-2", "4-3", "4-4", "4-5"],
           ["5-1", "5-2", "5-3", "5-4", "5-5"]]

board2a = [["1-1", "1-2", "1-3", "1-4", "1-5"],  # the shots of player 2 on player 1's board
           ["2-1", "2-2", "2-3", "2-4", "2-5"],
           ["3-1", "3-2", "3-3", "3-4", "3-5"],
           ["4-1", "4-2", "4-3", "4-4", "4-5"],
           ["5-1", "5-2", "5-3", "5-4", "5-5"]]

win_1 = 0
win_2 = 0


def main():
    os.system('clear')
    print("""
    888             888   888   888                888     d8b
    888             888   888   888                888     Y8P
    888             888   888   888                888
    88888b.  8888b. 888888888888888 .d88b. .d8888b 88888b. 88888888b.
    888 "88b    "88b888   888   888d8P  Y8b88K     888 "88b888888 "88b
    888  888.d888888888   888   88888888888"Y8888b.888  888888888  888
    888 d88P888  888Y88b. Y88b. 888Y8b.         X88888  888888888 d88P
    88888P" "Y888888 "Y888 "Y888888 "Y8888  88888P'888  88888888888P"
                                                            888
                                                            888
                                                            888           copyright: codecool team cicák
                                     |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                     BB-61/
 \_________________________________________________________________________|""")
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


main()

print_board(board1)
set_ship_1(board1)
set_ship_2(board1)
set_ship_3(board1)

print_board(board2)
set_ship_1(board2)
set_ship_2(board2)
set_ship_3(board2)

while True:
    print_board(board1a)
    print("Enemy Board ")
    print_enemy(board1)
    win_1 = win_1 + shoot(board2, board1a, board1, win_1)
    if win_1 == 6:
        break
    print_board(board2a)
    print("Enemy Board ")
    print_enemy(board2)
    win_2 = win_2 + shoot(board1, board2a, board2, win_2)
    if win_2 == 6:
        break

print("Score:")
print("Player 1:", win_1, "Player 2:", win_2)
if win_1 > win_2:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
