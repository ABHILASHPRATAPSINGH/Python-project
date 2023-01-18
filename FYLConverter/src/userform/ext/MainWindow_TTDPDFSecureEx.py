import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import AppConfig_TTDPDFSecure
from src.userform.MainWindow_TTDPDFSecure import MainWindow_TTDPDFSecure
from src.userform.ext.ProtectedPdfFrame_WithoutTitleEx import ProtectedPdfFrame_WithoutTitleEx

class MainWindow_TTDPDFSecureEx(MainWindow_TTDPDFSecure):
    def __init__(self,
                 applicationTitle="TTD PDF Secure",
                 applicationShortDesc: str = "Convert Unprotected PDF to Password protected PDF",
                 lblTextEasyToUse: str = "Easy to use",
                 lblTextSupportWindow: str = "Supports Windows 7, 8.1, 10",
                 lblTextSafeNSecure: str = "Safe & Secure",
                 applicationIcon: str = ":/resources/images/resources/images/pdf-secure_icon.png",
                 companyIcon: str = ":/resources/images/resources/images/companyIcon.png",
                 easyToUseIcon: str = ":/resources/images/resources/images/easyToUse.png",
                 safeNSecureIcon: str = ":/resources/images/resources/images/secure.png",
                 supportWindowIcon: str = ":/resources/images/resources/images/window.png"
                 ):

        super(MainWindow_TTDPDFSecureEx, self).__init__()
        self.label.setText(applicationTitle)
        self.label_2.setText(applicationShortDesc)
        self.label_4.setText(lblTextEasyToUse)
        self.label_9.setText(lblTextSupportWindow)
        self.label_6.setText(lblTextSafeNSecure)

        self._lblAppIcon.setPixmap(QtGui.QPixmap(applicationIcon))
        self._lblCompanyIcon.setPixmap(QtGui.QPixmap(companyIcon))
        self.label_3.setPixmap(QtGui.QPixmap(easyToUseIcon))
        self.label_5.setPixmap(QtGui.QPixmap(safeNSecureIcon))
        self.label_7.setPixmap(QtGui.QPixmap(supportWindowIcon))



        self.verticalLayout_10.setContentsMargins(0,0,0,0)
        windowTitle=applicationTitle
        self.setWindowTitle(windowTitle)
        # self.verticalLayout_2.setContentsMargins(20,0,0,0)
        self.horizontalLayout_5.setContentsMargins(30,0,40,0)
        self.label_4.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_6.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_9.setStyleSheet("font-size: 18px;font-weight: bold;")

        self.frame.setStyleSheet("background-color: white;")
        self._frameHome=ProtectedPdfFrame_WithoutTitleEx()
        s=self._frameHome.styleSheet()+ """\nQFrame{ background-color: white;}"""
        self._frameHome.setStyleSheet(s)

        self.verticalLayout_home.addWidget(self._frameHome)
        self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow_TTDPDFSecureEx()
    win.show()
    app.exec()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow
#
# class MainWindow_TTDPDFSecure(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow_TTDPDFSecure, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         MainWindow=self