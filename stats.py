import multiprocessing as mp
import time, timeit, math, queue, chess
import players, game_runner

NUM_PROCS = 4

'''
takes in string and makes a corresponding Player object
"minimax_naive" -> Minimax_Player_Naive
"minimax_advanced" -> Minimax_Plater_Advanced
"alpha_beta_naive" -> Minimax_Alpha_Beta_Player_Naive
"alpha_beta_advanced" -> Minimax_Alpha_Beta_Player_Advanced
"random" -> Random_Player

Returns created Player object
'''
def make_player_with_type(player_type):
    if player_type == 'minimax_naive':
        return players.Minimax_Player_Naive()
    elif player_type == 'minimax_advanced':
        return players.Minimax_Player_Advanced()
    elif player_type == 'alpha_beta_naive':
        return players.Minimax_Alpha_Beta_Player_Naive()
    elif player_type == 'alpha_beta_advanced':
        return players.Minimax_Alpha_Beta_Player_Advanced()
    elif player_type == 'random':
        return players.Random_Player()
    else:
        raise ValueError("player_type %s is not recognized" % player_type)



def avg_move_mp_runner(player_type, num_games=10, depth=2):
    out_queue = mp.Queue()
    procs = []
    remaining_games = num_games
    remaining_procs = NUM_PROCS
    for i in range(NUM_PROCS):
        games_to_play = int(math.ceil(float(remaining_games) / float(remaining_procs)))
        if games_to_play == 0:
            break
        else:
            remaining_games -= games_to_play
            remaining_procs -= 1

            print("process %d is about to run %d games" % (i, games_to_play))
            p = mp.Process(
                target=avg_move_calc_time,
                args=(player_type,
                      out_queue,
                      games_to_play,
                      depth))
            procs.append(p)
            p.start()


    # add up average moves times for all processes
    total_avgs = 0
    for i in range(NUM_PROCS - remaining_procs):
        total_avgs += out_queue.get()

    # join all processes
    for p in procs:
        p.join()


    avg_of_avgs = total_avgs / num_games
    print("average of averages is %f" % avg_of_avgs)
    return avg_of_avgs


def avg_move_calc_time(player_type, out_queue=None, num_games=10, depth=2):
    p1_total = 0
    p1_wins = 0
    for i in range(num_games):
        player1 = make_player_with_type(player_type)
        player2 = players.Random_Player()
        game = game_runner.Game(player1, player2, depth)
        winner, avg_p1, avg_p2 = game.play_with_avg_moves()
        p1_total += avg_p1
        if winner == chess.WHITE:
            p1_wins += 1
            print("finished game %d, %s, depth: %d, avg time: %f, p won: %s" % (i, player_type, depth,  avg_p1, winner == chess.WHITE))

    p1_avg = p1_total / num_games
    p1_win_prob = p1_wins / num_games
    print("overall average %f" % p1_avg)
    print("overall wins probability: %f" % p1_win_prob)

    if out_queue != None:
        out_queue.put(p1_avg)
        out_queue.close()


if __name__=='__main__':
    print("one process")
    t1 = timeit.default_timer()
    avg = avg_move_calc_time("minimax_advanced", num_games=10, depth=3)
    t2 = timeit.default_timer()
    one_proc_time = t2 - t1
    print("time taken: %f" % (one_proc_time))
    print("")

    # print("two processes")
    # t3 = timeit.default_timer()
    # avg = avg_move_mp_runner("alpha_beta", num_games=10, depth=3)
    # t4 = timeit.default_timer()
    # multi_proc_time = t4 - t3
    # diff = one_proc_time - multi_proc_time
    # print("time taken: %f" % (multi_proc_time))
    # print("")
    # print("mp is faster by %f seconds, or %f%%" % (diff, 100 * (diff / one_proc_time)))
