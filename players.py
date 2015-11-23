import chess, random, time
import minimax, game_tools, human, evaluator


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
    times executions of calculate_move function
    Returns tuple: move and time taken to calculate the move
    '''
    def calculate_move_timed(self, board, whites_turn, depth):
        start = time.clock()
        move = self.calculate_move(board, whites_turn, depth)
        end = time.clock()
        total_time = end - start
        return move, total_time


    '''
    returns name of algorithm as string
    '''
    def __str__(self): pass


class Minimax_Player_Naive(Player):
    def calculate_move(self, board, whites_turn, depth):
        value, move = minimax.minimax(board, None, depth,
                                      whites_turn, evaluator.evaluate_naive)
        return move

    def __str__(self):
        return "Minimax Player"

class Minimax_Player_Advanced(Player):
    def calculate_move(self, board, whites_turn, depth):
        value, move = minimax.minimax(board, None, depth,
                                      whites_turn, evaluator.evaluate_advanced)
        return move

    def __str__(self):
        return "Minimax Player"


class Minimax_Alpha_Beta_Player_Naive(Player):
    def calculate_move(self, board, whites_turn, depth):
        isMax = whites_turn
        value, move = minimax.minimax_alpha_beta(board, depth, isMax,
                                                 evaluator.evaluate_naive)
        return move

    def __str__(self):
        return "Minimax Alpha-Beta Player Naive"

class Minimax_Alpha_Beta_Player_Advanced(Player):
    def calculate_move(self, board, whites_turn, depth):
        isMax = whites_turn
        value, move = minimax.minimax_alpha_beta(board, depth, isMax,
                                                 evaluator.evaluate_advanced)
        return move

    def __str__(self):
        return "Minimax Alpha-Beta Player Advanced"


class Random_Player(Player):
    def calculate_move(self, board, whites_turn, depth):
        moves = list(board.legal_moves)
        num_moves = len(moves)
        move_index = random.randrange(0, num_moves)
        return moves[move_index]

    def __str__(self):
        return "Random Player"

class Human_Player(Player):
    def calculate_move(self, board, whites_turn, depth):
        move = human.get_move(board, whites_turn)
        return move

    def __str__(self):
        return "Human Player"
