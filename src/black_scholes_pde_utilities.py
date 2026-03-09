"""
Black-Scholes PDE Utilities Module

This module contains utilities related to the Black-Scholes model, including simulation
of Geometric Brownian Motion (GBM), which models stock price dynamics.
"""

import numpy as np


def simulate_gbm(S0, mu, sigma, T, N):
    """
    Simulate a Geometric Brownian Motion path for stock price modeling.

    Parameters:
    S0 (float): Initial stock price.
    mu (float): Drift parameter, representing the expected return (growth rate).
    sigma (float): Volatility parameter, representing the standard deviation of returns.
    T (float): Time horizon.
    N (int): Number of time steps.

    Returns:
    tuple: (t, S)
        - t (numpy.ndarray): Time array from 0 to T.
        - S (numpy.ndarray): Simulated stock price path.
    """
    dt = T / N
    t = np.linspace(0, T, N + 1)
    S = np.zeros(N + 1)
    S[0] = S0

    for i in range(1, N + 1):
        # Generate random normal variable
        Z = np.random.normal()
        # Update price using GBM formula
        # Drift term: (mu - 0.5*sigma^2)*dt accounts for the expected growth
        # Volatility term: sigma*sqrt(dt)*Z introduces randomness proportional to volatility
        S[i] = S[i - 1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return t, S