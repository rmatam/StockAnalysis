import sys
sys.dont_write_bytecode = True # prevents generation of .pyc files

from extract import extract
from process import process
import os

execfile("options.py")

if not os.stat("StockData"): os.mkdir("StockData")

for ticker in stocks:

    print ticker
    extract(ticker)
    process(ticker)
