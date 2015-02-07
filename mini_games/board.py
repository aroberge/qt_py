'''Simple board'''

from PyQt4 import QtCore
from PyQt4 import QtGui


class Board(QtGui.QWidget):

    def __init__(self, parent, nb_cols=10, nb_rows=10, tile_size=32):
        super().__init__()

        self.parent = parent
        self.nb_cols = nb_cols
        self.nb_rows = nb_rows
        self.create_empty_grid()
        self.tile_size = tile_size
        self.width = self.tile_size * self.nb_cols
        self.height = self.tile_size * self.nb_rows

    def create_empty_grid(self):
        '''creates a grid as a dict with (row, col) as keys
           and None as values'''
        self.grid = {}
        for row in range(self.nb_rows):
            for col in range(self.nb_cols):
                self.grid[(col, row)] = None

    def paintEvent(self, event):  # noqa
        '''Overriden QWidget method'''
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def mousePressEvent(self, event):  # noqa
        '''Overriden QWidget method'''
        tile = self.which_tile_clicked(event)
        if event.button() == QtCore.Qt.RightButton:
            self.handle_right_click(tile)
        elif event.button() == QtCore.Qt.LeftButton:
            self.handle_left_click(tile)

    def handle_right_click(self, tile):
        '''meant to be overriden'''
        self.send_message("{} clicked at {}".format("right", tile))

    def handle_left_click(self, tile):
        '''meant to be overriden'''
        self.send_message("{} clicked at {}".format("left", tile))

    def which_tile_clicked(self, event):
        '''Determine which row and col mouse click occurred'''
        x = event.x()
        y = event.y()
        col = x // self.tile_size
        row = y // self.tile_size
        return col, row

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

    def send_message(self, message):
        '''sends a message to the parent'''
        self.parent.receive_message(message)


class TestGame(QtGui.QMainWindow):
    '''Non real game set up to try various functions/methods
       that can be used in games'''

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Test Game")
        self.statusbar = self.statusBar()
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.resize(self.board.width, self.board.height)
        self.setFixedSize(self.board.width,
                          self.board.height+self.statusbar.height())
        self.show()

    def receive_message(self, message):
        self.statusbar.showMessage(message)


def main():

    app = QtGui.QApplication([])
    TestGame()
    app.exec_()


if __name__ == '__main__':
    main()
