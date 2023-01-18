

import Google
import os

# Variabels required to create service of google sheet api instance
# NAME OF CLIENT SECRET FILE
CLIENT_SECRET_FILE="amsDesktopClientSecretFile.json"

# NAME OF THE GOOGLE SHEET API
API_NAME="sheets"

# VERSION OF THE GOOGLE SHEET API
API_VERSION="v4"

# SCOPES FOR THE USER
# SCOPES DETAILS ARE AVAILABLE HERE: https://developers.google.com/sheets/api/guides/authorizing

SCOPES=["https://www.googleapis.com/auth/spreadsheets"]

service=Google.Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
