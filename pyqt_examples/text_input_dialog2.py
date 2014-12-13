'''Simple text input dialog'''
from PyQt4 import QtGui, QtCore

def text_input(question="Enter your response", default=""):
    app = QtGui.QApplication([])

    flags = QtCore.Qt.WindowFlags()
    flags |= QtCore.Qt.FramelessWindowHint

    text, ok = QtGui.QInputDialog.getText(None, '',
        question, QtGui.QLineEdit.Normal, default, flags)
    app.quit()
    if ok and text:
        return text

if __name__ == '__main__':
    answer = text_input(question="What is your name?")
    print(answer)
