'''Simple window with some custom values'''
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(300, 200)
w.move(100, 100)
w.setWindowTitle('Simple window')
w.show()

sys.exit(app.exec_())
