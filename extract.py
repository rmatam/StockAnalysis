import csv
import pandas as pd
import pandas_datareader as web
from stockstats import StockDataFrame as Sdf
from sys import argv

def extract(ticker):

    data = web.get_data_yahoo(ticker)

    stock_df = Sdf.retype(data)
    data['rsi']=stock_df['rsi_14']
    data['macd']=stock_df['macd']

    del data['close_-1_s']
    del data['close_-1_d']
    del data['rs_14']
    del data['rsi_14']
    del data['macds']

    ls = data.values.tolist()

    with open("StockData/"+ticker+"_raw.csv","w") as f:
        writer = csv.writer(f)
        writer.writerows(ls)
