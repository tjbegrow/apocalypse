#Apocalypse: A chess like game.

import pandas as pd
import pieces

columns = ['a', 'b', 'c', 'd', 'e']
ind = ['5', '4', '3', '2', '1']
# Piece placement. BK = Black Kight BP = Black Pawn WK = White Kight 
# WP = White Pawn

initial_setup = [[pieces.Knight('BK1', 'a5', '\u265E'), 
                  pieces.Pawn('BP2', 'b5', '\u265F'),
                  pieces.Pawn('BP3', 'c5', '\u265F'),
                  pieces.Pawn('BP4', 'd5', '\u265F'),
                  pieces.Knight('BK2', 'e5','\u265E')],
                 [pieces.Pawn('BP1', 'a4', '\u265F'), 'O', 'O', 'O', 
                  pieces.Pawn('BP5', 'e4', '\u265F'),],
                 ['O', 'O', 'O', 'O' ,'O'],
                 [pieces.Pawn('WP1', 'a2', '\u2659'), 'O', 'O', 'O',
                  pieces.Pawn('WP5', 'e2', '\u2659')],
                 [pieces.Knight('WK1', 'a1', '\u2658'),
                  pieces.Pawn('WP2', 'b1', '\u2659'),
                  pieces.Pawn('WP3', 'c1', '\u2659'), 
                  pieces.Pawn('WP4', 'd1', '\u2659'),
                  pieces.Knight('WK2', 'e1', '\u2658')]]

chessboard = pd.DataFrame(initial_setup, ind, columns)

def update_board(chess_board):
    """Updates the displayed chessboard.
    
    Args:
      chessboard: the logical DataFrame chessboard
    
    Side Effect: 
       Prints current chessboard configuration to terminal.
    """

    chessboard_display = chessboard.copy()
    for index, row in chessboard.iteritems():
        for ind, item in row.iteritems():
            # print(type(ind))
            if type(item) == pieces.Pawn:
                chessboard_display.at[ind, index[0]] = item.symbol
            if type(item) == pieces.Knight:
                chess_boarddisplay.at[ind, index[0]] = item.symbol
    print(chessboard_display)


# print(chess_board.at['5', 'a'].name) #Return the name of the Chess object
# print(chess_board.at['3', 'c'] == 'O')

# Get input from player asking them what piece they want to move based on 
# the coordinates

#TODO: Write docstrings for select_piece and select_coord()
def select_piece(select_coord):
    """Calls select_coord() and returns the piece object if valid
       
    Args:
      select_coord: the select_coord function to get the user
      coordinate
    
    Returns:
      piece_selected: A valid piece that is the player's
    """
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
    """Gets coordinate from user and returns it if valid
    
    Returns:
      coord: A valid coordinate selected by the user.
    
    Side Effects:
      This will print "Not a valid coordinate!" if the selection was
      not valid
    """
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
    update_board(chessboard)
    print()
    current_piece = select_piece()
    

