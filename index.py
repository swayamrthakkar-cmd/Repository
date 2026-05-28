import yfinance as yf
import pandas as pd
import math
import statistics

data = yf.download("AAPL", period="24mo", interval="1d")

print(data)

close_prices = []
volumes = []

for i in range(0, 361, 30):
    close_prices.append(float(data["Close"]["AAPL"].iloc[-1 - i]))
    volumes.append(float(data["Volume"]["AAPL"].iloc[-1 - i]))

def month12Momentum(array):
    positive = 0
    gains = []
    for i in range(len(array)-1):
        gains.append(array[i] - array[i+1])

    for g in gains:
        if g > 0:
            positive += 1
        
    score = (positive / len(gains)) * 100
    return score

def month12Momentum2(prices):
    total = 0

    for i in range(len(prices) - 1):
        old_price = prices[i + 1]
        new_price = prices[i]

        percent_change = (
            (new_price - old_price)
            / old_price
        ) * 100

        total += percent_change

    return total

def month12Growth(array):
    score = (statistics.mean(array) - array[-1]) * 10
    return score

def month12Agg(array, share):
    ticker = yf.Ticker(share)
    x = ticker.recommendations

    return x

def recordData(array):
    ...

print(statistics.mean([month12Momentum(close_prices), month12Momentum2(close_prices), month12Growth(close_prices)]))