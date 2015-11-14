import chess
import sys
import copy

def minimax(board, move, depth, isMax):
    if(depth > 0):
        if(isMax):
            best_value, best_move = (sys.maxsize*-1,None)
        else:
            best_value, best_move = (sys.maxsize,None)
        for legal_move in board.legal_moves:
            board_cpy = copy.deepcopy(board)
            board_cpy.push(legal_move)
            next_value = minimax(board_cpy,legal_move,depth-1,not isMax)[0]
            if(isMax):
                if(next_value > best_value):
                    best_value, best_move = next_value, legal_move
            else:
                if(next_value < best_value):
                    best_value, best_move = next_value, legal_move
        return best_value, best_move
    else:
        return evaluate(board), move

def evaluate(board):
    sum = 0
    for i in range(64):
        piece = board.piece_at(i)
        if(piece == 'p'):
            sum -= 1
        elif(piece == 'n' or piece == 'b'):
            sum -= 3
        elif(piece == 'r'):
            sum -= 5
        elif(piece == 'q'):
            sum -= 9
        elif(piece == 'P'):
            sum += 1
        elif(piece == 'N' or piece == 'B'):
            sum += 3
        elif(piece == 'R'):
            sum += 5
        elif(piece == 'Q'):
            sum += 9
    return sum

test_board = chess.Board()

for i in range(4):
    value, move = minimax(test_board,None,4,test_board.turn)
    test_board.push(move)
    print(move)
    print(test_board)
    print()