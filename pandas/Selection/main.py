import pandas as pd

df = pd.read_csv('data.csv', index_col="Name")

# Selection by column
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[['Name', 'Height', 'Weight']].to_string())

# Selection by rows
# print(df.to_string())
# print(df.loc["Bulbasaur":"Pikachu", ["Height", "Weight"]])
# print(df.iloc[0:11:2, 0:3])

# Exercise
pokemon = input('Enter pokemon name: ')

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} doesn't exist")