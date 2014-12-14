# pylint: disable=C0330
"""Basic Graphical User Interface Components
"""
import os
from collections import OrderedDict
from PyQt4 import QtGui, QtCore

CONFIG = {}
CONFIG['font'] = QtGui.QFont()
CONFIG['translator'] = QtCore.QTranslator()
CONFIG['locale'] = 'default'


def find_qm_files():
    """looking for files with names == qt_locale.qm"""
    all_files = OrderedDict()
    for root, _, files in os.walk(os.path.join(QtGui.__file__, "..")):
        for fname in files:
            if (fname.endswith('.qm') and fname.startswith("qt_")
                    and not fname.startswith("qt_help")):
                locale = fname[3:-3]
                all_files[locale] = root
    return all_files
QM_FILES = find_qm_files()


class SimpleApp(QtGui.QApplication):
    """A simple extention of the basic QApplication
       with added methods useful for working with dialogs
       that are not class based.
      """
    def __init__(self, locale=None, font_size=None):
        super().__init__([])
        if font_size is not None:
            self.set_font_size(font_size)
        self.setFont(CONFIG['font'])
        self.set_locale(locale)

    def set_locale(self, locale):
        """Sets the language of the basic controls for PyQt
           from a locale - provided that the corresponding qm files
           are present in the PyQt distribution.
        """
        if locale in QM_FILES:
            if CONFIG['translator'].load("qt_"+locale, QM_FILES[locale]):
                self.installTranslator(CONFIG['translator'])
                CONFIG['locale'] = locale
            else:
                print("language not available")
        elif locale is "default" and CONFIG['locale'] != 'default':
            self.removeTranslator(CONFIG['translator'])
            CONFIG['translator'] = QtCore.QTranslator()
            CONFIG['locale'] = 'default'
        elif CONFIG['locale'] in QM_FILES:
            if CONFIG['translator'].load("qt_"+CONFIG['locale'],
                                         QM_FILES[CONFIG['locale']]):
                self.installTranslator(CONFIG['translator'])

    @staticmethod
    def set_font_size(font_size):
        """Simple method to set font size; also called by individual GUI
           components.
        """
        try:
            CONFIG['font'].setPointSize(font_size)
        except TypeError:
            print("font_size must be an integer")

    @staticmethod
    def show_text_input(message="message", title="title",
                        default_response=""):
        """Obtain a response as a string from a user following a query.
           In many ways, this is meant as a GUI replacement for
           Python's input().
        """
        flags = QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
        text, ok = QtGui.QInputDialog.getText(None, title, message,
                               QtGui.QLineEdit.Normal, default_response, flags)
        if ok:
            return text

    @staticmethod
    def show_yes_no_question(question="question", title="title"):
        """Obtain a response as "yes" (returns True), "no" (returns False)
           or "cancel" (returns None).
        """
        reply = QtGui.QMessageBox.question(None, title, question,
                        QtGui.QMessageBox.Yes
                        | QtGui.QMessageBox.No
                        | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            return True
        elif reply == QtGui.QMessageBox.No:
            return False
        else:
            return None

    def show_select_language(self, title="Select language",
                             name="Language codes",
                             instruction="Click button when you are done"):
        """Calls a special dialog showing locale for language (qm) files
        that were found so that the language of the UI can be set.
        """
        selector = _LanguageSelector(self, title=title, name=name,
                                     instruction=instruction)
        selector.exec_()


class _LanguageSelector(QtGui.QDialog):
    """A specially constructed dialog which uses informations about
       available language (qm) files which can be used to change the
       default language of the basic PyQt ui components.
    """
    def __init__(self, parent, title="Language selection",
                 name="Language codes",
                 instruction="Click button when you are done"):
        super().__init__(None, QtCore.Qt.WindowSystemMenuHint |
                               QtCore.Qt.WindowTitleHint)

        self.qm_files_choices = {}
        self.parent = parent

        group_box = QtGui.QGroupBox(name)
        group_box_layout = QtGui.QGridLayout()

        for i, locale in enumerate(QM_FILES):
            check_box = QtGui.QCheckBox(locale)
            check_box.setAutoExclusive(True)
            self.qm_files_choices[check_box] = locale
            check_box.toggled.connect(self.check_box_toggled)
            group_box_layout.addWidget(check_box, i / 4, i % 4)

        # adding default language option. When using the PyQt distribution
        # no "en" files were found and yet "en" was the obvious default.
        # We need this option in case we want to revert a change.
        check_box = QtGui.QCheckBox("Default")
        check_box.setAutoExclusive(True)
        self.qm_files_choices[check_box] = "default"
        check_box.toggled.connect(self.check_box_toggled)
        i = len(QM_FILES)
        group_box_layout.addWidget(check_box, i / 4, i % 4)

        group_box.setLayout(group_box_layout)

        button_box = QtGui.QDialogButtonBox()

        confirm_button = button_box.addButton(QtGui.QDialogButtonBox.Ok)
        confirm_button.clicked.connect(self.confirm)

        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(group_box)
        main_layout.addWidget(QtGui.QLabel(instruction))
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)
        self.setWindowTitle(title)

    def check_box_toggled(self):
        """Callback when a checkbox is toggled"""
        self.locale = self.qm_files_choices[self.sender()]

    def confirm(self):
        """Callback from confirm_button used to set the locale"""
        self.parent.set_locale(self.locale)
        self.close()


def set_global_font(app=None, locale=None):
    """GUI component to set default font"""
    if app is None:
        app_quit = True
        app = SimpleApp(locale=locale)
    else:
        app_quit = False
    font, ok = QtGui.QFontDialog.getFont(CONFIG['font'], None)
    if app_quit:
        app.quit()
    if ok:
        CONFIG['font'] = font


def text_input(message="Enter your response", title="Title",
               default_response="",
               font_size: int=None,
               locale: "most often two letter code such as 'fr'"=None):
    """Simple text input box.  Used to query the user and get a string back.
    """
    app = SimpleApp(font_size=font_size, locale=locale)
    response = app.show_text_input(message=message, title=title,
                                   default_response=default_response)
    app.quit()
    return response


def yes_no_question(question="Answer this question", title="Title",
                    font_size=None, locale=None):
    """Simple yes or no question
      """

    app = SimpleApp(font_size=font_size, locale=locale)
    answer = app.show_yes_no_question(question=question, title=title)
    app.quit()
    return answer


def select_language(title="Select language", name="Language codes",
                 instruction="Click button when you are done"):
    """Dialog to choose language based on some locale code for
       files found on default path"""
    app = SimpleApp()
    app.show_select_language(title=title, name=name, instruction=instruction)
    app.quit()

def message_box(message="Message", title="Title", font_size=None, locale=None):
    """Simple message box.
    """
    app = SimpleApp(font_size=font_size, locale=locale)
    box = QtGui.QMessageBox(None)
    box.setWindowTitle(title)
    box.setText(message)
    box.show()
    box.exec_()
    app.quit()


def integer_input(message="Choose a number", title="Title",
                  default_value=1, min_=0, max_=100, step=1):
    """Simple dialog to ask a user to select a number within a certain range
    """
    app = QtGui.QApplication([])

    flags = QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint

    number, ok = QtGui.QInputDialog.getInteger(None,
                title, message, default_value, min_, max_, step, flags)
    app.quit()
    if ok:
        return number


if __name__ == '__main__':
    try:
        import bguic_demo
    except ImportError:
        print("Could not find demo.")
