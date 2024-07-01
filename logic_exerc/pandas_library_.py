import pandas

df = pandas.read_json('files/nacionalidade-income.json')
# pandas.options.display.max_rows = 10

print(df)

'''
df = pandas.read_csv('files/nacionalidade-income.csv')
pandas.options.display.max_rows = 10

print(df)
'''