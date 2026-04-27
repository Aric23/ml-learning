import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 5, 100)
y = x**2 - 4*x + 3 
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'r-', linewidth=2, label ='y = x² - 4x + 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('y = x² - 4x + 3')
plt.legend()
plt.show()
plt.figure(figsize=(12, 6))
months = ['Январь','Февраль','Март','Апрель','Май','Июнь']
sales = [354,14,9874,4567,677,244]
plt.bar(months, sales, color=['red','blue','green','brown','yellow','black'])
plt.xlabel('Месяцы')
plt.ylabel('Продажи')
plt.title('Месяц и продажи')
for i, v in enumerate(sales):
    plt.text(i, v, str(v), ha='center', fontsize=10)

plt.show()

plt.figure(figsize=(8,8))
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']
labels=['Еда','Транспорт','Жилье','Развличения','Другое']
cp = [30, 15, 35, 10, 10]
plt.pie(cp,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%'
)
plt.show()

fig = plt.figure(figsize=(12, 6))
x=np.linspace(1,10,100)
s=np.sin(x)
c=np.cos(x)
t=np.tan(x)
k= 1 / np.tan(x)
ax1 = fig.add_subplot(2,2,1)
ax1 = plt.plot(x,s)
ax2 = fig.add_subplot(2,2,2)
ax2 = plt.plot(x,c)
ax3 = fig.add_subplot(2,2,3)
ax3 = plt.plot(x,t)
ax4 = fig.add_subplot(2,2,4)
ax4 = plt.plot(x,k)
plt.show()