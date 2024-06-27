import matplotlib.pyplot as plt
import numpy as np
from numpy.random._examples.cffi.extending import rng

N_points = 100000
n_bins = 20

dist = rng.standard_normal(N_points)

fig, ax = plt.subplots()

ax.hist(dist, bins=n_bins)
ax.set_xlabel('Número de Ocorrências')
ax.set_ylabel('Valores')
ax.set_title('Histograma')


plt.show()