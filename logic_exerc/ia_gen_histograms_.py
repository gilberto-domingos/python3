import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)

s = np.exp(-t)
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlabel('Tempo')
ax.set_ylabel('Quantidade')
ax.set_title('Exponencial Decrescente')
ax.grid(True)

plt.show()

'''
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
'''