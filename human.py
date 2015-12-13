import chess

def get_move(board, whites_turn):
    is_uppercase = whites_turn
    if whites_turn:
        print("you are playing as white, your pieces are uppercase")
    else:
        print("you are playing as white, your pieces are uppercase")

    print(board)
    moves = [move.uci() for move in board.legal_moves]
    print(moves)
    print("")

    human_move = input("enter a move of the form 'a1b1': ")


    if human_move in moves:
        move = chess.Move.from_uci(human_move)
        return move
    else:
        print("that move was not legal :/")
        print("try again")
        return get_move(board, whites_turn)
