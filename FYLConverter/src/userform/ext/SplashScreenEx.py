import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from src.userform.SplashScreen_Dark import SplashScreen_Dark
from src.userform import Resources

class SplashScreenEx(SplashScreen_Dark):
    
    def __init__(self,app=None,timeoutSeconds:int=10):
        super(SplashScreenEx, self).__init__()
        self._app=app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        s="""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
            }
            
            QProgressBar::chunk {
                background-color: rgb(235, 123, 49);
                width: 20px;
            }
        """
        self.progressBar.setStyleSheet(s)
        self.progressBar.setMaximum(10)
        qr=self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

        # self.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter,
        #                  Qt.black)
        for i in range(1, 11):
            self.progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                if self._app is not None:
                    self._app.processEvents()

        # Simulate something that takes time
        time.sleep(timeoutSeconds)

    def finish(self,mainWindow):
        super(SplashScreenEx, self).finish(mainWindow)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=SplashScreenEx(app,5)
    dlg.show()
    app.exec()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QSplashScreen
# from src.styles import appResources
#
# class SplashScreen_Dark(QSplashScreen):
#
#     def __init__(self):
#         super(SplashScreen_Dark, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Dialog = self
