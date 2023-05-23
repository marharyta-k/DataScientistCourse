import matplotlib as plt
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 


# Прочитаємо дані у датафрейм
df_iris2 = pd.read_excel('data2.xls')
print(df_iris2.head())
print(np.unique(df_iris2['species']))

# Зробимо опис цього датафрейму
print(df_iris2.describe())

# В описі відсутні 2 колонки. Подивимось тип даних кожної колонки.
print(df_iris2.dtypes)
# Бачимо причину: sepal_width object та petal_length object, не числові дані, тому не відображаються в описі датафрейму. Змінимо це.
# Зробимо копію нашого датафрейму і працюватимемо з нею. 
df_iris2_new = df_iris2.copy()
print(df_iris2_new)

# Конвертуємо object колонки у float, при неможливості перевести у float переводимо в NaN. 
df_iris2_new['sepal_width'] = pd.to_numeric(df_iris2_new['sepal_width'], errors='coerce')
df_iris2_new['petal_length'] = pd.to_numeric(df_iris2_new['petal_length'], errors='coerce')
print(df_iris2_new.dtypes)
print(df_iris2_new.describe())

# Тепер бачимо повний опис. 
# В описі видно, що 1)є 3 зайві пусті колонки, приберемо їх, 2)є від'ємні значення в першому стовпчику sepal_length, це некоректні дані. 
# Замінимо їх на NaN. 3)є значення рівні 0, їх також замінимо/приберемо, 4) максимальне значення занадто велике, очима пробігла по датасету, 
# знайшла лише одне більше 10 - 70. Але задам, напевно, не більше 20. 

# # 1) Приберемо 3 останні пусті колонки.
df_iris2_new.drop(df_iris2_new.columns[[5, 6, 7]], axis=1, inplace=True)
print(df_iris2_new)

# 2) Замінимо від'ємні значення з першого стовпчика на NaN.
df_iris2_new['sepal_length'] = df_iris2_new['sepal_length'].mask(df_iris2_new['sepal_length']<0)
print(df_iris2_new)

# 3) Замінимо 0 значення на NaN.
df_iris2_new.replace(0, np.nan, inplace=True)
print(df_iris2_new)

# 4) Приберемо некоректно високі значення. Все, що більше 20 конвертуємо в NaN. 
df_iris2_new.iloc[:, 0:4] = df_iris2_new.iloc[:, 0:4].mask(df_iris2_new.iloc[:, 0:4]>20)
print(df_iris2_new.describe())

# Тепер дані по опису виглядають більш менш коректно. Можемо приступити до автозаповнення пропущених даних. 
# Заповнимо пропуски з перших 0-1000 рядочків методом середнього. 
# Заповнимо пропуски других 1000-2000 рядочків методов ffil, всі інші заповнимо методом bfil.
df_iris2_new.iloc[:1001] = df_iris2_new.iloc[:1001].fillna(df_iris2_new.mean(numeric_only=True))
df_iris2_new.iloc[1001:2001] = df_iris2_new.iloc[1001:2001].fillna(method='ffill')
df_iris2_new.iloc[2001:-1] = df_iris2_new.iloc[2001:-1].fillna(method='bfill')
print(df_iris2_new)
        
# Зробимо ще один опис після заповнення даних. 
print(df_iris2_new.describe())
# Цей опис виглядає коректним. 

# Перевіримо чи лишились значення NaN. 
print(df_iris2_new.isnull().sum().sum())
# Результат 0. Можемо приступати до створення моделі лінійної регресії. 
X = df_iris2_new.drop(labels = ['petal_width', 'species'], axis = 1)
Y = df_iris2_new['petal_width']
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
# Точність моделі приблизно 73 відсотки. Думаю, точність моделі могла б бути вищою, якби розділити дані на 4 сети, для кожного виду iris окремо. 
# Спробуємо зробити для whatever =) 
X1 = df_iris2_new[df_iris2_new['species']=='Iris-whatever'].drop(labels = ['sepal_length', 'species'], axis=1)
Y1 = df_iris2_new[df_iris2_new['species']=='Iris-whatever']['sepal_length']

X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, test_size=0.33, random_state = 101)
linear_regression1 = LinearRegression()
linear_regression1.fit(X1_train, Y1_train)
linear_regression1.predict(X1_test)
Y1_pred = linear_regression1.predict(X1_test)
score1 = r2_score(
    Y1_test,
    Y1_pred
)
print(score1)
# Точність виявилась нижчою, 65 відсотків. Варто зупинитись на попередньому варіанті з моделлю, що базується на даних про 4 види одночасно. 
# Наступним кроком можна було б також спробувати погратись з підходом до врегулювання відсутніх/некоректних даних: взагалі видалити або 
# спробувати заповнити іншими методами. 