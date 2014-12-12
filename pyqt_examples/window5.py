'''Simple window - with icon.'''
import sys
from PyQt4 import QtGui

class SimpleWindow(QtGui.QWidget):
    def __init__(self, title=None, position=None, size=None, icon=None):
        super().__init__()

        if title is None:
            title = "Simple Window"
        self.setWindowTitle(title)

        if position is not None:
            self.move(*position)

        if size is not None:
            self.resize(*size)

        if icon is not None:
            self.setWindowIcon(QtGui.QIcon(icon))
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = SimpleWindow()
    window2 = SimpleWindow(title="Other window", size=(400, 200),
                           position=(10, 10), icon="images/python.jpg")
    sys.exit(app.exec_())
