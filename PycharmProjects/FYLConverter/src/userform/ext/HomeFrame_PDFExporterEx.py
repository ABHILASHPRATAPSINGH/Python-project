import sys

from PyQt5.QtWidgets import QPushButton, QApplication

from src.userform import FYLStyleSheet
from src.userform.HomeFrame_PDFExporter import HomeFrame_PDFExporter

class HomeFrame_PDFExporterEx(HomeFrame_PDFExporter):



    def __init__(self):
        super(HomeFrame_PDFExporterEx, self).__init__()
        frameStyle=FYLStyleSheet.getStyle_HomeFrameEx()
        self.line.setStyleSheet("border-color: #DFDFDF;")
        self.setStyleSheet(frameStyle)
        self._btnExportPdf2SinglePdf.setStyleSheet(frameStyle)
        self._btnPdf2SeperatePdf.setStyleSheet(frameStyle)

    def getBtnPdf2SinglePdf(self)->QPushButton:
        wid=self._btnExportPdf2SinglePdf
        return wid

    def getBtnPdf2SeperatePdf(self)->QPushButton:
        wid= self._btnPdf2SeperatePdf
        return wid

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=HomeFrame_PDFExporterEx()
    win.show()
    app.exec()



# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFrame
#
# class HomeFrame_PDFExporter(QFrame):
#
#     def __init__(self):
#         super(HomeFrame_PDFExporter, self).__init__()
#         self.setupUi(self)
