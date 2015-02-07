
import random

from PyQt4 import QtGui

import board

class Tile:
    def __init__(self, image=None, value=None):
        self.image = image
        self.value = value


images = {}

for nb_mines in range(1, 9):
    images[nb_mines] = QtGui.QImage("images/number_{}.png".format(nb_mines))

for name in ["covered", "empty", "flag_mine", "flag_mine_wrong", "flag_suspect",
            "mine", "mine_wrong"]:
    images[name] = QtGui.QImage("images/{}.png".format(name))


class MyBoard(board.Board):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_started = False
        self.game_init((None, None))
        self.nb_mines = 10

    def game_init(self, tile):
        if tile == (None, None):
            for tile_ in self.grid:
                self.grid[tile_] = Tile(images["covered"], None)
            return
        mines = 0
        while mines < self.nb_mines:
            x = random.randint(0, self.nb_cols-1)
            y = random.randint(0, self.nb_rows-1)
            if (x, y) == tile:  # do not put a bomb at location of first click
                continue
            if self.grid[(x, y)].value is None:
                self.grid[(x, y)].value = "mine"
                mines += 1
        for tile_ in self.grid:
            if self.grid[tile_].value != "mine":
                self.count_mine_neighbours(tile_)
        self.game_started = True

    def count_mine_neighbours(self, tile):
        mines = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i==j and i== 0:
                    continue
                neighbour = (tile[0]+i, tile[1]+j)
                if neighbour in self.grid:
                    if self.grid[neighbour].value == "mine":
                        mines += 1
        if mines != 0:
            self.grid[tile].value = mines

    def draw(self, painter):
        '''Basic drawing method; usually overriden'''

        for tile in self.grid:
            col, row = tile
            painter.drawImage(col*self.tile_size, row*self.tile_size,
                self.grid[tile].image)

    def handle_mouse_pressed(self, button_clicked, tile):
        '''meant to be overriden'''
        message = "{} clicked at {}".format(button_clicked, tile)
        if not self.game_started:
            self.game_init(tile)
        if self.grid[tile].value is None:
            self.open_empty_region(tile)
            #self.grid[tile].image = images["empty"]
        else:
            self.grid[tile].image = images[self.grid[tile].value]

        self.repaint()
        self.send_message(message)

    def open_empty_region(self, tile):
        if tile not in self.grid:
            return
        if self.grid[tile].value is not None:
            self.grid[tile].image = images[self.grid[tile].value]
            return

        if self.grid[tile].image == images["empty"]:
            return
        self.grid[tile].image = images["empty"]
        x, y = tile
        self.open_empty_region((x-1, y))
        self.open_empty_region((x+1, y))
        self.open_empty_region((x, y-1))
        self.open_empty_region((x, y+1))


class TestGame(QtGui.QMainWindow):
    '''Non real game set up to try various functions/methods
       that can be used in games'''

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Test Game")
        self.statusbar = self.statusBar()
        self.board = MyBoard(self, tile_size=24)
        self.setCentralWidget(self.board)
        self.resize(self.board.width, self.board.height)
        self.setFixedSize(self.board.width,
                          self.board.height+self.statusbar.height())
        self.show()

    def receive_message(self, message):
        self.statusbar.showMessage(message)


def main():

    app = QtGui.QApplication([])
    game = TestGame()
    app.exec_()

if __name__ == '__main__':
    main()
