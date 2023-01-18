import time
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal


class WaitingShowThread(Thread,QObject):
    pleaseWaitSignal=pyqtSignal(str)
    okSignal=pyqtSignal()


    def __init__(self):
        Thread.__init__(self)
        QObject.__init__(self)
        self.__stop=False
        self.__maxDotCount=5
        print("pleasing waiting created")

    def setStop(self):
        self.__stop=True

    def run(self) -> None:
        while not self.__stop:
            for i in range(1,self.__maxDotCount):
                if self.__stop:
                    break
                self.pleaseWaitSignal.emit("please wait {}".format(" . "*i))
                time.sleep(1)
        self.okSignal.emit()