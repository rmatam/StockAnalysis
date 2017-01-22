import sys, os
import stockDataExtractor
import modelTrainer

sys.dont_write_bytecode = True # prevents generation of .pyc files

if __name__ == "__main__":

    exec(open("Options/options.py").read()) # read in all the options

    data = stockDataExtractor.extract(stocks, features) # extract data for all stocks
    modelTrainer.train(data) # train a neural net on the data
