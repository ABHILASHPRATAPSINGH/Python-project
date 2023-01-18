import pandas, openpyxl, requests, bs4, pyodbc


class ReadData:

    def __init__(self):
        pass

    def rExcel(self):
        excelFilePath: str = r"C:\Users\DELL\Desktop\Market_watch.xlsm"
        df = pandas.read_excel(excelFilePath, sheet_name='All')
        return df

    def rCurrentStockPriceInfoWeb(self):
        hdr = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
        URL_lst = ["https://www.financialexpress.com/market/stock-market/nse-top-gainers/","https://www.financialexpress.com/market/stock-market/nse-top-losers/"]
        df = []
        for url in URL_lst:
            resp = requests.get(url, headers=hdr)
            soup = bs4.BeautifulSoup(resp.text, 'html.parser')
            table = soup.find(id='modality')
            for tr in table.find_all('tr'):
                lst = []
                for td in tr.find_all('td'):
                    lst.append(td.text)
                df.append(lst)
        return df

    def rCurrentStockVolDelInfoWeb(self):
        hdr = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
        URL_lst = ["https://www.financialexpress.com/market/stock-market/nse-low-delivery/"]
        df = []
        for url in URL_lst:
            resp = requests.get(url, headers=hdr)
            soup = bs4.BeautifulSoup(resp.text, 'html.parser')
            table = soup.find(id='modality')
            for tr in table.find_all('tr'):
                lst = []
                for td in tr.find_all('td'):
                    lst.append(td.text)
                df.append(lst)
        return df