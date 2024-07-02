import pandas as pd

df = pd.read_csv("files/sport-activity2.csv")

# Verifique se há valores NaN na coluna 'Date'
nan_dates = df['Date'].isna().sum()
print(f"Valores NaN na coluna 'Date', quantidade: {nan_dates}")

# Remover linhas com valores NaN na coluna 'Date'
df.dropna(subset=['Date'], inplace=True)

# Verifique se há valores na coluna 'Date' que contenham apenas números e não sejam datas válidas
invalid_dates = df['Date'].apply(lambda x: x.isdigit() if isinstance(x, str) else False).sum()
print(f"Linhas na coluna 'Date' que possuem numeros e não são datas, quantidade: {invalid_dates}")

# Converter valores que contêm apenas números para o formato de data 'YYYY/mm/dd'
df['Date'] = df['Date'].apply(
    lambda x: pd.to_datetime(x, format='%Y%m%d').strftime('%Y/%m/%d') if isinstance(x, str) and x.isdigit() else x
)

# Verificar quantas linhas na coluna 'Date' são strings
string_dates_count = df['Date'].apply(lambda x: isinstance(x, str)).sum()

# Calcular quantas linhas na coluna 'Date' não são strings
non_string_dates_count = len(df) - string_dates_count

print(f"Linhas na coluna 'Date' que são strings: {string_dates_count}")
print(f"Linhas na coluna 'Date' que não são strings: {non_string_dates_count}")

print(df)









