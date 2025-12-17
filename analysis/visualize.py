from sim.engine import init_simulation
import matplotlib.pyplot as plt
import numpy as np

def plot_orbit(sim, filename="orbit_plot.png"):
    fig, ax = plt.subplots(figsize=(8,8))

    particles = sim.particles
    
    planet_x = []
    planet_y = []

    for i in range (5):
        planet_x.append(particles[i].x)
        planet_y.append(particles[i].y)
    
    tno_x = []
    tno_y = []
    
    for j in range(5,len(particles)):
        tno_x.append(particles[j].x)
        tno_y.append(particles[j].y)
    
    ax.scatter(planet_x, planet_y, c='blue', s=50, label='Planets')
    ax.scatter(tno_x, tno_y, c='red', s=10, label='TNOs')
    
    ax.legend()
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x [AU]')
    ax.set_ylabel('y [AU]')
    ax.set_title('Top-Down view of the Solar System')

    ax.set_xlim(-600,600)
    ax.set_ylim(-600,600)

    plt.savefig(filename)
    print(f"Snapshot of orbit saved to {filename}")
    plt.close(fig)