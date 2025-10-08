import pandas as pd

df = pd.read_csv('data.csv')

# print(df) # Displays the first 5 and last 5 rows of the DataFrame
print(df.to_string()) # Displays the entire DataFrame