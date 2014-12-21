import sys
from PyQt4 import QtGui, QtCore


class MultipleChoicesDialog(QtGui.QDialog):
    """Dialog with the possibility of selecting one or more
       items from a list"""
    def __init__(self, choices=None, title="Title"):
        super().__init__(None, QtCore.Qt.WindowSystemMenuHint |
                         QtCore.Qt.WindowTitleHint)
        if choices is None:
            choices = ["Item %d"%i for i in range(10)]
        self.setWindowTitle(title)

        main_widget = QtGui.QWidget()
        main_layout = QtGui.QVBoxLayout()
        main_widget.setLayout(main_layout)
        #self.setCentralWidget(main_widget)

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
        self.setLayout(main_layout)
        self.show()


        # todo: add buttons Ok, Cancel, Select all, Clear

    def return_choices(self):
        self.selection = [item.text() for item in
                          self.choices_widget.selectedItems()]
        self.close()

    def select_all(self):
        self.choices_widget.selectAll()

    def clear_all(self):
        self.choices_widget.clearSelection()

    def get_values(self):
        return self.selection


if __name__ == '__main__':

    def get_selection():
        app = QtGui.QApplication([])
        a = MultipleChoicesDialog()
        app.exec_()
        return a.get_values()

    b = get_selection()
    print(b)
