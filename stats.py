import multiprocessing as mp
import time
import timeit
import queue
import players
import game_runner


NUM_PROCS = 4

def make_player_with_type(player_type):
    if player_type == 'minimax':
        return players.Minimax_Player()
    elif player_type == 'alpha_beta':
        return players.Minimax_Alpha_Beta_Player()
    elif player_type == 'random':
        return players.Random_Player()
    else:
        raise ValueError("player_type %s is not recognized" % player_type)



def avg_move_mp_runner(player_type, num_games=10, depth=2):
    chunksize = int(num_games / float(NUM_PROCS))
    out_queue = mp.Queue()
    procs = []
    for i in range(NUM_PROCS):
        games_to_play = chunksize
        if i == NUM_PROCS - 1:
            games_to_play = num_games - (chunksize * (NUM_PROCS - 1))
        print("process %d is about to run %d games" % (i, games_to_play))
        p = mp.Process(
            target=avg_move_calc_time,
            args=(player_type,
                  out_queue,
                  games_to_play,
                  depth))
        procs.append(p)
        p.start()


    total_avgs = 0
    for i in range(NUM_PROCS):
        total_avgs += out_queue.get()

    for p in procs:
        p.join()

    avg_of_avgs = total_avgs / num_games
    print("average of averages is %f" % avg_of_avgs)
    return avg_of_avgs

def avg_move_calc_time(player_type, out_queue=None, num_games=10, depth=2):
    minimax_total = 0
    # print("starting calculations")
    for i in range(num_games):
        player1 = make_player_with_type(player_type)
        player2 = players.Random_Player()
        game = game_runner.Game(player1, player2, depth)
        winner, avg_p1, avg_p2 = game.play_with_avg_moves()
        minimax_total += avg_p1
        print("finished game %d with avg minimax time %f" % (i, avg_p1))

    minimax_avg = minimax_total / num_games
    print("overall average %f" % minimax_avg)
    if out_queue != None:
        out_queue.put(minimax_avg)
        # print(out_queue.qsize())
        out_queue.close()


if __name__=='__main__':
    print("one process")
    t1 = timeit.default_timer()
    avg = avg_move_calc_time("alpha_beta", num_games=4)
    t2 = timeit.default_timer()
    print("time taken: %f" % (t2 - t1))
    print("")
    print("two processes")
    print("")
    t3 = timeit.default_timer()
    avg = avg_move_mp_runner("alpha_beta", num_games=4)
    t4 = timeit.default_timer()
    print("time taken: %f" % (t4 - t3))
