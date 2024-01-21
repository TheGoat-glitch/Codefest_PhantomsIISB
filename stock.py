import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

company = input("Which stock would you like to invest in? Please enter the NYSE symbol")

shares = input("How many shares of the company would you like?")




# Download the Visa stock data
df = yf.download(company)

# Calculate the logarithmic returns
returns = np.log(1 + df['Adj Close'].pct_change())

# Calculate the mean and standard deviation of returns
mu, sigma = returns.mean(), returns.std()

# Simulate the returns for the same number of trading days
sim_rets = np.random.normal(mu, sigma, size=len(df) - 1)

# Get the last closing price
initial = df['Adj Close'].iloc[-1]

# Simulate the stock prices starting from the day after the last recorded day
sim_prices = initial * (1 + sim_rets).cumprod()

# Create a DataFrame for the simulated prices with the appropriate date index
sim_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=len(sim_prices))
simulated_df = pd.DataFrame({'Adj Close': sim_prices}, index=sim_dates)

# Concatenate the real and simulated data
combined_df = pd.concat([df['Adj Close'], simulated_df])



# Plot the combined stock prices
plt.plot(combined_df)
plt.legend(['Real Prices', 'Simulated Prices'])
plt.show()



