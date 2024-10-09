import pandas as pd
import matplotlib.pyplot as plt
ax = plt.gca()

# movie_data = pd.read_csv('IMDB.csv')
movie_data = pd.read_csv('avocado.csv')
print(movie_data.head(2))

# Use isna() to find all columns with NaN values:
# Use isnull() to find all columns with NaN values:
print(movie_data.isna().any())

# filling a null values using fillna()
print(movie_data["Date"].fillna("No Date", inplace=True))

# identify the year with the smallest average price
# to prevent multi index data frames use "as_index=False"
print(movie_data.groupby(['year'], as_index=False)['AveragePrice'].min())
# Group by two keys and then summarize each group
# smallavgp = movie_data.groupby(['year', 'AveragePrice']).min()
# print(smallavgp)

# identify the year with the smallest average price
# to prevent multi index data frames use "as_index=False"
print(movie_data.groupby(['year'], as_index=False)['AveragePrice'].max())
# identify the year with the highest average price
# print(movie_data['AveragePrice'].max())

# Finding the minimum ovacado type consumed
print(movie_data['type'].min())

# Finding the least consuming region
print(movie_data['region'].min())

# Finding the most consuming region
print(movie_data['region'].max())

# Finding the maxomum ovacado type consumed
print(movie_data['type'].max())

# Plotting Graphic representations(line,box,hist) in terms of Price category
visualOne = movie_data[['AveragePrice']]
print(visualOne)

visualOne.plot(kind='box', color='blue', y='AveragePrice', ax=ax)
plt.show()
