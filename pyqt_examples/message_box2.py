'''Simple message box with icon'''
from PyQt4 import QtGui, QtCore

def message_box(message="Message", title="Title", icon=None):
    """Simple message box.
    """
    app = QtGui.QApplication([])
    box = QtGui.QMessageBox(None)
    if icon is not None:
        box.setWindowIcon(QtGui.QIcon(icon))
    else:
        box.setWindowIcon(QtGui.QIcon("images/reeborg.png"))
    box.setWindowTitle(title)
    box.setText(message)
    box.show()
    box.exec_()
    app.quit()


if __name__ == '__main__':
    message_box("Simple test")
    message_box(icon="images/python.jpg")