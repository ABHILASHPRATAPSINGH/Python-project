import os
import sys
import traceback

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication

from src.commands.threadCommands.ExtractPng2Pdf_Thread import ExtractPng2Pdf_Thread
from src.pdfar.ImageArViewerWidget import ImageArViewerWidget
from src.userform import FYLStyleSheet
from src.userform.Png2PdfFrame_WithoutTitle import Png2PdfFrame_WithoutTitle


class Png2PdfFrame_WithoutTitleEx(Png2PdfFrame_WithoutTitle):

    def setPreviewNoImageAvailable(self):
        self._imageWidget.loadFile(":/resources/images/resources/images/NoImageAvailable.png")
        # self.preview.setPixmap(QtGui.QPixmap())
        # self._lblFrameIcon.setScaledContents(True)


    def __init__(self):

        super(Png2PdfFrame_WithoutTitleEx, self).__init__()
        self.listWidget.currentRowChanged.connect(self.onImageSelectionChanged)

        bodyFrameStyle = FYLStyleSheet.getStylePNG2PDFWithoutTitle()

        # previewWidgetStyle=FYLStyleSheet.getPreviewWidgetStyle()
        self.framePngList.setStyleSheet(bodyFrameStyle)
        self.framePngPreview.setStyleSheet(bodyFrameStyle)
        self.framePngControls.setStyleSheet(bodyFrameStyle)

        self._lblPreviewHeading.setStyleSheet(bodyFrameStyle)
        self._lblFileListHeading.setStyleSheet(bodyFrameStyle)

        self._imageWidget=ImageArViewerWidget()
        self._imageWidget.setContentsMargins(0,0,0,0)
        self._imageWidget.setStyleSheet(bodyFrameStyle)
        self._imageWidget.setMinimumSize(QtCore.QSize(320, 150))
        self._imageWidget.setMaximumSize(QtCore.QSize(400, 150))
        self.setPreviewNoImageAvailable()
        self.verticalLayout_previewLayout.addWidget(self._imageWidget)


        # bodyFrameStyle = FYLStyleSheet.getStyleTTDPDFSecureFrame()
        # bottomBodyFrameStyle = FYLStyleSheet.getStyleTTDPDFSecureFrame()
        self.bodyFrame.setStyleSheet(bodyFrameStyle)
        self.bottomFrame.setStyleSheet(bodyFrameStyle)

        self._btnAddImage.clicked.connect(self.addImageFile)
        self._btnRemoveImage.clicked.connect(self.removeImageFile)
        self._btnMoveImageUp.clicked.connect(self.moveUpImageFile)
        self._btnMoveImageDown.clicked.connect(self.moveDownImageFile)
        self._btnExportPng2Pdf.clicked.connect(self.exportPng2Pdf)
        self._btnClear.clicked.connect(self.clear)
        self.progressBar.setVisible(False)

    def clear(self):
        try:
            self.listWidget.blockSignals(True)
            self.listWidget.clear()
        finally:
            self.listWidget.blockSignals(False)
        self._txtTotalPages.setText("")
        self.setPreviewNoImageAvailable()

    def getPngFileList(self):
        itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
        return itemsTextList

    def exportPng2Pdf(self):
        pngFileList = self.getPngFileList()
        try:
            if len(pngFileList) == 0:
                raise ValueError("No any png file is selected")
            self.png2PdfThread=ExtractPng2Pdf_Thread(pngFileList)
            self.png2PdfThread.startedSignal.connect(self.threadStarted)
            self.png2PdfThread.processingStatusSignal.connect(self.lblStatusUpdate)
            self.png2PdfThread.maxCurrentPageProgressBarSignal.connect(self.updateProgressBar)
            self.png2PdfThread.completedSignal.connect(self.complete)
            self.png2PdfThread.finallyStatusSignal.connect(self.finalFunc)
            self.png2PdfThread.errorSignal.connect(self.errorFoundFound)
            self.png2PdfThread.start()

        except BaseException as e:
            traceback.print_exc()
            QMessageBox.critical(self,"Error ",str(e))


    def onImageSelectionChanged(self,imageRow):
        if imageRow>=0:
            imageName=self.listWidget.item(imageRow).text()
            self._imageWidget.loadFile(imageName)
        else:
            self.setPreviewNoImageAvailable()

    def addImageFile(self):
        try:
            self.listWidget.blockSignals(True)
            defaultPath=os.path.expanduser('~/Desktop')
            fNames = QFileDialog.getOpenFileNames(self, "Select PNG File", defaultPath, "PNG Files(*.png *.jpg *.jpeg)")
            fNames=fNames[0]
            # itemsTextList = [str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())]
            for fN in fNames:
                # if fN not in itemsTextList:
                self.listWidget.addItem(fN)
        finally:
            self.listWidget.blockSignals(False)
        self.updateTotalPagesListWidget()

    def updateTotalPagesListWidget(self):
        totalWidgetCount=self.listWidget.count()
        self._txtTotalPages.setText(str(totalWidgetCount))

    def removeImageFile(self):
        # items=self.listWidget.selectedItems()
        currentRow=self.listWidget.currentRow()
        if currentRow==-1:
            QMessageBox.warning(self,"Status","Please select item to remove")
            return
        self.listWidget.takeItem(currentRow)
        self.updateTotalPagesListWidget()

    def moveUpImageFile(self):
        currentRow=self.listWidget.currentRow()
        if currentRow==-1:
            QMessageBox.warning(self, "Status", "Please select item to move up")
            return

        targetRow=currentRow-1
        if currentRow==0:
            return
        else:
            self.swapListWidgetItems(currentRow,targetRow)

    def swapListWidgetItems(self,currentRow:int,targetRow:int):
        currentRowItem = self.listWidget.item(currentRow)
        currentRowItemText = currentRowItem.text()
        targetRowItem = self.listWidget.item(targetRow)
        futureRowItemText = targetRowItem.text()
        currentRowItem.setText(futureRowItemText)
        targetRowItem.setText(currentRowItemText)
        self.listWidget.setCurrentRow(targetRow)

    def moveDownImageFile(self):
        currentRow=self.listWidget.currentRow()
        if currentRow==-1:
            QMessageBox.warning(self, "Status", "Please select item to move down")
            return

        targetRow=currentRow+1
        lastIndex=self.listWidget.count()-1
        if currentRow==lastIndex:
            return
        else:
            self.swapListWidgetItems(currentRow,targetRow)

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
        # print("Current Value:- ",currentValue,"Max value : ",maxValue)
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

if __name__ == '__main__':
    app=QApplication(sys.argv)
    f=Png2PdfFrame_WithoutTitleEx()
    f.show()
    app.exec_()

# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QFrame
# import resources
#
# class Png2PdfFrame_WithoutTitle(QFrame):
#
#     def __init__(self):
#         super(Png2PdfFrame_WithoutTitle, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Frame=self
