from enum import Enum
from functools import total_ordering

class Chess:
    """A representation of a chess game
    """

    # BTW the pieces go;
    # 20 21 22 (0,0 is bottom left)
    # 10 11 12
    # 00 01 02
    
    def __init__(self, pieces=None, captured_pieces=[], 
        white_to_move=True, turns=0):
        self._pieces = pieces if pieces is not None else Chess.get_starting_pos()
        self._captured_pieces = captured_pieces
        self._white_to_move = white_to_move
        self._turns = turns
    
    # ---------- Properties/Getters ----------
    @property
    def get_pieces(self):
        """Returns a Pieces array representing all the pieces of a chess game
        
        Returns:
            {Piece[]} -- The pieces on the board
        """
        return sorted(self._pieces)

    @property
    def get_white_to_move(self):
        return self._white_to_move

    @property
    def get_turns(self):
        return self._turns
    
    def get_piece_at(self, x, y):
        for p in self.get_pieces:
            if p.location[0] == x and p.location[1] == y:
                return p
        return None
    # ---------- Methods ----------
    def print_board(self):
        characters = {Piece.PAWN : "P", Piece.BISHOP : "B", 
                    Piece.KNIGHT: "N", Piece.ROOK: "R", 
                    Piece.QUEEN: "Q", Piece.KING: "K"}

        board = []
        for i in range(7,-1,-1):
            row = []
            for j in range(8):
                found = False
                for p in self.get_pieces:
                    if p.location == (i,j) and not found:
                        char = characters[p.piece_type]
                        char = str.upper(char) if p.is_white else str.lower(char)
                        row.append(char)
                        found = True
                if not found: row.append(".")
            board.append("".join(row))
        
        board_str = "\n(lowercase is black)\n|"
        board_str += "\n┌ 12345678 ┐"
        for i in range(8):
            board_str += "\n{0} {1} {0}".format(chr(ord('A') + 7 - i), board[i])
        board_str += "\n└ 12345678 ┘"
        board_str += "\nOn turn {}".format(self.get_turns)
        board_str += "\n{} to move".format("White" if self.get_white_to_move else "Black")
        print(board_str)
            
    
    def move(self, piece_location, move_location):
        """Move a piece on the board. A.K.A. the big function
        
        Arguments:
            piece_location {(int, int)} -- x, y of the piece to move
            move_location {(int, int)} -- x, y to move to
        """
        pass
    
    def can_move(self, piece_location, move_location, is_capture) -> bool:
        """Returns 
        
        Arguments:
            piece_location {(int, int)} -- 
            move_location {(int, int)} -- move to here
            is_capture {bool} -- is it a capture?
        
        Returns:
            {bool} -- If that move is allowed
        """
    

    def moveable_spots(self, piece_type, piece_color, piece_location):
        """Gets the list of all moveable spots for a piece
        basically hardcoded in bc I CANT EVEN ANY MORE

        Returns:
            {[(int, int, bool)]} -- a list of x,y spots a piece can move to, as well as if it is a capture
        """

        list_of_moves = []
        # Special: En-passant
        if piece_type == Piece.PAWN:
            if piece_color == Piece.WHITE:
                self.get_piece_at(piece_location[0], piece_location[1])
                if piece_location[0] == 2:

            else:

        elif piece_type == Piece.KNIGHT:
            pass
        elif piece_type == Piece.BISHOP:
            pass
        elif piece_type == Piece.ROOK:
            pass
        elif piece_type == Piece.QUEEN:
            pass
        
        # Special: Castling
        elif piece_type == Piece.KING:
            pass
        else:
            raise ValueError("piece_type should be a valid Piece.[TYPE]\npls fix ur code")
        
        # And then check the board state to make sure your king is not in check



    # ---------- Helper methods ----------

    _starting_pos = None
    @classmethod
    def get_starting_pos(cls):
        """Returns a board's starting position
        
        Returns:
            {Piece[]} -- An array of all of the pieces on the board
        """
        if cls._starting_pos is None:
            # I know this is really inefficient but whatever
            pieces = []
            for i in range(8):
                pieces.append(Piece(Piece.PAWN, Piece.WHITE, (1, i)))
                pieces.append(Piece(Piece.PAWN, Piece.BLACK, (6, i)))
            for i in range(2):
                pieces.append(Piece(Piece.ROOK, Piece.WHITE, (0, i * 7)))
                pieces.append(Piece(Piece.ROOK, Piece.BLACK, (7, i * 7)))
                pieces.append(Piece(Piece.KNIGHT, Piece.WHITE, (0, i * 5 + 1)))
                pieces.append(Piece(Piece.KNIGHT, Piece.BLACK, (7, i * 5 + 1)))
                pieces.append(Piece(Piece.BISHOP, Piece.WHITE, (0, i * 3 + 2)))
                pieces.append(Piece(Piece.BISHOP, Piece.BLACK, (7, i * 3 + 2)))
            pieces.append(Piece(Piece.QUEEN, Piece.WHITE, (0, 3)))
            pieces.append(Piece(Piece.QUEEN, Piece.BLACK, (7, 3)))
            pieces.append(Piece(Piece.KING, Piece.WHITE, (0, 4)))
            pieces.append(Piece(Piece.KING, Piece.BLACK, (7, 4)))
            cls._starting_pos = pieces
        return cls._starting_pos




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

        if piece_type not in self.PIECES.values():
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
            return self.is_white
    
    def __repr__(self):
        piece_color = "White" if self.is_white else "Black"
        piece_type = {v: k for k, v in Piece.PIECES.items()}[self.piece_type]
        return "{} {} at ({}, {})".format(piece_color, piece_type, self.location[0], self.location[1])

if __name__ == "__main__":
    print("---------- Testing ----------")
    p1 = Piece(Piece.QUEEN, Piece.WHITE, (0,0))
    p2 = Piece(Piece.QUEEN, Piece.BLACK, (0,0))
    comp1 = "p1 == p2"
    comp2 = "p1 > p2"
    print(comp1, ": ", eval(comp1), sep="")
    print(comp2, ": ", eval(comp2), sep="")

    Chess().print_board()
        