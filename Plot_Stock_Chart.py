# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from numpy.ma.core import size
from matplotlib import colors


# Enter API key
api_key = "API_KEY"

# Create variables to customize the API URL for the wanted symbol and interval
ticker = "TSLA"
interval = "1day"

# Use th API URL and enter a start and end date as well as the number of days of data wanted
api_url = f"https://api.twelvedata.com/time_series?symbol={ticker}&start_date=2022-01-01&end_date=2022-06-01&interval={interval}&outputsize=365&apikey={api_key}"

# Create a variable to get the URL data and create a Pandas dataframe
data = requests.get(api_url).json()
data_in_df = pd.DataFrame(data["values"])
print(data_in_df)

# Set the stock chart data to only take the last 10 days
date = data_in_df["datetime"][:10]
close = data_in_df["close"][:10]

# To avoid plotting the chart backward, flip the date and closing price arrays
new_date = date[::-1]
new_close = close.astype(float)[::-1]

# Plot the TSLA stock chart and style it
plt.style.use('dark_background')

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)

plt.xlabel("Date", size="20")
plt.ylabel("Stock Price ($)", size="20")
plt.title("TSLA Stock Chart", size="20")
plt.grid(axis="both", linestyle="dotted")
plt.plot(new_date,new_close, '#FFFFFF', linewidth="2")
plt.show()
