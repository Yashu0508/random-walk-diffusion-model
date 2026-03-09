import matplotlib.pyplot as plt
from src.black_scholes_pde_utilities import simulate_gbm

# Parameters
S0 = 100  # Initial price
mu = 0.05  # Drift
sigma = 0.2  # Volatility
T = 1  # Time horizon (1 year)
N = 1000  # Number of steps
n_paths = 10  # Number of trajectories

# Generate and plot 10 stock price paths
plt.figure(figsize=(10, 6))
for _ in range(n_paths):
    t, S = simulate_gbm(S0, mu, sigma, T, N)
    plt.plot(t, S, alpha=0.7)

# Title and labels
plt.title("Simulated Stock Price Paths (Geometric Brownian Motion)")
plt.xlabel('Time (years)')
plt.ylabel('Stock Price')

# Save the figure
plt.savefig('plots/gbm_stock_paths.png')
plt.show()