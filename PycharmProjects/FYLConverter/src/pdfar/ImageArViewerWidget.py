from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel

from src.pdfar.DocViewerWidget import DocViewerWidget

class ImageArViewerWidget(DocViewerWidget,QWidget):

    def __init__(self,imageFilePath:str=None):
        super(ImageArViewerWidget, self).__init__()

        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0,0,0,0)
        self.setContentsMargins(0,0,0,0)
        self.setLayout(vLayout)
        self.label = QLabel()
        self.label.setScaledContents(True)
        if imageFilePath is not None:
            self.pixmap = QPixmap(imageFilePath)
            self.label.setPixmap(self.pixmap)
            self.resize(self.pixmap.width(), self.pixmap.height())
        vLayout.addWidget(self.label)


    def loadFile(self,imageFilePath):
        self.pixmap = QPixmap(imageFilePath)
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.label.setPixmap(self.pixmap)


