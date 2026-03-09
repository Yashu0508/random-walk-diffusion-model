# Theory Notes: From Random Walk to Black-Scholes

## 1. Random Walk

A **random walk** is a discrete-time stochastic process where the position at each step is determined by a sequence of independent random variables. Consider a simple symmetric random walk on the integer line, where each step $X_i$ is +1 or -1 with equal probability $1/2$.

The position after $n$ steps is:
$$S_n = \sum_{i=1}^n X_i$$

**Properties:**
- $E[S_n] = 0$ (unbiased)
- $Var(S_n) = n$ (variance grows linearly with time)
- The distribution of $S_n$ is binomial, which approaches normal as $n \to \infty$ by the Central Limit Theorem.

Random walks model diffusive behavior in discrete time and space.

## 2. Brownian Motion

**Brownian motion** (Wiener process) is the continuous-time analog of a random walk. It is a stochastic process $B(t)$ with the following properties:

1. $B(0) = 0$
2. Independent increments: $B(t) - B(s)$ is independent of $\{B(u) : u \leq s\}$ for $s < t$
3. Normally distributed increments: $B(t) - B(s) \sim N(0, t - s)$
4. Continuous paths (with probability 1)

The process can be constructed as the limit of scaled random walks:
$$B(t) = \lim_{n \to \infty} \frac{1}{\sqrt{n}} S_{nt}$$

Brownian motion models continuous diffusion and is fundamental in stochastic calculus.

## 3. Diffusion Equation

The **diffusion equation** (heat equation) describes how a quantity spreads over time due to random motion. In one dimension:

$$\frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}$$

Where:
- $u(x,t)$ is the concentration/density at position $x$ and time $t$
- $D$ is the diffusion coefficient

This PDE governs the evolution of probability densities in diffusive systems.

## 4. Gaussian Solution of the Heat Equation

For the initial condition $u(x,0) = \delta(x)$ (Dirac delta), the solution is the Gaussian kernel:

$$u(x,t) = \frac{1}{\sqrt{4\pi Dt}} \exp\left(-\frac{x^2}{4Dt}\right)$$

This represents the probability density of a particle starting at $x=0$ after time $t$ of diffusion. The width of the Gaussian grows as $\sqrt{t}$, reflecting the diffusive spread.

## 5. Geometric Brownian Motion

**Geometric Brownian motion** (GBM) models the evolution of stock prices, where the logarithm of the price follows Brownian motion:

$$dS = \mu S dt + \sigma S dB$$

In integral form:
$$S(t) = S(0) \exp\left((\mu - \frac{1}{2}\sigma^2)t + \sigma B(t)\right)$$

Where:
- $\mu$ is the drift (expected return)
- $\sigma$ is the volatility
- $B(t)$ is Brownian motion

GBM ensures that stock prices remain positive and captures the multiplicative nature of financial returns.

## 6. Black-Scholes PDE

The **Black-Scholes equation** prices European options under the assumption of geometric Brownian motion for the underlying asset:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$

With boundary conditions depending on the option type (call/put, strike price $K$, maturity $T$).

This PDE must be solved subject to the terminal condition $V(S,T) = \max(S - K, 0)$ for a call option.

## 7. Transformation to Heat Equation

The Black-Scholes PDE can be transformed into the heat equation using a logarithmic change of variables. Define:

$$x = \ln(S/K)$$
$$\tau = \frac{1}{2}\sigma^2 (T - t)$$
$$v(x,\tau) = \frac{V(S,t)}{K}$$

Substituting into the Black-Scholes PDE yields:

$$\frac{\partial v}{\partial \tau} = \frac{\partial^2 v}{\partial x^2} + \left(r - \frac{1}{2}\sigma^2\right) \frac{\partial v}{\partial x} - r v$$

For constant volatility and risk-free rate, this reduces to the heat equation:

$$\frac{\partial v}{\partial \tau} = \frac{\partial^2 v}{\partial x^2}$$

The boundary conditions transform accordingly, allowing the use of known heat equation solutions for option pricing.