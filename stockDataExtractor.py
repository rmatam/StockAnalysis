import pandas as pd, pandas_datareader as web
import csv
from stockstats import StockDataFrame as Sdf

def extract(stocks, features):

    if len(stocks) == 0: # read in all stocks currently on the NYSE
        NYSEListings = open("Options/NYSEListings.csv", "r")
        NYSEReader = csv.reader(NYSEListings)
        for row in NYSEReader:
            if '^' not in row[0] and '.' not in row[0]: # skip symbols with "^" or "." in name - appear to be duplicates
                stocks.append(row[0].strip())
        stocks.pop(0) # get rid of "Symbol" header from first line of file

    allExtractedData = pd.DataFrame() # empty data frame

    for ticker in stocks:

        print(ticker)
        webData = web.get_data_yahoo(ticker)
        webData = webData.round(2) # round all the open and close data to 2 decimal places
        sdfData = Sdf.retype(webData) # StockDataFrame extends the pandas DataFrame by being able to extract stock info on the fly
        extractedData = pd.DataFrame() # empty data frame

        for feature in features:
            extractedData[feature] = sdfData[feature]

        allExtractedData = allExtractedData.append(extractedData, ignore_index=True)

    allExtractedData = allExtractedData.dropna() # drop rows without all features

    return allExtractedData
