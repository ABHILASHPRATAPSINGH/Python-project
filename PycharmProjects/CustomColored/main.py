import sys

from PyQt5.QtWidgets import QApplication

from testing.coloredEx import coloredEx

# dynamically
# global()[""]
# String class
# hidden
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=coloredEx()
    window.show()
    app.exec_()
