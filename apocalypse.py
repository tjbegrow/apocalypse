#Apocalypse: A chess like game.

import pandas as pd

columns = ['a', 'b', 'c', 'd', 'e']
ind = [5, 4, 3, 2, 1]
# Piece placement. BK = Black Kight BP = Black Pawn WK = White Kight 
# WP = White Pawn

initial_setup = [['BK1', 'BP2', 'BP3', 'BP4', 'BK2'],
                 ['BP1', 'O', 'O', 'O', 'BP5'],
                 ['O', 'O', 'O', 'O' ,'O'],
                 ['WP1', 'O', 'O', 'O', 'WP5'],
                 ['WK1', 'WP2', 'WP3', 'WP4', 'WK2']]

chess_board = pd.DataFrame(initial_setup, ind, columns)
print(chess_board)