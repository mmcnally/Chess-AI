import players
import game_runner







def avg_move_calc_time(num_games=10, depth=2):
    minimax_total = 0
    print("starting calculations")
    for i in range(num_games):
        player1 = players.Minimax_Player()
        player2 = players.Random_Player()
        game = game_runner.Game(player1, player2, depth)
        winner, avg_p1, avg_p2 = game.play_with_avg_moves()
        minimax_total += avg_p1
        print("finished game %d with avg minimax time %f" % (i, avg_p1))

    minimax_avg = minimax_total / num_games
    print("overall average %f" % minimax_avg)
    return minimax_avg


if __name__=='__main__':
    avg = avg_move_calc_time()
