# 1. Importe a biblioteca Pandas usando o alias "pd"
import pandas as pd

# 2. Carregar dados a partir de um arquivo CSV em um dataframe a partir dos dados disponível
df = pd.read_csv('files/people-10000.csv')

# 3. Imprimir os 10 primeiros registros do dataframe df
print(df.head(10))

# 4. Imprimir a última linha do dataframe df
print(df[-1:])

# 5. Imprimir somente as linhas de índice par partindo do índice 2 (incluído) até 100 (excluído).
idxArray = range(2, 100, 2)
print(df.iloc[idxArray])

# 6. Imprimir as colunas "First Name", "Last Name", "Email" e "Sex" cujo valor da coluna "Sex" seja "Female".
print(df.loc[df['Sex'] == 'Female', ['First Name', 'Last Name', 'Email', 'Sex']])

# 7. Excluir as colunas "User Id" e "Index" do dataframe "df"
df.drop(["User Id", "Index"], axis=1, inplace=True)
print(df)

# 8. Atribuir para um dataframe "new_df" os nomes das profissões (coluna "Job Title") e a quantidade de ocorrências de cada profissão do dataframe "df"
new_df = df.pivot_table(index='Job Title', aggfunc='size')
print(new_df)
