import rebound
import random

def init_simulation():
    sim = rebound.Simulation() #Created simulation

    sim.units = ('yr', 'AU', "Msun")

    sim.add(m=1) #Sun
    #Skipping smaller planets b/c minimal affect on TNO and hurts performnace
    sim.add(m=9.543e-4, a=5.20, e=0.048) #Jupiter
    sim.add(m=2.8e-4, a=9.54, e=0.056) #Saturn
    sim.add(m=4.3e-5, a=19.19, e=0.046) #Uranus
    sim.add(m=5.1e-5, a=30.06, e=0.01) #Neptune
    
    for i in range(20):
        rand_a = random.uniform(350,800) #Estimated Semi Major Axis of planet 9
        rand_e = random.uniform(0.1, 0.6) #Estimated eccentricity of planet 9
        sim.add(m=0, a=rand_a, e=rand_e)
    
    sim.move_to_com()
    sim.integrator = "whfast"

    sim.dt = 0.5

    return sim