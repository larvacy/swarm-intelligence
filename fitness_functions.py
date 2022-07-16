import numpy as np


def f1_fitness(x):
    return np.sum(np.power(x, 2), axis=1)
