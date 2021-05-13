import pandas as pd 
import yfinance as yf
import datetime


my_stocks = ['TSLA']
#,'AAPL','SNAP','ETSY','LMND','RKT','PRPL','RDFN','DIS','MSFT','AMZN','NFLX','SHOP','NVDA','SFT','AMD','EXPI','TAN','ENPH']
my_portfolio = []


class Stock:

    def __init__(self, symbol,df):
        self.symbol = symbol
        self.df = df
    
    def get_symbol(self):
        return self.symbol

    def get_df(self):
        return self.df
    
    def find_opportunities(self):
        self.df = self.df.iloc[:,[0,3]]
        self.df['Pchange'] = ((self.df.Close - self.df.Open) / self.df.Open) * 100
        opportunities = self.df[self.df["Pchange"] < -3.0]
        return opportunities

def time_constructor():
    today = datetime.datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    start_day = int(today.strftime("%d")) - 1
    end_day = today.strftime("%d")
    start_time = '%s-%s-%d' % (year,month,start_day)
    end_time = '%s-%s-%s' % (year,month,end_day)
    return start_time, end_time



time = time_constructor()
for symbol in my_stocks:
    my_portfolio.append(Stock(symbol, yf.download(symbol, start='2018-01-01', end=time[1], progress=False)))

for stock in my_portfolio:
    print(stock.find_opportunities())
    