#Apocalypse: A chess like game.

import pandas as pd
import pieces

columns = ['a', 'b', 'c', 'd', 'e']
ind = ['5', '4', '3', '2', '1']
# Piece placement. BK = Black Kight BP = Black Pawn WK = White Kight 
# WP = White Pawn

initial_setup = [[pieces.Knight('BK1','a5'), 
                  pieces.Pawn('BP2','b5'),
                  pieces.Pawn('BP3','c5'),
                  pieces.Pawn('BP4','d5'),
                  pieces.Knight('BK2','e5')],
                 [pieces.Pawn('BP1','a4'), 'O', 'O', 'O', 
                  pieces.Pawn('BP5','e4'),],
                 ['O', 'O', 'O', 'O' ,'O'],
                 [pieces.Knight('WP1','a2'), 'O', 'O', 'O',
                  pieces.Knight('WP5','e2')],
                 [pieces.Knight('WK1','a1'),
                  pieces.Pawn('WP2','b1'),
                  pieces.Pawn('WP3','c1'), 
                  pieces.Pawn('WP4','d1'),
                  pieces.Knight('WK2','e1')]]

chess_board = pd.DataFrame(initial_setup, ind, columns)
# print(chess_board)

# BP1 = pieces.Pawn("BP1", "a4")

# print(chess_board.at['5', 'a'].name) #Return the name of the Chess object
# print(type(chess_board.at['5', 'a']))



# Get input from player asking them what piece they want to move based on 
# the coordinates

#TODO: CHECK IF COORDINATE HAS A CHESS PIECE THAT PLAYER OWNS
def player_piece_select():
    select_piece = ''
    while True:
        select_piece = str(input('What piece would you like to move?'))
        found = False
        for col in columns:
            if select_piece[0] == col:
                found = False
                for i in ind:
                    if select_piece[1] == i:
                        print('found')
                        found = True
                        break
                    else:
                        print('not found')
                if found == True:
                    break
            else:
               print('not found')
        if found == True:
            break
        else:
            print('Not a valid coordinate!')
    return select_piece

active_piece = player_piece_select()
print(active_piece)
