# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Png2PdfFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFrame
import resources

import resources

class Png2PdfFrame(QFrame):

    def __init__(self):
        super(Png2PdfFrame, self).__init__()
        self.setupUi()

    def setupUi(self):
        Frame=self



        Frame.setObjectName("Frame")
        Frame.resize(781, 440)
        Frame.setStyleSheet("\n"
"QFrame{\n"
"    border-width: 20;\n"
"    border-color: rgb(46, 177, 11);\n"
"    border-radius: 3;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-width: 1;\n"
"    border-color: rgb(46, 177, 11);\n"
"    border-radius: 3;\n"
"    border-style: solid;\n"
"    background-color: rgb(46, 177, 11);\n"
"    color: rgb(254, 254, 254);        \n"
"    font: 75 14pt \"Arial\";\n"
"}")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QtWidgets.QFrame(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy)
        self.titleFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titleFrame.setAutoFillBackground(False)
        self.titleFrame.setStyleSheet("\n"
"\n"
"\n"
"QFrame{\n"
"    border-width: 0;\n"
"    border-color: rgb(46, 177, 11);\n"
"    border-radius: 3;\n"
"    border-style: solid;\n"
"    background-color: rgb(222, 235, 244);\n"
"}\n"
"\n"
"")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._lblFrameIcon = QtWidgets.QLabel(self.titleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblFrameIcon.sizePolicy().hasHeightForWidth())
        self._lblFrameIcon.setSizePolicy(sizePolicy)
        self._lblFrameIcon.setMinimumSize(QtCore.QSize(50, 50))
        self._lblFrameIcon.setMaximumSize(QtCore.QSize(50, 50))
        self._lblFrameIcon.setStyleSheet("")
        self._lblFrameIcon.setText("")
        self._lblFrameIcon.setPixmap(QtGui.QPixmap(":/resources/images/resources/images/pdf2png2.png"))
        self._lblFrameIcon.setScaledContents(True)
        self._lblFrameIcon.setObjectName("_lblFrameIcon")
        self.horizontalLayout_5.addWidget(self._lblFrameIcon)
        self._lblFrameTitle = QtWidgets.QLabel(self.titleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblFrameTitle.sizePolicy().hasHeightForWidth())
        self._lblFrameTitle.setSizePolicy(sizePolicy)
        self._lblFrameTitle.setMinimumSize(QtCore.QSize(0, 50))
        self._lblFrameTitle.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self._lblFrameTitle.setFont(font)
        self._lblFrameTitle.setStyleSheet("")
        self._lblFrameTitle.setObjectName("_lblFrameTitle")
        self.horizontalLayout_5.addWidget(self._lblFrameTitle)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.titleFrame)
        self.bodyFrame = QtWidgets.QFrame(Frame)
        self.bodyFrame.setStyleSheet("QFrame{\n"
"    border-width: 0;\n"
"    border-color: rgb(46, 177, 11);\n"
"    border-radius: 3;\n"
"    border-style: solid;\n"
"    background-color: rgb(97, 156, 214);\n"
"}\n"
"\n"
"\n"
"")
        self.bodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyFrame.setObjectName("bodyFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bodyFrame)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.bodyFrame)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.framePngList = QtWidgets.QFrame(self.bodyFrame)
        self.framePngList.setMinimumSize(QtCore.QSize(0, 50))
        self.framePngList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePngList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePngList.setObjectName("framePngList")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.framePngList)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_fileListLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout_fileListLayout.setSpacing(0)
        self.verticalLayout_fileListLayout.setObjectName("verticalLayout_fileListLayout")
        self._lblFileListHeading = QtWidgets.QLabel(self.framePngList)
        self._lblFileListHeading.setMaximumSize(QtCore.QSize(16777215, 20))
        self._lblFileListHeading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._lblFileListHeading.setObjectName("_lblFileListHeading")
        self.verticalLayout_fileListLayout.addWidget(self._lblFileListHeading, 0, QtCore.Qt.AlignTop)
        self.listWidget = QtWidgets.QListWidget(self.framePngList)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_fileListLayout.addWidget(self.listWidget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_fileListLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_fileListLayout)
        self.horizontalLayout_4.addWidget(self.framePngList)
        self.framePngControls = QtWidgets.QFrame(self.bodyFrame)
        self.framePngControls.setMinimumSize(QtCore.QSize(150, 50))
        self.framePngControls.setMaximumSize(QtCore.QSize(200, 16777215))
        self.framePngControls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePngControls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePngControls.setObjectName("framePngControls")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.framePngControls)
        self.verticalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_controlLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout_controlLayout.setContentsMargins(5, -1, 5, 5)
        self.verticalLayout_controlLayout.setSpacing(8)
        self.verticalLayout_controlLayout.setObjectName("verticalLayout_controlLayout")
        self._btnAddImage = QtWidgets.QPushButton(self.framePngControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnAddImage.sizePolicy().hasHeightForWidth())
        self._btnAddImage.setSizePolicy(sizePolicy)
        self._btnAddImage.setMinimumSize(QtCore.QSize(0, 20))
        self._btnAddImage.setMaximumSize(QtCore.QSize(16777215, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/addFileIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnAddImage.setIcon(icon)
        self._btnAddImage.setObjectName("_btnAddImage")
        self.verticalLayout_controlLayout.addWidget(self._btnAddImage)
        self._btnRemoveImage = QtWidgets.QPushButton(self.framePngControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnRemoveImage.sizePolicy().hasHeightForWidth())
        self._btnRemoveImage.setSizePolicy(sizePolicy)
        self._btnRemoveImage.setMaximumSize(QtCore.QSize(16777215, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/removeImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnRemoveImage.setIcon(icon1)
        self._btnRemoveImage.setObjectName("_btnRemoveImage")
        self.verticalLayout_controlLayout.addWidget(self._btnRemoveImage)
        self._btnMoveImageUp = QtWidgets.QPushButton(self.framePngControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnMoveImageUp.sizePolicy().hasHeightForWidth())
        self._btnMoveImageUp.setSizePolicy(sizePolicy)
        self._btnMoveImageUp.setMaximumSize(QtCore.QSize(16777215, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/moveUpIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnMoveImageUp.setIcon(icon2)
        self._btnMoveImageUp.setObjectName("_btnMoveImageUp")
        self.verticalLayout_controlLayout.addWidget(self._btnMoveImageUp)
        self._btnMoveImageDown = QtWidgets.QPushButton(self.framePngControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnMoveImageDown.sizePolicy().hasHeightForWidth())
        self._btnMoveImageDown.setSizePolicy(sizePolicy)
        self._btnMoveImageDown.setMaximumSize(QtCore.QSize(16777215, 20))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/moveDownIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnMoveImageDown.setIcon(icon3)
        self._btnMoveImageDown.setObjectName("_btnMoveImageDown")
        self.verticalLayout_controlLayout.addWidget(self._btnMoveImageDown)
        self.verticalLayout_10.addLayout(self.verticalLayout_controlLayout)
        self.horizontalLayout_4.addWidget(self.framePngControls)
        self.framePngPreview = QtWidgets.QFrame(self.bodyFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePngPreview.sizePolicy().hasHeightForWidth())
        self.framePngPreview.setSizePolicy(sizePolicy)
        self.framePngPreview.setMinimumSize(QtCore.QSize(200, 50))
        self.framePngPreview.setMaximumSize(QtCore.QSize(400, 16777215))
        self.framePngPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePngPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePngPreview.setObjectName("framePngPreview")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.framePngPreview)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_previewLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout_previewLayout.setSpacing(0)
        self.verticalLayout_previewLayout.setObjectName("verticalLayout_previewLayout")
        self._lblPreviewHeading = QtWidgets.QLabel(self.framePngPreview)
        self._lblPreviewHeading.setMinimumSize(QtCore.QSize(0, 20))
        self._lblPreviewHeading.setMaximumSize(QtCore.QSize(16777215, 20))
        self._lblPreviewHeading.setAlignment(QtCore.Qt.AlignCenter)
        self._lblPreviewHeading.setObjectName("_lblPreviewHeading")
        self.verticalLayout_previewLayout.addWidget(self._lblPreviewHeading)
        self.verticalLayout_6.addLayout(self.verticalLayout_previewLayout)
        self.horizontalLayout_4.addWidget(self.framePngPreview)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.bodyFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self._txtTotalPages = QtWidgets.QLineEdit(self.bodyFrame)
        self._txtTotalPages.setEnabled(False)
        self._txtTotalPages.setObjectName("_txtTotalPages")
        self.horizontalLayout_2.addWidget(self._txtTotalPages)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.bodyFrame)
        self.bottomFrame = QtWidgets.QFrame(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setMinimumSize(QtCore.QSize(0, 80))
        self.bottomFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.bottomFrame.setStyleSheet("\n"
"\n"
"\n"
"QFrame{\n"
"    border-width: 0;\n"
"    border-color: rgb(46, 177, 11);\n"
"    border-radius: 3;\n"
"    border-style: solid;\n"
"    background-color: rgb(222, 235, 244);\n"
"}\n"
"\n"
"")
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.progressBar = QtWidgets.QProgressBar(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(130, 13))
        self.progressBar.setMaximumSize(QtCore.QSize(130, 13))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_14.addWidget(self.progressBar)
        self._lblProgressStatus = QtWidgets.QLabel(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._lblProgressStatus.sizePolicy().hasHeightForWidth())
        self._lblProgressStatus.setSizePolicy(sizePolicy)
        self._lblProgressStatus.setText("")
        self._lblProgressStatus.setObjectName("_lblProgressStatus")
        self.horizontalLayout_14.addWidget(self._lblProgressStatus)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self._btnExportPng2Pdf = QtWidgets.QPushButton(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnExportPng2Pdf.sizePolicy().hasHeightForWidth())
        self._btnExportPng2Pdf.setSizePolicy(sizePolicy)
        self._btnExportPng2Pdf.setMinimumSize(QtCore.QSize(120, 40))
        self._btnExportPng2Pdf.setMaximumSize(QtCore.QSize(150, 60))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnExportPng2Pdf.setIcon(icon4)
        self._btnExportPng2Pdf.setIconSize(QtCore.QSize(16, 16))
        self._btnExportPng2Pdf.setObjectName("_btnExportPng2Pdf")
        self.horizontalLayout_13.addWidget(self._btnExportPng2Pdf)
        self._btnClear = QtWidgets.QPushButton(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnClear.sizePolicy().hasHeightForWidth())
        self._btnClear.setSizePolicy(sizePolicy)
        self._btnClear.setMinimumSize(QtCore.QSize(120, 40))
        self._btnClear.setMaximumSize(QtCore.QSize(150, 60))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnClear.setIcon(icon5)
        self._btnClear.setObjectName("_btnClear")
        self.horizontalLayout_13.addWidget(self._btnClear)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addWidget(self.bottomFrame)
        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self._lblFrameTitle.setText(_translate("Frame", "Export PNG Images to PDF"))
        self.label_11.setText(_translate("Frame", "Select PNG Files"))
        self._lblFileListHeading.setText(_translate("Frame", "Image Files"))
        self._btnAddImage.setText(_translate("Frame", "Add"))
        self._btnRemoveImage.setText(_translate("Frame", "Remove"))
        self._btnMoveImageUp.setText(_translate("Frame", "Move Up"))
        self._btnMoveImageDown.setText(_translate("Frame", "move down"))
        self._lblPreviewHeading.setText(_translate("Frame", "preview"))
        self.label.setText(_translate("Frame", "Total Pages"))
        self._btnExportPng2Pdf.setText(_translate("Frame", "Export"))
        self._btnClear.setText(_translate("Frame", "Clear"))

