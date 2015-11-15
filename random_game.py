import chess
import random
import minimax
import game_tools

'''
Runs random game until game is over
Each player switches off making random legal moves
Returns losing player
'''
def run_random_game():
    board = chess.Board();
    num_turns = 0
    print("initial board")
    game_tools.print_turn(board)
    print(board)
    print("")

    while(not board.is_game_over()):
        num_turns += 1
        moves = list(board.legal_moves)
        num_moves = len(moves)
        move_index = random.randrange(0, num_moves)

        game_tools.print_turn(board)
        print(board)
        print("")
        board.push(moves[move_index])
        print(board)
        print("")
        print("")

    game_tools.print_game_enders(board)
    game_tools.print_turn(board) # loser
    return game_tools.get_winner(board)

def run_random_game_no_printing():
    board = chess.Board();
    num_turns = 0
    while(not board.is_game_over()):
        num_turns += 1
        moves = list(board.legal_moves)
        num_moves = len(moves)
        move_index = random.randrange(0, num_moves)
        board.push(moves[move_index])
    return game_tools.get_winner(board)








if __name__=='__main__':
    winner = run_random_game()
    # winner = run_random_game_vs_minimax()
    # winner = run_random_game_YAY() # prints shit
    print("winner is %s" % game_tools.player_str(winner))
