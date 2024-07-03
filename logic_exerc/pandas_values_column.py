import pandas as pd

df = pd.read_csv("files/sport-activity2.csv")
#df.loc[7, 'Duration'] = 45
'''
for x in df.index:
    if df.loc[x, "Pulse"] > 100:
        df.loc[x, "Pulse"] = 111

for x in df.index:
    if df.loc[x, "Pulse"] > 100:
        df.drop(x, inplace=True)
'''
#print(df.duplicated())

df.drop_duplicates(inplace=True)

print(df)