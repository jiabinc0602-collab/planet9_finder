from astroquery.jplhorizons import Horizons
import rebound
from analysis.metrics import cluster_score
import numpy as np

target_list = [
    '90377',  
    '2012 VP113', 
    '2004 VN112',
    '2010 GB174',
    '2007 TG422',
    '2013 RF98'
]

def real_cluster_score():
    sim = rebound.Simulation()

    sim.add(m = 1)

    for _ in range(4):
        sim.add(m=0)

    for target in target_list:
        print(f"Fetching {target}")
        obj = Horizons(id = target, location = '@sun',epochs = None)
        el = obj.elements()

        semi = el['a'][0]
        ecc = el['e'][0]
        inc = np.radians(el['incl'][0])
        Omega = np.radians(el['Omega'][0])
        omega = np.radians(el['w'][0])

        sim.add(a = semi, e = ecc, inc = inc, Omega = Omega, omega = omega)

    return cluster_score(sim)

if __name__ == "__main__":
    score = real_cluster_score()
    print(f"Real solar system score: {score}")
    #Returned a score of 0.7999, meaning high probability of gravitational interference with TNOs