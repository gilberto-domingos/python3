# dividir o array produtos em 3 partes, utilizar a função array_split do NumPy
import numpy as np

produtos = ['salame', 'cerveja', 'queijo', 'presunto', 'palmito', 'pão de alho', 'refrigerante', 'picanha', 'contra-filé']

resultsPage = np.array_split(produtos, 3)

print(resultsPage)

'''
# concatenar os elementos do array usersFromSource1 e usersFromSource2 em sequência no array users, você deve utilizar a função concatenate


import numpy as np

usersFromSource1 = np.array(
    ['john@email.com', 'sara@email2.com', 'crist@laznnn.com'])
usersFromSource2 = np.array(
    ['linda@email.com', 'hommer@email2.com', 'muhim@czwwz.com'])

users = np.concatenate((usersFromSource1, usersFromSource2))

print(users)
'''