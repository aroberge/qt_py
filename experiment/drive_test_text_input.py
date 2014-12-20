import subprocess
import threading
import time
import pyautogui

class TypewriteThread(threading.Thread):
    def __init__(self, msg, interval=0.0):
        super(TypewriteThread, self).__init__()
        self.msg = msg
        self.interval = interval


    def run(self):
        time.sleep(1.) # NOTE: BE SURE TO ACCOUNT FOR THIS QUARTER SECOND FOR TIMING TESTS!
        pyautogui.typewrite(self.msg, self.interval)


w, h = pyautogui.size()
pyautogui.moveTo(w/2, h/2)
t = TypewriteThread('Hi!\n')
t.start()
output = subprocess.check_output('pyconda test_text_input.py',
                                 universal_newlines=True)



print("captured output = ", output)
