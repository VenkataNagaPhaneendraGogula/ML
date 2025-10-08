import pandas as pd

# Aggregation reduces the set of values into a single summary value.
# Used to summarize and analyze data.
# Often used with the groupby() function

df = pd.read_csv('data.csv')

# Whole dataframe
# mean
mean = df.mean(numeric_only=True)
# print(mean)

# sum
sum = df.sum(numeric_only=True)
# print(sum)

# minimum
min = df.min(numeric_only=True)
# print(min)

# maximum
max = df.max(numeric_only=True)
# print(max)

# count
count = df.count()
# print(count)


# Single Column
# mean
mean = df["Height"].mean()
# print(mean)

# sum
sum = df["Height"].sum()
# print(sum)

# minimum
min = df["Height"].min()
# print(min)

# maximum
max = df["Height"].max()
# print(max)

# count
count = df["Height"].count()
# print(count)

# using groupby()
group = df.groupby(["Type1"])

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
print(group["Height"].count())