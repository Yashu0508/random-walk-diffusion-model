import numpy as np
import matplotlib.pyplot as plt
import os

# Create plots folder
os.makedirs("plots", exist_ok=True)

# =============================
# Model parameters
# =============================

S_max = 200      # Maximum stock price
K = 100          # Strike price
T = 1.0          # Time to maturity
sigma = 0.2      # Volatility
r = 0.05         # Risk-free rate

# =============================
# Grid parameters
# =============================

M = 100          # Stock price steps
N = 1000         # Time steps (IMPORTANT: increased for stability)

dS = S_max / M
dt = T / N

# =============================
# Grids
# =============================

S = np.linspace(0, S_max, M + 1)
t = np.linspace(0, T, N + 1)

# Option price grid
V = np.zeros((N + 1, M + 1))

# =============================
# Terminal condition
# =============================

V[N, :] = np.maximum(S - K, 0)

# =============================
# Boundary conditions
# =============================

V[:, 0] = 0

for n in range(N + 1):
    V[n, M] = S_max - K * np.exp(-r * (T - t[n]))

# =============================
# Explicit finite difference
# =============================

for n in range(N - 1, -1, -1):

    for j in range(1, M):

        d2V_dS2 = (V[n+1, j-1] - 2*V[n+1, j] + V[n+1, j+1]) / (dS**2)

        dV_dS = (V[n+1, j+1] - V[n+1, j-1]) / (2*dS)

        V[n, j] = V[n+1, j] + dt * (
            0.5 * sigma**2 * S[j]**2 * d2V_dS2
            + r * S[j] * dV_dS
            - r * V[n+1, j]
        )

# =============================
# Plot
# =============================

plt.figure(figsize=(10,6))
plt.plot(S, V[0,:], label="Finite Difference Solution")

plt.xlabel("Stock Price")
plt.ylabel("Option Price")
plt.title("European Call Option Price via Finite Difference Black-Scholes")

plt.grid(True)
plt.legend()
plt.savefig("plots/black_scholes_fd.png")
plt.show()