# realiza a impressão de cada elemento da matriz 3-dimensional precosPorCategoria

import numpy as np

precosPorCategoria = np.array(
    [[[12.50, 91.2, 5.66, 17.61], [6.29, 1.61, 8.93, 3.11]], [[10.50, 9.54, 1.08, 7.98], [3.69, 5.49, 6.39, 4.20]]])
for x in precosPorCategoria:
    for y in x:
        for z in y:
            print(z)


'''
# converter o vetor numeros em uma matriz 3x5 utilizando NumPy, utilizar o método reshape.

import numpy as np

numeros = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

matriz = numeros.reshape(3, 5)

print(matriz)
######################

# checar o shape (formato) do array idades, usar o atributo shape do NumPy
import numpy as np

idades = np.array([[68, 39, 11], [21, 12, 0]])

shape = idades.shape

print(shape)
###################

#  copiar o segundo até o quinto elemento do array alturas para o array novaAlturas, utilizar a indexação do NumPy
import numpy as np

alturas = np.array([1.88, 1.95, 1.64, 1.65, 1.72])

novaAlturas = alturas[1:5]
print(novaAlturas)
#########
# imprimir o intervalo do quarto (inclusive) ao décimo (exclusivo) elemento do array em NumPy
import numpy as np

array = np.array([0, 2, 4, 6, 8, 10, 15, 20, 30, 35, 40, 45])
print(array[3:10])
#############

import numpy as np

array = np.array([72, 983, 11, 0, 86])
print(array[1])
'''