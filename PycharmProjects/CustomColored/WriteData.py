import datetime

import pandas, openpyxl, requests, bs4, pyodbc

from ReadData import ReadData


class WriteData(ReadData):

    def wExcel(self, filePath,df):
        data = pandas.DataFrame(df)
        data.to_excel(filePath)

    def wStockPriceSQL(self):
        self.stockPriceInfo = super().rCurrentStockPriceInfoWeb()
        query1 = "delete from tblCurrentStockInfo"
        # query2 = "create table tblCurrentStockInfo ([Stock Name] nvarchar(60) not null primary key,[LTP] int,[Prev Price] int,[Change(%)] int,[Change Price] int,[Vol] int),[Date] date not null"
        query3 = "insert into tblCurrentStockInfo values ('{}',{},{},{},{},{},'{}')"

        try:

            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            try:
                cursor.execute(query1)
            except pyodbc.ProgrammingError:
                pass

            df = self.stockPriceInfo
            for i in range(0, len(df)):

                if len(df[i]) == 0:
                    continue
                cursor.execute(query3.format(df[i][0], df[i][1], df[i][2], df[i][3], df[i][4], df[i][5],
                                             datetime.datetime.now().date().strftime("%m/%d/%Y")))
                cursor.commit()
        finally:
            cursor.close()
            con.close()
            print('close')

    def wStockVolSQL(self):
        self.stockVolInfo = super().rCurrentStockVolDelInfoWeb()
        query1 = "delete from tblCurrentStockVolInfo"
        # query2 = "create table tblCurrentStockVolInfo ([Stock Name] nvarchar(60) not null primary key,[Trade Vol] float,[Delivery Vol] float,[Delivery(%)] float,[LTP] float)"
        query3 = "insert into tblCurrentStockVolInfo values ('{}',{},{},{},{})"

        try:
            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            try:
                cursor.execute(query1)
            except pyodbc.ProgrammingError:
                pass
            # cursor.execute(query2)
            df = self.stockVolInfo
            for i in range(0, len(df)):
                if len(df[i]) == 0:
                    continue
                cursor.execute(query3.format(df[i][0], df[i][1], df[i][2], df[i][3], df[i][4]))
            cursor.commit()
        finally:

            cursor.close()
            con.close()
            print('close')

    def makeCurrentNayiTable(self):
        query1 = "drop table nayiTable"
        query2 = "select [dbo].[tblCurrentStockInfo].[Stock Name],[dbo].[tblCurrentStockInfo].[LTP],[dbo].[tblCurrentStockInfo].[Change(%)],[dbo].[tblCurrentStockInfo].[Change Price],[dbo].[tblCurrentStockInfo].[Vol],[dbo].[tblCurrentStockVolInfo].[Delivery Vol],[dbo].[tblCurrentStockVolInfo].[Delivery(%)],[Date] into nayiTable from [Stock_Market_K].[dbo].[tblCurrentStockInfo] inner join dbo.tblCurrentStockVolInfo on dbo.tblCurrentStockInfo.[Stock Name]=dbo.tblCurrentStockVolInfo.[Stock Name]"
        try:
            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
#             try:
            cursor.execute(query1)
#             except pyodbc.ProgrammingError:
#                 pass
            cursor.execute(query2)
            cursor.commit()
        finally:

            cursor.close()
            con.close()
            print('close')

    def allDateStockInfo(self):

        query2 = "insert into allDateStockInfo select * from allDateStockInfo union all select * from nayiTable"
        try:
            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            cursor.execute(query2)
            cursor.commit()
        finally:
            cursor.close()
            con.close()
            print('close')

    def sqlFinalStocklistOfTuple(self):

        query = "Select stoke,[LTP],[Change(%)] from dbo.All$ inner join dbo.nayiTable on dbo.All$.Stoke=dbo.nayiTable.[Stock Name] where Industry='{}' and where '{} > {} order by Change(%)"
        try:
            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            cursor.execute(query)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()
            print('close')
        return df

    def fetchFromAllDateStockInfo(self):
        query = "sel" \
                ""
        try:
            connection_string = 'Driver={SQL Server};Server=DESKTOP-2CDQJ66\SQLEXPRESS;Database=Stock_Market_K;Trusted_Connection=yes;'
            con = pyodbc.connect(connection_string)
            cursor = con.cursor()
            cursor.execute(query)
            df = cursor.fetchall()

        finally:
            cursor.close()
            con.close()
            print('close')
        return df



