import chess
import random

''' Boolean definitions for turns '''
WHITE = True
BLACK = False

''' prints which player's turn it is '''
def print_turn(board):
    if board.turn is WHITE:
        print("white's turn")
    else:
        print("black's turn")
    pass



''' converts player (boolean) to string '''
def player_str(player):
    if player is WHITE:
        return "WHITE"
    else:
        return "BLACK"


''' prints list of legal moves for current player '''
def print_legal_moves(board):
    moves = list(board.legal_moves)
    for move in moves:
        board.push(move)
        print(board)
        board.pop()
    pass


''' returns winner from endgame state '''
def get_winner(board):
    if(not board.is_game_over):
        raise ValueError("game is not over!")
    return not board.turn


''' prints out information about how game ended '''
def print_game_enders(board):
    print("fivefold repitition: %r" % board.is_fivefold_repetition())
    print("seventy five moves: %r" %board.is_seventyfive_moves())
    print("checkmate: %r" % board.is_checkmate())
    print("stalemate: %r" % board.is_stalemate())
    print("insufficient material: %r" % board.is_insufficient_material())
