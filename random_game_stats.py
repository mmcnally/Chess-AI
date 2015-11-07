from __future__ import division
import sys

import random_game


white_wins = 0
black_wins = 0
num_games = 10

# change num_games to command line arg if entered
if(len(sys.argv) is 2):
    num_games = int(sys.argv[1])

print(num_games)
for i in range(num_games):
    winner = random_game.run_random_game_no_printing()
    if winner is random_game.WHITE:
        white_wins += 1
    else:
        black_wins += 1

print("white wins: %d" % white_wins)
print("black wins: %d" % black_wins)
print("white wins %f of matches" % (white_wins / (white_wins + black_wins)))
