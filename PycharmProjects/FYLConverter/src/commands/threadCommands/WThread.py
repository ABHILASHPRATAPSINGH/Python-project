from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal


class WThread(Thread, QObject):
    startedSignal = pyqtSignal()
    completedSignal = pyqtSignal()

    def __init__(self):
        Thread.__init__(self)
        QObject.__init__(self)