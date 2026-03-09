"""
Random Walk Model Module

This module implements a 1D symmetric random walk model. A random walk is a mathematical
object that describes a path consisting of a succession of random steps. In a symmetric
random walk, each step is equally likely to be +1 or -1.

Mathematically, the position after n steps is S_n = sum_{i=1}^n X_i, where X_i are i.i.d.
random variables with P(X_i = 1) = P(X_i = -1) = 1/2.

The expected position E[S_n] = 0, and the variance Var(S_n) = n, since Var(X_i) = 1 and
steps are independent. Thus, the variance grows linearly with time (number of steps).
"""

import numpy as np


def random_walk(n_steps):
    """
    Generate a single 1D symmetric random walk path.

    Parameters:
    n_steps (int): Number of steps in the random walk.

    Returns:
    numpy.ndarray: Array of positions at each step, starting from 0.
    """
    steps = np.random.choice([-1, 1], size=n_steps)
    positions = np.cumsum(steps)
    return positions


def multiple_random_walks(n_steps, n_paths):
    """
    Generate multiple 1D symmetric random walk paths.

    Parameters:
    n_steps (int): Number of steps per path.
    n_paths (int): Number of independent random walk paths to generate.

    Returns:
    numpy.ndarray: 2D array of shape (n_paths, n_steps) with positions.
    """
    steps = np.random.choice([-1, 1], size=(n_paths, n_steps))
    paths = np.cumsum(steps, axis=1)
    return paths


def compute_statistics(paths):
    """
    Compute mean and variance of positions at each step across multiple paths.

    Parameters:
    paths (numpy.ndarray): 2D array of shape (n_paths, n_steps) with random walk paths.

    Returns:
    tuple: (mean_positions, variance_positions)
        - mean_positions (numpy.ndarray): Mean position at each step.
        - variance_positions (numpy.ndarray): Variance of positions at each step.
    """
    mean_positions = np.mean(paths, axis=0)
    variance_positions = np.var(paths, axis=0)
    return mean_positions, variance_positions