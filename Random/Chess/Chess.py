from enum import Enum
from functools import total_ordering

class Chess:
    """An immutable representation of a chess game
    """

    # BTW the pieces go;
    # 00 01 02 (0,0 is top left)
    # 10 11 12
    # 20 21 22


    def __init__(self):
        self.pieces = []
    
    def resetGame(self):
        self.pieces = self.getStartingPos()
    

    @staticmethod
    def getStartingPos():
        pieces = []
        for i in range(0,7):
            pieces.append(Piece(Piece.PAWN, Piece.WHITE, (7, i)))
            pieces.append(Piece(Piece.PAWN, Piece.BLACK, (0, i)))
        
        pieces.sort()
        return pieces

@total_ordering
class Piece(object):
    """Represents a single chess piece
    """
    PAWN = 0
    BISHOP = 1
    KNIGHT = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

    PIECES = {
        "PAWN": PAWN,
        "BISHOP": BISHOP,
        "KNIGHT": KNIGHT,
        "ROOK": ROOK,
        "QUEEN": QUEEN,
        "KING": KING }

    WHITE = True
    BLACK = False

    def __init__(self, piece_type: int, is_white: bool, location):
        """Creates a new instance of the Piece object
        
        Arguments:
            piece_type {int} -- type of the piece (pawn, bishop, etc)
            is_white {bool} -- is the piece white?
            location {(int, int)} -- x and y of this piece
        
        Raises:
            ValueError -- piece_type must be a valid piece number
        """

        if piece_type not in PIECES.values():
            raise ValueError("piece_type must be a valid piece number")
        self._piece_type = piece_type
        self._is_white = is_white
        self._location = location
    
    @property
    def piece_type(self):
        return self._piece_type
    
    @property
    def is_white(self):
        return self._is_white
    
    @property
    def location(self):
        return self._location
    
    def __eq__(self, other):
        # Location doesn't matter
        return (self. piece_type, self.is_white) == (other.piece_type, other.is_white)
    
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        # White before black (not to be racist)
        if self.is_white == other.is_white:
            # Numeric order by piece type
            return self.piece_type < other.piece_type
        else:
            return not self.is_white
    
    def __repr__(self):
        piece_color = "White" if self.is_white else "Black"
        piece_type = 0
        return "{} {} at ({}, {})".format(piece_color, piece_type, self.location[0], self.location[1])

if __name__ == "__main__":
    print("---------- Testing ----------")
    p1 = Piece(Piece.QUEEN, Piece.WHITE, (0,0))
    p2 = Piece(Piece.QUEEN, Piece.BLACK, (0,0))
    comp1 = "p1 == p2"
    comp2 = "p1 > p2"
    print(comp1, ": ", eval(comp1), sep="")
    print(comp2, ": ", eval(comp2), sep="")

        