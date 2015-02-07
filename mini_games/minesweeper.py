
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

    def game_init(self, tile):
        if tile[0] is None:
            for tile_ in self.grid:
                self.grid[tile_] = Tile(images["covered"], None)
            return

    def draw(self, painter):
        '''Basic drawing method; usually overriden'''

        for tile in self.grid:
            col, row = tile
            painter.drawImage(col*self.tile_size, row*self.tile_size,
                self.grid[tile].image)


    def handle_mouse_pressed(self, button_clicked, tile):
        '''meant to be overriden'''
        if not self.game_started:
            self.game_init(tile)
        self.grid[tile].image = images["empty"]
        self.repaint()
        self.send_message("{} clicked at {}".format(button_clicked, tile))


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
