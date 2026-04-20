import pandas as pd 
import numpy as np 
 
Magaz = pd.DataFrame({
'Name' : ['Potato', 'Tomato', 'Cucumber', 'Pepper', 'Sosage', 'Pelmeni', 'Hachipuri', 'Brod', 'Cupcake', 'Apple'],
'Prise' : [39, 567, 345, 56, 75, 34, 54, 35, 54, 564],
'Size' : [34, 35, 64, 24, 53, 53, 776, 35, 74, 753],
'Cotigory' :['V','V','V','V','P','P','P','P', 'P','Frt']
})

print(Magaz)

print(Magaz[(Magaz['Prise'] < 100) & (Magaz['Prise'] > 50)])

print(Magaz['Prise'].describe())

MagaZ = Magaz.groupby('Cotigory')['Prise'].mean() * 100
print(MagaZ.head())

MagaZZ = Magaz.nlargest(5, 'Prise')
print(MagaZZ)