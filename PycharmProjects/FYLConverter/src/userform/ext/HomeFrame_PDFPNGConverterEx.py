import sys

from PyQt5.QtWidgets import QPushButton, QApplication

from src.userform import FYLStyleSheet
from src.userform.HomeFrame_PDFPNGConverter import HomeFrame_PDFPNGConverter


class HomeFrame_PDFPNGConverterEx(HomeFrame_PDFPNGConverter):

    def __init__(self):
        super(HomeFrame_PDFPNGConverterEx, self).__init__()
        frameStyle=FYLStyleSheet.getStyle_HomeFrameEx()

        self.line.setStyleSheet("border-color: #DFDFDF;")
        self.setStyleSheet(frameStyle)
        self._btnPng2Pdf.setStyleSheet(frameStyle)
        self._btnExportPdf2Png.setStyleSheet(frameStyle)


    def getBtnPng2Pdf(self)->QPushButton:
        wid=self._btnPng2Pdf
        return wid

    def getBtnExportPdf2Png(self)->QPushButton:
        wid= self._btnExportPdf2Png
        return wid

if __name__ == '__main__':
    app=QApplication(sys.argv)
    f=HomeFrame_PDFPNGConverterEx()
    f.show()
    app.exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFrame
#
# class HomeFrame_PDFPNGConverter(QFrame):
#
#     def __init__(self):
#         super(HomeFrame_PDFPNGConverter, self).__init__()
#         self.setupUi(self)
