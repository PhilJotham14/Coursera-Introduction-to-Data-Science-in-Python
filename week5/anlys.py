import pandas as pd
from pandas.core import series
first_list = [10, 20, 30, 40, 50, 60, 70, 80, 'N/A']
first_serie = pd.Series(first_list)
print("The series values are : ", first_serie.values)
print("The index values of the serie are : ", first_serie.index.values)

second_serie = pd.Series(first_list, index=[
                         'uganda', 'kenya', 'tanzania', 'rwanda', 'USA', 'UK', 'SouthAfrica', 'Botsawana', 'Canada'])
print("Drinking competition results ", second_serie)

serie_copy = first_list.slice[1:4]
print(serie_copy)
print(second_serie['UK'])
fruits = {"apples": 40,
          "mangoes": 50,
          "bananas": 60,
          "strawberries": 70,
          "pears": 80,
          "oranges": 90,
          }
third_series = pd.Series(fruits)
print('Fruits and quantities on market : ', third_series)
print(third_series["oranges"])
