import sys

from PyQt5.QtWidgets import QPushButton, QApplication
from src.userform import FYLStyleSheet
from src.userform.HomeFrame_PDFExporter2 import HomeFrame_PDFExporter2

class HomeFrame_PDFExporter2Ex(HomeFrame_PDFExporter2):
    """
    It has 3 button widgets
    """
    def __init__(self):
        super(HomeFrame_PDFExporter2Ex, self).__init__()
        frameStyle=FYLStyleSheet.getStyle_HomeFrameEx()
        self.line.setStyleSheet("border-color: #DFDFDF;")
        self.line_2.setStyleSheet("border-color: #DFDFDF;")
        self.setStyleSheet(frameStyle)
        self._btnExportPdf2SinglePdf.setStyleSheet(frameStyle)
        self._btnPdf2SeperatePdf.setStyleSheet(frameStyle)
        self._btnPdf2ImagedPdf.setStyleSheet(frameStyle)


    def getBtnPdf2SinglePdf(self)->QPushButton:
        wid=self._btnExportPdf2SinglePdf
        return wid

    def getBtnPdf2SeperatePdf(self)->QPushButton:
        wid= self._btnPdf2SeperatePdf
        return wid

    def getBtnPdf2ImagedPdf(self)->QPushButton:
        wid= self._btnPdf2ImagedPdf
        return wid


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=HomeFrame_PDFExporter2Ex()
    win.show()
    app.exec()



# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFrame
#
#
# class HomeFrame_PDFExporter2(QFrame):
#
#     def __init__(self):
#         super(HomeFrame_PDFExporter2, self).__init__()
#         self.setupUi(self)
#
#     def setupUi(self, Frame):
