import sqlite3
import sys
import traceback
import datetime

import pandas, openpyxl, requests, bs4, pyodbc

from ReadData import ReadData

import pandas, openpyxl,requests, bs4, pyodbc
import datetime

import pyodbc
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFileDialog
from resource import imageRC

from WriteData import WriteData
from sqlLite import sqlLite
from testing.colored import colored
# from testing.filterWindow import filterWindow
from testing.filterWindowEx import filterWindowEx
from utility import PathUtility




class coloredEx(colored):

    def __init__(self):
        super().__init__()
        self.ls = [self.label1 ,self.label2 ,self.label3 ,self.label4 ,self.label5 ,self.label6 ,self.label7 ,self.label8 ,self.label9 ,self.label10 ,self.label11 ,self.label12 ,self.label13 ,self.label14 ,self.label15 ,self.label16 ,self.label17 ,self.label18 ,self.label19 ,self.label20 ,self.label21 ,self.label22 ,self.label23 ,self.label24 ,self.label25 ,self.label26 ,self.label27 ,self.label28 ,self.label29 ,self.label30 ,self.label31 ,self.label32 ,self.label33 ,self.label34 ,self.label35 ,self.label36 ,self.label37 ,self.label38 ,self.label39 ,self.label40]
        self.dbFile = PathUtility.getPackagedFilePathStrict("resource", "College.db")
        for lbl in self.ls:
            lbl.setHidden(True)
        indexList=['Abrasives','Agriculture','Air Conditioners','Airlines','Aluminium & Aluminium Products','Amusement Parks/Recreation/Club','Aquaculture','Auto Ancillary','Automobile Two & Three Wheelers','Automobiles - Passenger Cars','Automobiles-Tractors','Automobiles-Trucks/Lcv','Bank - Private','Bank - Public','Batteries','Bearings','BPO/ITeS','Breweries & Distilleries','Cable','Carbon Black','Castings/Forgings','Cement & Construction Materials','Ceramics/Marble/Granite/Sanitaryware','Chemicals ','Cigarettes/Tobacco','Compressors / Pumps','Construction - Real Estate','Consumer Durables - Domestic Appliances','Consumer Durables - Electronics','Consumer Food','Courier Services','Cycles','Defence','Diamond & Jewellery','Diesel Engines','Diversified','Dyes & Pigments','e-Commerce','Educational Institutions','Electric Equipment','Electrodes & Welding Equipment','Electronics - Components','Engineering','Engineering - Construction','Engineering - Industrial Equipments','Fasteners','Ferro & Silica Manganese','Fertilizers','Film Production, Distribution & Entertainment','Finance - Asset Management','Finance - Housing','Finance - Investment','Finance - NBFC','Finance - Others','Finance - Stock Broking','Finance Term Lending','Footwear','Forgings','Gas Transmission/Marketing','Glass','Hospital & Healthcare Services','Hotel, Resort & Restaurants','Household & Personal Products','Industrial Gases & Fuels','Insurance','IT - Education','IT - Hardware','IT - Networking','IT - Software ','Laminates/Decoratives','Leather','Logistics','Lubricants','Medical Equipment/Supplies/Accessories','Metal - Non Ferrous ','Mining & Minerals','Miscellaneous','Oil Exploration','Paints','Paper & Paper Products','Pesticides & Agrochemicals','Petrochemicals','Pharmaceuticals & Drugs','Photographic Products','Plastic Products','Port','Power Generation/Distribution','Printing & Stationery','Printing And Publishing','Railways Wagons','Ratings','Refineries','Refractories','Retailing','Rubber Products','Sector','Ship Building','Shipping','Solvent Extraction','Steel & Iron Products','Steel/Sponge Iron/Pig Iron','Sugar','Tea/Coffee','Telecommunication - Equipment','Telecommunication - Service Provider','Textile ','Textile - Machinery','Textile - Manmade Fibres','Textile - Spinning','Textile - Weaving','Trading','Transmission Towers / Equipments','Travel Services','TV Broadcasting & Software Production','Tyres & Allied','Watches & Accessories','Wood & Wood Products']
        self.comboBox.addItems(indexList)
        UpdatedOn=self.lastUpdatedTableInSQL()
        self.label.setText("Last Updated on: "+UpdatedOn[0][0])
        self.pushButton_3.clicked.connect(self.setTextIntoLabel)
        self.pushButton_5.clicked.connect(self.openFilterWindow)
        self.pushButton.clicked.connect(self.showGridView)
        self.pushButton_2.clicked.connect(self.showTableView)
        self.pushButton_7.clicked.connect(self.updateCurrentDataToSQL)
        self.pushButton_6.clicked.connect(self.showAllStock)
        self.pushButton_4.clicked.connect(self.browse)
        # self.dbFile = PathUtility.getPackagedFilePathStrict("resource", "College.db")

    def browse(self):
        # QFileDialog.getOpenFileName()
        selectedPath=QFileDialog.getExistingDirectory()
        fName=selectedPath+"/"+self.comboBox.currentText()+str(datetime.datetime.now().date().strftime("%d-%m-%Y"))+".xlsx"
        print(fName)
        WriteData().wExcel(fName,self.chooseIndex(self.comboBox.currentText()))
        # msg=QMessageBox()
        # msg.setIcon(QMessageBox.information)
        # msg.setText("Download Successfully!!")


    def showGridView(self):
        self.stackedWidget.setCurrentIndex(0)
    def showTableView(self):
        self.stackedWidget.setCurrentIndex(1)

    def showData(self,df):
        try:
            for lbl in self.ls:
                lbl.setHidden(True)

            gCount=0
            rCount=0
            for itm in df:
                if itm[2]>0:
                    gCount=gCount+1
                else:
                    rCount=rCount+1
            j = 0
            gr = 0
            gg = 115
            gb = 0
            r=255
            g=100
            b=100


            for i in df:

                self.ls[j].setVisible(True)
                if df[j][2]>0:
                    grgba = "{},{},{}".format(gr, gg, gb)
                    stylegreen = ("QLabel {\n"

                                  "    border-radius : 5px; \n"
                                  "    background-color: rgb("+grgba+");\n"
                                                                     "    font: 87 8pt \"Arial Black\";\n"
                                                                     "    border-color: rgb(0, 0, 0);\n"
                                                                     "    border: 2px solid White\n"
                                                                     "}\n"
                                                                     "QLabel:hover {\n"
                                                                     "    border: 2px #d4d4d4\n"
                                                                     "}")
                    stockName = """<html><head/><body><p><span style=" font-weight:600; text-decoration: underline; color:#ffffff;">""" + df[j][0] + """</span></p></body></html>"""
                    self.ls[j].setText(stockName)
                    self.ls[j].setStyleSheet(stylegreen)
                    # gr = gr + 30
                    gg = gg +int(140/gCount)
                    # gb = gr +51
                    # ga = ga-2
                else:
                    rgba = "{},{},{}".format(r, g, b)
                    stylered = ("QLabel {\n"

                                "    border-radius : 5px; \n"
                                "    background-color: rgb("+rgba+");\n"
                                                                  "    font: 87 8pt \"Arial Black\";\n"
                                                                  "    border-color: rgb(0, 0, 0);\n"
                                                                  "    border: 2px solid White\n"
                                                                  "}\n"
                                                                  "QLabel:hover {\n"
                                                                  "    border: 2px #d4d4d4\n"
                                                                  "}")
                    stockName="""<html><head/><body><p><span style=" font-size:9pt; font-weight:600; text-decoration: underline; color:#ffffff;">"""+df[j][0]+"""</span></p></body></html>"""
                    self.ls[j].setText(stockName)
                    self.ls[j].setStyleSheet(stylered)
                    r = r -int(60/rCount)
                    g = g - int(100/rCount)
                    b = b - int(100/rCount)
                if j>len(df)-1:
                    break;
                j=j+1
        except IndexError as e:
            pass
        except BaseException:
            traceback.print_exc()
        self.populateTableView(df)


    def setTextIntoLabel(self):
        try:
            for lbl in self.ls:
                lbl.setHidden(True)
            self.df=self.chooseIndex(self.comboBox.currentText())
            self.showData(self.df)
        except BaseException as e:
            traceback.print_exc()


    def chooseIndex(self,Industry):

        # query = "Select stoke,[LTP],[Change(%)],[Change Price],Vol,[Delivery Vol],[Delivery(%)],Industry,[Market Cap] from dbo.All$ inner join dbo.nayiTable on dbo.All$.Stoke=dbo.nayiTable.[Stock Name] where [Industry]= '{}' order by [Change(%)] desc".format(Industry)
        liteQuery='''Select nayiTable."Stock Name","LTP","Change(%)","Change Price","Vol","Delivery Vol","Delivery(%)","Industry","Market Cap" from staticStockInfoTable inner join nayiTable on staticStockInfoTable."Stock Name"=nayiTable."Stock Name" where "Industry"= '{}' order by [Change(%)] desc'''.format(Industry)
        try:
            # connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            # con = pyodbc.connect(connection_string)
            # cursor = con.cursor()
            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(liteQuery)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()
            print('close')
        return df

    def openFilterWindow(self):
        fWindow=filterWindowEx(self)
        fWindow.show()

    def filterBy(self,filterValue):
        print("Inside parent ",filterValue)

    def getSelectedComboxValue(self):
        r= self.comboBox.currentText()
        return r

    def filterQuery(self,i,a,b,c,d):
        # query=self.rString(self.comboBox.currentText()) + "and [{}] {} {} order by [{}] desc".format(a,b,c,d)
        # query="Select stoke,[LTP],[Change(%)],[Change Price],Vol,[Delivery Vol],[Delivery(%)],Industry,[Market Cap] from dbo.All$ inner join dbo.nayiTable on dbo.All$.Stoke=dbo.nayiTable.[Stock Name] where [Industry]= '{}'  and [{}] {} {} order by [{}] desc".format(i,a,b,c,d)
        liteQuery='''Select nayiTable."Stock Name","LTP","Change(%)","Change Price","Vol","Delivery Vol","Delivery(%)","Industry","Market Cap" from staticStockInfoTable inner join nayiTable on staticStockInfoTable."Stock Name"=nayiTable."Stock Name" where "Industry"= '{}'  and [{}] {} {} order by [{}] desc'''.format(i,a,b,c,d)
        try:
            # connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            # con = pyodbc.connect(connection_string)
            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(liteQuery)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()
            print('close')
        return df

    # def rString(self,Industry):
    #     query = "Select stoke,[LTP],[Change(%)],[Change Price],Vol,[Delivery Vol],[Delivery(%)],Industry,[Market Cap] from dbo.All$ inner join dbo.nayiTable on dbo.All$.Stoke=dbo.nayiTable.[Stock Name] where [Industry]= '{}'".format(Industry)
    #     return query

    def populateTableView(self,df):
        rCount=len(df)
        self.tableWidget.setRowCount(rCount)
        r = 0
        for eachTuple in df:
            c = 0
            for eachItem in eachTuple:
                self.tableWidget.setItem(r, c, QTableWidgetItem(str(eachItem)))
                c = c + 1
            r = r + 1

    def updateCurrentDataToSQL(self):



        try:
            sqlLite(self.dbFile).sqlLiteStockPrice()
            sqlLite(self.dbFile).sqlLiteStockVol()
            sqlLite(self.dbFile).makeCurrentNayiTable()

            msg=QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Done !!")
            msg.setWindowTitle("Update status")
            msg.exec()
            Updated_on = str(datetime.datetime.now().date().strftime("%m/%d/%Y"))
            self.label.setText("Last Updated on: " + Updated_on)
            # WriteData().wStockPriceSQL()
            # WriteData().wStockVolSQL()
            # WriteData().makeCurrentNayiTable()
        except BaseException as e:

            traceback.print_exc()
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Not Updated")
            msg.setWindowTitle("Update status")
            msg.exec()
            pass

    def lastUpdatedTableInSQL(self):

        query = "select Distinct [Date] from tblCurrentStockPriceInfo"
        try:
            # connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            # con = pyodbc.connect(connection_string)
            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            # dbFile=PathUtility.getPackagedFilePathStrict("resource","College.db")

            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(query)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()
            print('close')
        return df

    def showAllStock(self):

        liteQuery = '''Select nayiTable."Stock Name","LTP","Change(%)","Change Price","Vol","Delivery Vol","Delivery(%)","Industry","Market Cap" from staticStockInfoTable inner join nayiTable on staticStockInfoTable."Stock Name"=nayiTable."Stock Name" order by "Change(%)" desc'''
        try:

            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(liteQuery)
            df = cursor.fetchall()
        finally:
            cursor.close()
            con.close()
            print('close')
        try:
            for lbl in self.ls:
                lbl.setHidden(True)
            self.showData(df)
        except BaseException as e:
            traceback.print_exc()





# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     window=coloredEx()
#     window.show()
#     app.exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow
# from resource import imageRC
#
#
# class colored(QMainWindow):
#     def __init__(self):
#         super(colored, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         MainWindow=self

