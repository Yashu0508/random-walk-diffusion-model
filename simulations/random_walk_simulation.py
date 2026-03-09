import matplotlib.pyplot as plt
import os
from src.random_walk_model import multiple_random_walks

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ensure plots folder exists
plots_dir = os.path.join(BASE_DIR, "plots")
os.makedirs(plots_dir, exist_ok=True)

# Generate 20 random walk paths with 1000 steps
n_steps = 1000
n_paths = 20
paths = multiple_random_walks(n_steps, n_paths)

# Plot the trajectories
plt.figure(figsize=(10,6))
for i in range(n_paths):
    plt.plot(range(n_steps), paths[i], alpha=0.7)

plt.xlabel("Time (steps)")
plt.ylabel("Position")
plt.title("Random Walk Trajectories")

# Save figure
save_path = os.path.join(plots_dir, "random_walk_paths.png")
plt.savefig(save_path)

plt.show()