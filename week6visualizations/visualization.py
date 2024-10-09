import pandas as pd
import matplotlib.pyplot as plt
ax = plt.gca()

movie_data = pd.read_csv('IMDB.csv')

# Read data with specific explicit index
indexed_data = pd.read_csv('IMDB.csv', index_col="Title")

print(movie_data[['Revenue (Millions)']])
visualOne = movie_data[['Revenue (Millions)', 'Title', 'Rating']]
print(visualOne)

visualOne.plot(kind='scatter', x='Title', y='Revenue (Millions)', ax=ax)
visualOne.plot(kind='line', color='red', y='Rating', ax=ax)
plt.show()

# print(movie_data.info())

print(movie_data[['Director']])
sliceSsr = movie_data.iloc[[0]][['Title', 'Revenue (Millions)']]
print(sliceSsr)
