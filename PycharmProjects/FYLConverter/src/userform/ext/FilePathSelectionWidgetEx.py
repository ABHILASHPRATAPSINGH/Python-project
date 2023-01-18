import os
import sys
from enum import Enum
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton, QApplication
from src.userform.FilePathSelectionWidget import FilePathSelectionWidget


class PathType(Enum):
    FILE="file"
    DIR="dir"


class FilePathSelectionWidgetEx(FilePathSelectionWidget):

    def __init__(self,parent,pathType:PathType=PathType.FILE,dialogTitle:str="Choose File",fileType:str="Excel Files(*.xls *.xlsx)",defaultPath="Desktop"):
        super().__init__(parent)
        self.__pathType=pathType
        self.__dialogTitle=dialogTitle
        self.__fileType=fileType
        self.__defaultPath=os.path.expanduser('~/Desktop')

        self.btnBrowse.clicked.connect(self.browsePath)
        self.lineEditPath.setEnabled(False)

        # lineEditStyle=self.getStyleLineEdit()
        # self.lineEditPath.setStyleSheet(lineEditStyle)
        # btnBrowseStyle=self.getStyleBtnBrowse()
        # self.btnBrowse.setStyleSheet(btnBrowseStyle)

    def getStyleLineEdit(self):
        style="""
                border-radius: 5px;
                margin: 0px 20px 0px 0px;
            """
        return style

    def getStyleBtnBrowse(self):
        style="""
                border-radius: 5px;
                min-width: 150px;
                background-color:rgb(0, 255, 1);
                color: rgb(0, 0, 0);            
                    
            """
        return style

    def getDialogTitle(self):
        dialog=self.__dialogTitle
        return dialog

    def getFileType(self):
        fileType=self.__fileType
        return fileType

    def getPathType(self)->PathType:
        pathType=self.__pathType
        return pathType

    def browsePath(self):
        selectedPath=self.lineEditPath.text()
        pathType=self.getPathType()
        if selectedPath.strip()!="":
            if pathType == PathType.DIR:
                defaultPath=selectedPath
            elif pathType == PathType.FILE:
                defaultPath=toPath(selectedPath).parent.__str__()
        else:
            defaultPath=self.__defaultPath

        dialogTitle=self.getDialogTitle()
        if pathType == PathType.DIR:
            path = QFileDialog.getExistingDirectory(self,dialogTitle,defaultPath)
            self.lineEditPath.setText(path)

        elif pathType == PathType.FILE :
            fileType = self.getFileType()
            fName=QFileDialog.getOpenFileName(self,dialogTitle,defaultPath,fileType)
            self.lineEditPath.setText(fName[0])

    def getPathWidget(self)->QLineEdit:
        pathWidget=self.lineEditPath
        return pathWidget

    def getBrowseWidget(self)->QPushButton:
        browseWidget=self.btnBrowse
        return browseWidget

    def clear(self):
        self.lineEditPath.setText("")

    def getPath(self)->str:
        path=self.lineEditPath.text()
        return path


def toPath(path: str) -> Path:
    """
    """
    if not isinstance(path, str):
        raise TypeError(
            "TypeError : path must be of type str (path like) , Provided '{}' type.".format(path.__class__.__name__))
    if path.strip() == "":
        raise ValueError("ValueError : path can't blank")
    try:
        result = Path(path)
    except TypeError:
        raise TypeError(
            "TypeError : path must be of type str (path like) , Provided '{}' type.".format(path.__class__.__name__))
    return result


if __name__ == '__main__':
    app=QApplication(sys.argv)
    f=FilePathSelectionWidgetEx(app)
    f.show()
    app.exec_()


# from PyQt5.QtWidgets import QWidget
# import resources
#
# class FilePathSelectionWidget(QWidget):
#
#     def __init__(self,parent):
#         super(FilePathSelectionWidget, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Form=self
