import math
import chess
from stockfish import Stockfish

MOVE_DEPTH = 18

# -- Weird 1 --
# STARTING_FEN = "QQQQQQQQ/PPPPPPPP/rnbqkbnr/pppppppp/PPPPPPPP/RNBQKBNR/pppppppp/qqqqqqqq w - - 0 1"
# -- Weird 2 --
# STARTING_FEN = "rnbqkbnr/pppppppp/8/8/PPPPPPPP/RNBQKBNR/pppppppp/qqqqqqqq w kq - 0 1"
# -- King Queen vs King Pawn --
# STARTING_FEN = "8/6P1/5K2/8/8/8/1q6/1k6 w - - 0 1"
# -- Standard --
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# -- Standard Upsidedown --
# STARTING_FEN = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w - - 0 1"
# -- Chess but good https://www.youtube.com/watch?v=PTcvbDbVbtM&t=185s --
# STARTING_FEN = "Q2nB3/Pp1pp1PP/1P1rR2P/3PppP1/q2bKpN1/Rrp1N1P1/B1pk4/2b3n1 w - - 0 1"

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
    print(f"State: {state}")

san_board = chess.Board(STARTING_FEN)
moves = san_board.variation_san(board.move_stack)
pgn = f"""[Variant "From Position"]
[FEN "{STARTING_FEN}"]

{moves}"""

print("--- PGN ---")
print(pgn)
