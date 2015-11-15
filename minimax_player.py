import chess
import random
import minimax


def run_random_game_vs_minimax_with_printing():
    board = chess.Board();
    num_turns = 0
    is_mini = True
    print("initial board")
    print_turn(board)
    print(board)
    print("")

    while(not board.is_game_over()):
        chosen_move = None
        if(is_mini):
            print("minimax")
            val, move = minimax.minimax(board, None, 3, True)
            chosen_move = move
        else:
            print("random bitch")
            num_turns += 1
            moves = list(board.legal_moves)
            num_moves = len(moves)
            move_index = random.randrange(0, num_moves)
            chosen_move = moves[move_index]

        print_turn(board)
        board.push(chosen_move)
        print(board)
        print("")
        print("")
        is_mini = not is_mini

    print_game_enders(board)
    print_turn(board) # loser
    return get_winner(board)



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
    return get_winner(board)
