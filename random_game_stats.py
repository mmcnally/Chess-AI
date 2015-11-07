from __future__ import division
import random_game

white_wins = 0
black_wins = 0

for i in range(10):
    winner = random_game.run_random_game_no_printing()
    if winner is random_game.WHITE:
        white_wins += 1
    else:
        black_wins += 1

print("white wins: %d" % white_wins)
print("black wins: %d" % black_wins)
print("white wins %f of matches" % (white_wins / (white_wins + black_wins)))
