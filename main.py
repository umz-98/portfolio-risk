# define ETF tickers
# VUSA.L  -> US equities (S&P 500)
# VWRL.L  -> Global equities
# EMIM.L  -> Emerging market equities
# SMEA.L  ->  European equity
# set date range
# download price data
# check for missing values
import yfinance as yf
import pandas as pd
tickers = ["VUSA.L" , "VWRL.L" , "EMIM.L" , "SMEA.L"]
prices = yf.download(tickers,
                     start= "2017-12-18",
                       end= "2025-12-18",)
close = prices["Close"]
print(close.head()) 
print(close.shape)

returns = close.pct_change()
returns = returns.dropna()
print(returns.head())

mean_returns = returns.mean()
std_returns = returns.std()
print(mean_returns)
print(std_returns)
x = returns["SMEA.L"].describe()
print(x)