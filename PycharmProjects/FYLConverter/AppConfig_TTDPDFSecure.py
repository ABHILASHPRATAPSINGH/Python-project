import os
import pathlib
from enum import Enum

from AppEnvironments import AppEnvironments


def getEnvironment():
    environ=AppEnvironments.PRODUCTION.value
    return environ

class Details(Enum):
    APPLICATION_VERSION="0.0.3"
    APPLICATION_ENVIRONMENT=getEnvironment()
    APPLICATION_SHORTDESC="Convert Unprotected PDF to Password protected PDF"
    APPLICATION_TAGLINE="PDF Protect Application"
    APPLICATION_ICON_PATH=":/resources/images/resources/images/pdf-secure_icon.png"
    APPLICATION_NAME="TTD PDF Secure"
    COMPANY_ICON=":/resources/images/resources/images/companyIcon.png"
    COMPANY_NAME="ToTheDigital"
    APPLICATION_DEVELOPERS=""
    DEFAULT_SELECTED_DIR=os.path.expanduser("~/Documents")
    # UPDATE_URL="https://raw.githubusercontent.com/ChitreshPratap/FilFo_Prod/main/app.xml"
    UPDATE_URL_WIN_X86="https://raw.githubusercontent.com/tothedigital/TTD-PDF-SECURE/main/win_x86.xml"
    UPDATE_URL_WIN_X64 = "https://raw.githubusercontent.com/tothedigital/TTD-PDF-SECURE/main/win_x64.xml"
    PROJECT_ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root