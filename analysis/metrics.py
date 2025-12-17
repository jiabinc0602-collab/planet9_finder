import numpy as np
import rebound

#Calculating orientation cluster using perihelions to evaluate possibility of TNO orbits with/without planet 9
def cluster_score(sim):
    tnos = sim.particles[5:]

    vector_x = []
    vector_y = []

    #pomega is built in that returns perihelion angle
    for p in tnos:
        vector_x.append(np.cos(p.pomega))
        vector_y.append(np.sin(p.pomega))

    score = np.sqrt(np.average(vector_x)**2 + np.average(vector_y)**2)
    
    return score