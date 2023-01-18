# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProtectPdfFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFrame
import resources

class ProtectPdfFrame(QFrame):

    def __init__(self):
        super(ProtectPdfFrame, self).__init__()
        self.setupUi()

    def setupUi(self):
        Frame = self
        Frame.setObjectName("Frame")
        Frame.resize(730, 383)
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
        self._lblFrameIcon.setPixmap(QtGui.QPixmap(":/resources/images/resources/images/FileLock3.png"))
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
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.bodyFrame)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.bodyFrame)
        self.label_12.setMinimumSize(QtCore.QSize(80, 20))
        self.label_12.setMaximumSize(QtCore.QSize(100, 30))
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self._txtPassword = QtWidgets.QLineEdit(self.bodyFrame)
        self._txtPassword.setMinimumSize(QtCore.QSize(90, 20))
        self._txtPassword.setMaximumSize(QtCore.QSize(400, 30))
        self._txtPassword.setStyleSheet("")
        self._txtPassword.setInputMask("")
        self._txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self._txtPassword.setAlignment(QtCore.Qt.AlignCenter)
        self._txtPassword.setClearButtonEnabled(False)
        self._txtPassword.setObjectName("_txtPassword")
        self.horizontalLayout_7.addWidget(self._txtPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
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
        self._lblProgressStatus.setText("")
        self._lblProgressStatus.setObjectName("_lblProgressStatus")
        self.horizontalLayout_14.addWidget(self._lblProgressStatus)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self._btnProtect = QtWidgets.QPushButton(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnProtect.sizePolicy().hasHeightForWidth())
        self._btnProtect.setSizePolicy(sizePolicy)
        self._btnProtect.setMinimumSize(QtCore.QSize(120, 40))
        self._btnProtect.setMaximumSize(QtCore.QSize(150, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/lock-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnProtect.setIcon(icon)
        self._btnProtect.setIconSize(QtCore.QSize(16, 16))
        self._btnProtect.setObjectName("_btnProtect")
        self.horizontalLayout_13.addWidget(self._btnProtect)
        self._btnClear = QtWidgets.QPushButton(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._btnClear.sizePolicy().hasHeightForWidth())
        self._btnClear.setSizePolicy(sizePolicy)
        self._btnClear.setMinimumSize(QtCore.QSize(120, 40))
        self._btnClear.setMaximumSize(QtCore.QSize(150, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/images/resources/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btnClear.setIcon(icon1)
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
        self._lblFrameTitle.setText(_translate("Frame", "Convert Unprotected PDF to Password Protected PDF"))
        self.label_11.setText(_translate("Frame", "Select PDF File"))
        self.label_12.setText(_translate("Frame", "Password"))
        self._txtPassword.setPlaceholderText(_translate("Frame", "Enter Password"))
        self._btnProtect.setText(_translate("Frame", "Protect"))
        self._btnClear.setText(_translate("Frame", "Clear"))

