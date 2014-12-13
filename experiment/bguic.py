'''Basic Graphical User Interface Components

The font for all components can be change/set globally at any time using:

    >>> global_font.setFamily(family:str)
    >>> global_font.setPointSize(size:int)
'''
from PyQt4 import QtGui, QtCore

global_font = QtGui.QFont()


def _set_font(font, app):
    '''Private function to set font; called by individual components
       More restricted in what can be set than what the public dialog
       can do.
    '''
    if font is None:
        font = global_font.family(), global_font.pointSize()
    try:
        family, size = font
        current_font = QtGui.QFont()
        if family:
            current_font.setFamily(family)
        if size:
            current_font.setPointSize(size)
        app.setFont(current_font)
    except:
        print("Can not set font. Expected font = (family:str, size:int).")
        print("Got font =", font)

def set_global_font():
    '''GUI component to set default font'''
    global global_font
    app = QtGui.QApplication([])
    font, ok = QtGui.QFontDialog.getFont(global_font, None)
    app.quit()
    if ok:
        global_font = font


def text_input(message="Enter your response", default="", font=None):
    '''Simple frameless text input box.

       'font' is a tuple: (family:str, size:int).
      '''
    app = QtGui.QApplication([])
    _set_font(font, app)

    flags = QtCore.Qt.WindowFlags()
    flags |= QtCore.Qt.FramelessWindowHint

    text, ok = QtGui.QInputDialog.getText(None, '',
        message, QtGui.QLineEdit.Normal, default, flags)
    app.quit()
    if ok:
        return text


if __name__ == '__main__':
    try:
        import bguic_demo
    except ImportError:
        print("Could not find demo.")
