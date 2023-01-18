from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import AppConfig
from src.pdfar.DocViewerWidget import DocViewerWidget


class PDFARViewerWidget(QWebEngineView,DocViewerWidget):

    def __init__(self,pdfFilePath:str=None,viewerHtml=None):
        super(PDFARViewerWidget, self).__init__()
        # viewerHtmlFile=PathUtility.getPackagedFilePathStrict("src.pyWeb","/web/viewer.html")
        # viewerHtmlFile = viewerHtmlFile.replace("\\", "/")
        _viewerHtmlFile=AppConfig.Details.PROJECT_ROOT_DIR.value
        viewerHtmlFile=_viewerHtmlFile.as_posix() + "/src/pyWeb/web/viewer.html"
        # print(viewerHtmlFile)
        # print(projectRootDirectory,"is project root")

        # print(viewerHtmlFile)
        self.PDFJS="file:///{}".format(viewerHtmlFile)
        # self.PDFJS = r"file:///C:/Users/DELL/Documents/kPython/PycharmProjects/FYLConverter/src/pyWeb/web/viewer.html"
        # PDFJS = f"file://{os.path.abspath('./pyWeb/viewer.html')}"
        # print(self.PDFJS)
        # PDF = f'file://{"%20".join(sys.argv[1:])}'

        # PDF = r"file:///C:/Users/DELL/Desktop/dmo/Gmail - DXC Offer Details.pdf"
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.netUrl = '{}?file={}'
        if pdfFilePath is not None:
            PDF = pdfFilePath
            netUrl=self.netUrl.format(self.PDFJS, PDF)
            self.load(QUrl.fromUserInput(netUrl))

    def loadFile(self,pdfFilePath):
        netUrl = self.netUrl.format(self.PDFJS, pdfFilePath)
        self.load(QUrl.fromUserInput(netUrl))
