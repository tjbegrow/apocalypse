class ChessPiece:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
class Pawn(ChessPiece):
    def __init__(self, name, position, symbol):
        super().__init__(name, position)
        self.symbol = symbol

class Knight(ChessPiece):
    def __init__(self, name, position, symbol):
        super().__init__(name, position)
        self.symbol = symbol