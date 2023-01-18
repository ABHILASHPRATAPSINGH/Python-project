import os
import pathlib
from enum import Enum

class Details(Enum):
    APPLICATION_VERSION="0.0.1"
    APPLICATION_ENVIRONMENT="production"
    APPLICATION_NAME="FYLConverter"
    COMPANY_NAME="ToTheDigital"
    APPLICATION_DEVELOPERS=""
    DEFAULT_SELECTED_DIR=os.path.expanduser("~/Documents")
    # UPDATE_URL="https://raw.githubusercontent.com/ChitreshPratap/FilFo_Prod/main/app.xml"
    UPDATE_URL_WIN_X86="https://raw.githubusercontent.com/ChitreshPratap/FYLConverter_Prod/main/app_win_x86.xml"
    UPDATE_URL_WIN_X64 = "https://raw.githubusercontent.com/ChitreshPratap/FYLConverter_Prod/main/app_win_x64.xml"
    PROJECT_ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root