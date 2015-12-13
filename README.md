# Chess-AI
### Final Project for CS 383

Chess playing program that uses minimax with alpha beta pruning and training from real game data to choose the best moves it can.

#### How to run from terminal:
##### Make sure you have Python 3.5 installed on your machine
```
$ python3 game_runner.py <player1> <player2> <optional depth>
```

#### Player Option:
- "minimax_naive" = minimax with naive eval function
- "minimax_advanced" = minimax with advanced eval function
- "alpha_beta_naive" = minimax with alpha-beta pruning and naive eval function
- "alpha_beta_advanced" = minimax with alpha-beta pruning and naive eval function
- "random" = chooses random moves
- "human" = asks for input from user for each move

#### Depth
Depth defaults to 2 but can be changed with optional third parameter to game_runner