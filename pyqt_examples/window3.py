'''Simple window with some custom values, using setGeometry instead
   of two separate methods'''
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.setGeometry(100, 100, 300, 200)
w.setWindowTitle('Simple window')
w.show()

sys.exit(app.exec_())
