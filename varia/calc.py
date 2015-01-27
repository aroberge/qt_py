from math import *
import math

import PyQt4.QtCore as Core
import PyQt4.QtGui as Gui

class Calculatrice(Gui.QDialog):
    def __init__(self):
        super().__init__()

        self.entrees = Gui.QLineEdit()
        self.resultats = Gui.QTextBrowser()
        help = Gui.QTextBrowser()
        self.setWindowTitle("Calculatrice")

        layout = Gui.QVBoxLayout()
        layout.addWidget(self.entrees)
        layout.addWidget(self.resultats)
        layout.addWidget(help)
        display = ''
        for index, expr in enumerate(dir(math)):
            if not expr.startswith('_'):
                if (index + 1) % 3 == 0:
                    help.append(display)
                    display = expr + "\t"
                else:
                    display += expr + "\t"
        help.append(display)
        self.setLayout(layout)
        self.entrees.selectAll()
        self.entrees.setFocus()

        self.entrees.returnPressed.connect(self.evalue)


    def evalue(self):
        text = self.entrees.text()
        try:
            self.resultats.append('{0} = <b>{1}</b>'.format(text, eval(text)))
        except:
            self.resultats.append(
                "<font color=red>Expression non-valide:</font> {}".format(
                                                                         text))
        self.entrees.setText('')





if __name__ == '__main__':
    app = Gui.QApplication([])
    calc = Calculatrice()
    calc.show()
    app.exec_()