from sim.engine import init_simulation
from analysis.visualize import plot_orbit

#Creating sim object
sim = init_simulation()


print("Simulating 1,000 years")
sim.integrate(1000)

print("Saving plot as image")
plot_orbit(sim)
