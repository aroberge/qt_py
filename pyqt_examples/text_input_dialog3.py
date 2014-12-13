'''Simple text input dialog'''
from PyQt4 import QtGui, QtCore

def text_input(question="Enter your response", default="", font=None):
    app = QtGui.QApplication([])
    if font is not None:
        try:
            family, size = font
            default_font = QtGui.QFont()
            default_font.setFamily(family)
            default_font.setPointSize(size)
            app.setFont(default_font)
        except:
            print("Can not set font. Expected font = (family:str, size:int).")
            print("Got font =", font)

    flags = QtCore.Qt.WindowFlags()
    flags |= QtCore.Qt.FramelessWindowHint

    text, ok = QtGui.QInputDialog.getText(None, '',
        question, QtGui.QLineEdit.Normal, default, flags)
    app.quit()
    if ok:
        return text
    else:
        return None  # I know, not needed since it is the default...

if __name__ == '__main__':
    answer = text_input(question="What is your name?")
    print(answer)
    answer = text_input(default="response")
    print(answer)
    answer = text_input(font=("Helvetica", 12))
    print(answer)
    answer = text_input(font="Helvetica")
    print(answer)
