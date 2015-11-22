import chess

def get_move(board, whites_turn):
    is_uppercase = whites_turn
    if whites_turn:
        print("you are playing as white, your pieces are uppercase")
    else:
        print("you are playing as white, your pieces are uppercase")

    print(board)
    print("")

    human_move = input("enter a move of the form 'a1b1': ")
    move = chess.Move.from_uci(human_move)
    if move in board.legal_moves:
        # move is legal
        return move
    else:
        print("that move was not legal :/")
        print("try again")
        # print("here are your legal moves:")
        # print(list(board.legal_moves))
        get_move(board, whites_turn)
