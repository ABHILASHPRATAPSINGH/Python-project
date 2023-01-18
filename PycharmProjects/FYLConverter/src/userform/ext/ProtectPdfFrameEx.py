import traceback
from PyQt5.QtWidgets import QMessageBox, QWidget, QHBoxLayout, QPushButton
from src.commands.threadCommands.ProtectPDFThread import ProtectPDFThread
from src.commands.threadCommands.ProtectPdf_Thread import ProtectPdf_Thread
from src.commands.threadCommands.WaitingShowThread import WaitingShowThread
from src.pdfar.DocViewContainer import DocViewContainer
from src.pdfar.PDFARViewerWidget import PDFARViewerWidget
from src.userform import FYLStyleSheet
from src.userform.ProtectPdfFrame import ProtectPdfFrame
from src.userform.ext.FilePathSelectionWidgetEx import FilePathSelectionWidgetEx

class ProtectPdfFrameEx(ProtectPdfFrame):

    def __init__(self):

        super(ProtectPdfFrameEx, self).__init__()

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

        titleFrameStyle=FYLStyleSheet.getStyleTitleFrame()
        bodyFrameStyle=FYLStyleSheet.getStyleBodyFrame1()
        bottomBodyFrameStyle= FYLStyleSheet.getStyleBottomBodyFrame1()
        self.titleFrame.setStyleSheet(titleFrameStyle)
        self.bodyFrame.setStyleSheet(bodyFrameStyle)
        self.bottomFrame.setStyleSheet(bottomBodyFrameStyle)
        self.progressBar.setVisible(False)
        self._btnClear.clicked.connect(self.clearFields)
        self._btnProtect.clicked.connect(self.protectPdf)
        self.outputFiles = ""

    def preview(self):

        selectedPdf = self.filePathWidget.getPath()
        if selectedPdf.strip()=="":
            QMessageBox.warning(self,"PDFFileNotSelected : ","Select PDF file")
            return
        docViewerWidget = PDFARViewerWidget()
        docContainer = DocViewContainer(self,docViewerWidget,selectedPdf)
        docContainer.preview()

    def _addPreviewButton(self):
        self.pdfWidgetHLayout.insertWidget(1, self._btnPreview)

    def _removePreviewButton(self):
        self.pdfWidgetHLayout.removeWidget(self._btnPreview)

    # def pdfFileChanged(self):
    #     try:
    #         selectedPdf=self.filePathWidget.getPath()
    #         if selectedPdf.strip()!="":
    #             self._addPreviewButton()
    #         else:
    #             self._removePreviewButton()
    #     except BaseException as e:
    #         self._removePreviewButton()
    #         QMessageBox.critical(self,"ValueError",str(e))


    def protectPdf(self):
        pdfFilePath=self.filePathWidget.getPath()
        password=self._txtPassword.text()
        # password=self.editLinePassword.text()
        try:
            if pdfFilePath.lower()=="":
                raise ValueError("Please Select PDF File First")
            if password=="":
                raise ValueError("Please Enter Password")

            # self.waitingShowThread=WaitingShowThread()
            # self.waitingShowThread.pleaseWaitSignal.connect(self.lblStatusUpdate)
            # self.waitingShowThread.okSignal.connect(self.afterProcessingUpdate)

            # self.protectThread=ProtectPdf_Thread(pdfFilePath,password)
            # self.protectThread.startedSignal.connect(self.protectingStarted)
            # self.protectThread.outputFilesSignal.connect(self.setOutputFiles)
            # self.protectThread.completedSignal.connect(self.protectingFinished)

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

    def hideUpdateStatus(self):
        self.progressBar.setVisible(False)
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
        # self.hideUpdateStatus()



    # def updateProcessStatus(self,progressStatus):
    #     self.lblStatusUpdate(progressStatus)
        # self._lblProcessStatus.setText(progressStatus)

    # def setOutputFiles(self,outputFiles:str):
    #     self.outputFiles=outputFiles

    # def getOutputFiles(self)->str:
    #     outputFiles=self.outputFiles
    #     return outputFiles

    def clearFields(self):
        self._txtPath.setText("")
        self._txtPassword.clear()
        self._lblProgressStatus.setStyleSheet("")
        self._lblProgressStatus.setText("")

    # def stopThread(self):
    #     try:
    #         self.protectThread.disconnect()
    #     except BaseException as e:
    #         print(e)


# from PyQt5.QtWidgets import QFrame
# import resources

# class ProtectPdfFrame(QFrame):
#     def __init__(self):
#         super(ProtectPdfFrame, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Frame = self

def toDict(age:int,name:str)->None:
    """
    It prints the given age and name as dict.
    :param age: it will be value of key
    :param name: it will be used as key of dict
    :return: None
    """
    d=dict()
    d[name]=age
    print(d)
# a=toDict(25,"Arjuna")
# print(a,type(a))


