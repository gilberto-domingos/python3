'''
 implementar a função DictToList que deve receber um dicionário como parâmetro e retorna uma lista contendo os valores de cada chave do dicionário
  utilize a função que realiza a soma de valores de um array da biblioteca Numpy
'''

import numpy as np


# Implemente uma função que retorne os valores das chaves de um dicionário em uma lista
def DictToList(dict):
    valores = []

    for v in dict:
        valores.append(dict.get(v))

    return valores


faturamento = {
    "01/01/2023": 5500,
    "02/01/2023": 8850,
    "03/01/2023": 10500,
    "04/01/2023": 6000,
    "05/01/2023": 4500,
    "06/01/2023": 11000,
    "07/01/2023": 1260
}

lista_faturamento = DictToList(faturamento)

# Imprima a soma dos valores contidos em lista_faturamento usando uma função de soma do NumPy
print(np.sum(lista_faturamento))
