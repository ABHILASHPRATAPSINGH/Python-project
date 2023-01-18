import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from src.userform import FYLStyleSheet
from src.userform.MainWindow_TTDPDF_PNG_Converter import MainWindow_TTDPDF_PNG_Converter
from src.userform.ext.HomeFrame_PDFPNGConverterEx import HomeFrame_PDFPNGConverterEx
from src.userform.ext.Pdf2PngFrame_WithoutTitleEx import Pdf2PngFrame_WithoutTitleEx
from src.userform.ext.Png2PdfFrame_WithoutTitleEx import Png2PdfFrame_WithoutTitleEx


class MainWindow_TTDPDF_PNG_ConverterEx(MainWindow_TTDPDF_PNG_Converter):
    def __init__(self,
                 applicationTitle: str = "TTD PDF PNG Converter",
                 appShortDesc="PDF ~ PNG Converter",
                 lblTextEasyToUse="Easy to use",
                 lblTextSupportWindow="Supports Windows 7, 8.1, 10",
                 lblTextSafeNSecure="Safe & Secure",
                 applicationIcon=":/resources/images/resources/images/PDF_PNG_Converter.png",
                 companyIcon=":/resources/images/resources/images/companyIcon.png",
                 easyToUseIcon=":/resources/images/resources/images/easyToUse.png",
                 safeNSecureIcon=":/resources/images/resources/images/secure.png",
                 supportWindowIcon=":/resources/images/resources/images/window.png"

                 ):
        # super(MainWindow_TTDPDFExporterEx, self).__init__("TTD PDF Exporter","Export specified pdf pages",":/resources/images/resources/images/PDF-exporter.png")
        super(MainWindow_TTDPDF_PNG_ConverterEx, self).__init__()
        styleBtnHome=FYLStyleSheet.getStyle_BtnHome()
        self._btnHome.setStyleSheet(styleBtnHome)
        self.label_9.setText(lblTextSupportWindow)
        self.label_6.setText(lblTextSafeNSecure)
        self.label_4.setText(lblTextEasyToUse)
        self.label_2.setText(appShortDesc)
        self.label.setText(applicationTitle)
        self._lblAppIcon.setPixmap(QtGui.QPixmap(applicationIcon))
        self.label_3.setPixmap(QtGui.QPixmap(easyToUseIcon))
        self.label_5.setPixmap(QtGui.QPixmap(safeNSecureIcon))
        self.label_7.setPixmap(QtGui.QPixmap(supportWindowIcon))
        self._lblCompanyIcon.setPixmap(QtGui.QPixmap(companyIcon))

        self.setWindowTitle(applicationTitle)
        self._btnHome.clicked.connect(self.showHomeWidgetFrame)
        self.verticalLayout_10.setContentsMargins(0,0,0,0)

        # self.verticalLayout_2.setContentsMargins(20,0,0,0)
        self.horizontalLayout_5.setContentsMargins(30,0,40,0)
        self.label_4.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_6.setStyleSheet("font-size: 18px;font-weight: bold;")
        self.label_9.setStyleSheet("font-size: 18px;font-weight: bold;")

        self.frame.setStyleSheet("background-color: white;")
        self._frameHome=HomeFrame_PDFPNGConverterEx()
        s=self._frameHome.styleSheet()+ """\nQFrame{ background-color: white;}"""
        self._frameHome.setStyleSheet(s)

        self.verticalLayout_home.addWidget(self._frameHome)
        self.stackedWidget.setCurrentIndex(0)

        self._framePdf2Png=Pdf2PngFrame_WithoutTitleEx()
        self.verticalLayout_pdf2Png.addWidget(self._framePdf2Png)
        self._btnShowPdf2PngFrame=self._frameHome.getBtnExportPdf2Png()
        self._btnShowPdf2PngFrame.clicked.connect(self.showPdf2PngFrame)

        self._framePng2Pdf=Png2PdfFrame_WithoutTitleEx()
        self.verticalLayout_png2Pdf.addWidget(self._framePng2Pdf)
        self._btnShowPng2Pdf=self._frameHome.getBtnPng2Pdf()
        self._btnShowPng2Pdf.clicked.connect(self.showPng2PdfFrame)

    def showHomeWidgetFrame(self):
        self.stackedWidget.setCurrentIndex(0)

    def showPdf2PngFrame(self):
        self.stackedWidget.setCurrentIndex(1)

    def showPng2PdfFrame(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    f=MainWindow_TTDPDF_PNG_ConverterEx()
    f.show()
    app.exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow
#
#
# class MainWindow_TTDPDF_PNG_Converter(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow_TTDPDF_PNG_Converter, self).__init__()
#         self.setupUi(self)
