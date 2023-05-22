import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer




df_iris2 = pd.read_csv('test2.csv')
# print(df_iris)
#print(df_iris.head())
#print(np.unique(df_iris['species']))
#print(df_iris.describe())

df_iris2_new = df_iris2.copy()
print(df_iris2_new)

df_iris2_new.drop(df_iris2_new.columns[[5, 6, 7]], axis=1, inplace=True)
print(df_iris2_new)


#df_iris_new['sepal_length'] = df_iris_new['sepal_length'].mask(df_iris_new['sepal_length']<0)
num = df_iris2_new._get_numeric_data()
num[num < 0] = 0
print(df_iris2_new)

# df_iris_new.replace(0, np.nan, inplace=True)
# print(df_iris_new)

# df_iris_new.iloc[:5] = df_iris_new.iloc[:5].fillna(df_iris_new.mean(numeric_only=True))

# df_iris_new.iloc[5:8] = df_iris_new.iloc[5:8].fillna(method='ffill')

# df_iris_new.iloc[8:] = df_iris_new.iloc[8:].fillna(method='bfill')

# print(df_iris_new)