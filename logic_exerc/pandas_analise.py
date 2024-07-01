import pandas


df = pandas.read_csv('files/sport-activity.csv')
#pandas.options.display.max_rows = 10

# print(df.head(10))
# print(df.tail(10))
# print(df.info())
# print(df.describe())
# print(df.describe(percentiles=[0.2,0.4,0.6,0.8]))
# print(df.describe(include=['float64']))

print(df.describe(exclude=['float64']).info())

