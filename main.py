# define ETF tickers
# VUSA.L  -> US equities (S&P 500)
# VWRL.L  -> Global equities
# EMIM.L  -> Emerging market equities
# VAGP.L  -> Global bonds
# VUKP.L  -> UK property / REITs
# set date range
# download price data
# check for missing values
import yfinance as yf
import pandas as pd
tickers = ["VUSA.L" , "VWRL.L" , "EMIM.L" , "VAGP.L", "VUKP.L"]
prices = yf.download(tickers,
                     start= "2017-12-18",
                       end= "2025-12-18",)
print(prices.head())