import sys
from src.userform.HomeFrame import HomeFrame
from PyQt5.QtWidgets import QPushButton, QApplication



class HomeFrameEx(HomeFrame):

    def __init__(self):
        super(HomeFrameEx, self).__init__()

    def getBtnProtectPdf(self)->QPushButton:
        wid= self._btnProtectPdf
        return wid

    def getBtnPdf2SinglePdf(self)->QPushButton:
        wid=self._btnExportPdf2SinglePdf
        return wid

    def getBtnPdf2SeperatePdf(self)->QPushButton:
        wid= self._btnPdf2SeperatePdf
        return wid

    def getBtnPdf2Png(self)->QPushButton:
        wid= self._btnExportPdf2Png
        return wid

    def getBtnPng2Pdf(self)->QPushButton:
        wid= self._btnPng2Pdf
        return wid

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=HomeFrameEx()
    window.show()
    app.exec_()

# from PyQt5.QtWidgets import QFrame
# import resources
#
# class HomeFrame(QFrame):
#
#     def __init__(self):
#         super(HomeFrame, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Frame = self