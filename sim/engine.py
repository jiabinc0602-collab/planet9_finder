import rebound
import random
import numpy as np

def init_simulation(include_planet9: bool):
    sim = rebound.Simulation() #Created simulation

    sim.units = ('yr', 'AU', "Msun")

    sim.add(m = 1) #Sun
    #Skipping smaller planets b/c minimal affect on TNO and hurts performnace
    sim.add(m = 9.543e-4, a = 5.20, e = 0.048) #Jupiter
    sim.add(m = 2.8e-4, a = 9.54, e = 0.056) #Saturn
    sim.add(m = 4.3e-5, a = 19.19, e = 0.046) #Uranus
    sim.add(m = 5.1e-5, a=30.06, e = 0.01) #Neptune
    
    if include_planet9:
        sim.add(m=1.5e-5, a = 700, e = 0.6) #Estimated stats of planet 9

    #Adding TNOs to simulation
    for i in range(30):
        rand_a = random.uniform(325,800) #Estimated Semi Major Axis of planet 9
        rand_e = random.uniform(0.1, 0.6) #Estimated eccentricity of planet 9
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