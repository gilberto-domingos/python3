import pandas as pd

pedido = {
      'idCliente': [2995, 3001, 1112, 9999],
      'produto': ['Refrigerador 220V', 'Smartphone 10', 'Monitor 19 LCD', 'Mouse Logitech'],
      'valor': [2649.99, 4999.00, 679.90, 29.90]
}

# Carrega o Set em um dataframe df
df = pd.DataFrame(pedido)

# Carregar a segunda linha do dataframe
print(df.loc[1])

# Impressão da coluna produto
print(df.loc[:, 'produto'])

# Imprimir as informações do dataframe
df = pd.DataFrame(pedido)

# Imprimir as informações do dataframe
print(df.info())
