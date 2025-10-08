import pandas as pd

# DataFrame is a two-dimensional labeled data structure with columns of potentially different types
# Creating a DataFrame from a dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])
# print(df)
# print(df.loc['Employee 3'])  # loc means location by label
# print(df.iloc[0])  # iloc means location by integer position

# Adding a new column
df["Job"] = ["Engineer", "Doctor", "N/A"]
# print(df)

# Adding a new row
# new_row = pd.DataFrame({
#     "Name": ["David"],
#     "Age": [28],
#     "City": ["San Francisco"],
#     "Job": ["Artist"]
# }, index=['Employee 4'])
# df = pd.concat([df, new_row])
# print(df)

# Adding new rows
new_rows = pd.DataFrame({
    "Name": ["Eve", "Frank"],
    "Age": [22, 29],
    "City": ["Miami", "Seattle"],
    "Job": ["N/A", "Manager"]
}, index=['Employee 4', 'Employee 5'])
df = pd.concat([df, new_rows])
print(df)