import pandas as pd
from openpyxl import load_workbook
import random

# Abrir o arquivo Excel existente
file_path = 'files/filebill.xlsx'
wb = load_workbook(file_path)
ws = wb.active

# Lendo os dados no DataFrame
df = pd.read_excel(file_path)

# Criando a coluna de telefones celulares
df['Telefone'] = '55479'

# Gerando números aleatórios para os últimos 8 dígitos do telefone
for index in range(len(df)):
    random_number = ''.join(random.choice('0123456789') for i in range(8))
    df.loc[index, 'Telefone'] += random_number

# Inserindo a coluna "Telefone" após a coluna "Empresa"
df.insert(df.columns.get_loc("Empresa") + 1, "Telefone", df["Telefone"])

# Salvando o DataFrame modificado no arquivo Excel
df.to_excel(file_path, index=False)

print("Coluna de telefones celulares adicionada com sucesso!")