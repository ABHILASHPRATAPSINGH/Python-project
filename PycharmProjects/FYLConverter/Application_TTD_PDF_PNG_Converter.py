import platform
import sys
import traceback
from PyQt5.QtWidgets import QApplication
import AppConfig_TTDPDF_PNG_Converter
from AppEnvironments import AppEnvironments
from src.autoupdater.PyAutoUpdater import PyAutoUpdater
from src.userform.ext.MainWindow_TTDPDFSecureEx import MainWindow_TTDPDFSecureEx
from src.userform.ext.MainWindow_TTDPDF_PNG_ConverterEx import MainWindow_TTDPDF_PNG_ConverterEx
from src.userform.ext.SplashScreen_TransparentEx import SplashScreen_TransparentEx

def start():
    try:
        app=QApplication(sys.argv)
        splash=SplashScreen_TransparentEx(app,3,
                                          AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_NAME.value,
                                          AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_TAGLINE.value,
                                          AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_ICON.value
                                          )

        window=MainWindow_TTDPDF_PNG_ConverterEx(
                            applicationTitle=AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_NAME.value,
                            appShortDesc=AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_SHORT_DESC.value,
                            applicationIcon=AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_ICON.value,
                            companyIcon=AppConfig_TTDPDF_PNG_Converter.Details.COMPANY_ICON.value
                                            )
        window.show()
        splash.finish(window)
        if AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_ENVIRONMENT.value !=AppEnvironments.DEVELOPMENT.value:
            if platform.architecture()[0]=="64bit":
                updateUrl = AppConfig_TTDPDF_PNG_Converter.Details.UPDATE_URL_WIN_X64.value
            else:
                updateUrl = AppConfig_TTDPDF_PNG_Converter.Details.UPDATE_URL_WIN_X86.value
            companyName = AppConfig_TTDPDF_PNG_Converter.Details.COMPANY_NAME.value
            appName = AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_NAME.value
            appVersion = AppConfig_TTDPDF_PNG_Converter.Details.APPLICATION_VERSION.value
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