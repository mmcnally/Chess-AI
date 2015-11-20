import players
import chess
import game_tools
import sys

DEFAULT_DEPTH = 3


class Game(object):

    def __init__(self, player1, player2, depth):
        self.player1 = player1
        self.player2 = player2
        self.depth = depth
        self.board = chess.Board()

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

def minimax_vs_random():
    player1 = players.Minimax_Player()
    player2 = players.Random_Player()
    simulate_game(player1, player2, DEFAULT_DEPTH)

def random_vs_random():
    player1 = players.Random_Player()
    player2 = players.Random_Player()
    simulate_game(player1, player2, DEFAULT_DEPTH)

def minimax_vs_minimax():
    player1 = players.Minimax_Player()
    player2 = players.Minimax_Player()
    simulate_game(player1, player2, DEFAULT_DEPTH)

def minimax_vs_alpha_beta():
    player1 = players.Minimax_Player()
    player2 = players.Minimax_Alpha_Beta_Player()
    simulate_game(player1, player2, DEFAULT_DEPTH)

def create_player_from_str(s):
    if s == "minimax":
        return players.Minimax_Player()
    elif s == "alpha_beta" or s == "minimax_alpha_beta":
        return players.Minimax_Alpha_Beta_Player()
    elif s == "alpha_beta_2" or s == "minimax_alpha_beta_2":
        return players.Minimax_Alpha_Beta_Player_2()
    elif s == "random":
        return players.Random_Player()
    else:
        print("you done messed up son :(")
        print("players should be 'minimax', 'alpha_beta', or 'random', " +
              "each without single quotes\n")
        print("example call: python3 game_runner random minimax")


'''
usage: can take in 2 or 3 args to dynamically make game
  arg1 = player1 algorithm ["minimax" | "alpha_beta" | "random"]
  arg2 = player2 algorithm ["minimax" | "alpha_beta" | "random"]
  arg3 = option depth (default is DEFAULT_DEPTH)

examples:
  python3 game_runner minimax random
  python3 game_runner minimax random 2
  python3 game_runner random alpha_beta 1
'''
if __name__=='__main__':
    if len(sys.argv) is 3:
        # two players and default depth
        p1 = create_player_from_str(sys.argv[1])
        p2 = create_player_from_str(sys.argv[2])
        print("player 1 is %s\n" % p1+
              "player 2 is %s" % p2)
        print("")
        simulate_game(p1, p2, DEFAULT_DEPTH)
        print(DEFAULT_DEPTH)
    elif len(sys.argv) is 4:
        # two players and depth
        p1 = create_player_from_str(sys.argv[1])
        p2 = create_player_from_str(sys.argv[2])
        depth = int(sys.argv[3])
        simulate_game(p1, p2, depth)
    else:
        # default game to play
        minimax_vs_random()
