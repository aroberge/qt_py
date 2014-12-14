'''Simple message box'''
from PyQt4 import QtGui, QtCore

def message_box(message="Message", title="Title"):
    """Simple message box.
    """
    app = QtGui.QApplication([])
    box = QtGui.QMessageBox(None)
    box.setWindowTitle(title)
    box.setText(message)
    box.show()
    box.exec_()
    app.quit()


if __name__ == '__main__':
    message_box("Simple test")