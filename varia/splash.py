''' Small app: just a text splash screen '''

import sys

import PyQt4.QtCore as Core
import PyQt4.QtGui as Gui

def show_message(message):
    '''shows a message as a splash screen'''
    app = Gui.QApplication(sys.argv)
    label = Gui.QLabel( message)
    label.setStyleSheet("QWidget { font-size:100em }" )
    label.setWindowFlags(Core.Qt.SplashScreen)
    label.show()
    Core.QTimer.singleShot(10000, app.quit)
    app.exec_()

if __name__ == '__main__':
    show_message("Hello world!")
