
import board

from PyQt4 import QtGui


images = {}

for nb_mines in range(1, 9):
    images[nb_mines] = QtGui.QImage("images/number_{}.png".format(nb_mines))

for name in ["covered", "empty", "flag_mine", "flag_mine_wrong", "flag_suspect",
            "mine", "mine_wrong"]:
    images[name] = QtGui.QImage("images/{}.png".format(name))


class MyBoard(board.Board):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = QtGui.QColor(200, 0, 0)

    def draw(self, painter):
        '''Basic drawing method; usually overriden'''

        for tile in self.grid:
            col, row = tile
            painter.drawImage(col*self.tile_size, row*self.tile_size,
                images["covered"])


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
