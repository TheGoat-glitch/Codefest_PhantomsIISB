import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# This will show the stock price of Apple.inc. When using this, its important to put the name of the company in the NYSE (New York Stock Exchange) name
df = yf.download("AAPL")

# This shows the logarithmic returns compounded over time
returns = np.log(1 + df['Adj Close'].pct_change())

# This calculates the mean and standard deviation and the simulated returns taking this into account
mu, sigma = returns.mean(), returns.std()

# Simulate the returns for the same number of trading days
sim_rets = np.random.normal(mu, sigma, size=len(df) - 1)

# This will get the last closing price
initial = df['Adj Close'].iloc[-1]

# This shows how the stock price will continue to either rise or fall after the closing price
sim_prices = initial * (1 + sim_rets).cumprod()

# Create a DataFrame for the simulated prices with the appropriate date index
sim_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=len(sim_prices))
simulated_df = pd.DataFrame({'Adj Close': sim_prices}, index=sim_dates)

# Concatenate the real and simulated data
combined_df = pd.concat([df['Adj Close'], simulated_df])

# The data gets plotted into a graph
plt.plot(combined_df)
plt.legend(['Real Prices', 'Simulated Prices'])
plt.show()
