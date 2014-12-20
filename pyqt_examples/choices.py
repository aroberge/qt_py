import sys
from PyQt4 import QtGui


class MultipleChoicesDialog(QtGui.QMainWindow):
    """Dialog with the possibility of selecting one or more
       items from a list"""
    def __init__(self, choices=None, title="Title"):
        super().__init__()
        if choices is None:
            choices = ["Item %d"%i for i in range(10)]
        self.setWindowTitle(title)

        main_widget = QtGui.QWidget()
        main_layout = QtGui.QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.choices_widget = QtGui.QListWidget()
        self.choices_widget.setSelectionMode(
                                    QtGui.QAbstractItemView.ExtendedSelection)

        for choice in choices:
            item = QtGui.QListWidgetItem()
            item.setText(choice)
            self.choices_widget.addItem(item)

        main_layout.addWidget(self.choices_widget)

        Button_01 = QtGui.QPushButton("Print Current Items")
        Button_01.clicked.connect(self.printCurrentItems)
        main_layout.addWidget(Button_01)


    def printCurrentItems(self):
        for item in self.choices_widget.selectedItems():
            print("Current Items are : ", item.text())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog_1 = MultipleChoicesDialog()
    dialog_1.show()
    app.exec_()