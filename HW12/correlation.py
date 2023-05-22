import pandas as pd

df = pd.read_excel(r'C:\Users\Marharyta\Programming\DataScientist\data_clean.xlsx')
df.head()

df.isnull().sum()

print(df.describe())