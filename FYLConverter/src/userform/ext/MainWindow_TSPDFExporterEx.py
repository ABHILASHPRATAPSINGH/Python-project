
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import AppConfig_TTDPDFExporter
from src.userform import FYLStyleSheet
from src.userform.MainWindow_TSPDFExporter import MainWindow_TSPDFExporter
from src.userform.ext.HomeFrame_PDFExporter2Ex import HomeFrame_PDFExporter2Ex
from src.userform.ext.HomeFrame_PDFExporterEx import HomeFrame_PDFExporterEx
from src.userform.ext.Pdf2ImagedPdfFrame_WithoutTitleEx import Pdf2ImagedPdfFrame_WithoutTitleEx
from src.userform.ext.Pdf2SeperatePdfFrame_WithoutTitleEx import Pdf2SeperatePdfFrame_WithoutTitleEx
from src.userform.ext.Pdf2SinglePdfFrame_WithoutTitleEx import Pdf2SinglePdfFrame_WithoutTitleEx

class MainWindow_TSPDFExporterEx(MainWindow_TSPDFExporter):
    def __init__(self,
                windowTitle: str = "TS PDF Exporter",
                appShortDesc="Export specified pdf pages",
                lblTextEasyToUse="Easy to use",
                lblTextSupportWindow="Supports Windows 7, 8.1, 10",
                lblTextSafeNSecure="Safe & Secure",
                applicationIcon=":/resources/images/resources/images/PDF-exporter.png",
                companyIcon=":/resources/images/resources/images/companyIcon.png",
                easyToUseIcon=":/resources/images/resources/images/easyToUse.png",
                safeNSecureIcon=":/resources/images/resources/images/secure.png",
                supportWindowIcon=":/resources/images/resources/images/window.png"

                 ):

        super(MainWindow_TSPDFExporterEx, self).__init__()
        fStyle=FYLStyleSheet.getStyle_BtnHome()
        self._btnHome.setStyleSheet(fStyle)
        self.label_9.setText(lblTextSupportWindow)
        self.label_6.setText(lblTextSafeNSecure)
        self.label_4.setText(lblTextEasyToUse)
        self.label_2.setText(appShortDesc)
        self.label.setText(windowTitle)
        self._lblAppIcon.setPixmap(QtGui.QPixmap(applicationIcon))
        self.label_3.setPixmap(QtGui.QPixmap(easyToUseIcon))
        self.label_5.setPixmap(QtGui.QPixmap(safeNSecureIcon))
        self.label_7.setPixmap(QtGui.QPixmap(supportWindowIcon))
        self._lblCompanyIcon.setPixmap(QtGui.QPixmap(companyIcon))



        windowTitle=windowTitle
        self.setWindowTitle(windowTitle)
        self._btnHome.clicked.connect(self.showHomeWidgetFrame)
        self.verticalLayout_10.setContentsMargins(0,0,0,0)

        # self.verticalLayout_2.setContentsMargins(20,0,0,0)
        self.horizontalLayout_5.setContentsMargins(30,0,40,0)
        self.label_4.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_6.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_9.setStyleSheet("font-size: 18px;font-weight: bold;")

        self.frame.setStyleSheet("background-color: white;")

        self._frameHome=HomeFrame_PDFExporter2Ex()
        s=self._frameHome.styleSheet()+ """\nQFrame{ background-color: white;}"""
        self._frameHome.setStyleSheet(s)

        self.verticalLayout_home.addWidget(self._frameHome)
        self.stackedWidget.setCurrentIndex(0)

        self._framePdf2SinglePdf=Pdf2SinglePdfFrame_WithoutTitleEx()
        self.verticalLayout_pdf2SinglePdf.addWidget(self._framePdf2SinglePdf)
        self._btnShowPdf2SinglePdfFrame=self._frameHome.getBtnPdf2SinglePdf()
        self._btnShowPdf2SinglePdfFrame.clicked.connect(self.showPdf2SinglePdfFrame)

        self._framePdf2SeperatePdf=Pdf2SeperatePdfFrame_WithoutTitleEx()
        self.verticalLayout_SeperatePdf.addWidget(self._framePdf2SeperatePdf)
        self._btnShowPdf2SeperatePdf=self._frameHome.getBtnPdf2SeperatePdf()
        self._btnShowPdf2SeperatePdf.clicked.connect(self.showPdf2SeperatePdfFrame)

        self._framePdf2ImagedPdf=Pdf2ImagedPdfFrame_WithoutTitleEx()
        self.verticalLayout_pdf2ImagedPdf.addWidget(self._framePdf2ImagedPdf)
        self._btnShowPdf2ImagedPdf=self._frameHome.getBtnPdf2ImagedPdf()
        self._btnShowPdf2ImagedPdf.clicked.connect(self.showPdf2ImagedPdfFrame)


    def showHomeWidgetFrame(self):
        self.stackedWidget.setCurrentIndex(0)

    def showPdf2SinglePdfFrame(self):
        self.stackedWidget.setCurrentIndex(1)

    def showPdf2SeperatePdfFrame(self):
        self.stackedWidget.setCurrentIndex(2)

    def showPdf2ImagedPdfFrame(self):
        self.stackedWidget.setCurrentIndex(3)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow_TSPDFExporterEx()
    win.show()
    app.exec()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow
#
#
# class MainWindow_TSPDFExporter(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow_TSPDFExporter, self).__init__()
#         self.setupUi(self)
#
#     def setupUi(self, MainWindow):