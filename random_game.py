import chess
import random

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


'''
Runs random game until game is over
Each player switches off making random legal moves
Returns losing player
'''
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
        move_index = random.randrange(0, num_moves)

        print_turn(board)
        print(board)
        print("")
        board.push(moves[move_index])
        print(board)
        print("")
        print("")

    print_game_enders(board)
    print_turn(board) # loser
    return get_winner(board)

def run_random_game_no_printing():
    board = chess.Board();
    num_turns = 0
    while(not board.is_game_over()):
        num_turns += 1
        moves = list(board.legal_moves)
        num_moves = len(moves)
        move_index = random.randrange(0, num_moves)

        board.push(moves[move_index])


    # print_game_enders(board)
    return get_winner(board)



if __name__=='__main__':
    winner = run_random_game()
    print("winner is %s" % player_str(winner))
