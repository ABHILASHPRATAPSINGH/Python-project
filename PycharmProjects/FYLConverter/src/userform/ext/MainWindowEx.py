import sys
from PyQt5.QtWidgets import QApplication
import AppConfig
from src.userform.MainWindow import MainWindow
from src.userform.ext.HomeFrameEx import HomeFrameEx
from src.userform.ext.Pdf2PngFrameEx import Pdf2PngFrameEx
from src.userform.ext.Pdf2SeperatePdfFrameEx import Pdf2SeperatePdfFrameEx
from src.userform.ext.Pdf2SinglePdfFrameEx import Pdf2SinglePdfFrameEx
from src.userform.ext.Png2PdfFrameEx import Png2PdfFrameEx
from src.userform.ext.ProtectPdfFrameEx import ProtectPdfFrameEx

class MainWindowEx(MainWindow):

    def __init__(self):
        super(MainWindowEx, self).__init__()
        windowTitle=AppConfig.Details.APPLICATION_NAME.value

        self.setWindowTitle(windowTitle)
        self._btnHome.clicked.connect(self.showHomeWidgetFrame)

        self._frameHome=HomeFrameEx()
        self.verticalLayout_home.addWidget(self._frameHome)

        self._frameProtectPdf=ProtectPdfFrameEx()
        self.verticalLayout_pdf2ProtectedPdf.addWidget(self._frameProtectPdf)
        self._btnshowProtectPdfFrame=self._frameHome.getBtnProtectPdf()
        self._btnshowProtectPdfFrame.clicked.connect(self.showProtectPdfFrame)

        self._framePdf2SinglePdf=Pdf2SinglePdfFrameEx()
        self.verticalLayout_pdf2SinglePdf.addWidget(self._framePdf2SinglePdf)
        self._btnShowPdf2SinglePdfFrame=self._frameHome.getBtnPdf2SinglePdf()
        self._btnShowPdf2SinglePdfFrame.clicked.connect(self.showPdf2SinglePdfFrame)

        self._framePdf2SeperatePdf=Pdf2SeperatePdfFrameEx()
        self.verticalLayout_SeperatePdf.addWidget(self._framePdf2SeperatePdf)
        self._btnShowPdf2SeperatePdf=self._frameHome.getBtnPdf2SeperatePdf()
        self._btnShowPdf2SeperatePdf.clicked.connect(self.showPdf2SeperatePdfFrame)

        self._framePdf2Png=Pdf2PngFrameEx()
        self.verticalLayout_pdf2Png.addWidget(self._framePdf2Png)
        self._btnShowPdf2PngFrame=self._frameHome.getBtnPdf2Png()
        self._btnShowPdf2PngFrame.clicked.connect(self.showPdf2PngFrame)

        self._framePng2Pdf= Png2PdfFrameEx()
        self.verticalLayout_png2pdf.addWidget(self._framePng2Pdf)

        self._btnShowPng2PdfFrame=self._frameHome.getBtnPng2Pdf()
        self._btnShowPng2PdfFrame.clicked.connect(self.showPng2PdfFrame)
        self.stackedWidget.setCurrentIndex(0)


    def showHomeWidgetFrame(self):
        # print("HomeWidget is poppulated")
        self.stackedWidget.setCurrentIndex(0)

    def showProtectPdfFrame(self):
        # print("Show Protect Pdf")
        self.stackedWidget.setCurrentIndex(1)

    def showPdf2PngFrame(self):
        # print("Show Pdf2Png")
        self.stackedWidget.setCurrentIndex(5)

    def showPdf2SinglePdfFrame(self):
        # print("Show Pdf2SinglePdf")
        self.stackedWidget.setCurrentIndex(2)

    def showPdf2SeperatePdfFrame(self):
        # print("Show Pdf2 Seperate Pdf")
        self.stackedWidget.setCurrentIndex(3)

    def showPng2PdfFrame(self):
        # print("Show Pdf2 Seperate Pdf")
        self.stackedWidget.setCurrentIndex(4)





# from PyQt5 import QtGui, QtWidgets, QtCore
# from PyQt5.QtWidgets import QMainWindow
# from src.userform import Resources
# import resources
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         MainWindow = self

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MainWindowEx()
    window.show()
    app.exec_()
