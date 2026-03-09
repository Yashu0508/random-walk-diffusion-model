import numpy as np
import matplotlib.pyplot as plt

# Define spatial grid
x = np.linspace(-10, 10, 1000)

# Diffusion coefficient
D = 1

# Times to plot
times = [0.5, 1, 2, 4]

# Plot the Gaussian solutions
plt.figure(figsize=(10, 6))
for t in times:
    # Heat equation Gaussian solution
    u = (1 / np.sqrt(4 * np.pi * D * t)) * np.exp(-x**2 / (4 * D * t))
    plt.plot(x, u, label=f't={t}')

# Title and labels
plt.title("Diffusion of Probability Density Over Time")
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.legend()

# Save the figure
plt.savefig('plots/diffusion_gaussian.png')
plt.show()