import time
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal, QObject

from src.commands import Commands


class ProtectPdf_Thread(Thread, QObject):
    startedSignal = pyqtSignal()
    completedSignal = pyqtSignal()
    outputFilesSignal = pyqtSignal(str)

    def __init__(self,pdfFilePath:str,password:str):
        Thread.__init__(self)
        QObject.__init__(self)
        self.__pdfFilePath=pdfFilePath
        self.__password=password

    def run(self) -> None:
        self.startedSignal.emit()
        oPath=Commands.protectPdf(self.__pdfFilePath,self.__password)
        self.outputFilesSignal.emit(oPath)
        self.completedSignal.emit()

class _ProtectPdf_Thread(Thread,QObject):
    statusSignal=pyqtSignal(str)
    pbarStatus=pyqtSignal(int)
    completeStatus=pyqtSignal()
    stopSignal=pyqtSignal()

    def __init__(self):
        Thread.__init__(self)
        QObject.__init__(self)

        print("Thread Created")
        
    def run(self) -> None:
        self.statusSignal.emit("Please wait")
        for i in range(20):
            st="Please Wait {}".format("."*i)
            # self.statusSignal.emit(st)
            # j=i+1
            # self.pbarStatus.emit(j)
            # print(st)
            time.sleep(1)
        self.completeStatus.emit()



