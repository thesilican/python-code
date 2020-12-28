import math
import chess
from stockfish import Stockfish

MOVE_DEPTH = 24

# -- Weird 1 --
# STARTING_FEN = "QQQQQQQQ/PPPPPPPP/rnbqkbnr/pppppppp/PPPPPPPP/RNBQKBNR/pppppppp/qqqqqqqq w - - 0 1"
# -- Weird 2 --
# STARTING_FEN = "rnbqkbnr/pppppppp/8/8/PPPPPPPP/RNBQKBNR/pppppppp/qqqqqqqq w kq - 0 1"
# -- King Queen vs King Pawn --
# STARTING_FEN = "8/6P1/5K2/8/8/8/1q6/1k6 w - - 0 1"
# -- Standard --
# STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# -- Standard Upsidedown --
STARTING_FEN = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w - - 0 1"

# Stockfish vs Stockfish

fen = STARTING_FEN
stockfish = Stockfish("./stockfish",
                      depth=MOVE_DEPTH,
                      parameters={
                          "Threads": 4,
                      })
board = chess.Board(fen)
state = "*"
ply = 0
while state == "*":
    ply += 1
    stockfish.set_fen_position(fen)
    moveUCI, evaluation = stockfish.get_move_and_evaluation()
    move = chess.Move.from_uci(moveUCI)
    moveSAN = board.san(move)
    moveNum, toMove = math.ceil(ply/2), "white" if ply % 2 else "black"
    print(f"-- Move {moveNum} {toMove} --")
    print(f"Move: {moveSAN} ({moveUCI})")
    if evaluation['type'] == 'cp':
        print(f"Eval: {evaluation['value']/100}")
    else:
        print(f"Eval: {evaluation['value']}")

    board.push(move)
    fen = board.fen()
    print(board.unicode(invert_color=True, empty_square=" "))
    state = board.result()

san_board = chess.Board(STARTING_FEN)
moves = san_board.variation_san(board.move_stack)
pgn = f"""[Variant "From Position"]
[FEN "{STARTING_FEN}"]

{moves}"""

print("--- PGN ---")
print(pgn)
