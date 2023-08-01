import pandas as pd
import datetime
import glob, os
import yfinance as yf

# ...

fpath =  "C:\\Users\\f2013\\Downloads\\ccM Strategies\\Database\\Stock-DataBase\\"

class DownloadData:

    def __init__(self, asset, filepath, timeframe='1m', period=5):
        # Initialize the class with asset symbol, file path to store data, timeframe, and period.
        self.asset = asset
        self.filepath = filepath
        self.timeframe = timeframe
        self.period = period
        self.end_datetime = datetime.datetime.now()
        self.start_datetime = self.end_datetime - datetime.timedelta(days=self.period)

        try:
            # Check if the symbol's data already exists in the specified file path.
            symbol_exists = self.Check_if_symbol_exists()
            if symbol_exists:
                # If data exists, then download new data and append it.
                self.Download_and_Append()
            else:
                # If data doesn't exist, then download data and save it.
                self.Download_and_Save()
        except:
            print(f"We encountered some error in the try block for the symbol of {self.asset}!")

    def Download_and_Save(self):
        # Download data from Yahoo Finance for the given asset, timeframe, and period.
        dummy = yf.download(self.asset, start=self.start_datetime, end=self.end_datetime, interval=self.timeframe)
        dummy.index.name = "Datetime"
        # Save the downloaded data to a CSV file with the asset name as the filename.
        dummy.to_csv(self.filepath + f"{self.asset}.csv")
        print(f"Downloaded the data for {self.asset} successfully and saved at {self.filepath}.")

    def Check_if_symbol_exists(self):
        # Check if the CSV file for the asset exists in the specified file path.
        if os.path.isfile(self.filepath + self.asset + ".csv"):
            print(f"Data for symbol {self.asset} already exists.")
            return True
        return False

    def Return_latest_datetime(self):
        # Read the latest datetime index from the existing CSV file for the asset.
        path_csv = glob.glob(self.filepath + self.asset + ".csv")
        df = pd.read_csv(path_csv[0], index_col="Datetime")
        print(f"The latest datetime index for the data is {max(df.index)}.")
        return pd.to_datetime(df.index[-1])

    def Download_and_Append(self):
        # Adjust the end_datetime to the current time.
        self.end_datetime = datetime.datetime.now()
        # Get the latest datetime index from the existing data.
        latest_index = self.Return_latest_datetime()
        # Download new data from Yahoo Finance starting from the latest index to the current time.
        dummy = yf.download(self.asset, start=latest_index, end=self.end_datetime, interval=self.timeframe)
        dummy.index.name = "Datetime"
        print(f"We already have data from {latest_index} so we will just append data from that timestamp.")
        # Filter out the rows with datetime greater than the latest index.
        dummy = dummy.loc[dummy.index > latest_index]
        print(f"We have added new {len(dummy)} rows to the data.")
        # Read the existing data and concatenate it with the new data.
        df = pd.read_csv(self.filepath + self.asset + ".csv", index_col="Datetime")
        concat_df = pd.concat((df, dummy), axis=0, join="outer")
        # Save the combined data to the CSV file.
        concat_df.to_csv(self.filepath + f"{self.asset}.csv")
