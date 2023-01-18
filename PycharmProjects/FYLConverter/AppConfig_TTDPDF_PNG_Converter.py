import os
import pathlib
from enum import Enum

from AppEnvironments import AppEnvironments


def getEnvironment():
    environ=AppEnvironments.PRODUCTION.value
    return environ

class Details(Enum):
    APPLICATION_VERSION="0.0.1"
    APPLICATION_ENVIRONMENT=getEnvironment()
    APPLICATION_NAME="TTD PDF ~ PNG Converter"
    APPLICATION_TAGLINE="PDF ~ PNG Converter"
    APPLICATION_SHORT_DESC = "PDF ~ PNG Converter"
    COMPANY_NAME="ToTheDigital"
    COMPANY_ICON=":/resources/images/resources/images/companyIcon.png"
    APPLICATION_ICON=":/resources/images/resources/images/PDF_PNG_Converter.png"
    APPLICATION_DEVELOPERS=""
    DEFAULT_SELECTED_DIR=os.path.expanduser("~/Documents")
    # UPDATE_URL="https://raw.githubusercontent.com/ChitreshPratap/FilFo_Prod/main/app.xml"

    UPDATE_URL_WIN_X86="https://raw.githubusercontent.com/tothedigital/TTD_PDF_PNG_Converter/main/TTD_PDF_PNG_Converter_win_x86.xml"
    UPDATE_URL_WIN_X64 = "https://raw.githubusercontent.com/tothedigital/TTD_PDF_PNG_Converter/main/TTD_PDF_PNG_Converter_win_x64.xml"
    PROJECT_ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root