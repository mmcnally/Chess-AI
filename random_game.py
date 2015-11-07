import chess
import random

WHITE = True
BLACK = False


# prints which player's turn it is
def print_turn(board):
    if board.turn is WHITE:
        print("white's turn")
    else:
        print("black's turn")
    pass

# prints list of legal moves for current player
def print_legal_moves(board):
    moves = list(board.legal_moves)
    for move in moves:
        board.push(move)
        print(board)
        board.pop()
    pass

# runs random game until game is over
# each player switches off making random legal moves

def run_random_game():
    board = chess.Board();
    num_turns = 0
    print("initial board")
    print_turn(board)
    print(board)
    print("")

    while(not board.is_game_over()):
        num_turns += 1

        moves = list(board.legal_moves)
        num_moves = len(moves)
        r = random.randrange(0, num_moves)
        # print(num_moves)
        # print("random num: %d" % r)
        # print("legal moves", board.legal_moves)
        print_turn(board)
        print(board)
        print("")
        board.push(moves[r])
        print(board)
        print("")
        print("")

    print("fivefold repitition: %r" % board.is_fivefold_repetition())
    print("seventy five moves: %r" %board.is_seventyfive_moves())
    print("checkmate: %r" % board.is_checkmate())
    print("stalemate: %r" % board.is_stalemate())
    print("insufficient material: %r" % board.is_insufficient_material())
    print_turn(board) # loser
    pass



if __name__=='__main__':
    run_random_game()
