'''Simple integer input dialog'''
from PyQt4 import QtGui, QtCore

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
    from random import randint
    min_ = 1
    max_ = 50
    answer = randint(min_, max_)
    print(answer)
    guess = 0
    title = "Guessing game"
    while guess != answer:
        message = "Guess a number between {} and {}".format(min_, max_)
        guess = integer_input(message=message, title=title,
                              default_value=guess, min_=min_ ,max_=max_)
        if guess < answer:
            title = "Too low"
            min_ = guess
        elif guess > answer:
            title = "Too high"
            max_ = guess
    print("You got it! {} was the answer".format(guess))
