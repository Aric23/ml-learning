import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
"""print(tips.head())
print(tips.describe())
plt.figure(figsize=(15,12))
plt.subplot(2,1,1)
sns.histplot(tips['total_bill'], kde=True)
plt.subplot(2,1,2)
sns.boxplot(data=tips, x='tip', y='day')
plt.show()
plt.figure(figsize=(15,12))
plt.subplot(3,1,1)
sns.barplot(data=tips, x='tip', hue='sex')
plt.subplot(3,1,2)
sns.violinplot(data=tips, x='total_bill', y='time')
plt.subplot(3,1,3)
sns.countplot(data=tips, x='smoker', hue='sex')
plt.show()
plt.subplot(3, 1, 1)
sns.scatterplot(data=tips, x='total_bill', y = 'tip', hue='sex')
plt.subplot(3, 1, 2)
sns.lmplot(data=tips, x='tip', y = 'total_bill')
plt.subplot(3, 1, 3)
sns.jointplot(data=tips, x='total_bill', y = 'tip')
plt.show()

ddd = tips.select_dtypes(include=[np.number])
corr = ddd.corr()
plt.figure(figsize=(15,12))
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1,)
plt.show()
"""
"""tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
plt.subplot(4,1,1)
sns.boxplot(data=titanic, x='age', y='pclass')
plt.subplot(4,1,2)
sns.barplot(data=titanic, x='survived', y='sex')
plt.subplot(4,1,3)
sns.boxplot(data=tips, x='tip', y='sex')
plt.subplot(4,1,4)
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()"""




