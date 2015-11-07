import chess
import random

board = chess.Board();



## print all legal next boards
# moves = list(board.legal_moves)
# for move in moves:
#     board.push(move)
#     print(board)
#     board.pop()

while(not board.is_game_over()):
    moves = list(board.legal_moves)
    num_moves = len(moves)
    print(num_moves)
    r = random.randrange(0, num_moves)
    print("random num: %d" % r)
    print("legal moves", board.legal_moves)
    board.push(moves[r])
    print(board)
