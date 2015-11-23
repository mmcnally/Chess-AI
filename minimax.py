import chess, sys, copy, time


# def minimax_alpha_beta_2(board, depth, isMax):
#     alpha = -sys.maxsize
#     beta = sys.maxsize
#     return minimax_alpha_beta_internals_2(board, None, depth, isMax, alpha, beta)

# def minimax_alpha_beta_internals_2(board, move, depth, isMax, alpha, beta):
#     if depth > 0:
#         if isMax:
#             best_value, best_move = (sys.maxsize*-1,None)
#         else:
#             best_value, best_move = (sys.maxsize,None)
#         for legal_move in board.legal_moves:
#             if alpha < beta:
#                 board_cpy = copy.deepcopy(board)
#                 board_cpy.push(legal_move)
#                 next_value = minimax_alpha_beta_internals_2(board_cpy,legal_move,depth-1,not isMax,alpha,beta)[0]
#                 if isMax:
#                     if next_value > best_value:
#                         best_value, best_move = next_value, legal_move
#                     if next_value > alpha:
#                         alpha = next_value
#                 else:
#                     if next_value < best_value:
#                         best_value, best_move = next_value, legal_move
#                     if next_value < beta:
#                         beta = next_value
#         return best_value, best_move
#     else:
#         return evaluator.evaluate2(board), move


'''
Runner for Minimax algorithm with Alpha-Beta pruning
calls internal algorithm and simplifies parameters
'''
def minimax_alpha_beta(board, depth, isMax, eval_function):
    alpha = -sys.maxsize
    beta = sys.maxsize
    return minimax_alpha_beta_internals(board, None, depth, isMax,
                                        eval_function, alpha, beta)

def minimax_alpha_beta_internals(board, move, depth, isMax, eval_function, alpha, beta):
    if depth > 0:
        if isMax:
            best_value, best_move = (sys.maxsize*-1,None)
        else:
            best_value, best_move = (sys.maxsize,None)
        for legal_move in board.legal_moves:
            if alpha < beta:
                board_cpy = copy.deepcopy(board)
                board_cpy.push(legal_move)
                next_value = minimax_alpha_beta_internals(board_cpy,legal_move,
                                                          depth-1,not isMax,
                                                          eval_function,alpha,beta)[0]
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
        return eval_function(board), move


def minimax(board, move, depth, isMax, eval_function):
    if depth > 0:
        if isMax:
            best_value, best_move = (sys.maxsize*-1,None)
        else:
            best_value, best_move = (sys.maxsize,None)
        for legal_move in board.legal_moves:
            board_cpy = copy.deepcopy(board)
            board_cpy.push(legal_move)
            next_value = minimax(board_cpy,legal_move,depth-1,
                                 not isMax, eval_function)[0]
            if isMax:
                if next_value > best_value:
                    best_value, best_move = next_value, legal_move
            else:
                if next_value < best_value:
                    best_value, best_move = next_value, legal_move
        return best_value, best_move
    else:
        return eval_function(board), move
