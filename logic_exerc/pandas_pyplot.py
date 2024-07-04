import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("files/sport-activity3.csv")

# df.plot()

# df.plot(kind='scatter',x='Duration',y='Calories')

# df['Duration'].plot(kind='hist', bins=3, rwidth=0.9)

df.hist(column='Duration', range=[100,200], grid=False, rwidth=0.9, sharex=True)

plt.show()