import csv
import pandas as pd
import pandas_datareader as web
from stockstats import StockDataFrame as Sdf
from sys import argv

#ticker = argv[1]
def extract(ticker):
	data = web.get_data_yahoo(ticker)

	stock_df = Sdf.retype(data)
	data['rsi_14']=stock_df['rsi_14']
	data['rsi_6']=stock_df['rsi_6']
	data['macd']=stock_df['macd']
	data['boll_ub']=stock_df['boll_ub']
	data['boll_lb']=stock_df['boll_lb']
	data['tr']=stock_df['tr']
	data['dma']=stock_df['dma']
	data['pdi']=stock_df['pdi']
	data['mdi']=stock_df['mdi']
	data['trix']=stock_df['trix']
	data['vr']=stock_df['vr']
	data['cr']=stock_df['cr']
	data['kdjk']=stock_df['kdjk']
	ls = data.values.tolist()

	with open("StockData/"+ticker+"_raw.csv","w") as f:
		writer = csv.writer(f)
		writer.writerows(ls)


	


