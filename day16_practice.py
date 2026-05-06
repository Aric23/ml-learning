import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = sns.load_dataset('iris')
print(iris.head())
print(iris.info())
print(iris['species'].value_counts())

plt.figure(figsize=(15,8))
sns.histplot(data=iris, y ='petal_length', x = 'species', bins=30, kde=True, color='blue')
plt.show()

plt.figure(figsize=(15,8))
sns.boxplot(data=iris, x='petal_length', y='species')
plt.show()

plt.figure(figsize=(15,8))
sns.pairplot(iris, hue='species')
plt.show()

numeric_cols = iris.select_dtypes(include=[np.number])
corr = numeric_cols.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})

plt.show()

plt.figure(figsize=(10, 8))
sns.violinplot(data=iris,inner='quartile', x='sepal_length',y='species')
plt.show()