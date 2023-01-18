# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

mainFilePath=r"C:\Users\DELL\Documents\kPython\PycharmProjects\FYLConverter"
mainPythonFile="Application_TTD_PDF_Secure.py"
iconPath=mainFilePath+r"\resources\images\pdf-secure_icon.ico"

exeName="TTD_PDF_Secure"
needConsole=False


a = Analysis([mainPythonFile],
             pathex=[mainFilePath],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=exeName,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=needConsole, icon=iconPath )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=exeName)