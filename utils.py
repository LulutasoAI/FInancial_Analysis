from pandas_datareader import data
from datetime import date
def stock_id_to_prices(stock_id,start_date):
    today = date.today()
    end_date = "{}".format(today)
    df = data.DataReader(stock_id, "yahoo", start_date, end_date)
    df = df[[ "Open", "High", "Low", "Close", "Volume"]]
    prices = df["Close"]
    return prices