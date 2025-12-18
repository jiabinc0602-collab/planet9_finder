from sim.engine import init_simulation
from analysis.visualize import plot_orbit
from analysis.metrics import cluster_score
from real_data import _

#Creating sim object
sim = init_simulation(True)


print("Simulating 300,000 years")
sim.integrate(300000)

print("Saving plot as image")
plot_orbit(sim)

c_score = cluster_score(sim)
print(f"Cluster Score: {c_score}")

