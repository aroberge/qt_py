'''Basic Graphical User Interface Components
'''
import os
from collections import OrderedDict
from PyQt4 import QtGui, QtCore

config = {}
config['font'] = QtGui.QFont()
config['translator'] = QtCore.QTranslator()
config['locale'] = 'default'
qm_files = OrderedDict()

def find_qm_files():
    '''looking for files with names == qt_locale.qm'''
    all_files = []
    for root, _, files in os.walk(os.path.join(QtGui.__file__, "..")):
        for fname in files:
            if (fname.endswith('.qm') and
                fname.startswith("qt_") and
                not fname.startswith("qt_help")):
                locale = fname[3:-3]
                all_files.append(locale)
                qm_files[locale] = root
find_qm_files()


class SimpleApp(QtGui.QApplication):
    def __init__(self, locale=None, font_size=None):
        super().__init__([])
        if font_size is not None:
            self.set_font_size(font_size)
        self.setFont(config['font'])
        self.set_locale(locale)

    def set_locale(self, locale):
        print(locale, config['locale'])
        if locale in qm_files:
            if config['translator'].load("qt_"+locale, qm_files[locale]):
                self.installTranslator(config['translator'])
                config['locale'] = locale
            else:
                print("language not available")
        elif locale is "default" and config['locale'] != 'default':
            self.removeTranslator(config['translator'])
            config['translator'] = QtCore.QTranslator()
            config['locale'] = 'default'
        elif config['locale'] in qm_files:
            if config['translator'].load("qt_"+config['locale'], qm_files[config['locale']]):
                self.installTranslator(config['translator'])

    def set_font_size(self, font_size):
        '''Simple method to set font size; also called by individual GUI components.
        '''
        try:
            config['font'].setPointSize(font_size)
        except:
            print("Can not set font size.")

    def show_text_input(self, message="message", title="title",
                        default_response=""):
        flags = QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
        text, ok = QtGui.QInputDialog.getText(None, title, message,
                               QtGui.QLineEdit.Normal, default_response, flags)
        if ok:
            return text

    def show_yes_no_question(self, question="question", title="title"):
        reply = QtGui.QMessageBox.question(None, title, question,
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            return True
        elif reply == QtGui.QMessageBox.No:
            return False
        else:
            return None

    def show_select_language(self, title="Select language",
                            name="Language codes",
                            instruction="Click button when you are done"):
        selector = LanguageSelector(self, title=title, name=name,
                              instruction=instruction)
        selector.exec_()


class LanguageSelector(QtGui.QDialog):
    def __init__(self, parent, title="Language selection", name="Language codes",
                 instruction="Click button when you are done"):
        super().__init__(None,  QtCore.Qt.WindowSystemMenuHint |
                                QtCore.Qt.WindowTitleHint)

        self.qm_files_choices = {}
        self.parent = parent

        group_box = QtGui.QGroupBox(name)
        group_box_layout = QtGui.QGridLayout()

        for i, locale in enumerate(qm_files):
            check_box = QtGui.QCheckBox(locale)
            check_box.setAutoExclusive(True)
            self.qm_files_choices[check_box] = locale
            check_box.toggled.connect(self.check_box_toggled)
            group_box_layout.addWidget(check_box, i / 4, i % 4)

        check_box = QtGui.QCheckBox("None")
        check_box.setAutoExclusive(True)
        self.qm_files_choices[check_box] = "default"
        check_box.toggled.connect(self.check_box_toggled)
        i = len(qm_files)
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
        self.locale = self.qm_files_choices[self.sender()]

    def confirm(self):
        self.parent.set_locale(self.locale)
        self.close()


def set_global_font(app=None, locale=None):
    '''GUI component to set default font'''
    if app is None:
        app_quit = True
        app = SimpleApp(locale=locale)
    else:
        app_quit = False
    font, ok = QtGui.QFontDialog.getFont(config['font'], None)
    if app_quit:
        app.quit()
    if ok:
        config['font'] = font


def text_input(message="Enter your response", title="Title",
               default_response="",
               font_size: int = None,
               locale: "most often two letter code such as 'fr'" = None):
    '''Simple text input box.  Used to query the user and get a string back.
    '''
    app = SimpleApp(font_size=font_size, locale=locale)
    response = app.show_text_input(message=message, title=title,
                               default_response=default_response)
    app.quit()
    return response


def yes_no_question(question="Answer this question", title="Title",
                    font_size=None, locale=None):
    '''Simple yes or no question
      '''

    app = SimpleApp(font_size=font_size, locale=locale)
    answer= app.show_yes_no_question(question=question, title=title)
    app.quit()
    return answer


def select_language(title="Select language", name="Language codes",
                 instruction="Click button when you are done"):
    '''Dialog to choose language based on some locale code for
       files found on default path'''
    app = SimpleApp()
    app.show_select_language(title=title, name=name, instruction=instruction)
    app.quit()



if __name__ == '__main__':
    try:
        import bguic_demo
    except ImportError:
        print("Could not find demo.")
