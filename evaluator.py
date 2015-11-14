import chess


def eval(board):
    sum = 0
    for i in range(64):
        piece = board.piece_at(i)
        if(piece.color):
            sum += piece.piece_type
        else:
            sum -= piece.piece_type
    return sum
