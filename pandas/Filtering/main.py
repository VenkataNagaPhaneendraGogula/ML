import pandas as pd

# Filtering means keeping the rows that matches the condition
df = pd.read_csv('data.csv')

# tall_pokemon = df[df["Height"] >= 2]
# heavy_pokemon = df[df["Weight"] > 100]
# legendary_pokemon = df[df["Legendary"] == 1]

# water_pokemon = df[(df["Type1"] == "Water") |
#                     (df["Type2"] == "Water")]

ff_pokemon = df[(df["Type1"] == "Fire") &
                (df["Type2"] == "Flying")]
print(ff_pokemon)

