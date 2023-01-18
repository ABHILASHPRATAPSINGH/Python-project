import sys
import traceback

from src.commands.threadCommands.ProtectPDFThread import ProtectPDFThread
from src.pdfar.DocViewContainer import DocViewContainer
from src.pdfar.PDFARViewerWidget import PDFARViewerWidget
from src.userform import FYLStyleSheet
from src.userform.ext.FilePathSelectionWidgetEx import FilePathSelectionWidgetEx
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMessageBox

from src.userform.ProtectedPdfFrame_WithoutTitle import ProtectedPdfFrame_WithoutTitle


class ProtectedPdfFrame_WithoutTitleEx(ProtectedPdfFrame_WithoutTitle):

    def __init__(self):
        super(ProtectedPdfFrame_WithoutTitleEx, self).__init__()
        self.verticalLayout_2.setContentsMargins(60,0,80,0)
        self.horizontalLayout_13.setContentsMargins(60,0,80,0)
        self.pdfWidget=QWidget()
        self.pdfWidget.setContentsMargins(0,0,0,0)
        self.pdfWidgetHLayout=QHBoxLayout()
        self.pdfWidget.setLayout(self.pdfWidgetHLayout)
        self.pdfWidgetHLayout.setContentsMargins(0,0,0,0)
        self.filePathWidget=FilePathSelectionWidgetEx(self,fileType="PDF Files(*.pdf)")
        transparentStyle=FYLStyleSheet.getTransparentButtonStyle()
        self._btnPreview=QPushButton("Preview")
        self._btnPreview.setStyleSheet(transparentStyle)
        self._btnPreview.clicked.connect(self.preview)
        self.pdfWidgetHLayout.addWidget(self.filePathWidget)
        self.pdfWidgetHLayout.addWidget(self._btnPreview)
        self.verticalLayout_2.insertWidget(1, self.pdfWidget)

        self._txtPath=self.filePathWidget.getPathWidget()
        # self._txtPath.textChanged.connect(self.pdfFileChanged)
        # self.verticalLayout_2.insertWidget(1,self.filePathWidget)

        # bodyFrameStyle=FYLStyleSheet.getStyleBodyFrame1()
        # bottomBodyFrameStyle= FYLStyleSheet.getStyleBottomBodyFrame1()

        bodyFrameStyle=FYLStyleSheet.getStyleTTDPDFSecureFrame()
        bottomBodyFrameStyle=FYLStyleSheet.getStyleTTDPDFSecureFrame()

        # self.titleFrame.setStyleSheet(titleFrameStyle)
        self.bodyFrame.setStyleSheet(bodyFrameStyle)
        self.bottomFrame.setStyleSheet(bottomBodyFrameStyle)
        self.progressBar.setVisible(False)
        self._btnClear.clicked.connect(self.clearFields)
        self._btnProtect.clicked.connect(self.protectPdf)
        self._lblProgressStatus.setMinimumHeight(15)
        self.outputFiles = ""




    def _addPreviewButton(self):
        self.pdfWidgetHLayout.insertWidget(1, self._btnPreview)

    def _removePreviewButton(self):
        self.pdfWidgetHLayout.removeWidget(self._btnPreview)


    def preview(self):

        selectedPdf = self.filePathWidget.getPath()
        if selectedPdf.strip()=="":
            QMessageBox.warning(self,"PDFFileNotSelected : ","Select PDF file")
            return
        docViewerWidget = PDFARViewerWidget()
        docContainer = DocViewContainer(self,docViewerWidget,selectedPdf)
        docContainer.preview()

    def protectPdf(self):
        pdfFilePath=self.filePathWidget.getPath()
        password=self._txtPassword.text()
        # password=self.editLinePassword.text()
        try:
            if pdfFilePath.lower()=="":
                raise ValueError("Please Select PDF File First")
            if password=="":
                raise ValueError("Please Enter Password")

            self.protectThread=ProtectPDFThread(pdfFilePath,password)
            self.protectThread.startedSignal.connect(self.protectingStarted)
            self.protectThread.processingPageStatusSignal.connect(self.lblStatusUpdate)
            self.protectThread.maxCurrentPageProgressBarSignal.connect(self.updateProgressBar)
            self.protectThread.completedSignal.connect(self.complete)
            self.protectThread.finallyStatusSignal.connect(self.finalFunc)
            self.protectThread.errorSignal.connect(self.errorFoundFound)
            self.protectThread.start()

        except BaseException as e:
            traceback.print_exc()
            QMessageBox.critical(self,"Error ",str(e))

    def updateProgressBar(self,currentValue,maxValue):
        self.progressBar.setMaximum(maxValue)
        self.progressBar.setValue(currentValue)

    def errorFoundFound(self,err):
        QMessageBox.critical(self,"Error Found",err)
        self.hideUpdateStatus()

    def setBottomButtonsVisibility(self,visibility:bool):
        self._btnProtect.setVisible(visibility)
        self._btnClear.setVisible(visibility)

    def showUpdateStatus(self):
        self.progressBar.setVisible(True)
        self.setBottomButtonsVisibility(False)
        styleSheet="""QLabel{
                        padding-left: 10px;   
                        font: 8pt Arial;
                        max-height: 16px;                     
                        color: rgb(255, 228, 239);
                        background-color: rgb(255, 29, 33);
                        }"""
        self._lblProgressStatus.setStyleSheet(styleSheet)

    def hideUpdateStatus(self):
        self.progressBar.setVisible(False)
        self.setBottomButtonsVisibility(True)
        styleSheet=""""""
        self._lblProgressStatus.setText("")
        self._lblProgressStatus.setStyleSheet(styleSheet)

    def protectingStarted(self):
        self.showUpdateStatus()

    def lblStatusUpdate(self,status):
        self._lblProgressStatus.setText(status)

    def complete(self,status:str):
        QMessageBox.information(self, "Encrypted Succesfully", status)
        self.hideUpdateStatus()

    def finalFunc(self):
        self.hideUpdateStatus()

    def clearFields(self):
        self._txtPath.setText("")
        self._txtPassword.clear()
        self._lblProgressStatus.setStyleSheet("")
        self._lblProgressStatus.setText("")



if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=ProtectedPdfFrame_WithoutTitleEx()
    dlg.show()
    app.exec()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFrame
# class ProtectedPdfFrame_WithoutTitle(QFrame):
#
#     def __init__(self):
#         super(ProtectedPdfFrame_WithoutTitle, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Frame=self