def data_url(symbol, api_key):
    """
    Composes website url to direct code where to fetch data from (distinguishes from crypto and regular stocks)

    Param1: symbol (string) clicker symbol of a crypto stock

    Param2: api_key (string) environment variable stored in .env file (import os, from dotenv import load_dotenv, declare variable)

    Example: data_url(BTC, ALPHAVANTAGE_API_KEY)

    Returns: https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={BTC}&apikey={SG...}

    """
    if len(symbol) == 4:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={(symbol)}&apikey={(api_key)}&datatype=csv"
    else:
        return f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={(symbol)}&apikey={(api_key)}"