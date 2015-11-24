import players
import chess
import game_tools
import sys

DEFAULT_DEPTH = 3

TRUE = 1
FALSE = 0


class Game(object):

    def __init__(self, player1, player2, depth):
        self.player1 = player1
        self.player2 = player2
        self.depth = depth
        self.board = chess.Board()


    def play_with_avg_moves(self):
        total_time_p1 = 0
        total_time_p2 = 0
        num_moves_p1 = 0
        num_moves_p2 = 0
        while not self.board.is_game_over():
            if self.is_white_turn():
                move, move_time = self.player1.calculate_move_timed(self.board, True, self.depth)
                total_time_p1 += move_time
                num_moves_p1 += 1
                self.board.push(move)
            else:
                move, move_time = self.player2.calculate_move_timed(self.board, False, self.depth)
                total_time_p1 += move_time
                num_moves_p2 += 1
                self.board.push(move)

        avg_move_time_p1 = total_time_p1 / num_moves_p1
        avg_move_time_p2 = total_time_p2 / num_moves_p2
        return game_tools.get_winner(self.board), avg_move_time_p1, avg_move_time_p2


    def play_no_printing(self):
        while not self.board.is_game_over():
            if self.is_white_turn():
                move = self.player1.calculate_move(self.board, True, self.depth)
                self.board.push(move)
            else:
                move = self.player2.calculate_move(self.board, False, self.depth)
                self.board.push(move)

        return game_tools.get_winner(self.board)


    def play(self):
        while not self.board.is_game_over():
            if self.is_white_turn():
                print("player 1, white's turn, %s" % self.player1)
                move = self.player1.calculate_move(self.board, True, self.depth)
                self.board.push(move)
            else:
                print("player 2, black's turn, %s" % self.player2)
                move = self.player2.calculate_move(self.board, False, self.depth)
                self.board.push(move)

            print(self.board)
            print("")
            print("")

        return game_tools.get_winner(self.board)


    def is_white_turn(self):
        return self.board.turn is game_tools.WHITE



def simulate_game(player1, player2, depth):
    game = Game(player1, player2, depth)
    winner = game.play()
    print("winner is %s!" % game_tools.player_str(winner))

def simulate_game_avg_move(player1, player2, depth):
    game = Game(player1, player2, depth)
    winner, avg_p1, avg_p2 = game.play_with_avg_moves()
    print("winner is %s!" % game_tools.player_str(winner))
    print("average time to calculate move for player 1: %f" % avg_p1)
    print("average time to calculate move for player 2: %f" % avg_p2)




def minimax_vs_random():
    player1 = players.Minimax_Player_Naive()
    player2 = players.Random_Player()
    simulate_game_avg_move(player1, player2, 2)

def create_player_from_str(s):
    if s == "minimax_naive":
        return players.Minimax_Player_Naive()
    if s == "minimax_advanced":
        return palyers.Minimax_Player_Advanced()
    elif s == "alpha_beta_naive":
        return players.Minimax_Alpha_Beta_Player_Naive()
    elif s == "alpha_beta_advanced":
        return players.Minimax_Alpha_Beta_Player_Advanced()
    elif s == "human":
        return players.Human_Player()
    elif s == "random":
        return players.Random_Player()
    else:
        print("you done messed up son :(")
        print("players should be 'minimax_naive', 'minimax_advanced, " +
              "'alpha_beta_naive', 'alpha-beta_advanced', 'human', or 'random', " +
              "each without single quotes\n")
        print("example call: python3 game_runner random minimax")

def get_stat_option(s):
    if s == "stats":
        return True
    elif s == "nostats":
        return False
    else:
        print("your stats/nostats argument was neither 'stats' nor 'nostats'\n" +
              "please fix and reconsider your life choices")




'''
usage: can take in 2 or 3 args to dynamically make game
  arg1 = player1 ['minimax_naive'|'minimax_advanced'|'alpha_beta_naive'|
                  'alpha_beta_advanced'|'random'|'human']
  arg2 = player2 ['minimax_naive'|'minimax_advanced'|'alpha_beta_naive'|
                  'alpha_beta_advanced'|'random'|'human']
  arg3 = option depth (default is DEFAULT_DEPTH)
  arg4 = option avg move times ["stats" | "nostats"] (default is nostats)

examples:
  python3 game_runner minimax_naive random
  python3 game_runner minimax_advanced random 2
  python3 game_runner random alpha_beta_naive 1
  python3 game_runner random alpha_beta_advanced 1 stats
'''
if __name__=='__main__':
    num_args = len(sys.argv)
    if num_args >= 3:
        p1 = create_player_from_str(sys.argv[1])
        p2 = create_player_from_str(sys.argv[2])
        depth = DEFAULT_DEPTH if num_args < 4 else int(sys.argv[3])
        stats = False if num_args < 5 else get_stat_option(sys.argv[4])

        print("player 1 is %s\n" % p1+
              "player 2 is %s" % p2)
        print("depth is %d" % depth)
        print("play with stats: %s" % stats)
        print("")
        if stats:
            simulate_game_avg_move(p1, p2, depth)
        else:
            simulate_game(p1, p2, depth)
    else:
        # default game to play
        minimax_vs_random()
