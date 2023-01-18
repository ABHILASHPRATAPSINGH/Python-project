from pywinsparkle import pywinsparkle

class PyAutoUpdater:

    def __init__(self,updateUrl:str,companyName:str,appName:str,appVersion:str):
        """
        :param updateUrl: url/path of sparkle format app cast.xml file which contains information about application
        :param companyName: name of the company
        :param appName: Name of the application
        :param version: version of the application
        """
        self.__updateUrl=updateUrl
        self.__companyName=companyName
        self.__appName=appName
        self.__version=appVersion
        self.setUpdateUrl(self.__updateUrl)
        self.setAppDetails(self.__companyName,self.__appName, self.__version)
        self.initialize()

    def getUpdateUrl(self):
        updateUrl=self.__updateUrl
        return updateUrl

    def getCompanyName(self):
        companyName=self.__companyName
        return companyName

    def getAppName(self):
        appName=self.__appName
        return appName

    def getAppVersion(self):
        version=self.__version
        return version

    def setAppDetails(self,companyName,appName,version):
        pywinsparkle.win_sparkle_set_app_details(companyName, appName, version)

    def setUpdateUrl(self,updateUrl):
        pywinsparkle.win_sparkle_set_appcast_url(updateUrl)

    def setUpdateFoundCallBack(self,foundUpdate):
        pywinsparkle.win_sparkle_set_did_find_update_callback(foundUpdate)

    def setErrorCallBack(self,encountredError):
        pywinsparkle.win_sparkle_set_error_callback(encountredError)

    def setUpdateCancelledCallBack(self,updateCancelled):
        pywinsparkle.win_sparkle_set_update_cancelled_callback(updateCancelled)

    def setNoUpdateFoundCallBack(self,noUpdateFound):
        pywinsparkle.win_sparkle_set_did_not_find_update_callback(noUpdateFound)

    def setShutdownRequestCallBack(self,shutdown):
        pywinsparkle.win_sparkle_set_shutdown_request_callback(shutdown)

    def initialize(self):
        pywinsparkle.win_sparkle_init()

    def checkUpdateWithUI(self):
        pywinsparkle.win_sparkle_check_update_with_ui()

    def cleanUp(self):
        pywinsparkle.win_sparkle_cleanup()

    def setLanguage(self,language):
        pywinsparkle.win_sparkle_set_lang(language)

    def __del__(self):
        self.cleanUp()
