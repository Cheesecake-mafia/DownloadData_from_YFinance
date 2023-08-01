from DataDownload_csv import DownloadData
import pandas as pd
import datetime
import glob, os
import sys
import yfinance as yf
import time

wiki_url = 'https://en.wikipedia.org/wiki/NIFTY_50'
symbols = pd.read_html(wiki_url)[2]["Symbol"]

for i,symbol in enumerate(symbols):
    symbols[i] = symbol + ".NS"

fpath = "C:\\Users\\f2013\\Downloads\\ccM Strategies\\Database\\Nifty-50\\"

for symbol in symbols:
    DownloadData(symbol,fpath,period=5)
    print(f"Done for {symbol.split('.')[0]} symbol.")
    print("-"*50)

