import os
from battleship_functions import *
from battleship_boards import *
from battleship_artwork import *

win_1 = 0
win_2 = 0

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
