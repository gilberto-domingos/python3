import pandas
import pandas as pd

dados = {"cliente": ["Jonas", "Kim", "Lucas"], "idade": [15, 39, 68]}
df = pd.DataFrame(dados)
print(df)

print("--------- Find local dataframe row ----------")
print(df.loc[[0, 1]])

print("--------- Rename index string ----------")
df = pandas.DataFrame(dados, index=["p1", "p2", "p3"])
print(df)

print("--------- find Rows by named indexes ----------")
print(df.loc[["p2", "p3"]])

print("--------- find Column by named indexes ----------")
print(df.loc[["p2"], ["cliente"]])

print("--------- find Column by named indexes loc number ----------")
# print(df.iloc[0:2][["idade"]])

# Porque essa linha abaixo da erro ? a saida de erro da console não condiz com a situação.
print(df.loc[0:1,["idade"]])


