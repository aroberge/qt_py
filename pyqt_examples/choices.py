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


#        button_box = QtGui.QGroupBox(name)
        button_box_layout = QtGui.QGridLayout()

        return_choices_btn = QtGui.QPushButton("Ok")
        return_choices_btn.clicked.connect(self.return_choices)
        select_all_btn = QtGui.QPushButton("Select all")
        select_all_btn.clicked.connect(self.select_all)
        clear_all_btn = QtGui.QPushButton("Clear all")
        clear_all_btn.clicked.connect(self.clear_all)


        button_box = QtGui.QWidget()
        button_box_layout.addWidget(select_all_btn, 0, 0)
        button_box_layout.addWidget(clear_all_btn, 1, 0)
        button_box_layout.addWidget(return_choices_btn, 1, 1)
        button_box.setLayout(button_box_layout)

        main_layout.addWidget(button_box)


        # todo: add buttons Ok, Cancel, Select all, Clear

    def return_choices(self):
        print([item.text() for item in self.choices_widget.selectedItems()])

    def select_all(self):
        self.choices_widget.selectAll()

    def clear_all(self):
        self.choices_widget.clearSelection()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog_1 = MultipleChoicesDialog()
    dialog_1.show()
    app.exec_()