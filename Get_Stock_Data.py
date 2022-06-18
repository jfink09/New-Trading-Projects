import requests
import pandas as pd
import json

api_key = "API_KEY"

ticker = "AAPL"
interval = "1day"
api_url = f"https://api.twelvedata.com/time_series?symbol={ticker}&start_date=2022-01-01&end_date=2022-06-01&interval={interval}&outputsize=365&apikey={api_key}"

data = requests.get(api_url).json()
data_in_df = pd.DataFrame(data["values"])
print(data_in_df)

