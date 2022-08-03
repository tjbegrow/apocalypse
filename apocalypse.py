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
# print(chess_board.at['3', 'c'] == 'O')



# Get input from player asking them what piece they want to move based on 
# the coordinates

#TODO: CHECK IF COORDINATE HAS A CHESS PIECE THAT PLAYER OWNS

def select_piece():
    piece_selected = None
    while True:
        coord = select_coord()
        if chess_board.at[coord[1], coord[0]] == 'O':
            print('No piece found at that coordinate')
            continue
        else:
            piece_selected = chess_board.at[coord[1], coord[0]]
            if piece_selected.name[0] == 'B':
                continue
            else:
                print("You selected {} at position {}".format(piece_selected.name, piece_selected.position))
                break
    return piece_selected
            



def select_coord():
    coord = ''
    while True:
        coord = str(input('What piece would you like to move?\n▶'))
        found = False
        for col in columns:
            if coord[0] == col:
                found = False
                for i in ind:
                    if coord[1] == i:
                        # print('found')
                        found = True
                        break
                    # else:
                        # print('not found')
                if found == True:
                    break
            # else:
               # print('not found')
        if found == True:
            break
        else:
            print('Not a valid coordinate!')
    return coord

if __name__ == '__main__':
    print('''---------Apocalypse--------

(\__/) (\__/) (\__/) (\__/)
 |oo|   |oo|   |oo|   |oo|
 (OO)   (OO)   (OO)   (OO) 

The classic C.S. Lewis chess varient, by Tyler Begrow
-----------------------------------------------------
''')
    current_piece = select_piece()
