
"""We are creating a class to download data intraday data of required granularity for any security from Yahoo Finance and then adding 
it to a database. If the table for the particular security already exists in the database, we are then appending just the extra data 
to the database. """

# Imports
import pandas as pd
import numpy as np
import datetime
import os, glob
import sys
import yfinance as yf
from sqlalchemy import create_engine


class Download_Data:

    def __init__(self, asset, timeframe = '1m', days = 5, create_database=True):
        self.asset = asset
        self.timeframe = timeframe
        self.days = days
        self.create_database = create_database
        self.end_datetime = datetime.datetime.now()
        self.start_datetime = self.end_datetime - datetime.timedelta(days = self.days)
        self.engine = create_engine('sqlite:///Database.db')
        self.data = yf.download(self.asset, start=self.start_datetime, end=self.end_datetime, interval= self.timeframe).round(2)
        self.data.index.name = "Datetime"
        self.storing_in_db()
        print(self.retrieving_last_dt())


    def storing_in_db(self):
        self.data.to_sql(f'{self.asset}', self.engine, if_exists='append')
    
    def retrieving_last_dt(self):
        dummy = pd.read_sql(f'SELECT MAX(Datetime) from "{self.asset}"', self.engine)
        latest_datetime = dummy.iloc[0,0]
        return latest_datetime
    
        
abc = Download_Data("BTC-USD", '1m', days=2)



