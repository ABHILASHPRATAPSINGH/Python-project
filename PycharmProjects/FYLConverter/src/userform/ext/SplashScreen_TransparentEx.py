import sys
import time

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from src.userform import Resources
from src.userform.SplashScreen_Transparent import SplashScreen_Transparent


class SplashScreen_TransparentEx(SplashScreen_Transparent):

    def __init__(self,app=None,timeoutSeconds:int=10,applicationTitle:str="Application Name",applicationShortDesc:str="Application Tag Line",imagePathWRTResources:str=":/resources/images/resources/images/pdf-secure_icon.png"):
        super(SplashScreen_TransparentEx, self).__init__()
        title=applicationTitle
        titleDesc=applicationShortDesc
        self.label_2.setText("""<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; color:#03468b;">{title}</span></p></body></html>""".format(title=title))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_3.setText("""<html><head/><body><p align="center"><span style=" font-size:18pt; text-decoration: underline; color:#0570da;">{titleDesc}</span></p></body></html>""".format(titleDesc=titleDesc))
        self.label_3.setStyleSheet("background-color: transparent;")

        self.label.setPixmap(QtGui.QPixmap(imagePathWRTResources))
        self.label.setScaledContents(True)
        self.label.setStyleSheet("background-color: transparent;")

        self._app=app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        s = """
            QProgressBar {
                background-color: transparent;
                border-radius: 15px;
            }

            QProgressBar::chunk {
                background-color: rgb(1,136,166);                
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


        for i in range(1, 11):
            self.progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                if self._app is not None:
                    self._app.processEvents()

        # Simulate something that takes time
        time.sleep(timeoutSeconds)

    def finish(self,mainWindow):
        super(SplashScreen_TransparentEx, self).finish(mainWindow)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=SplashScreen_TransparentEx(app,1)
    dlg.show()
    app.exec()



# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QSplashScreen
#
#
# class SplashScreen_Transparent(QSplashScreen):
#
#     def __init__(self):
#         super(SplashScreen_Transparent, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Dialog = self