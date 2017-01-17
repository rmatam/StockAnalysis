import sys
sys.dont_write_bytecode = True # prevents generation of .pyc files

from extract_V1_2 import extract
from processor_V1_2 import process
import os

#execfile("options.py")
exec(compile(open("options.py","r").read(),"options.py",'exec'))

if not os.stat("StockData"): os.mkdir("StockData")

for ticker in stocks:

    print(ticker)
    extract(ticker)
    process(ticker)
