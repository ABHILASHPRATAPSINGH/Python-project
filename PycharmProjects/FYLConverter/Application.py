
import platform
import sys
import traceback
from PyQt5.QtWidgets import QApplication

import AppConfig

from src.autoupdater.PyAutoUpdater import PyAutoUpdater
from src.userform.ext.MainWindowEx import MainWindowEx
from src.userform.ext.SplashScreenEx import SplashScreenEx


def start():
    try:
        app=QApplication(sys.argv)
        splash=SplashScreenEx(app,3)
        window=MainWindowEx()
        window.show()
        splash.finish(window)
        if platform.architecture()[0]=="64bit":
            updateUrl = AppConfig.Details.UPDATE_URL_WIN_X64.value
        else:
            updateUrl = AppConfig.Details.UPDATE_URL_WIN_X86.value

        companyName = AppConfig.Details.COMPANY_NAME.value
        appName = AppConfig.Details.APPLICATION_NAME.value
        appVersion = AppConfig.Details.APPLICATION_VERSION.value
        updater = PyAutoUpdater(updateUrl, companyName, appName, appVersion)
        updater.checkUpdateWithUI()
        app.exec()

    except BaseException as e:
        print(e)
        traceback.print_exc()

if __name__ == '__main__':
    start()
    # app = QApplication(sys.argv)
    # window = PDFARViewerWidget()
    # window.setGeometry(600, 50, 800, 600)
    # window.show()
    # sys.exit(app.exec_())