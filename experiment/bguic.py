'''Basic Graphical User Interface Components
'''
import os
from PyQt4 import QtGui, QtCore

_FONT = QtGui.QFont()
_TRANSLATOR = QtCore.QTranslator()
_LOCALE = 'en'

LOCALES = {}

for root, dirs, files in os.walk(os.path.join(QtGui.__file__, "..")):
    for fname in files:
        if fname.endswith('.qm') and fname.startswith("qt_"):
            LOCALES[fname[3:-3]] = root

class SimpleApp(QtGui.QApplication):
    def __init__(self, locale=None, font=None):
        super().__init__([])
        self.set_font(font)
        self.set_locale(locale)

    def set_locale(self, locale):
        global _LOCALE
        if locale is not None and locale in LOCALES:
            if _TRANSLATOR.load("qt_"+locale, LOCALES[locale]):
                self.installTranslator(_TRANSLATOR)
                _LOCALE = locale
            else:
                print("language not available")
        elif _LOCALE in LOCALES:
            if _TRANSLATOR.load("qt_"+_LOCALE, LOCALES[_LOCALE]):
                self.installTranslator(_TRANSLATOR)

    def set_font(self, font):
        '''Simple method to set font; called by individual GUI components.
           More restricted in what can be set than what the public dialog
           can do.
        '''
        if font is None:
            font = _FONT.family(), _FONT.pointSize()
        try:
            family, size = font
            if family:
                _FONT.setFamily(family)
            if size:
                _FONT.setPointSize(size)
            self.setFont(_FONT)
        except:
            print("Can not set font. Expected font = (family:str, size:int).")
            print("Got font =", font)


def set_global_font(font=None, locale=None):
    '''GUI component to set default font'''
    global _FONT
    app = SimpleApp(font=font, locale=locale)
    font, ok = QtGui.QFontDialog.getFont(_FONT, None)
    app.quit()
    if ok:
        _FONT = font


def text_input(message="Enter your response", default="", font=None, locale=None):
    '''Simple frameless text input box.

       'font' is a tuple: (family:str, size:int).
      '''
    app = SimpleApp(font=font, locale=locale)

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
