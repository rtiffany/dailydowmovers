#!/usr/bin/python

import yfinance as yf
import json
date = ""

class stock:
    def __init__(self,Ticker,Open,Close,Change,Pchange):
        self.Ticker = Ticker
        self.Open = Open
        self.Close = Close
        self.Change = Change
        self.Pchange = Pchange

def write_json(data, filename='movers.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def get_stocks(filename='dow30.txt'):
    global date
    unsortedStocks = []
    with open(filename, "r") as f:
        for l in f.readlines():
            ticker = yf.Ticker(l.strip())
            hist = ticker.history(period = "1d", interval = "1d")
            for t in hist.itertuples():
                change = t.Close - t.Open
                pchange = change / t.Open * 100
                unsortedStocks.append(stock(l.strip(), t.Open, t.Close, change, pchange))
                date = t.Index
                break
    return unsortedStocks

def sort_stocks(data):
    json_obj = {}
    json_obj[str(date)] = []
    sortedStocks = sorted(data, key=lambda stock: -stock.Pchange)
    for stock in data:
        json_obj[str(date)].append({
            'rank' : data.index(stock)+1,
            'ticker' : stock.Ticker,
            'open' : stock.Open,
            'close' : stock.Close,
            'change' : stock.Change,
            'percent' : stock.Pchange
            })
    return json_obj

def main():
    unsortedStocks = get_stocks()
    sortedStocks = sort_stocks(unsortedStocks)
    write_json(sortedStocks)

if __name__ == "__main__":
    main()