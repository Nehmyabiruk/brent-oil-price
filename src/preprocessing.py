import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess Brent oil price data
path = "data/BrentOilPrices.csv"
data = pd.read_csv(path)
data['Date'] = pd.to_datetime(data['Date'], format='mixed', dayfirst=False)
data = data.sort_values(by='Date').set_index('Date')
data['Price'] = data['Price'].interpolate(method='time')
data = data.dropna(subset=['Price'])
data['Log_Return'] = np.log(data['Price']).diff().dropna()

# Save preprocessed data
data.to_csv("data/BrentOilPrices_Preprocessed.csv")

# Basic EDA
plt.figure(figsize=(12, 6))
plt.plot(data['Price'], label='Brent Oil Price')
plt.title('Brent Oil Prices (1987-2022)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.savefig('plots/price_trend.png')
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(data['Log_Return'], label='Log Returns')
plt.title('Log Returns of Brent Oil Prices')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.legend()
plt.savefig('plots/log_returns.png')
plt.close()
