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
import numpy as np

tickers = ["VUSA.L" , "VWRL.L" , "EMIM.L" , "SMEA.L"]
prices = yf.download(tickers,
                     start= "2017-12-18",
                       end= "2025-12-18",)
close = prices["Close"]
print(close.head()) 
print(close.shape)

returns = close.pct_change()
returns = returns.dropna()
# print(returns.head())
returns = returns[abs(returns["SMEA.L"]) <= 0.2 ]


mean_returns = returns.mean()   
std_returns = returns.std()
returns_matrix = returns.corr()
retuns_covmatrix = returns.cov()
print(mean_returns)
print(std_returns)
print(returns_matrix)
print(retuns_covmatrix)


weights = np.array([0.25, 0.25, 0.25, 0.25])
portfolio_variance = np.dot(weights, np.dot(returns_covmatrix, weights))
portfolio_volatility = portfolio_variance ** 0.5
