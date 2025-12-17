import matplotlib.pyplot as plt
import numpy as np
import rebound

def plot_orbit(sim, filename="orbit_plot.png"):
    fig, ax = plt.subplots(figsize=(8,8))

    orbit = rebound.OrbitPlot(sim, unitlabel="[AU]", color = True, xlim =[-600,600], ylim=[-600,600])
    
    orbit.fig.savefig(filename)
    print(f"Snapshot of orbit saved to {filename}")
    plt.close(fig)