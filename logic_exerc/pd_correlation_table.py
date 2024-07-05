import pandas

df = pandas.read_csv('https://www.w3schools.com/python/pandas/data.csv')

# Calcular a tabela de correlação
correlation_table = df.corr()

# Exibir a tabela de correlação
print(correlation_table)

# Identificar a coluna que tem a maior correlação com 'Duration'
duration_correlation = correlation_table['Duration'].drop('Duration').idxmax()

print(f"A coluna que apresenta maior correlação com a duração da atividade física é: {duration_correlation}")
