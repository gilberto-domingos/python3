import pandas as pd

df = pd.read_csv("files/sport-activity3.csv")

pd.set_option('display.max_rows', 169)

# print(df)

# rows_na = [df['Calories'].isna()]

# nan_calories = df[df['Calories'].isna()]

# print(nan_calories)

print(df.corr())