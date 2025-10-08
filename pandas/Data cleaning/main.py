import pandas as pd

# Data cleaning = the process of removing/fixing:
#                   incomplete, incorrect, or irrelevant data.
#                  ~75% of work done with Pandas is data cleaning.

df = pd.read_csv('data.csv')

#1 Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

#2 Handling missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

#3 Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                    "Water": "WATER"})

#4 Standardize text
# df["Name"] = df["Name"].str.upper()

#5 Fix Data Types
# df["Legendary"] = df["Legendary"].astype(bool)

#6 Remove duplicate values
# df = df.drop_duplicates()
print(df.to_string())