class ChessPiece:
    def __init__(self, name, position):
        self.name = name
        self.position = position



class Pawn(ChessPiece):
    def avail_moves(self):
        return self.position

class Knight(ChessPiece):
    pass