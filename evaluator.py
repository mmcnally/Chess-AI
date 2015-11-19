import chess
import sys

def evaluate(board):
    sum = 0
    for i in range(64):
        piece = board.piece_at(i)
        if(piece != None):
            if(piece.color == chess.WHITE):
                sum += piece.piece_type
            else:
                sum -= piece.piece_type
    return sum

def evaluate2(board):
    sum = 0
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            return sys.maxsize
        else:
            return sys.maxsize*-1
    for i in range(64):
        piece = board.piece_at(i)
        if(piece != None):
            if(piece.color == chess.WHITE):
                sum += piece.piece_type + (len(board.attacks(i))*.025)
            else:
                sum -= piece.piece_type + (len(board.attacks(i))*.025)
    return sum