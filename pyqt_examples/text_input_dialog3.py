'''Simple text input dialog'''
from PyQt4 import QtGui, QtCore

def text_input(message="Enter your response", default="", font=None):
    app = QtGui.QApplication([])
    if font is not None:
        try:
            family, size = font
            default_font = QtGui.QFont()
            if family:
                default_font.setFamily(family)
            if size:
                default_font.setPointSize(size)
            app.setFont(default_font)
        except:
            print("Can not set font. Expected font = (family:str, size:int).")
            print("Got font =", font)

    flags = QtCore.Qt.WindowFlags()
    flags |= QtCore.Qt.FramelessWindowHint

    text, ok = QtGui.QInputDialog.getText(None, '',
        message, QtGui.QLineEdit.Normal, default, flags)
    app.quit()
    if ok:
        return text
    else:
        return None  # I know, not needed since it is the default...

if __name__ == '__main__':
    answer = text_input(message="What is your name?")
    print(answer)
    answer = text_input(default="response")
    print(answer)
    answer = text_input(message="Test set font", font=("Times", 12))
    print(answer)
    answer = text_input(message="Test set font size only", font=("", 12))
    print(answer)
    answer = text_input(message="Test set font family only", font=("Courier", 0))
    print(answer)
    answer = text_input(message="Intentional font error", font="Helvetica")
    print(answer)