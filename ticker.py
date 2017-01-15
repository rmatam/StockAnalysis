import yahoo_finance as yf
import pandas as pd
import datetime as datetime
from matplotlib import pyplot as plt



#from yahoo_finance import Share

def getTicker(ticker):
	try:
		return yf.Share(ticker)
	except:
		print("Could not find ticker")



def getData(symbolName,startDate,endDate,filename):
	symbol=yf.Share(symbolName)
	data = symbol.get_historical(startDate,endDate)
	df = pd.DataFrame(data)
	# Output data into CSV
	df.to_csv(filename)
	return data


def plotLast20(ShareObject):
	data = ShareObject

