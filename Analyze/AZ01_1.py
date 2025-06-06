import pandas as pd

df = pd.read_csv('fifa.csv')

print(df.head())
print(df.info())
print(df.describe())

df1 = pd.read_csv('dz.csv')
df1.fillna(0, inplace=True)
group = df1.groupby('City')['Salary'].mean()
print(group)
