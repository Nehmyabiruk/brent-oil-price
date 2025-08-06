import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import numpy as np

# Load preprocessed data
data = pd.read_csv("data/BrentOilPrices_Preprocessed.csv", index_col='Date', parse_dates=True)
prices = data['Price'].values
n_points = len(prices)

# Bayesian Change Point Model
with pm.Model() as model:
    # Prior for change point
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_points-1)
    # Priors for means before and after change point
    mu_1 = pm.Normal("mu_1", mu=50, sigma=20)
    mu_2 = pm.Normal("mu_2", mu=50, sigma=20)
    # Switch function
    mu = pm.math.switch(tau >= np.arange(n_points), mu_1, mu_2)
    # Likelihood
    observation = pm.Normal("obs", mu=mu, sigma=10, observed=prices)
    # Sampling
    trace = pm.sample(2000, tune=1000, return_inferencedata=True)

# Plot posterior distributions
az.plot_trace(trace)
plt.savefig('plots/change_points.png')
plt.close()

# Summary
summary = az.summary(trace)
print(summary)
