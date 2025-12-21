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
# Upgrade to auto-dates later this allows continous monitoring.

returns = close.pct_change()
returns = returns.dropna()
returns = returns[abs(returns["SMEA.L"]) <= 0.2 ]
# For future purposes the manual cleaning (like removing outliers) those rules still apply, 
# but the rows affected may change depending on the new period.

mean_returns = returns.mean()   
std_returns = returns.std()
returns_matrix = returns.corr()
returns_covmatrix = returns.cov()
print(mean_returns)
print(std_returns)
print(returns_matrix)
print(returns_covmatrix)

weights = np.array([0.20, 0.20, 0.40, 0.20])
portfolio_variance = np.dot(weights, np.dot(returns_covmatrix, weights))
portfolio_volatility = portfolio_variance ** 0.5
print(portfolio_variance)

trading_days = 252
annual_portfolio_volatility = portfolio_volatility * (trading_days ** 0.5)
annual_portfolio_volatility_pct = annual_portfolio_volatility * 100
print(annual_portfolio_volatility_pct)

portfolio_expected_return = np.dot(mean_returns, weights)
annual_portfolio_exp_return_pct = portfolio_expected_return * trading_days * 100
print(annual_portfolio_exp_return_pct)