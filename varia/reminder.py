''' Small reminder app '''

import sys
import time

import PyQt4.QtCore as Core
import PyQt4.QtGui as Gui

def get_info():
    '''gets info from command line'''
    alert_time = Core.QTime.currentTime()
    message = "Ready!"

    if len(sys.argv) < 2:
        raise ValueError

    hour, minutes = sys.argv[1].split(":")
    alert_time = Core.QTime(int(hour), int(minutes))
    if not alert_time.isValid():
        print("invalid time")
        raise ValueError

    if len(sys.argv) == 2:
        message = sys.argv[2]
    else:
        message = ' '.join(sys.argv[2:])
    return message, alert_time

def show_alert(message, alert_time):
    app = Gui.QApplication(sys.argv)
    while Core.QTime.currentTime() < alert_time:
        time.sleep(2)
    label = Gui.QLabel("<font color=blue size=20><b>" + message + "</b></font>")
    label.setWindowFlags(Core.Qt.SplashScreen)
    label.show()
    Core.QTimer.singleShot(10000, app.quit)
    app.exec_()

if __name__ == '__main__':
    try:
        message, alert_time = get_info()
    except Exception as e:
        print(e)
        print("usage: python reminder.py hour:min message")
        sys.exit()
    show_alert(message, alert_time)
