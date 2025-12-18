import rebound
import random
import numpy as np

def init_simulation(p9_stats = None):
    sim = rebound.Simulation() #Created simulation

    sim.units = ('yr', 'AU', "Msun")

    sim.add(m = 1) #Sun
    #Skipping smaller planets b/c minimal affect on TNO and hurts performnace
    sim.add(m = 9.543e-4, a = 5.20, e = 0.048) #Jupiter
    sim.add(m = 2.8e-4, a = 9.54, e = 0.056) #Saturn
    sim.add(m = 4.3e-5, a = 19.19, e = 0.046) #Uranus
    sim.add(m = 5.1e-5, a=30.06, e = 0.01) #Neptune
    
    if p9_stats:
        sim.add(
            m = p9_stats['m'],
            a = p9_stats['a'],
            e = p9_stats['e'],
            inc = p9_stats['inc'],
            Omega = p9_stats['Omega'],
            omega = p9_stats['omega']
        )
    
    #Adding TNOs to simulation with randomness
    for i in range(30):
        rand_a = random.uniform(325,800)
        rand_e = random.uniform(0.1, 0.6) 
        rand_inc = random.uniform(np.radians(10),np.radians(30))
        pi = np.pi
        rand_omega = random.uniform(0,2*pi)
        rand_f = random.uniform(0,2*pi)
        rand_Omega = random.uniform(0, 2*pi)
        sim.add(m = 0, a = rand_a, e = rand_e, Omega = rand_Omega, inc = rand_inc, omega = rand_omega, f = rand_f)
    
    sim.move_to_com()
    sim.integrator = "whfast"

    sim.dt = 0.5

    return sim