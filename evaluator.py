import chess


def evaluate(board):
    sum = 0
    for i in range(64):
        pieceObj = board.piece_at(i)
        piece = ""
        if(pieceObj != None):
            piece = pieceObj.symbol()
        if piece == 'p':
            sum -= 1
        elif piece == 'n' or piece == 'b':
            sum -= 3
        elif piece == 'r':
            sum -= 5
        elif piece == 'q':
            sum -= 9
        elif piece == 'P':
            sum += 1
        elif piece == 'N' or piece == 'B':
            sum += 3
        elif piece == 'R':
            sum += 5
        elif piece == 'Q':
            sum += 9
    return sum
