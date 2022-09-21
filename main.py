from art import logo
from objects import Board
import os

game_on = True
i = 0
print(logo)
board = Board()
while game_on:
    while i < 10:
        board.show_board()
        if i % 2 == 0:
            move = input(
                "Player X's turn to play\nFormat answer as 'number of row', 'number of column' (11, 21, 32)\n")
        elif i % 2 == 1:
            move = input(
                "Player O's turn to play\nFormat answer as 'number of row', 'number of column' (11, 21, 32)\n")
        if move not in board.mapping:
            os.system('cls')
            print("Incorrect move")
            continue
        elif board.mapping[move] == "X" or board.mapping[move] == "O":
            os.system('cls')
            print("Move already played, try again")
            continue
        else:
            if i % 2 == 0:
                board.mapping[move] = "X"
            else:
                board.mapping[move] = "O"
            os.system('cls')
        if board.check_winner():
            game_on = False
            i = 11
            board.show_board()
        i += 1
        if i == 9:
            print("It's a tie!")
            game_on = False
            i = 11
