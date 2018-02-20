from re import split
from abc import ABCMeta, abstractmethod
from numpy import where, random

class Player():
    """An abstract player class for playing MNK games"""

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_move(self, grid):
        """Get location of the next move on the grid."""
        pass


class RealPlayer(Player):
    """A real player, with keyboard input."""

    def __init__(self):
        Player.__init__(self)

    def get_move(self, grid):
        """Gets move from player input."""
        return tuple(int(x) for x in split("[,\s]", raw_input("Your turn. Enter a location (ex. 0,1): ").strip()))


class RandomPlayer(Player):
    """A player that picks a position on the grid randomly."""

    def __init__(self):
        Player.__init__(self)

    def get_move(self, grid):
        """Randomly picks an open space on the grid."""
        x, y = where(grid == 0)
        i = random.randint(len(x))
        return (x[i], y[i])[::-1]
