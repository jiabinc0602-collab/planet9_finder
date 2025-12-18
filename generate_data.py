import pandas as pd
import random
import numpy as np
from sim.engine import init_simulation
from analysis.metrics import cluster_score


data = []
num_sims = 10
time = 300000

def sim_planet9():
    pi = np.pi
    #Creating multiple randomized possible planet 9 variables to pass to ML
    for i in range(num_sims):
        #Control group (without p9)
        if random.random() < 0.3:
            sim = init_simulation(None)

            sim.integrate(time)

            score = cluster_score(sim)

            data.append({
                'mass_planet' : 0,
                'semi-major-axis' : 0,
                'eccentricity' : 0,
                'cluster-score' : score
                         })
        #Test group (with p9)
        else:
            mass_earth = random.uniform(3,12)
            mass_solar = mass_earth * 3e-6
            dist = random.uniform(300, 800)
            ecc = random.uniform(0.1, 0.7)
            inc = random.uniform(0, 2*pi)
            asc = random.uniform(0, 2*pi)
            peri = random.uniform(0, 2*pi)
            f = random.uniform(0, 2*pi)

            engine_inputs = {
                'm' : mass_solar,
                'a' : dist,
                'e' :ecc,
                'inc' : inc,
                'Omega' : asc,
                'omega' : peri,
                'f' : f
            }

            sim = init_simulation(p9_stats = engine_inputs)

            sim.integrate(time)

            score = cluster_score(sim)

            data.append({
                'mass_planet' : mass_earth,
                'semi-major-axis' : dist,
                'eccentricity' : ecc,
                'cluster-score' : score
                })
    df = pd.DataFrame(data)

    df.to_csv("planet9_dataset.csv", index = False)

    print("Succesfully loaded randomized planet 9 data into planet9_dataset.csv")

if __name__ == "__main__":
    sim_planet9()
