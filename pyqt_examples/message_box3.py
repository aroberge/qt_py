'''Simple message box with iconl default image embedded in source code'''
import base64

from PyQt4 import QtGui, QtCore
from tempfile import TemporaryFile

encoded_icon = (b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6i'+
                b'AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAB3RJTUUH3gwOEys1/2xprg'+
                b'AAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJ'+
                b'ISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbi'+
                b'B0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERp'+
                b'c2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWH'+
                b'RTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRU'+
                b'aXRsZQCo7tInAAABQUlEQVRIid2VQW6FIBBAn80/hktM3HsB7yGH4R'+
                b'5u8TjuTWTpPejm+6sUvow2pu1L2ME8GWcGvPfEFuCvrK7rfCq2957i'+
                b'KdlRFIUHaJqGuq4BqKrq274QpRRlWQLQ9z0A1toitjcplkpj8rZteU'+
                b'X3fvcBH0eBJFIA5xzLshzuOxSHzPOMMQallPTojof0wDAMWGtxzuUd'+
                b'CFK8Ir7xT3FKrLW+P9XGGID8VCf4W6kW8RxG94sTHIrneRYF3E4uQN'+
                b'5O4zgyTZNIHpvVKaKzGr4eiiv4xG3fircfsD4YVVVhjNkt4NXTWuu3'+
                b'si1ZxbVKU5zp6UtVvb31beIrUjgxMlfpVbLEa1utxRVy5sHIqmpJwN'+
                b'yqPhSHHxG2Vq4o5PfO6n8nPtVOW2LFl/PfL4nD1lJKobXOOns61dJ3'+
                b'OkTcTjn7clL9CaQWvgP3zR49AAAAAElFTkSuQmCC')


def message_box(message="Message", title="Title", icon=None):
    """Simple message box.
    """
    app = QtGui.QApplication([])
    box = QtGui.QMessageBox(None)
    if icon is not None:
        box.setWindowIcon(QtGui.QIcon(icon))
    else:
        temp_file = TemporaryFile(suffix=".png")
        fname = temp_file.name
        temp_file.close()
        ff = open(fname, "wb")
        ff.write(base64.b64decode(encoded_icon))
        ff.close()
        box.setWindowIcon(QtGui.QIcon(fname))
    box.setWindowTitle(title)
    box.setText(message)
    box.show()
    box.exec_()
    app.quit()


if __name__ == '__main__':
    message_box("Simple test")
    message_box(icon="images/python.jpg")
