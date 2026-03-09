# From Random Walk to Option Pricing: The Heat Equation Behind Financial Markets

## Overview

This project explores the profound mathematical connections between stochastic processes, partial differential equations, and financial mathematics. Starting from the simple random walk, we build up to the Black-Scholes model for option pricing, demonstrating how Brownian motion serves as the continuous limit of random walks and how the heat equation provides the analytical foundation for pricing financial derivatives. Through computational simulations, we visualize these concepts and illustrate their applications in quantitative finance.

## Mathematical Ideas

### Random Walk
A random walk is a discrete-time stochastic process where each step is a random variable, typically ±1 with equal probability. The position after n steps follows a binomial distribution, with variance growing linearly with time. This model captures diffusive behavior in discrete settings.

### Brownian Motion
Brownian motion, or the Wiener process, is the continuous-time limit of a random walk. It is characterized by independent, normally distributed increments and continuous paths. The process B(t) has the property that B(t) - B(s) ~ N(0, t-s) for s < t.

### Heat Equation
The heat equation ∂u/∂t = D ∂²u/∂x² describes the diffusion of heat (or probability density) over time. Its fundamental solution is the Gaussian kernel, which emerges from the central limit theorem applied to random walks. This PDE connects stochastic processes to deterministic diffusion phenomena.

### Black-Scholes PDE
The Black-Scholes equation for option pricing is ∂V/∂t + (1/2)σ²S² ∂²V/∂S² + rS ∂V/∂S - rV = 0, where V is the option value, S is stock price, σ is volatility, and r is risk-free rate. This PDE arises from the geometric Brownian motion model of stock prices and can be solved using the heat equation through a change of variables.

## Computational Experiments

### Random Walk Simulation
Simulates multiple 1D random walk paths and visualizes their trajectories, demonstrating the diffusive spread over time.

### Diffusion Visualization
Plots the analytical Gaussian solution of the heat equation at different times, showing how an initial delta function spreads according to the diffusion equation.

### Geometric Brownian Motion
Generates stock price paths using geometric Brownian motion, illustrating the stochastic nature of asset prices in the Black-Scholes framework.

### Numerical Black-Scholes Solution
Implements finite difference methods to solve the Black-Scholes PDE numerically, providing option prices for comparison with analytical solutions.

## Project Structure

```
random-walk-diffusion-model/
├── README.md
├── requirements.txt
├── docs/
│   ├── project_report.md
│   └── theory_notes.md
├── simulations/
│   ├── random_walk_simulation.py
│   ├── diffusion_process_simulation.py
│   ├── geometric_brownian_motion_simulation.py
│   └── finite_difference_black_scholes.py
├── src/
│   ├── random_walk_model.py
│   ├── brownian_motion_generator.py
│   ├── heat_equation_utilities.py
│   └── black_scholes_pde_utilities.py
├── plots/
└── notebooks/
```

## How to Run Simulations

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run individual simulations:
   ```bash
   python simulations/random_walk_simulation.py
   python simulations/diffusion_process_simulation.py
   python simulations/geometric_brownian_motion_simulation.py
   python simulations/finite_difference_black_scholes.py
   ```

3. Generated plots will be saved in the `plots/` directory.

## Learning Outcomes

This project demonstrates the unity of mathematics across disciplines: from probability theory and stochastic processes to partial differential equations and financial engineering. Students will gain understanding of:
- The continuum limit connecting discrete random walks to continuous Brownian motion
- The role of the heat equation in modeling diffusion processes
- The mathematical foundation of modern option pricing theory
- Computational methods for simulating stochastic processes and solving PDEs
- The interdisciplinary nature of applied mathematics in quantitative finance
