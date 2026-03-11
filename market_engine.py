import requests
from config import STOCKS

def get_price(symbol):

    try:

        url=f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"

        r=requests.get(url).json()

        price=r["quoteResponse"]["result"][0]["regularMarketPrice"]
        change=r["quoteResponse"]["result"][0]["regularMarketChangePercent"]

        return round(price,2),round(change,2)

    except:

        return None,None


def premarket_scan():

    movers=[]

    for s in STOCKS:

        price,change=get_price(s)

        if change and abs(change)>2:

            movers.append(f"{s} {change}%")

    return movers
