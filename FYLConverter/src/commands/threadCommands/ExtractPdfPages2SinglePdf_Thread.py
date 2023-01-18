import pathlib
import traceback
from threading import Thread
from typing import List

from PyPDF2 import pdf
from PyQt5.QtCore import pyqtSignal, QObject

from src.commands import Commands
from src.commands.threadCommands.WThread import WThread


class ExtractPdfPages2SinglePdf_Thread(Thread, QObject):

    # outputFilesSignal=pyqtSignal(str)
    startedSignal = pyqtSignal() # This signal is sent when the process started
    processingStatusSignal = pyqtSignal(str)  # This signal is sent to update processing status.
    completedSignal = pyqtSignal(str) # This signal is sent when the processing is done succesfully without error
    finallyStatusSignal = pyqtSignal() #This signal is sent when finally is completed.
    errorSignal = pyqtSignal(str) #This signal is sent when there is error information
    maxCurrentPageProgressBarSignal = pyqtSignal(int,int)  # This signal is sent to update (currentPage,Maximum Page) . it is mainly for progress. It does not sent exact pages.

    def __init__(self,pdfFilePath:str,requiredPageList:List[int]):
        Thread.__init__(self)
        QObject.__init__(self)
        self._pdfFilePath=pdfFilePath
        self._requiredPageList=requiredPageList
        self._totalSteps=4+len(requiredPageList)
        self._currentStep=0

    def getFilePath(self)->pathlib.Path:
        _filePath=pathlib.Path(self._pdfFilePath)
        return _filePath

    def getRequiredPageList(self)->List[int]:
        requiredPageList=self._requiredPageList
        return requiredPageList

    def increaseCurrentStep(self):
        self._currentStep=self._currentStep+1
        # self._totalSteps= self._totalSteps - 1
        self.maxCurrentPageProgressBarSignal.emit(self._currentStep, self._totalSteps)

    def run(self) -> None:
        try:
            self.startedSignal.emit()
            self.increaseCurrentStep()#1
            _pdfFilePath=self.getFilePath()
            requiredPageList=self.getRequiredPageList()
            fileBaseName= _pdfFilePath.with_suffix("").name
            _outputPath=_pdfFilePath.parent
            self.increaseCurrentStep() #2
            processingStatusSignal = "Reading File.. please wait..."
            self.processingStatusSignal.emit(processingStatusSignal)
            pdfReader = pdf.PdfFileReader(_pdfFilePath.__str__())
            totalPdfPages = pdfReader.getNumPages()
            for i in requiredPageList:
                pg=i-1
                if pg> totalPdfPages:
                    raise ValueError("Page is not in range, provided page: '{}' , total page : '{}'".format(i,totalPdfPages+1))
            pdfWriter = pdf.PdfFileWriter()
            page_suffix = "_".join([str(i) for i in requiredPageList])
            fileBaseNameLength=len(fileBaseName)
            pageSuffixLen=len(page_suffix)
            if (pageSuffixLen+fileBaseNameLength)>=240:
                page_suffix=page_suffix[:(95-fileBaseNameLength)]

            processingStatusSignal = "Reading pages.. please wait..."
            self.processingStatusSignal.emit(processingStatusSignal)
            for i in requiredPageList:
                pageI = pdfReader.getPage(i - 1)
                pdfWriter.addPage(pageI)
                processingStatusSignal = "extracting page...{} please wait...".format(i)
                self.processingStatusSignal.emit(processingStatusSignal)
                self.increaseCurrentStep()

            oFileName = "{}_{}.pdf".format(fileBaseName, page_suffix)
            self.increaseCurrentStep()#3
            processingStatusSignal = "creating output file..please wait..."
            self.processingStatusSignal.emit(processingStatusSignal)
            oFilePath = _outputPath / oFileName
            with open(oFilePath.__str__(), "wb") as f:  # 1 is added as python starts indexing from 0
                pdfWriter.write(f)
            self.processingStatusSignal.emit("process done")
            self.increaseCurrentStep() #4
            outputSummaryStatus="PDF Extracted Successfully.\n" \
                                "Output File : '{}'".format(oFilePath.__str__())
            self.completedSignal.emit(outputSummaryStatus)

        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
        finally:
            self.finallyStatusSignal.emit()
        # return oFilePath

