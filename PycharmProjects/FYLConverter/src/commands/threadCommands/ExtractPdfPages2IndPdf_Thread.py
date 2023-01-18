import pathlib
import traceback
from threading import Thread
from typing import List
from PyPDF2 import pdf
from PyQt5.QtCore import pyqtSignal, QObject

class ExtractPdfPages2IndPdf_Thread(Thread, QObject):

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
        self._totalSteps=3+(2*len(requiredPageList))
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

    def run(self):
        try:
            self.startedSignal.emit()
            self.increaseCurrentStep()#1
            processingStatusSignal = "Exporting initiated.. please wait..."
            self.processingStatusSignal.emit(processingStatusSignal)
            _pdfFilePath=self.getFilePath()
            requiredPageList=self.getRequiredPageList()
            fileBaseName= _pdfFilePath.with_suffix("").name
            _outputPath=_pdfFilePath.parent
            self.increaseCurrentStep()  # 2
            processingStatusSignal = "Reading File.. please wait..."
            self.processingStatusSignal.emit(processingStatusSignal)
            pdfReader = pdf.PdfFileReader(_pdfFilePath.__str__())
            totalPdfPages = pdfReader.getNumPages()
            for i in requiredPageList:
                pg=i-1
                if pg> totalPdfPages:
                    raise ValueError("Page is not in range, provided page: '{}' , total page : '{}'".format(i,totalPdfPages+1))

            readPages={}            
            for i in requiredPageList:
                indPdfFileName="{}_{}.pdf".format(fileBaseName,i)
                pageI = pdfReader.getPage(i - 1)
                readPages[indPdfFileName]=pageI
                self.increaseCurrentStep()
                processingStatusSignal = "Reading page..{} please wait...".format(i)
                self.processingStatusSignal.emit(processingStatusSignal)


            for pdfN,pdfData in readPages.items():
                pdfWriter = pdf.PdfFileWriter()
                pdfWriter.addPage(pdfData)
                _indPdfFilePath=_outputPath / pdfN                
                with open(_indPdfFilePath.__str__(), "wb") as f:  # 1 is added as python starts indexing from 0
                    pdfWriter.write(f)
                self.increaseCurrentStep()
                processingStatusSignal = "created file : {} ".format(_indPdfFilePath.__str__())
                self.processingStatusSignal.emit(processingStatusSignal)

            self.processingStatusSignal.emit("process done")
            self.increaseCurrentStep()#3
            outputSummaryStatus="PDF Extracted Successfully.\n" \
                                "Output Folder : {}".format(_outputPath.__str__())
            self.completedSignal.emit(outputSummaryStatus)


        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
        finally:
            self.finallyStatusSignal.emit()
