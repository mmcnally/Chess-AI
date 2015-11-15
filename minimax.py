import chess
import sys
import copy
import time
import evaluator

'''
Runner for Minimax algorithm with Alpha-Beta pruning
calls internal algorithm and simplifies parameters
'''
def minimax_alpha_beta(board, depth, isMax):
    alpha = -sys.maxsize
    beta = sys.maxsize
    return minimax_alpha_beta_internals(board, None, depth, isMax, alpha, beta)

def minimax_alpha_beta_internals(board, move, depth, isMax, alpha, beta):
    if depth > 0:
        if isMax:
            best_value, best_move = (sys.maxsize*-1,None)
        else:
            best_value, best_move = (sys.maxsize,None)
        for legal_move in board.legal_moves:
            if alpha < beta:
                board_cpy = copy.deepcopy(board)
                board_cpy.push(legal_move)
                next_value = minimax(board_cpy,legal_move,depth-1,not isMax)[0]
                if isMax:
                    if next_value > best_value:
                        best_value, best_move = next_value, legal_move
                    if next_value > alpha:
                        alpha = next_value
                else:
                    if next_value < best_value:
                        best_value, best_move = next_value, legal_move
                    if next_value < beta:
                        beta = next_value
        return best_value, best_move
    else:
        return evaluator.evaluate(board), move


def minimax(board, move, depth, isMax):
    if depth > 0:
        if isMax:
            best_value, best_move = (sys.maxsize*-1,None)
        else:
            best_value, best_move = (sys.maxsize,None)
        for legal_move in board.legal_moves:
            board_cpy = copy.deepcopy(board)
            board_cpy.push(legal_move)
            next_value = minimax(board_cpy,legal_move,depth-1,not isMax)[0]
            if isMax:
                if next_value > best_value:
                    best_value, best_move = next_value, legal_move
            else:
                if next_value < best_value:
                    best_value, best_move = next_value, legal_move
        return best_value, best_move
    else:
        return evaluator.evaluate(board), move



board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
print(evaluator.evaluate(board))
