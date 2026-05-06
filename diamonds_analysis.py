import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
diamonds = sns.load_dataset('diamonds')
print(f"Датасет содержит {len(diamonds)} записей")
print(diamonds.head())

plt.figure(figsize=(15,12))
plt.subplot(2, 2, 1)
sns.histplot(diamonds['price'], bins=50, kde=True)
plt.title('Распределние цен на алмазы')

plt.subplot(2, 2, 2)
sns.boxplot(data=diamonds, x='cut', y='price')
plt.title('Цена в зависимости от огранки')

plt.subplot(2, 2, 3)
sns.scatterplot(data=diamonds.sample(1000), x='carat', y='price', hue='cut', alpha=0.6)
plt.title('Цена вс Карат (цветом огранка)')

plt.subplot(2, 2, 4)
numeric_cols = diamonds.select_dtypes(include=['int64', 'float64'])
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Корреляция числовых признаков')

plt.tight_layout()
plt.savefig('diamonds_analysis.png', dpi=150)
plt.show()

