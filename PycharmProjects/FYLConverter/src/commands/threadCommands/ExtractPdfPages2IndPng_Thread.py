import pathlib
import time
import traceback
from threading import Thread
from typing import List
import pdf2image
from PyQt5.QtCore import pyqtSignal, QObject

class ExtractPdfPages2IndPng_Thread(Thread, QObject):
    startedSignal = pyqtSignal() # This signal is sent when the process started
    processingStatusSignal = pyqtSignal(str)  # This signal is sent to update processing status.
    # outputSummaryStatusSignal=pyqtSignal(str)
    completedSignal = pyqtSignal(str) # This signal is sent when the processing is done succesfully without error
    finallyStatusSignal = pyqtSignal() #This signal is sent when finally is completed.
    errorSignal = pyqtSignal(str) #This signal is sent when there is error information
    maxCurrentPageProgressBarSignal = pyqtSignal(int,int)  # This signal is sent to update (currentPage,Maximum Page) . it is mainly for progress. It does not sent exact pages.
    #
    # outputFilesSignal = pyqtSignal(str)
    # totalPageCountSignal=pyqtSignal(int)


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

    def run(self):

        self.startedSignal.emit()
        self.increaseCurrentStep()
        _pdfFilePath=self.getFilePath()
        requiredPageList=self.getRequiredPageList()
        # fileBaseName = pdfFilePath.replace(".pdf", "")
        fileBaseName= _pdfFilePath.with_suffix("").name
        _outputPath=_pdfFilePath.parent
        processedPages = []
        failedPages=[]
        try:
            totalPdfPages = int(pdf2image.pdfinfo_from_path(_pdfFilePath.__str__())["Pages"])
            for i in requiredPageList:
                pg = i
                if pg > totalPdfPages:
                    raise ValueError(
                        "Page is not in range, provided page: '{}' , total page : '{}'".format(i, totalPdfPages))

            processingStatusSignal="Reading File.. please wait..."
            self.increaseCurrentStep()
            self.processingStatusSignal.emit(processingStatusSignal)
            imgs = pdf2image.convert_from_path(_pdfFilePath.__str__())
            processingStatusSignal = "processing File.."
            self.processingStatusSignal.emit(processingStatusSignal)
            self.increaseCurrentStep()

            for i in requiredPageList:
                # time.sleep(1)
                ofName = "{}_{}.png".format(fileBaseName, i)
                _ofName = _outputPath / ofName
                try:
                    processingStatusSignal = "processing page : {}".format(i)
                    self.processingStatusSignal.emit(processingStatusSignal)
                    imgs[i - 1].save(_ofName.__str__())
                    processingStatusSignal = "created File : {}".format(_ofName.__str__())
                    self.processingStatusSignal.emit(processingStatusSignal)
                    processedPages.append(i)
                except:
                    failedPages.append(i)
                finally:
                    self.increaseCurrentStep()
            self.increaseCurrentStep()
            outputSummaryStatus="Pages exported succesfully.\n" \
                                "Number Pages Required :{} \n" \
                                       "Extracted Pages Count : {}\n" \
                                       "Failed to extract : {}\n" \
                                "Output File : {}".format(len(requiredPageList),len(processedPages),len(failedPages),_outputPath.__str__())
            # self.outputSummaryStatusSignal.emit(outputSummaryStatus)
            self.processingStatusSignal.emit("process done")
            self.completedSignal.emit(outputSummaryStatus)

        # except PdfReadError as e:
        #     traceback.print_exc()
        #     strError="File :'{}'\n pdf is not readable may be currupted or protected".format(pdfFilePath)
        #     self.errorSignal.emit(strError)
        #     # raise PdfReadError()
        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
            # raise PdfReadError()
        finally:
            self.finallyStatusSignal.emit()

        # oPath=Commands.pdf2Pngs(self.__pdfFilePath,self.__pageList)
        # fNames = "; ".join(oPath)
        # self.outputFilesSignal.emit(fNames)
        # self.completedSignal.emit()
