import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from src.userform.ext.SplashScreenEx import SplashScreenEx
from PyQt5.QtCore import Qt

class SplashScreen_TTDPDFSecureEx(SplashScreenEx):

    def __init__(self, app, timeoutSeconds: int):
        super(SplashScreen_TTDPDFSecureEx, self).__init__(app,timeoutSeconds)
        self._app = app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    d=SplashScreen_TTDPDFSecureEx(None,5)
    d.show()
    app.exec_()

