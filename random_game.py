import chess
import random


WHITE = True
BLACK = False

def print_turn(board):
    if board.turn is WHITE:
        print("white's turn")
    else:
        print("black's turn")
    pass

def print_legal_moves(board):
    moves = list(board.legal_moves)
    for move in moves:
        board.push(move)
        print(board)
        board.pop()
    pass

def run_random_game():
    board = chess.Board();
    num_turns = 0

    while(not board.is_game_over()):
        num_turns += 1
        print_turn(board)
        moves = list(board.legal_moves)
        num_moves = len(moves)
        r = random.randrange(0, num_moves)
        # print(num_moves)
        # print("random num: %d" % r)
        # print("legal moves", board.legal_moves)
        board.push(moves[r])
        print(board)
        print("")
    pass


if __name__=='__main__':
    run_random_game()
