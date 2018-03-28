import os
import time
from battleship_functions import *
from battleship_boards import *
from battleship_artwork import *

win_1 = 0
win_2 = 0

main()
single_or_multi = ""
while single_or_multi.lower() != "s" or single_or_multi.lower() != "m":
    single_or_multi = input("Enter game mode: [S]ingle player, [M]ulti player :")
    if single_or_multi.lower() == "m" or single_or_multi.lower() == "s":
        break

###############################
###### MULTI PLAYER MODE ######
###############################

if single_or_multi.lower() == "m":
    print_board(board1)
    create_player_table(board1)
    print_board(board2)
    create_player_table(board2)

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

###############################
###### SINGLE PLAYER MODE ##### 
###############################

if single_or_multi.lower() == "s":
    print_board(board1)
    create_player_table(board1)

    generate_computer_table(board2)

    while True:
        print_board(board1a)
        print("Enemy Board ")
        print_enemy(board1)
        win_1 = win_1 + shoot(board2, board1a, board1, win_1)
        if win_1 == 6:
            break
        print_board(board1a)
        print("Enemy Board ")
        print_enemy(board1)
        time.sleep(3)

        print_board(board2a)
        win_2 = win_2 + shoot(board1, board2a, board2, win_2, random=True)
        print_board(board2a)
        whos_turn(board2, True)
        time.sleep(3)
        if win_2 == 6:
            break

    print("Score:")
    print("Player 1:", win_1, "Computer:", win_2)
    if win_1 > win_2:
        print("Player 1 wins!")
    else:
        print("Computer wins!")
