"""
Brownian Motion Generator Module

This module implements the generation of Brownian motion (Wiener process), a continuous-time
stochastic process. Brownian motion B(t) has the following properties:
- B(0) = 0
- Independent increments: B(t) - B(s) is independent of the past for s < t
- Normally distributed increments: B(t) - B(s) ~ N(0, t - s)
- Continuous paths

The discretization approximates the continuous process by dividing time into N steps.
Each increment dB = B(t_{i+1}) - B(t_i) is approximated by sqrt(dt) * Z_i, where Z_i ~ N(0,1).
This connects to random walks: a random walk is the discrete analog, and Brownian motion
is the limit as the step size goes to zero.
"""

import numpy as np


def generate_brownian_motion(T, N):
    """
    Generate a Brownian motion path over time [0, T] with N steps.

    Parameters:
    T (float): Total time.
    N (int): Number of time steps.

    Returns:
    tuple: (t, B)
        - t (numpy.ndarray): Time array from 0 to T.
        - B (numpy.ndarray): Brownian motion path, B[0] = 0.
    """
    dt = T / N
    # Generate independent normal increments: each ~ N(0, dt)
    # This reflects the normal distribution property of increments
    increments = np.random.normal(0, np.sqrt(dt), N)
    # Cumulative sum gives the path, showing independent increments
    B_path = np.cumsum(increments)
    # Prepend 0 for B(0) = 0
    B = np.concatenate([[0], B_path])
    # Time array
    t = np.linspace(0, T, N + 1)
    return t, B