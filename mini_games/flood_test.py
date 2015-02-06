

from PyQt4 import QtCore
from PyQt4 import QtGui

import board


class ExperimentalBoard(board.Board):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = QtGui.QColor(200, 0, 0)

    def draw(self, painter):
        '''Basic drawing method; usually overriden'''
        painter.setBrush(QtGui.QColor(200, 200, 200))
        painter.drawRect(0, 0, self.width, self.height)

        painter.setPen(QtGui.QColor(155, 155, 155))
        for row in range(self.nb_rows + 1):
            y = row * self.tile_size
            painter.drawLine(0, y, self.width, y)

        for col in range(self.nb_cols + 1):
            x = col * self.tile_size
            painter.drawLine(x, 0, x, self.height)

        self.draw_tiles(painter)

    def draw_tiles(self, painter):
        for tile in self.grid:
            if self.grid[tile] is not None:
                col, row = tile
                x = col * self.tile_size
                y = row * self.tile_size
                painter.setBrush(self.grid[tile])
                painter.drawRect(x, y, self.tile_size, self.tile_size)

    def handle_mouse_pressed(self, button_clicked, col, row):
        '''meant to be overriden'''
        if button_clicked == "left":
            self.grid[(col, row)] = self.color
            self.repaint()
        else:
            old_color = self.grid[(col, row)]
            self.flood_fill(col, row, old_color, self.color)
            self.repaint()

    def flood_fill(self, x, y, old_color, new_color):
        if (x, y) not in self.grid:
            return
        if self.grid[(x, y)] != old_color:
            return
        self.grid[(x, y)] = new_color

        self.flood_fill(x + 1, y, old_color, new_color)
        self.flood_fill(x - 1, y, old_color, new_color)
        self.flood_fill(x, y + 1, old_color, new_color)
        self.flood_fill(x, y - 1, old_color, new_color)


class FloodTest(QtGui.QMainWindow):
    '''Non real game set up to try various functions/methods
       that can be used in games'''

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Test Game")
        self.statusbar = self.statusBar()
        self.board = ExperimentalBoard(self, 10, 10)
        self.setCentralWidget(self.board)
        self.resize(self.board.width, self.board.height)
        self.setFixedSize(self.board.width,
                          self.board.height+self.statusbar.height())
        self.show()

    def receive_message(self, message):
        self.statusbar.showMessage(message)

    def keyPressEvent(self, event):  # noqa
        if event.key() == QtCore.Qt.Key_B:
            self.board.color = QtGui.QColor(0, 0, 200)
        elif event.key() == QtCore.Qt.Key_R:
            self.board.color = QtGui.QColor(200, 0, 0)
        elif event.key() == QtCore.Qt.Key_G:
            self.board.color = QtGui.QColor(0, 200, 0)
        elif event.key() == QtCore.Qt.Key_F:
            self.showFullScreen()
            print(self.width(), self.height())
        elif event.key() == QtCore.Qt.Key_Escape:
            self.resize(self.board.width, self.board.height)
            self.show()


def main():

    app = QtGui.QApplication([])
    FloodTest()
    app.exec_()


if __name__ == '__main__':
    main()
