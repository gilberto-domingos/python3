import pandas

df = pandas.read_csv('files/sport-activity2.csv')
#df.info()
#print(df)

print('Pós limpeza')

# new_df = df.dropna()
# new_df.info()

# print(new_df)

#df.fillna('Valor de preenchimento', inplace=True)
#print(df)

# Converti as colunas que podem conter NaN para o tipo object
df['Calories'] = df['Calories'].astype(object)
df['Date'] = df['Date'].astype(object)
df['Duration'] = df['Duration'].astype(object)  # Adicionado para garantir que 'Duration' possa conter strings

# Preenchendo os valores NaN com uma string específica
# df.fillna('Valor de preenchimento', inplace=True)

# Espeficificando uma coluna específica para substituição de valor
# df['Date'].fillna('Valor de preenchimento', inplace=True)

# Substitu valores vazios pela média, mediana ou moda
# media = df['Calories'].mean()
# df['Calories'].fillna(media, inplace=True)

# mediana = df['Calories'].median()
# df['Calories'].fillna(mediana, inplace=True)

moda = df['Calories'].mode()[0]
df['Calories'].fillna(moda, inplace=True)

print(df)




