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
    APPLICATION_NAME="TTD PDF Exporter"
    APPLICATION_SHORT_DESC="Export specified pdf pages"
    APPLICATION_TAGLINE="PDF to PDF exporter"
    APPLICATION_ICON=":/resources/images/resources/images/PDF-exporter.png"
    COMPANY_NAME="ToTheDigital"
    COMPANY_ICON=":/resources/images/resources/images/companyIcon.png"
    APPLICATION_DEVELOPERS=""
    DEFAULT_SELECTED_DIR=os.path.expanduser("~/Documents")
    # UPDATE_URL="https://raw.githubusercontent.com/ChitreshPratap/FilFo_Prod/main/app.xml"

    UPDATE_URL_WIN_X86="https://raw.githubusercontent.com/tothedigital/TTD_PDF_Exporter/main/ttd_pdf_export_win_x86.xml"
    UPDATE_URL_WIN_X64 = "https://raw.githubusercontent.com/tothedigital/TTD_PDF_Exporter/main/ttd_pdf_export_win_x64.xml"
    PROJECT_ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root