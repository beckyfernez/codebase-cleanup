

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv

from app.utils import to_usd
from app.data_fetch import data_url

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
url = data_url(symbol, ALPHAVANTAGE_API_KEY)

df = read_csv(url)
#print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
