'''Logic for minesweeper board'''

import random

# While we try to separate the model from the view, we have to
# use a consistent naming convention between the two.
# Cells/tiles can have mines, hidden (covered) or not, they can
# be flagged by the player as hiding mines, etc.
# The following names are chosen to be similar to those of
# the relevant images - just for convenience.

CELL_VALUES = ["covered", "empty", "flag_mine", "flag_mine_wrong",
               "flag_suspect", "mine", "mine_wrong"]


class Tile:
    '''A tile hides a cell of a given value, and has a certain
       appearance which can change as the game evolves'''
    def __init__(self):
        self.appear = None
        self.value = None


class Board:
    '''A Board is a collection of tiles/cells arranged in a rectangular grid'''
    def __init__(self, parent=None, nb_cols=10, nb_rows=10, nb_mines=10):
        self.parent = parent
        self.resize(nb_cols, nb_rows)
        self.new_game(nb_mines=nb_mines)

    def set_size(self, nb_cols, nb_rows):
        '''sets the size and create a corresponding rectangular grid'''
        self.nb_cols = nb_cols
        self.nb_rows = nb_rows
        self.create_empty_grid()

    def create_empty_grid(self):
        '''creates a grid as a dict with (row, col) as keys
           and empty Tile as values'''
        self.grid = {}
        for row in range(self.nb_rows):
            for col in range(self.nb_cols):
                self.grid[(col, row)] = Tile()

    def prepare_for_new_game(self, nb_mines=10):
        '''Prepare for new game by setting the number of mines and
           various flag.  However, does not actually position the
           mines.'''
        self.nb_mines = nb_mines
        self.flags = 0
        self.game_over = False
        self.game_won = False
        self.game_started = False

    def start_new_game(self, cell):
        '''starts a new game after a player has chosen a given grid location
           for the first action'''
        self.position_mines(cell)
        for cell_ in self.grid:
            if self.grid[cell_].value != "mine":
                self.count_mine_neighbours(cell_)
        self.game_started = True

    def position_mines(self, cell):
        '''Puts the required number of mines on the board.
           This is not done until the player has chosen a first grid location
           (cell/tile) to ensure that the first guess is not where a mine
           is located - thus avoiding an immediate game loss'''
        mines = 0
        while mines < self.nb_mines:
            x = random.randint(0, self.nb_cols-1)
            y = random.randint(0, self.nb_rows-1)
            if (x, y) == cell:  # do not put a bomb at location of first click
                continue
            if self.grid[(x, y)].value is None:
                self.grid[(x, y)].value = "mine"
                mines += 1

    def count_mine_neighbours(self, cell):
        '''Counts the number of mines that are immediate neighbour to a
           given cell and sets the value of the value of the cell to
           this number of mine if it is greater than zero'''
        mines = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i==j and i== 0:
                    continue
                neighbour = (cell[0]+i, cell[1]+j)
                if neighbour in self.grid:
                    if self.grid[neighbour].value == "mine":
                        mines += 1
        if mines != 0:
            self.grid[cell].value = mines

    def reveal_tile(self, tile):
        '''reveals what is hidden under a tile clicked by the player'''
        # We don't position the mines until the player selects a first
        # tile/cell to avoid having the player lose the game on the first
        # click
        if not self.game_started:
            self.start_new_game(tile)

        if self.grid[tile].value is None:
            self.reveal_empty_region(tile)
        else:
            self.grid[tile].appear = self.grid[tile].value
            if self.grid[tile].value == "mine":
                self.grid[tile].appear = "mine_wrong"
                self.game_over = True
            elif self.grid[tile].appear == "flag_mine":
                self.flags -= 1

    def reveal_empty_region(self, tile):
        '''recursive function used to open up an empty region surrounding
           a given empty cell'''
        # recursive calls can reach outside the grid
        if tile not in self.grid:
            return

        # reveal only one non-empty cell in a given direction
        if self.grid[tile].value is not None:
            self.grid[tile].appear = self.grid[tile].value
            return

        # avoid backtracking and creating infinite recursion
        if self.grid[tile].appear == "empty":
            return

        # value is None, cell should appear empty
        self.grid[tile].appear = "empty"

        # process surrounding tiles recursively
        x, y = tile
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                self.reveal_empty_region((x+i, y+j))

    def mark_tile(self, tile):
        '''puts or remove a flag on a given tile'''

        if self.grid[tile].appear == "covered":
            self.grid[tile].appear = "flag_mine"
            self.marked_mines += 1
            if self.marked_mines == self.nb_mines:
                self.confirm_all_flags()
        elif self.grid[tile].appear == "flag_mine":
            self.grid[tile].appear = "flag_suspect"
            self.marked_mines -= 1
        elif self.grid[tile].appear == "flag_suspect":
            self.grid[tile].appear = "covered"
        else:
            pass

    def confirm_all_flags(self):
        '''confirm that all flags have been set correctly.
           This should only be called if the number of flags set is
           equal to the number of mines'''
        # Note: alternative game play could use a different condition
        # for example, one could not allow the user to use flags and simply
        # verify that all hidden tiles hide a mine.
        assert self.flags == self.nb_mines
        self.game_over = True
        for tile in self.grid:
            if self.grid[tile].value == "mine":
                if self.grid[tile].appear != "flag_mine":
                    return
        self.game_won = True

    def show_mistakes(self):
        '''sets the board "appearance" to the correct value, pointing
        out errors in player selection'''
        for tile in self.grid:
            cell = self.grid[tile]
            if cell.value == "mine":
                if cell.appear == "covered":
                    cell.appear = "mine"
            elif cell.appear in ["flag_mine", "flag_suspect"]:
                    cell.appear = "flag_mine_wrong"


CELL_VALUES = ["covered", "empty", "flag_mine", "flag_mine_wrong",
               "flag_suspect", "mine", "mine_wrong"]