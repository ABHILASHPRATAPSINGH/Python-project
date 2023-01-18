
btnBackgroundColor="rgb(0, 119, 162)"
btnBackgroundColor_Hover="rgb(0, 100, 162)"
btnBackgroundColor_Pressed="rgb(0, 121, 162)"

def getStyleTitleFrame():
    style ="""
        QFrame{
            border-width: 0;
            border-color: rgb(46, 177, 11);
            border-radius: 3;
            border-style: solid;                                                        
            background-color: rgb(222, 235, 244);                                                
        }
        QLabel{
            font: 25 16pt "Arial";
            color: rgb(47, 118, 146);
        }
    """
    return style



def getBaseStyleBodyFrame():
    style = """
        QFrame{
            border-width: 0;
            border-color: rgb(46, 177, 11);
            border-radius: 3;
            border-style: solid;              
            padding-top: 30px;                            
            color: rgb(255, 255, 255);                              
        }

        QLabel{
            padding: 0px;
            font: 25 16pt "Arial";
            color: rgb(255, 255, 255);            
        }
        QLineEdit{
            border-radius: 5px;
            font: 25 16pt "Arial";
            color: rgb(47, 118, 146);
            min-height: 30px;
            max-height: 40px;
        }
    """
    return style

def getStyleBodyFrame1():

    style =getBaseStyleBodyFrame()+ """

        QFrame,QLabel{
            background-color: rgb(0, 90, 124);                  
        }
        QLineEdit#LineEditPath {
                    border-radius: 5px;
                    margin: 0px 20px 0px 0px;
        }
        QLineEdit{
            background-color: "white";            
        }

        QLineEdit#_txtPassword{
            background-color: rgb(0, 89, 83);
            color: white;
        }
                
        QPushButton#btnBrowse {
                    border-radius: 5px;
                    min-width: 150px;
                    background-color:rgb(0, 255, 1);
                    color: rgb(0, 0, 0);
        }

    """
    return style

def getStyleBodyFrame2():
    style=getBaseStyleBodyFrame()+"""
        QFrame, QLabel{
            background-color: rgb(97, 156, 214);                  
        }
        QLabel{
            min-width: 150px;                              
        }               
        QLineEdit{
            background-color: "white";            
        }
        QLineEdit#_txtTotalPages{
            background-color: rgb(0, 89, 83);
            color: white;
        }
        
        QLineEdit#LineEditPath{
                border-radius: 5px;
                margin: 0px 20px 0px 0px;
                }
                
        QPushButton#btnBrowse{
            border-radius: 5px;
            min-width: 150px;
            background-color:rgb(255, 247, 154);
            color: rgb(0, 0, 0);                
        }

    """
    return style

def getStyleBodyFrame3():
    style = getBaseStyleBodyFrame() + """
        QFrame, QLabel{
            background-color: rgb(158, 167, 176);                  
        }
        QLabel{
            min-width: 150px;                              
        }               
        QLineEdit{
            background-color: "white";
        }
        QLineEdit#_txtTotalPages{
            background-color: rgb(0, 89, 83);
            color: white;
        }

        QLineEdit#LineEditPath{
                border-radius: 5px;
                margin: 0px 20px 0px 0px;
                }

        QPushButton#btnBrowse{
            border-radius: 5px;
            min-width: 150px;
            background-color: rgb(255, 247, 154);
            color: rgb(0, 0, 0);
        }

    """
    return style

def getStyleBodyFrame4():
    style = getBaseStyleBodyFrame() + """
        QFrame, QLabel{
            background-color: rgb(0, 49, 89);                  
        }
        QLabel{
            min-width: 150px;                              
        }               
        QLineEdit{
            background-color: "white";
        }
        QLineEdit#_txtTotalPages{
            background-color: rgb(0, 89, 83);
            color: white;
        }

        QLineEdit#LineEditPath{
                border-radius: 5px;
                margin: 0px 20px 0px 0px;
            }

        QPushButton#btnBrowse{
            background-color: rgb(255, 247, 154);
            color: rgb(0, 0, 0);
        }

    """
    return style

def getTransparentButtonStyle():
    style="""
    QPushButton{
        background-color: rgba(255, 255, 255, 0);
        border: 0px;
        color: blue;
        font-size: 16px;
        padding-left: 5px;
        padding-right: 5px;
        font-style: italic;
        text-decoration: 
        }
        QPushButton:hover {
            text-decoration: underline; 
        }

        QPushButton:pressed {
            color: #19A919;
            text-decoration: underline;             
        }

    """
    return style



def getBaseStyleBottomFrame():
    style = """
        QFrame{
            border-width: 0;
            border-color: rgb(46, 177, 11);
            border-radius: 3;
            border-style: solid;                                                                                
        }
        QLabel{
            font: 25 16pt "Arial";
        }

        QPushButton{
            border-radius: 5px;
            margin: 0px 20px 0px 0px;
        }
    """
    return style

def getStyleBottomBodyFrame1():
    style = getBaseStyleBottomFrame()+ """
        QFrame{                                
            background-color: rgb(222, 235, 244);                                                
        }
        QLabel{
            color: rgb(47, 118, 146);
        }

        QPushButton#_btnProtect{
            background-color: rgb(0, 119, 162);        
        }
        QPushButton#_btnClear{
            background-color: rgb(247, 148, 29);
        }

    """
    return style


def getStylePNG2PDFWithoutTitle():
    # style = getBaseStyleBodyFrame() + """
    style = f"""
        QFrame {{
            border-width: 0;
            border-color: rgb(46, 177, 11);
            border-radius: 3;
            border-style: solid;
            background-color: rgb(0, 90, 124);        
        }}
        QFrame#bodyFrame {{
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
        }}
        QFrame#bottomFrame {{
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;            
            }}
    
        QFrame#framePngList {{
            border: 1px solid white;        
        }}
        
        QFrame#framePngPreview {{
            min-width: 340px;
            max-width: 400px;
            min-height: 170px;
            max-height: 200px;
            background: transparent;
            border: 1px solid white;            
        }}
                
        QLineEdit#_txtTotalPages{{
            border: 0px solid white;
            padding: 0px;
            background-color: rgb(0, 90, 124);
            font-size: 14px;
            color: white;            
        }}

        QLabel#_lblPreviewHeading {{
            border-bottom: 1px solid white;
            border-radius: 0px;
            color: blue;                        
            background-color: white;
            color: rgb(0, 90, 124);
        }}        

        
        QLabel#_lblFileListHeading{{
            border-bottom: 1px solid white;
            border-radius: 0px;
            color: blue;
            font-size: 14px;            
            min-height: 28px;
            background-color: white;
            color: rgb(0, 90, 124);
        }}        
        
        QLabel#label {{
            padding: 0px;
            font-size: 14px;
            color: white;            
        }}

        QLabel#label_11 {{
            padding: 0px;
            font-size: 12px;
            color: rgb(255, 255, 255);            

        }}                
                
        QPushButton#_btnClear {{
            border: 0px solid blue;
            background-color: rgb(247, 148, 29);
        }}
        
        QPushButton#_btnClear:hover {{
            background-color: rgb(247, 112, 29);
            color: white;
            border: 1px solid rgb(176,94,43);
        }}
        
        QPushButton#_btnClear:pressed {{
            background-color: rgb(247, 148, 29);
            color: white;
        }}
        
        QPushButton#_btnExportPng2Pdf {{
            background-color: {btnBackgroundColor};
            border: 0px solid blue;        
        }}
        QPushButton#_btnExportPng2Pdf:hover {{
            background-color: {btnBackgroundColor_Hover};
            border: 1px solid rgb(0,90,145);        
        }}
        QPushButton#_btnExportPng2Pdf:pressed {{
            background-color: {btnBackgroundColor_Pressed};        
        }}
        
        QPushButton#_btnAddImage, #_btnRemoveImage, #_btnMoveImageUp, #_btnMoveImageDown {{
            border: 1px solid white;
            border-radius: 5px;
            font-size: 14px;
            background-color: rgb(0, 90, 124);                    
        }}
        QPushButton#_btnAddImage:hover, #_btnRemoveImage:hover, #_btnMoveImageUp:hover, #_btnMoveImageDown:hover {{
            border: 1px solid white;
            border-radius: 5px;
            font-size: 14px;
            color: rgb(0, 90, 124);
            background-color: white;                    
        }}
        QPushButton#_btnAddImage:pressed, #_btnRemoveImage:pressed, #_btnMoveImageUp:pressed, #_btnMoveImageDown:pressed {{
            border: 1px solid white;
            border-radius: 5px;
            font-size: 14px;
            background-color: rgb(0, 90, 124);
            color: white;                    
        }}
        
        QListView::item {{
            background-color: #3AB3FF;
            color: white;            
        }}  
        QListView::item:alternate {{
            background-color: #A5DCFF;
            color: #00436D;
            
        }}  
              
        QListView::item:selected
        {{
            border : 1px solid rgb(150,150,150);
            background-color: rgb(150,150,150);
            color: white;            
        }}
        
        QListView::item:hover
        {{
            border : 1px solid gray;        
            background-color: rgb(203,203,203);
            color: rgb(81,81,81);            
        }}
        
        QListView::item:selected {{
           border: 1px solid #6a6ea9;
        }}

        QListView::item:selected:!active {{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #ABAFE5, stop: 1 #8588B2);
        }}

        QListView::item:selected:active {{
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #3E86A1, stop: 1 #888dd9);
            border: 1px solid #006A92;
            font-size: 14px;            
        }}

        QListView::item:hover {{
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);
        }}
                      
        """
    return style

def getStyle_BtnHome():
    fStyle = """
        QPushButton{
            background-color: rgb(50, 190, 255);
            border-radius: 3px;            
        }

        QPushButton:hover {
            border: 1px solid rgb(27,122,165);
            border-radius: 3px;     
            background-color: rgb(27,122,165);
            color: white;                       
        }

        QPushButton:pressed {
            border: 1px solid rgb(120,120,120);
            background-color: white;
            color: rgb(120,120,120);
            border-radius: 3px;            
        }

        """
    return fStyle

def getStyle_HomeFrameEx():
    frameStyle = """

            QFrame{
                border-width: 20;
                border-color: rgb(255,255,255);
                border-radius: 3;
                border-style: solid;
            }

            QPushButton{
                border-width: 1;
                border-color: rgb(46, 177, 11);
                border-radius: 3;
                border-style: solid;
                background-color: rgb(46, 177, 11);
                color: rgb(254, 254, 254);        
                font: 75 14pt \"Arial\";
            }

            QLabel{
                border-width: 0;
                color: rgb(94,94,94);
                font-size: 18px;
            }

            QLabel:hover{
                border-width: 0;
                color: black;
                font-size: 18px;
            }

            QPushButton#_btnExportPdf2SinglePdf, #_btnExportPdf2Png {
                border: 0px solid green;
                background-color: rgb(70, 148, 200);
            }
            QPushButton#_btnExportPdf2SinglePdf:hover, #_btnExportPdf2Png:hover {
                background-color: #2C5A79;
                border: 1px solid #1C5277;
                color: #D5EAF7;
            }
            QPushButton#_btnExportPdf2SinglePdf:pressed, #_btnExportPdf2Png:pressed {
                border: 0px solid green;
                background-color: rgb(70, 148, 200);
                color: white;
            }


            QPushButton#_btnPdf2SeperatePdf, #_btnPng2Pdf {
                border: 0px solid green;
                background-color: rgb(55, 49, 118);
            }
            QPushButton#_btnPdf2SeperatePdf:hover, #_btnPng2Pdf:hover {
                background-color: rgb(155, 149, 212);
                border: 1px solid rgb(155, 149, 212);
                color: rgb(55, 49, 118);
            }
            QPushButton#_btnPdf2SeperatePdf:pressed, #_btnPng2Pdf:pressed {
                border: 0px solid green;
                background-color: rgb(55, 49, 118);
                color: white;

            }
                        
            QPushButton#_btnPdf2ImagedPdf, #_btnPng2Pdf {
                border: 0px solid green;
                background-color: #22816E;
            }
            QPushButton#_btnPdf2ImagedPdf:hover, #_btnPng2Pdf:hover {
                background-color: #A9F8E8;
                border: 1px solid #A9F8E8;
                color: #22816E;
            }
            QPushButton#_btnPdf2ImagedPdf:pressed, #_btnPng2Pdf:pressed {
                border: 0px solid green;
                background-color: #22816E;
                color: white;

            }

        """
    return frameStyle

def getStyleTTDPDFSecureFrame():


    style = getBaseStyleBodyFrame() + f"""
                                
        QFrame,QLabel{{
            background-color: rgb(0, 90, 124);        
        }}
        QLineEdit#LineEditPath {{
                    border-radius: 5px;
                    margin: 0px 20px 0px 0px;
        }}
        QLineEdit{{
            background-color: "white";            
        }}

        QLineEdit#_txtPassword, #_txtRequiredPages{{
            background-color: white;
            color: rgb(0, 89, 83);
        }}
        QLineEdit#_txtPassword:hover, #_txtRequiredPages:hover {{
            background-color: white;
            border: 1px solid black;
            color: rgb(0, 89, 83);
        }}

        QPushButton#btnBrowse {{
                    border: 0px solid blue;
                    border-radius: 5px;
                    min-width: 150px;
                    background-color:rgb(0, 255, 1);                    
                    color: rgb(0, 0, 0);
        }}
        
        QPushButton#btnBrowse:hover {{
                    border-radius: 5px;
                    min-width: 150px;                    
                    background-color:rgb(50, 145, 50);
                    color: rgb(0, 255, 1);
                    border: 1px solid rgb(40,100,40);                
        }}

        QPushButton#btnBrowse:pressed {{
                    border-radius: 5px;
                    min-width: 150px;                    
                    background-color:rgb(0, 255, 1);
                    color: rgb(0, 0, 0);                
        }}
                    
        QPushButton#_btnClear{{
            border: 0px solid blue;
            background-color: rgb(247, 148, 29);
        }}
        QPushButton#_btnClear:hover {{
            background-color: rgb(247, 112, 29);
            color: white;
            border: 1px solid rgb(176,94,43);
        }}
        QPushButton#_btnClear:pressed {{
            background-color: rgb(247, 148, 29);
            color: white;
        }}
        
        
        QFrame#bodyFrame{{
            border-top-left-radius: 40px;
            border-top-right-radius: 40px;
        }}
        QFrame#bottomFrame{{
            border-bottom-left-radius: 40px;
            border-bottom-right-radius: 40px;
            
        }}
        
        QPushButton#_btnProtect, #_btnExport2SeperatePdf, #_btnExport2SinglePdf, #_btnExportPdf2Png {{
            background-color: {btnBackgroundColor};
            border: 0px solid blue;        
        }}
        QPushButton#_btnProtect:hover, #_btnExport2SeperatePdf:hover, #_btnExport2SinglePdf:hover, #_btnExportPdf2Png:hover {{
            background-color: {btnBackgroundColor_Hover};
            border: 1px solid rgb(0,90,145);        
        }}
        QPushButton#_btnProtect:pressed, #_btnExport2SeperatePdf:pressed, #_btnExport2SinglePdf:pressed, #_btnExportPdf2Png:pressed {{
            background-color: {btnBackgroundColor_Pressed};        
        }}
    """
    return style

def getStyleBottomBodyFrame2():
    style = getBaseStyleBottomFrame() + """
        QFrame{                                
            background-color: rgb(222, 235, 244);                                                
        }
        QLabel{
            color: rgb(47, 118, 146);
        }

        QPushButton#_btnExport2SinglePdf{
            background-color: rgb(0, 119, 162);
        }
        QPushButton#_btnClear{
            background-color: rgb(247, 148, 29);
        }

    """
    return style

def getStyleBottomBodyFrame3():
    style = getBaseStyleBottomFrame() + """
        QFrame{                                
            background-color: rgb(222, 235, 244);                                                
        }
        QLabel{
            color: rgb(47, 118, 146);
        }

        QPushButton#_btnExport2SeperatePdf{
            background-color: rgb(123, 46, 0);
        }
        QPushButton#_btnClear{
            background-color: rgb(247, 148, 29);
        }

    """
    return style

def getStyleBottomBodyFrame4():
    style = getBaseStyleBottomFrame() + """
        QFrame{                                
            background-color: rgb(222, 235, 244);                                                
        }
        QLabel{
            color: rgb(47, 118, 146);
        }

        QPushButton#_btnExportPdf2Png{
            background-color: rgb(237, 27, 36);
        }
        QPushButton#_btnClear{
            background-color: rgb(247, 148, 29);
        }
    """
    return style


def getPreviewWidgetStyle():
    style="""                                       
    """
    return style
