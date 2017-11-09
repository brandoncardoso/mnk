import numpy as np

class MNK_Game():
    """A connect k-in-a-row game on an m*n grid."""

    def __init__(self, grid_width, grid_height, win_chain_length, player1, player2, symbols={1:'x', 2:'o'}):
        self.width = grid_width
        self.height = grid_height
        self.grid = np.zeros(shape=(self.width, self.height), dtype=np.int8)
        self.win_chain_length = win_chain_length
        self.turn = 1
        self.winner_found = False
        self.tie_game = False
        self.players = [player1, player2]
        self.player_symbols = symbols


    def grid_full(self):
        """Check if the game grid is full."""
        return np.all(self.grid)


    def try_move(self, location):
        """Try placing move at location on grid."""

        if len(location) is not 2:
            raise ValueError("Bad location. Try something like '0,1' or '2 2'.")
        elif not (location[0] >= 0 and location[0] < self.width and
                location[1] >= 0 and location[1] < self.height):
            raise ValueError('Bad location. Try to stay on the grid.')
        elif self.grid[location] != 0:
            raise ValueError('Bad location. That spot is already taken. Try again.')
        else:
            self.grid[location] = self.turn


    def draw(self):
        """Print the grid to console 'nicely'."""
        print # new line
        print '  ', '   '.join(str(x) for x in range(len(self.grid))) # x labels
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print ('|' if j > 0 else '{0} '.format(i)), # filler or vertical edge between cells
                if self.grid[i, j] == 0:
                    print ' ', # empty space
                elif self.grid[i, j] in self.player_symbols:
                    print self.player_symbols[self.grid[i, j]], # replace the turn number with the player symbol
                else:
                    print self.grid[i, j], # if we don't have a symbol for some reason, just draw the turn number
            print # new line
            if i < self.height - 1:
                print ' ', '---+' * (len(self.grid) - 1) + '---' # between rows
        print # new line


    def check_for_win(self, location):
        win = np.full(shape=(1, self.win_chain_length), fill_value=self.turn, dtype=np.int8)[0]

        axes = [self.grid[:,location[1]], # relevant column
                self.grid[location[0],:], # relevant row
                self.grid.diagonal(location[1] - location[0]), # relevant diagonal 1 (\)
                np.fliplr(self.grid).diagonal(self.width - location[0] - location [1] - 1)] #relevant diagonal 2 (/)

        for axis in axes:
            for i in range(axis.size - self.win_chain_length + 1):
                if np.array_equal(axis[i:i+self.win_chain_length], win):
                    return True

        return False # no win chains found


    def play(self, draw_grid=False):
        """Play the game until there is a winner or the board is full."""
        while not self.winner_found and not self.tie_game:
            try:
                location = self.players[turn - 1].get_move(self.grid) # provide the player with the grid, and get their move
                location = location[::-1] # reverse location. (y, x) -> (x, y). numpy does things backwarsd
                self.try_move(location)

                if (draw_grid):
                    self.draw()

                if self.check_for_win(location): # check if player won
                    self.winner_found = True
                elif self.grid_full(): # check if grid is full
                    self.tie_game = True
                else: # next turn
                    self.turn = 2 if self.turn == 1 else 1

            except ValueError as e:
                print e, '\n'
