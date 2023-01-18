import pathlib
import traceback
from threading import Thread
from typing import List
from PIL import Image
from PyQt5.QtCore import QObject, pyqtSignal


class ExtractPng2Pdf_Thread(Thread, QObject):
    startedSignal = pyqtSignal() # This signal is sent when the process started
    processingStatusSignal = pyqtSignal(str)  # This signal is sent to update processing status.
    completedSignal = pyqtSignal(str) # This signal is sent when the processing is done succesfully without error
    finallyStatusSignal = pyqtSignal() #This signal is sent when finally is completed.
    errorSignal = pyqtSignal(str) #This signal is sent when there is error information
    maxCurrentPageProgressBarSignal = pyqtSignal(int,int)  # This signal is sent to update (currentPage,Maximum Page) . it is mainly for progress. It does not sent exact pages.

    def __init__(self,pngFilesList:List[str]):
        Thread.__init__(self)
        QObject.__init__(self)
        self._pngFileList=pngFilesList
        self._totalSteps=3+len(pngFilesList)
        self._currentStep=0

    def getPngFileList(self):
        fileList=self._pngFileList
        return fileList


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
            pngFileNameList=self.getPngFileList()
            _pngFile0 = pathlib.Path(pngFileNameList[0])
            # oN = _pngFile0.name[:pngFile0.name.find(pngFile0.suffix)]
            baseFileName=_pngFile0.with_suffix("").name
            baseFileName = "{}_merged.pdf".format(baseFileName)
            _outputFilePath = _pngFile0.with_name(baseFileName)
            images = []
            for pngFile in pngFileNameList:
                im = Image.open(pngFile)
                if im.mode == "RGBA":
                    im = im.convert("RGB")
                images.append(im)
                self.increaseCurrentStep()
                processingStatusSignal = "Reading File {} please wait...".format(pngFile)
                self.processingStatusSignal.emit(processingStatusSignal)

            processingStatusSignal = "Creating output File . . please wait . . ."
            self.processingStatusSignal.emit(processingStatusSignal)
            self.increaseCurrentStep()  # 2
            images[0].save(_outputFilePath.__str__(), save_all=True, quality=100, append_images=images[1:])
            self.increaseCurrentStep()  # 3
            processingStatusSignal = "successfully exported"
            self.processingStatusSignal.emit(processingStatusSignal)
            processingStatusSignal = "successfully exported.\n" \
                                     "Output File : {}".format(_outputFilePath.__str__())
            self.completedSignal.emit(processingStatusSignal)

        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
        finally:
            self.finallyStatusSignal.emit()

