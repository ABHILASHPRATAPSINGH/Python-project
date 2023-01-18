import time
import traceback
from threading import Thread
from typing import Tuple

from PyQt5.QtCore import QObject, pyqtSignal
from PyPDF2.utils import PdfReadError
import PyPDF2 as pdf

class ProtectPDFThread(Thread, QObject):

    startedSignal = pyqtSignal() # This signal is sent when the process started
    completedSignal = pyqtSignal(str) # This signal is sent when the processing is done succesfully without error
    outputFilesSignal = pyqtSignal(str)
    processingPageStatusSignal=pyqtSignal(str)  # This signal is sent to update processing status.
    maxCurrentPageProgressBarSignal=pyqtSignal(int,int) #This signal is sent to update (currentPage,Maximum Page) . it is mainly for progress. It does not sent exact pages.
    finallyStatusSignal=pyqtSignal() #This signal is sent when finally is completed.
    errorSignal=pyqtSignal(str) #This signal is sent when there is error information
    totalPageCountSignal=pyqtSignal(int)

    def __init__(self,pdfFilePath:str,password:str):
        Thread.__init__(self)
        QObject.__init__(self)
        self.__pdfFilePath=pdfFilePath
        self.__password=password

    def getFilePath(self)->str:
        filePath=self.__pdfFilePath
        return filePath

    def getPassword(self)->str:
        password=self.__password
        return password

    def run(self) -> None:
        self.startedSignal.emit()
        pdfFilePath=self.getFilePath()
        password=self.getPassword()
        fileBaseName = pdfFilePath.replace(".pdf", "")
        try:
            pdfReader = pdf.PdfFileReader(pdfFilePath)
            pdfPagesCount = pdfReader.getNumPages()
            self.totalPageCountSignal.emit(pdfPagesCount)
            pdfWriter = pdf.PdfFileWriter()
            page_suffix = "protected"
            readPagesList=[]
            maxPage=2*pdfPagesCount
            currPage=1
            for i in range(pdfPagesCount):
                processStatusStr="reading page {}".format(i+1)
                self.processingPageStatusSignal.emit(processStatusStr)
                pageContent = pdfReader.getPage(i)
                readPagesList.append(pageContent)
                self.maxCurrentPageProgressBarSignal.emit(currPage,maxPage)
                currPage=currPage+1
                time.sleep(0.03)

            for i in range(pdfPagesCount):
                processStatusStr="writing page {}".format(i+1)
                self.processingPageStatusSignal.emit(processStatusStr)
                pdfWriter.addPage(readPagesList[i])
                self.maxCurrentPageProgressBarSignal.emit(currPage,maxPage)
                currPage=currPage+1
                time.sleep(0.03)

            self.processingPageStatusSignal.emit("encripting pages")
            pdfWriter.encrypt(password)

            oFilePath = "{}_{}.pdf".format(fileBaseName, page_suffix)
            self.processingPageStatusSignal.emit("please wait . . . encrypting file")
            with open(oFilePath, "wb") as f:  # 1 is added as python starts indexing from 0
                pdfWriter.write(f)
            self.processingPageStatusSignal.emit("protected file : {} created".format(oFilePath))
            self.outputFilesSignal.emit(oFilePath)
            outputStatus="Encrypted Succesfully.\n" \
                         "Encrypted File : {}".format(oFilePath)
            self.completedSignal.emit(outputStatus)

        except PdfReadError as e:
            traceback.print_exc()
            strError="File :'{}'\n pdf is not readable may be currupted or protected".format(pdfFilePath)
            self.errorSignal.emit(strError)
            # raise PdfReadError()
        except BaseException as e:
            traceback.print_exc()
            strError=str(e)
            self.errorSignal.emit(strError)
            # raise PdfReadError()
        finally:
            self.finallyStatusSignal.emit()

        # return oFilePath
        # self.outputFilesSignal.emit(oFilePath)
        # self.completedSignal.emit()