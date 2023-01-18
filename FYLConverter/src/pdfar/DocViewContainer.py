
from pathlib import Path
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame
from src.pdfar.DocViewerWidget import DocViewerWidget

class DocViewContainer():

    def __init__(self,parent:QFrame,viewer:DocViewerWidget,fileToView:str):
        # previewWind=QDialog(parent)
        # previewWind.setWindowTitle("Doc Viewer")
        # vBoxLayout=QVBoxLayout()
        # viewer.loadFile()
        # viewer.loadFile(fileToView)
        # vBoxLayout.addWidget(viewer)
        # previewWind.setLayout(vBoxLayout)
        # previewWind.resize(parent.width()-40, parent.height()-40)
        # previewWind.exec_()
        self._parent=parent
        self._viewer=viewer
        self._fileToView=fileToView
        self._title="Doc Viewer"
        self._fileToView=Path(fileToView)

    def getFileToView(self)->str:
        if not self._fileToView.exists():
            raise FileNotFoundError("File : '{}' not found".format(self._fileToView.__str__()))
        fileToView=str(self._fileToView)
        return fileToView

    def getViewer(self)->DocViewerWidget:
        viewer=self._viewer
        return viewer

    def getTitle(self):
        title=self._title
        return title

    def getParent(self):
        parent=self._parent
        return parent

    def preview(self):
        parent=self.getParent()
        title=self.getTitle()
        fileToView=self.getFileToView()
        viewer=self.getViewer()
        previewWind=QDialog(parent)
        previewWind.setWindowTitle(title)
        vBoxLayout=QVBoxLayout()
        viewer.loadFile(fileToView)
        vBoxLayout.addWidget(viewer)
        previewWind.setLayout(vBoxLayout)
        previewWind.resize(parent.width()-40, parent.height()-40)
        previewWind.exec_()