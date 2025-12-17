from sim.engine import init_simulation
from analysis.visualize import plot_orbit

#Creating sim object
sim = init_simulation(True)


print("Simulating 100,000 years")
sim.integrate(100000)

print("Saving plot as image")
plot_orbit(sim)
