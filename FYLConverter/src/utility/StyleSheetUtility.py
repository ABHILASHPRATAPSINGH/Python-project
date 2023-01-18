from PyQt5.QtCore import QFile

def getStyleSheet_From_QssFilePath(qssFilePath)->str:
    """
    It read .qss style sheet file and return its content as str
    :param qssFilePath: absolute path to the .qss file
    :return: str
    """
    qFile = QFile(qssFilePath)
    qFile.open(QFile.ReadOnly)
    st = qFile.readAll()
    styleSheet = st.data().decode()
    return styleSheet

