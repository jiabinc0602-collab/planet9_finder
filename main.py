from sim.engine import init_simulation

sim = init_simulation()

sim.integrate(100)
sim.status()