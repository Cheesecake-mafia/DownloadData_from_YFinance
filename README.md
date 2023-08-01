# DownloadData Class

The `DownloadData` class is a Python script that facilitates the download of historical financial data for a given asset from Yahoo Finance. The data is downloaded in the form of OHLCV (Open, High, Low, Close, Volume) for a specified time frame and period. The class handles scenarios when the data already exists for the asset and appends new data if available.

## Requirements

- Python 3.x
- pandas
- yfinance

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using pip:

```
pip install pandas yfinance
```

## Usage

1. Import the `DownloadData` class from the script where you want to use it:

```python
from DataDownload_csv import DownloadData
```

2. Create an instance of the `DownloadData` class with the desired parameters:

```python
# Define the asset symbol, file path, timeframe, and period.
asset = "AAPL"  # Example asset symbol (replace with your desired asset symbol)
filepath = "C:\\Users\\YourUserName\\Downloads\\Stock-DataBase\\"  # Replace with your desired file path
timeframe = '1d'  # Example timeframe: '1d' (daily), '1h' (hourly), '5m' (5 minutes), etc.
period = 30  # Example period in days

# Create an instance of the DownloadData class
data_downloader = DownloadData(asset, filepath, timeframe, period)
```

3. The class will automatically check if the data for the specified asset already exists in the specified file path. If data exists, it will download new data from the latest index up to the current time and append it to the existing data. If data does not exist, it will download data for the specified period and save it as a CSV file named after the asset.

4. The downloaded data will be saved in CSV format with the asset name as the filename, and it will be stored in the specified file path.

## Notes

- The class uses the Yahoo Finance API (`yfinance`) to download historical financial data. Please ensure that you comply with Yahoo Finance's terms of use and data usage policies.

- The class assumes that the specified file path exists and has write permissions. If the directory does not exist, you may encounter an error during data download.

- For each asset, the class will download data starting from the latest available index in the existing CSV file (if it exists) up to the current time.

- The class provides basic error handling, but it is recommended to handle specific exceptions and edge cases based on your requirements.

## Contributing

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request.

## License

This code is licensed under the MIT License. See the LICENSE file for more details.

---
Replace "YourUserName" in the filepath with your actual username. Make sure to include any additional details, instructions, or disclaimers relevant to your specific use case and requirements.
