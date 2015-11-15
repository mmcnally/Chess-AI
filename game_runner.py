import players
import chess
import game_tools

class Game(object):

    def __init__(self, player1, player2, depth):
        self.player1 = player1
        self.player2 = player2
        self.depth = depth
        self.board = chess.Board()

    def run(self):
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


        return game_tools.get_winner(board)


    def is_white_turn(self):
        return self.board.turn is game_tools.WHITE




def mini_vs_rand():
    player1 = players.Minimax_Player()
    player2 = players.Random_Player()
    game = Game(player1, player2, 3)
    winner = game.run()
    print("winner is %s!" % game_tools.player_str(winner))

if __name__=='__main__':
    mini_vs_rand()
