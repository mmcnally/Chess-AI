import chess
import random
import minimax
import game_tools

class Player(object):
    '''
    Calculates move to a specified depth in game tree
    board: chess board object from python-chess library
    whites_turn: True if it is white's turn, False otherwise
    depth: int, how many levels to go down in game tree
    Returns move
    '''
    def calculate_move(self, board, whites_turn, depth): pass

    '''
    returns name of algorithm as string
    '''
    def __str__(self): pass


class Minimax_Player(Player):
    def calculate_move(self, board, whites_turn, depth):
        value, move = minimax.minimax(board, None, depth, whites_turn)
        return move

    def __str__(self):
        return "Minimax Player"

class Minimax_Alpha_Beta_Player(Player):
    def calculate_move(self, board, whites_turn, depth):
        isMax = whites_turn
        value, move = minimax.minimax_alpha_beta(board, depth, isMax)
        return move

    def __str__(self):
        return "Minimax Alpha-Beta Player"

class Minimax_Alpha_Beta_Player_2(Player):
    def calculate_move(self, board, whites_turn, depth):
        isMax = whites_turn
        value, move = minimax.minimax_alpha_beta_2(board, depth, isMax)
        return move

    def __str__(self):
        return "Minimax Alpha-Beta Player 2"


class Random_Player(Player):
    def calculate_move(self, board, whites_turn, depth):
        moves = list(board.legal_moves)
        num_moves = len(moves)
        move_index = random.randrange(0, num_moves)
        return moves[move_index]

    def __str__(self):
        return "Random Player"



def run_random_game_vs_minimax_with_printing():
    board = chess.Board();
    num_turns = 0
    is_mini = True
    minimax_player = Minimax_Alpha_Beta_Player()
    random_player = Random_Player()
    print("initial board")
    game_tools.print_turn(board)
    print(board)
    print("")

    while not board.is_game_over():
        chosen_move = None
        if(is_mini):
            print("minimax")
            move = minimax_player.calculate_move(board, True, 3)
            # minimax.minimax(board, None, 3, True)
            chosen_move = move
        else:
            print("random bitch")
            num_turns += 1
            move = random_player.calculate_move(board, False, 3)
            chosen_move = move

        game_tools.print_turn(board)
        board.push(chosen_move)
        print(board)
        print("")
        print("")
        is_mini = not is_mini

    game_tools.print_game_enders(board)
    game_tools.print_turn(board) # loser
    return game_tools.get_winner(board)



def run_random_game_vs_minimax():
    board = chess.Board();
    num_turns = 0
    is_mini = True
    while(not board.is_game_over()):
        if(is_mini):
            val, move = minimax.minimax(board, None, 3, True)
            board.push(move)
        else:
            moves = list(board.legal_moves)
            num_moves = len(moves)
            move_index = random.randrange(0, num_moves)
            board.push(moves[move_index])
        num_turns += 1
        is_mini = not is_mini
    return game_tools.get_winner(board)


if __name__=='__main__':
    run_random_game_vs_minimax_with_printing()
