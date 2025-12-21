### Project Objective

This project is about properly learning portfolio theory, risk, and long-term investing by actually building something real in Python.

The aim is to design a real, investable portfolio and then put ~£500 of real money into it (with ongoing contributions), focusing on risk-adjusted returns, not trading or gambling.

## Investment Philosophy

- Long-term buy & hold

- Focus on best risk-adjusted performance

- Target is roughly 7–10% annual returns over the long run

- Only LSE-listed, GBP-denominated UCITS ETFs

Assets Analysed

So far I’ve analysed the following LSE ETFs:

- VWRL.L – Global equity

- VUSA.L – US equity (S&P 500)

- SMEA.L – European equity

- EMIM.L – Emerging markets equity

These were used to calculate returns, volatility, correlations, covariances, and portfolio-level risk.

## Tools & Architecture

- Python (pandas, numpy, yfinance) for all core analysis

- SQL to store data and keep a record of portfolio runs

- Excel + VBA for reporting, dashboards, and derivatives-related work

- SAS for statistical validation (e.g. CAPM, beta estimation)

- Git/GitHub to keep everything versioned and reproducible

## Current Status

- Core risk/return analysis is done

- Portfolio design is in progress

Next step is locking the final portfolio and moving toward real-money implementation