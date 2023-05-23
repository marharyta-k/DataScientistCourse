# - Маючи на вхід файл data.xlsx потрібно прочитати дані у датафрейм та зробити опис цього датафрейму. 
# Зверніть увагу, що це не типовий IRIS датасет, який є в інтернеті. Він змінений!

# - Заповнити пропуски з перших 0 - 1000 рядочків методом середнього. Заповнити пропуски других 1000 - 2000 рядочків методов ffil, 
# всі інші заповнити методом bfil.

# - Зробити ще один опис після заповнення даних. Що змінилось? Чи є в описі щось дивне?

# 5 балів. Якщо з описом та правильною відповіддю то +5 балів.

# - Побудувати лінійну регресію (для передбачення PETAL WIDTH) та зробити опис отриманого результату.
# 3 бали.
# - Додаткове завдання: Зробити всі попередні пункти для складнішого датасету data2.xlsx (з підвохом!).
# 5 балів.

import matplotlib as plt
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 


# Прочитаємо дані у датафрейм
df_iris = pd.read_excel('data.xls')
print(df_iris)
print(df_iris.head())
print(np.unique(df_iris['species']))

# Зробимо опис цього датафрейму
print(df_iris.describe())

# В описі видно, що є від'ємні значення в першому стовпчику sepal_length, це некоректні дані. Замінимо їх на NaN (можна ще на 0, або взагалі опустити). 
# Також є значення рівні 0, їх також замінимо на Nan, щоб в наступному кроці заповнити даними разом з іншими пропусками.
# Створимо копію нашого датафрейму і працюватимемо з нею. 
df_iris_new = df_iris.copy()
print(df_iris_new)

# Замінимо від'ємні значення на NaN. 
df_iris_new['sepal_length'] = df_iris_new['sepal_length'].mask(df_iris_new['sepal_length']<0)
# Це варіант заміни на 0. 
# num = df_iris_new._get_numeric_data()
# num[num < 0] = 0
print(df_iris_new)

# Замінимо 0 значення на NaN.
df_iris_new.replace(0, np.nan, inplace=True)
print(df_iris_new)

# Заповнити пропуски з перших 0-1000 рядочків методом середнього. 
# Заповнити пропуски других 1000-2000 рядочків методов ffil, всі інші заповнити методом bfil.
df_iris_new.iloc[:1001] = df_iris_new.iloc[:1001].fillna(df_iris_new.mean(numeric_only=True))
df_iris_new.iloc[1001:2001] = df_iris_new.iloc[1001:2001].fillna(method='ffill')
df_iris_new.iloc[2001:-1] = df_iris_new.iloc[2001:-1].fillna(method='bfill')
print(df_iris_new)
        
# Зробити ще один опис після заповнення даних. Що змінилось? Чи є в описі щось дивне?
print(df_iris_new.describe())
# Цей опис виглядає коректним. 

# Перевіримо чи лишились значення NaN. 
print(df_iris_new.isnull().sum().sum())
# Бачимо, що лишилось 4 пустих значення, це останній рядок, він не заповнився, так як використовувалась функція bfill, 
# яка бере наступне начення і вставлє у попереднє. Для останнього значення це не спрацьовує. Використаємо для останнього елемента функцію ffill. 
df_iris_new.iloc[-2:] = df_iris_new.iloc[-2:].fillna(method='ffill')
# І знову порахуємо значення NaN. 
print(df_iris_new.isnull().sum().sum())
# Тепер значень NaN немає. Можемо будувати лінійну регресію. 

X = df_iris_new.drop(labels = ['petal_width', 'species'], axis = 1)
Y = df_iris_new['petal_width']
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state = 101)
linear_regression = LinearRegression()
linear_regression.fit(X_train, Y_train)

model_lr = linear_regression.fit(X_train, Y_train)

# Поглянемо на коефецієнти. 
print(model_lr.coef_)
# Всі коефіціенти позитивні. Це означає, що залежність між petal_width та усіма іншими характеристиками прямопропорційна. 

# Подивимось як працює натренована модель на тестових даних. Передбачимо значення petal_width.
Y_pred = linear_regression.predict(X_test)
print(Y_pred)
# Візуально порівняємо передбачені дані зі справжніми тестовими. 
print(Y_test)

# Подивимось метрики побудованої моделі. 
score = r2_score(
    Y_test,
    Y_pred
)
print(score)
# Отже, точність моделі приблизно 73 відсотки. 

# Експортуємо в ексель, індекс фолс, щоб не було зайвої колонки з індексами Unnamed:0
df_iris_new.to_excel('data_clean.xlsx', index=False)

