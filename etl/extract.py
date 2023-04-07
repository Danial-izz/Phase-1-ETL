import yfinance as yf 

class DataExtractor:

    def __init__(self, stock_symbol):
        self.symbol = stock_symbol
        self.stock_data = None

    def extract_stock_data(self,period):
        self.stock_data = yf.Ticker(self.symbol).history(period = period)

    
