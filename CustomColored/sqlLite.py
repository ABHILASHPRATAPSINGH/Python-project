import datetime
import sqlite3

import pandas, openpyxl, requests, bs4, pyodbc

from ReadData import ReadData


class sqlLite(ReadData):

    def __init__(self,file):
        self.dbFile=file

    def sqlLiteStockPrice(self):
        # self.dbFile=dbFile
        self.stockPriceInfo = super().rCurrentStockPriceInfoWeb()
        query1 = "drop table tblCurrentStockPriceInfo"
        query2 = '''CREATE TABLE "tblCurrentStockPriceInfo" ("Stock Name" TEXT NOT NULL,"LTP" NUMERIC,"Prev Price" NUMERIC,"Change(%)" NUMERIC,"Change Price" NUMERIC,"Vol" NUMERIC,"Date" TEXT not null)'''
        query3 = "insert into tblCurrentStockPriceInfo values ('{}',{},{},{},{},{},'{}')"

        try:

            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            try:
                cursor.execute(query1)
            except sqlite3.OperationalError:
                pass

            cursor.execute(query2)
            df = self.stockPriceInfo
            for i in range(0, len(df)):

                if len(df[i]) == 0:
                    continue
                cursor.execute(query3.format(df[i][0], df[i][1], df[i][2], df[i][3], df[i][4], df[i][5],
                                             datetime.datetime.now().date().strftime("%m/%d/%Y")))
                con.commit()
        finally:
            cursor.close()
            con.close()


    def sqlLiteStockVol(self):
        self.stockVolInfo = super().rCurrentStockVolDelInfoWeb()
        query1 = "drop Table tblCurrentStockVolInfo"
        query2 = '''CREATE TABLE "tblCurrentStockVolInfo" ("Stock Name" TEXT NOT NULL,"Vol" NUMERIC,"Delivery Vol" NUMERIC,"Delivery(%)" NUMERIC,"LTP" NUMERIC)'''
        query3 = "insert into tblCurrentStockVolInfo values ('{}',{},{},{},{})"

        try:

            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            try:
                cursor.execute(query1)
            except sqlite3.OperationalError:
                pass

            cursor.execute(query2)
            df = self.stockVolInfo
            for i in range(0, len(df)):

                if len(df[i]) == 0:
                    continue
                cursor.execute(query3.format(df[i][0], df[i][1], df[i][2], df[i][3], df[i][4]))
                con.commit()
        finally:

            cursor.close()
            con.close()


    def sqlFinalStocklistOfTuple(self):

        query = '''select * from nayiTable'''
        try:
            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(query)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()

        return df

    def makeCurrentNayiTable(self):
        query1 = "drop table nayiTable"
        query2 = '''
create Table nayiTable as
select tblCurrentStockPriceInfo."Stock Name",tblCurrentStockPriceInfo."LTP",tblCurrentStockPriceInfo."Change(%)",
tblCurrentStockPriceInfo."Change Price",tblCurrentStockPriceInfo.[Vol],[tblCurrentStockVolInfo]."Delivery Vol",
[tblCurrentStockVolInfo]."Delivery(%)",tblCurrentStockPriceInfo."Date" from tblCurrentStockPriceInfo
inner join tblCurrentStockVolInfo on "tblCurrentStockPriceInfo"."Stock Name"=tblCurrentStockVolInfo."Stock Name"'''

        try:
            # dbFile = r"C:\Users\DELL\Desktop\College.db"
            con = sqlite3.connect(self.dbFile)
            cursor = con.cursor()
            cursor.execute(query1)
            cursor.execute(query2)
            con.commit()
        finally:

            cursor.close()
            con.close()



