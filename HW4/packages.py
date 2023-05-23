# Згенерувати послідовність зі 100 випадкових чисел (НЕ цілочисельних, в проміжку від 1 до 100). 100 раз. 
# Для кожного з разів порахувати середнє та суму і зберегти ці значення в два окремі списки. Вивести на екран ці списки. 
# Подивившись на ці списки очима, які є припущення, спостереження?

import math
import random 
import statistics as st

mean_list = []
sum_list = []
i = 0
while i<100:
    random_100 = [random.uniform(1, 100) for i in range(100)]
    mean_value = st.fmean(random_100)
    mean_list.append(mean_value)
    sum_value = math.fsum(random_100)
    sum_list.append(sum_value)
    i+=1

print(mean_list)
print(sum_list)
