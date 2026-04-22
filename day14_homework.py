import pandas as pd
import numpy as np


df = pd.DataFrame({
'A' : [np.nan, 4, 5, np.nan ,7 ,4,np.nan,76,np.nan,7],
'B' : [4,74,np.nan,67,3,np.nan,65,np.nan,2,4],
'C' : [np.nan,4,2,7,np.nan,5,np.nan,3,6,3],
})

print(df)
df_mean = df.fillna(df.mean())
print(df_mean)
df_median = df.fillna(df.median())
print(df_median)

df1 = pd.DataFrame({
    'Имя': ['Анна', 'Иван', 'Мария', 'Пётр', 'Ольга'],
    'Возраст': [25, 45, 28, 22, 57],
    'Зарплата': [50000, 60000, 56000, 55000, 70000],
    'Город': ['Москва', 'СПб', 'Москва', 'Москва', 'Казань']
})

Name = df1.groupby('Город').agg({
 'Возраст' : ['mean', 'sum'],
 'Зарплата' : ['mean', 'sum']
 })

print(Name)


df2=pd.DataFrame({
  'id' : [1, 2 ,3 ,5, 6],
  'Color' : ['red','green','red','yellow','blue']
})

df3=pd.DataFrame({
  'id' : [1, 2 ,3 ,5, 6],
  'Name' : ['Alex','Artem','Kati','Dr','Boo']
})

df4=pd.merge(df2, df3, on='id')
print(df4)

df5 = pd.DataFrame({
    'Имя': ['анна', 'иван', 'мария', 'петр'],
    'Цена': [50000, 60000, 55000, 70000],
    'Количество': [3, 5, 2, 4]
})

def get_discount(row):
    if row['Цена'] > 1000:
        return row['Цена'] * 0.9
    return row['Цена'] * 0.95
df5['Цена со скидкой'] = df5.apply(get_discount, axis=1)

print(df5)