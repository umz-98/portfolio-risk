### Project Objective

This project is about properly learning portfolio theory, risk, and long-term investing by actually building something real in Python.

The aim is to design a real, investable portfolio and then put ~£500 of real money into it (with ongoing contributions), focusing on risk-adjusted returns, not trading or gambling.

## Investment Philosophy

- Long-term buy & hold

- Focus on best risk-adjusted performance

- Target is roughly 7–10% annual returns over the long run

- Only LSE-listed, GBP-denominated UCITS ETFs

Assets Analysed

Historical data was analysed for the following ETFs:

- VWRL.L – Global equity

- VUSA.L – US equity (S&P 500)

- SMEA.L – European equity

- EMIM.L – Emerging markets equity

- VAGS.L – Global aggregate bonds, GBP-hedged (Accumulating)

- AGBP.L – Global aggregate bonds, GBP-hedged (Distributing, used for validation)

These were used to calculate returns, volatility, correlations, covariances, and portfolio-level risk.

For each asset and portfolio combination, the following were calculated:

- Daily and annualised returns

- Volatility

- Correlation and covariance matrices

- Portfolio-level risk and return

- Sharpe ratios

## Portfolio Construction & Results

# Multiple portfolios were tested, including:

- 100% equity

- 90/10, 80/20, and 70/30 equity/bond allocations

- Addition of a third ETF (emerging markets)

# Using Sharpe ratio as the decision rule:

- 80% Global Equity / 20% Global Bonds provided the  best practical balance between return and risk

- Adding a third ETF (EMIM) reduced Sharpe and was therefore rejected

## Final Portfolio

- 80% VWRL.L – Global Equity

- 20% VAGS.L – Global Bonds (GBP-hedged, Accumulating)

This portfolio offers strong diversification, controlled volatility, and robust long-term growth characteristics.

## Tools & Architecture

- Python (pandas, numpy, yfinance) for all core analysis

- SQL to store data and keep a record of portfolio runs

- Excel + VBA for reporting, dashboards, and derivatives-related work

- SAS for statistical validation (e.g. CAPM, beta estimation)

- Git/GitHub to keep everything versioned and reproducible

## Current Status

- Core portfolio analysis completed

- Sharpe-based portfolio selection completed

- Final allocation selected

Ready to extend into database storage, dashboards, and statistical validation