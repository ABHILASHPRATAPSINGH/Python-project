import sys
import traceback

from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox, QApplication

from src.commands import Commands
from src.commands.threadCommands.ExtractPdfPages2IndPdf_Thread import ExtractPdfPages2IndPdf_Thread
from src.pdfar.DocViewContainer import DocViewContainer
from src.pdfar.PDFARViewerWidget import PDFARViewerWidget
from src.userform import FYLStyleSheet
from src.userform.ext.FilePathSelectionWidgetEx import FilePathSelectionWidgetEx
from src.userform.Pdf2SeperatePdfFrame_WithoutTitle import Pdf2SeperatePdfFrame_WithoutTitle


class Pdf2SeperatePdfFrame_WithoutTitleEx(Pdf2SeperatePdfFrame_WithoutTitle):

    def __init__(self):
        super(Pdf2SeperatePdfFrame_WithoutTitleEx, self).__init__()

        self.verticalLayout_2.setContentsMargins(60, 0, 80, 0)
        self.horizontalLayout_13.setContentsMargins(60, 0, 80, 0)

        self.label.setMinimumSize(QtCore.QSize(170, 0))
        self.label.setMaximumSize(QtCore.QSize(170, 16777215))

        self.label_2.setMinimumSize(QtCore.QSize(170, 0))
        self.label_2.setMaximumSize(QtCore.QSize(170, 16777215))

        self.label_12.setMinimumSize(QtCore.QSize(170, 0))
        self.label_12.setMaximumSize(QtCore.QSize(170, 16777215))

        self.pdfWidget = QWidget()
        self.pdfWidget.setContentsMargins(0, 0, 0, 0)
        self.pdfWidgetHLayout = QHBoxLayout()
        self.pdfWidget.setLayout(self.pdfWidgetHLayout)
        self.pdfWidgetHLayout.setContentsMargins(0, 0, 0, 0)
        self._txtTotalPages.setEnabled(False)
        self._txtTotalPages.setText("0")
        self.filePathWidget = FilePathSelectionWidgetEx(self, fileType="PDF Files(*.pdf)")
        self._inputPathWidget=self.filePathWidget.getPathWidget()
        self._inputPathWidget.textChanged.connect(self.pdfFileChanged)

        transparentStyle = FYLStyleSheet.getTransparentButtonStyle()
        self._btnPreview = QPushButton("Preview")
        self._btnPreview.setStyleSheet(transparentStyle)
        self._btnPreview.clicked.connect(self.preview)
        self.pdfWidgetHLayout.addWidget(self.filePathWidget)
        self.pdfWidgetHLayout.addWidget(self._btnPreview)

        self.verticalLayout_2.insertWidget(1, self.pdfWidget)

        bodyFrameStyle = FYLStyleSheet.getStyleTTDPDFSecureFrame()
        bottomBodyFrameStyle = FYLStyleSheet.getStyleTTDPDFSecureFrame()
        self.bodyFrame.setStyleSheet(bodyFrameStyle)
        self.bottomFrame.setStyleSheet(bottomBodyFrameStyle)
        self._btnClear.clicked.connect(self.clear)
        self._btnExport2SeperatePdf.setStyleSheet(bodyFrameStyle)
        self._btnExport2SeperatePdf.clicked.connect(self.exportPdf2SeperatePdf)
        self.progressBar.setVisible(False)

    def pdfFileChanged(self):
        try:
            selectedPdf=self.filePathWidget.getPath()
            if selectedPdf.strip()!="":
                totalPages=Commands.getPdfTotalPages(selectedPdf)
                self._txtTotalPages.setText(str(totalPages))
            else:
                self._txtTotalPages.setText("0")
        except BaseException as e:
            QMessageBox.critical(self,"ValueError",str(e))
            self.filePathWidget.clear()
            self._txtTotalPages.clear()

    def preview(self):
        selectedPdf = self.filePathWidget.getPath()
        if selectedPdf.strip()=="":
            QMessageBox.warning(self,"PDFFileNotSelected : ","Select PDF file")
            return
        docViewerWidget=PDFARViewerWidget()
        docContainer = DocViewContainer(self,docViewerWidget,selectedPdf)
        docContainer.preview()

    def clear(self):
        self._txtTotalPages.clear()
        self._txtRequiredPages.clear()
        self.filePathWidget.clear()

    def threadStarted(self):
        self.showUpdateStatus()

    def showUpdateStatus(self):
        self.progressBar.setVisible(True)
        styleSheet="""QLabel{
                        padding-left: 10px;   
                        font: 8pt Arial;
                        max-height: 16px;                     
                        color: rgb(255, 228, 239);
                        background-color: rgb(255, 29, 33);
                        }"""
        self._lblProgressStatus.setStyleSheet(styleSheet)

    def lblStatusUpdate(self,status):
        self._lblProgressStatus.setText(status)

    def updateProgressBar(self,currentValue,maxValue):
        self.progressBar.setMaximum(maxValue)
        self.progressBar.setValue(currentValue)

    def complete(self,completedText):
        QMessageBox.information(self, "Status",completedText)
        self.hideUpdateStatus()

    def hideUpdateStatus(self):
        self.progressBar.setVisible(False)
        styleSheet=""""""
        self._lblProgressStatus.setText("")
        self._lblProgressStatus.setStyleSheet(styleSheet)

    def finalFunc(self):
        self.hideUpdateStatus()

    def errorFoundFound(self,err):
        QMessageBox.critical(self,"Error Found",err)
        self.hideUpdateStatus()

    def exportPdf2SeperatePdf(self):
        pdfFilePath = self.filePathWidget.getPath()
        pageListStr=self._txtRequiredPages.text()
        try:
            if pdfFilePath.lower() == "":
                raise ValueError("Please Select PDF File First")
            if pageListStr.strip()=="":
                raise ValueError("Please Enter required pages")
            else:
                requiredPageLists = Commands.getPageList(pageListStr)

            self.pdf2SeperatePdfThread=ExtractPdfPages2IndPdf_Thread(pdfFilePath,requiredPageLists)
            self.pdf2SeperatePdfThread.startedSignal.connect(self.threadStarted)
            self.pdf2SeperatePdfThread.processingStatusSignal.connect(self.lblStatusUpdate)
            self.pdf2SeperatePdfThread.maxCurrentPageProgressBarSignal.connect(self.updateProgressBar)
            self.pdf2SeperatePdfThread.completedSignal.connect(self.complete)
            self.pdf2SeperatePdfThread.finallyStatusSignal.connect(self.finalFunc)
            self.pdf2SeperatePdfThread.errorSignal.connect(self.errorFoundFound)
            self.pdf2SeperatePdfThread.start()

        except BaseException as e:
            traceback.print_exc()
            QMessageBox.critical(self,"Error ",str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Pdf2SeperatePdfFrame_WithoutTitleEx()
    dlg.show()
    app.exec()




# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFrame
#
#
# class Pdf2SeperatePdfFrame_WithoutTitle(QFrame):
#
#     def __init__(self):
#         super(Pdf2SeperatePdfFrame_WithoutTitle, self).__init__()
#         self.setupUi(self)