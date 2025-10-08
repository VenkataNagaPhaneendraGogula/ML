import pandas as pd

# Series is a one-dimensional labeled array capable of holding any data type
# List example

# data = [10, 20, 30, 40]
# series = pd.Series(data, index=['a', 'b', 'c', 'd'])
# print(series)
# print(series.loc['d'])  # loc means location by label
# series.loc['d'] = 100  # Update value at label 'd'
# print(series.iloc[3])  # iloc means location by integer position

# print(series.loc[series < 20])  # Conditional selection or filtering values

# Dictionary example

calories = {"Day 1": 1000, "Day 2": 1500, "Day 3": 2000}
series = pd.Series(calories)
print(series.loc[series <= 1500])