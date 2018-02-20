# MNK Game
A connect K-in-a-row game on a M*N grid.

### Setup
With pip.
```
$ pip install git+https://github.com:BrandonCardoso/mnk_game.git
```

Without pip.
```
$ git clone https://github.com/BrandonCardoso/mnk_game.git
$ cd mnk_game
$ python setup.py install
```

### How to use
Here's an example of setting up a Tic-Tac-Toe game between 2 random players.
```
from mnk_game import MNK_Game, RandomPlayer

p1 = RandomPlayer()
p2 = RandomPlayer()
game = MNK_Game(grid_width=3, grid_height=3, win_chain_length=3, p1, p2)
game.play(draw_grid=True)
```
