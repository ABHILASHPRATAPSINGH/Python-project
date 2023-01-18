from abc import abstractmethod
from PyQt5.QtWidgets import QWidget


class DocViewerWidget(QWidget):

    def __init__(self):
        super(DocViewerWidget, self).__init__()

    @abstractmethod
    def loadFile(self):
        pass