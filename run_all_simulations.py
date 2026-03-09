import subprocess
import sys

simulations = [
    "simulations.random_walk_simulation",
    "simulations.diffusion_process_simulation",
    "simulations.geometric_brownian_motion_simulation",
    "simulations.finite_difference_black_scholes"
]

for sim in simulations:
    print(f"\nRunning {sim}...\n")
    result = subprocess.run([sys.executable, "-m", sim])

    if result.returncode != 0:
        print(f"Error occurred while running {sim}")
        break
    else:
        print(f"{sim} completed successfully.")