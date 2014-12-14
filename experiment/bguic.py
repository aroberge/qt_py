'''Basic Graphical User Interface Components
'''
import os
from PyQt4 import QtGui, QtCore

config = {}
config['font'] = QtGui.QFont()
config['translator'] = QtCore.QTranslator()
config['locale'] = 'en'
qm_files = {}

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
    def __init__(self, locale=None, font=None):
        super().__init__([])
        self.set_font(font)
        self.set_locale(locale)

    def set_locale(self, locale):
        if locale is not None and locale in qm_files:
            if config['translator'].load("qt_"+locale, qm_files[locale]):
                self.installTranslator(config['translator'])
                config['locale'] = locale
            else:
                print("language not available")
        elif config['locale'] in qm_files:
            if config['translator'].load("qt_"+config['locale'], qm_files[config['locale']]):
                self.installTranslator(config['translator'])

    def set_font(self, font):
        '''Simple method to set font; called by individual GUI components.
           More restricted in what can be set than what the public dialog
           can do.
        '''
        if font is None:
            font = config['font'].family(), config['font'].pointSize()
        try:
            family, size = font
            if family:
                config['font'].setFamily(family)
            if size:
                config['font'].setPointSize(size)
            self.setFont(config['font'])
        except:
            print("Can not set font. Expected font = (family:str, size:int).")
            print("Got font =", font)


class LanguageChooser(QtGui.QDialog):
    def __init__(self, app, title="Language codes",
                 instruction="Click button when you are done"):
        super().__init__(None, QtCore.Qt.FramelessWindowHint)

        self.qm_files_choices = {}
        self.app = app

        group_box = QtGui.QGroupBox(title)
        group_box_layout = QtGui.QGridLayout()

        for i, locale in enumerate(qm_files):
            check_box = QtGui.QCheckBox(locale)
            check_box.setAutoExclusive(True)
            self.qm_files_choices[check_box] = locale
            check_box.toggled.connect(self.check_box_toggled)
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

    def check_box_toggled(self):
        self.locale = self.qm_files_choices[self.sender()]

    def confirm(self):
        self.app.set_locale(self.locale)
        self.close()


def set_global_font(app=None, font=None, locale=None):
    '''GUI component to set default font'''
    if app is None:
        app_quit = True
        app = SimpleApp(font=font, locale=locale)
    else:
        app_quit = False
    font, ok = QtGui.QFontDialog.getFont(config['font'], None)
    if app_quit:
        app.quit()
    if ok:
        config['font'] = font


def text_input(app=None, message="Enter your response", default="", font=None, locale=None):
    '''Simple frameless text input box.

       'font' is a tuple: (family:str, size:int).
      '''
    if app is None:
        app_quit = True
        app = SimpleApp(font=font, locale=locale)
    else:
        app_quit = False
    flags = QtCore.Qt.WindowFlags()
    flags |= QtCore.Qt.FramelessWindowHint
    text, ok = QtGui.QInputDialog.getText(None, '',
        message, QtGui.QLineEdit.Normal, default, flags)
    if app_quit:
        app.quit()
    if ok:
        return text


def choose_language(app=None, title="Language codes",
                 instruction="Click button when you are done"):
    if app is None:
        app_quit = True
        app = SimpleApp()
    else:
        app_quit = False
    chooser = LanguageChooser(app=app, title=title, instruction=instruction)
    chooser.exec_()
    if app_quit:
        app.quit()



if __name__ == '__main__':
    try:
        import bguic_demo
    except ImportError:
        print("Could not find demo.")
