import pathlib
import traceback
from threading import Thread
from typing import List
import pdf2image
from PyQt5.QtCore import pyqtSignal, QObject

class ExtractPdf2ImagedPdf_Thread(Thread, QObject):
    startedSignal = pyqtSignal() # This signal is sent when the process started
    processingStatusSignal = pyqtSignal(str)  # This signal is sent to update processing status.
    # outputSummaryStatusSignal=pyqtSignal(str)
    completedSignal = pyqtSignal(str) # This signal is sent when the processing is done succesfully without error
    finallyStatusSignal = pyqtSignal() #This signal is sent when finally is completed.
    errorSignal = pyqtSignal(str) #This signal is sent when there is error information
    maxCurrentPageProgressBarSignal = pyqtSignal(int,int)  # This signal is sent to update (currentPage,Maximum Page) . it is mainly for progress. It does not sent exact pages.

    def __init__(self,pdfFilePath:str,requiredPageList:List[int]):
        Thread.__init__(self)
        QObject.__init__(self)
        self._pdfFilePath=pdfFilePath
        self._requiredPageList=requiredPageList
        self._totalSteps=3
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

        self.startedSignal.emit()
        self.increaseCurrentStep()
        _pdfFilePath=self.getFilePath()
        requiredPageList=self.getRequiredPageList()
        # fileBaseName = pdfFilePath.replace(".pdf", "")
        fileBaseName= _pdfFilePath.with_suffix("").name
        imagedPdfFileName="Imaged_" +fileBaseName +".pdf"
        _outputPath=_pdfFilePath.parent
        _imagePdfOutputPath=_pdfFilePath.parent / imagedPdfFileName
        try:
            totalPdfPages = int(pdf2image.pdfinfo_from_path(_pdfFilePath.__str__())["Pages"])
            for i in requiredPageList:
                pg = i
                if pg > totalPdfPages:
                    raise ValueError(
                        "Page is not in range, provided page: '{}' , total page : '{}'".format(i, totalPdfPages))

            # Reading pdf file
            processingStatusSignal="Reading File.. please wait..."
            self.increaseCurrentStep()
            self.processingStatusSignal.emit(processingStatusSignal)
            images = pdf2image.convert_from_path(_pdfFilePath.__str__())
            requiredImages=[]
            for i in requiredPageList:
                # time.sleep(1)
                requiredImages.append(images[i-1])
            processingStatusSignal = "Output File is creating.. please wait..."
            self.increaseCurrentStep()
            self.processingStatusSignal.emit(processingStatusSignal)
            requiredImages[0].save(_imagePdfOutputPath.__str__(), save_all=True, quality=20, append_images=requiredImages[1:],optimize=True)
            self.increaseCurrentStep()
            outputSummaryStatus="Imaged pdf exported succesfully.\n" \
                                "Output File : {}".format(_imagePdfOutputPath.__str__())
            # self.outputSummaryStatusSignal.emit(outputSummaryStatus)
            self.processingStatusSignal.emit("process done")
            self.completedSignal.emit(outputSummaryStatus)

        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
            # raise PdfReadError()
        finally:
            self.finallyStatusSignal.emit()