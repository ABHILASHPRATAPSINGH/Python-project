import traceback

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox

from src.commands import Commands
from src.commands.threadCommands.ExtractPdfPages2IndPdf_Thread import ExtractPdfPages2IndPdf_Thread
from src.pdfar.DocViewContainer import DocViewContainer
from src.pdfar.PDFARViewerWidget import PDFARViewerWidget
from src.userform import FYLStyleSheet
from src.userform.Pdf2SeperatePdfFrame import Pdf2SeperatePdfFrame
from src.userform.ext.FilePathSelectionWidgetEx import FilePathSelectionWidgetEx


class Pdf2SeperatePdfFrameEx(Pdf2SeperatePdfFrame):

    def __init__(self):
        super(Pdf2SeperatePdfFrameEx, self).__init__()

        self.pdfWidget=QWidget()
        self.pdfWidget.setContentsMargins(0,0,0,0)
        self.pdfWidgetHLayout=QHBoxLayout()
        self.pdfWidget.setLayout(self.pdfWidgetHLayout)
        self.pdfWidgetHLayout.setContentsMargins(0,0,0,0)
        self._txtTotalPages.setEnabled(False)
        self._txtTotalPages.setText("0")
        self.filePathWidget=FilePathSelectionWidgetEx(self,fileType="PDF Files(*.pdf)")
        self._inputPathWidget=self.filePathWidget.getPathWidget()
        self._inputPathWidget.textChanged.connect(self.pdfFileChanged)

        transparentStyle=FYLStyleSheet.getTransparentButtonStyle()
        self._btnPreview=QPushButton("Preview")
        self._btnPreview.setStyleSheet(transparentStyle)
        self._btnPreview.clicked.connect(self.preview)
        self.pdfWidgetHLayout.addWidget(self.filePathWidget)
        self.pdfWidgetHLayout.addWidget(self._btnPreview)

        self.verticalLayout_2.insertWidget(1, self.pdfWidget)

        titleFrameStyle=FYLStyleSheet.getStyleTitleFrame()
        self.titleFrame.setStyleSheet(titleFrameStyle)

        bodyFrameStyle=FYLStyleSheet.getStyleBodyFrame3()
        self.bodyFrame.setStyleSheet(bodyFrameStyle)
        self._btnClear.clicked.connect(self.clear)
        self._btnExport2SeperatePdf.clicked.connect(self.exportPdf2SeperatePdf)
        bottomFrameStyle=FYLStyleSheet.getStyleBottomBodyFrame3()
        self.bottomFrame.setStyleSheet(bottomFrameStyle)
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




# from PyQt5.QtWidgets import QFrame
# import resources

# class Pdf2SeperatePdfFrame(QFrame):
#     def __init__(self):
#         super(Pdf2SeperatePdfFrame, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Frame = self